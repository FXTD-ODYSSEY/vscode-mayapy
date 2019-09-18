/*---------------------------------------------------------
 * Copyright (C) Microsoft Corporation. All rights reserved.
 *--------------------------------------------------------*/

import * as vscode from 'vscode';
import * as path from 'path';
import { Socket } from 'net';

const net = require('net');

export class TimeUtils {
	public static getTime(): String {
		return new Date()
			.toISOString()
			.replace(/T/, ' ')
			.replace(/\..+/, '')
			.split(' ')[1];
	}
}

// NOTE Logger 信息输出
export class Logger {
	private static _outputPanel: vscode.OutputChannel;

	public static registerOutputPanel(outputPanel: vscode.OutputChannel) {
		this._outputPanel = outputPanel;
	}

	public static info(log: string) {
		this.typeLog(log, 'INFO');
	}

	public static error(log: string) {
		this.typeLog(log, 'ERROR');
		vscode.window.showErrorMessage(log);
	}

	public static success(log: String) {
		this.typeLog(log, 'SUCCESS');
	}

	public static response(log: String) {
		this.typeLog(log, 'RESPONSE');
	}

	private static typeLog(log: String, type: String) {
		if (!this._outputPanel) {
			return;
		}
		let util = require('util');
		let time = TimeUtils.getTime();
		if (!log || !log.split) return;
		this._outputPanel.appendLine(util.format('mayapy [%s][%s]\t %s', time, type, log));
	}
}

export function activate(context: vscode.ExtensionContext) {

	let outputPanel = vscode.window.createOutputChannel('mayapy');
	Logger.registerOutputPanel(outputPanel);
	Logger.info("activate complete !!!!!");

	let pythonConfig = vscode.workspace.getConfiguration("python")

	// NOTE 添加 python 自动补全路径
	let extraPaths: Array<string> = pythonConfig.get("autoComplete.extraPaths")
	let completionPath: string = path.join(path.dirname(__dirname), "mayaSDK")
	if (!extraPaths.includes(completionPath)) {
		extraPaths.splice(0, 0, completionPath);
		pythonConfig.update("autoComplete.extraPaths", extraPaths, true)
	}



	function debug_func(uri: vscode.Uri) {
		const ptvsdPath: string = path.join(path.dirname(__dirname), "py")
		const file_name: string = path.basename(uri.fsPath, ".py");
		const fileDirname: string = path.dirname(uri.fsPath);

		const config = vscode.workspace.getConfiguration('mayapy');
		const hostname: string = config.get("hostname");
		const port: number = config.get("port");

		let ptvsd_socket = net.createConnection(port, hostname).on("connect", (e) => {
			ptvsd_socket.destroy()

			let run_code: string = `
current_directory = r"${fileDirname}"
if current_directory not in sys.path:
	sys.path.insert(0,current_directory)

import ${file_name}
reload(${file_name})`;

			const debugFile = vscode.Uri.parse('untitled:' + path.join(vscode.workspace.rootPath, 'debug.py'));
			vscode.workspace.openTextDocument(debugFile).then(document => {
				const edit = new vscode.WorkspaceEdit();

				edit.insert(debugFile, new vscode.Position(0, 0), run_code);
				return vscode.workspace.applyEdit(edit).then(success => {
					if (success) {
						vscode.window.showTextDocument(document);
						Logger.info(`open document`);

						let activeDebugSession = vscode.debug.activeDebugSession
						// NOTE 检查当前 Debug 状态
						if (activeDebugSession) {
							let configuration = activeDebugSession.configuration;
							if ("MayaDebugMode" in configuration) {
								// NOTE 发送当前代码
								vscode.commands.executeCommand("mayacode.sendPythonToMaya")
							} else {
								Logger.error(`please stop the current debug mode and try again`)
							}
						} else {
							// NOTE 设置 Debug 设定 | 开启 Debug 模式
							let configuration = new function () {
								this.name = "Maya Python Debugger : Remote Attach"
								this.type = "python"
								this.request = "attach"
								this.port = port
								this.host = hostname
								this.pathMappings = [
									{
										"localRoot": `${fileDirname}`,
										"remoteRoot": `${fileDirname}`
									}
								]
								this.MayaDebugMode = true
							}
							vscode.debug.startDebugging(undefined, configuration).then((param) => {
								// NOTE 发送当前代码
								vscode.commands.executeCommand("mayacode.sendPythonToMaya")
							});
						}

						// NOTE 关闭当前打开的文件
						vscode.commands.executeCommand("workbench.action.closeActiveEditor")
						Logger.info(`close document`);

					} else {
						vscode.window.showInformationMessage('Debug Running File Error!');
					}

				});
			});


		}).on("error", (err) => {

			ptvsd_socket.destroy()

			// NOTE 连接 ptvsd 代码
			const attach_code: string = `
import sys
ptvsd_module = r"${ptvsdPath}"
if ptvsd_module not in sys.path:
	sys.path.insert(0,ptvsd_module)

import ptvsd
ptvsd.enable_attach(('${hostname}',${port}))`;

			const attachFile = vscode.Uri.parse('untitled:' + path.join(vscode.workspace.rootPath, 'attach.py'));
			vscode.workspace.openTextDocument(attachFile).then(document => {
				const edit = new vscode.WorkspaceEdit();

				edit.insert(attachFile, new vscode.Position(0, 0), attach_code);
				return vscode.workspace.applyEdit(edit).then(success => {
					if (success) {
						vscode.window.showTextDocument(document).then(() => {

							// NOTE 发送当前代码
							vscode.commands.executeCommand("mayacode.sendPythonToMaya")
							// NOTE 关闭当前打开的文件
							vscode.commands.executeCommand("workbench.action.closeActiveEditor")

						});
					} else {
						vscode.window.showInformationMessage('Debug Attaching File Error!');
					}
				});
			})

			vscode.window.showInformationMessage('start to activate the ptvsd module in Maya \nplease wait for the maya response and run the command again !');
		});
	}


	const debug_py = vscode.commands.registerCommand('mayapy.debugPythonFile', async (uri: vscode.Uri) => {

		const mayaCodeConfig = vscode.workspace.getConfiguration('mayacode');
		const mayahost: string = mayaCodeConfig.get('hostname');
		const mayaport: number = mayaCodeConfig.get("mel.port");

		// NOTE 检测 Maya 端口是否开启
		let maya_socket = net.createConnection(mayaport, mayahost).on("error", (e) => {
			maya_socket.destroy()
			// NOTE 端口未开启 提示错误
			Logger.error(`
			Unable to connect to port ${mayaport} on Host ${mayahost} in Maya
			Please run the mel command below in the maya script editor \n\n
			
			commandPort -n "localhost:7001" -stp "mel" -echoOutput;

			`)
		}).on("connect", (e) => {
			maya_socket.destroy()
			debug_func(uri)
		})

	});

	context.subscriptions.push(debug_py);

}
