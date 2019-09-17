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
	Logger.info(`socket: ${Socket}`);
	Logger.info(`socket: ${net}`);
	Logger.info(`socket: ${Object.keys(net)}`);

	let pythonConfig = vscode.workspace.getConfiguration("python")

	// NOTE 添加 python 自动补全路径
	let extraPaths: Array<string> = pythonConfig.get("autoComplete.extraPaths")
	let completionPath: string = path.join(path.dirname(__dirname), "mayaSDK")
	if (!extraPaths.includes(completionPath)) {
		extraPaths.splice(0, 0, completionPath);
		pythonConfig.update("autoComplete.extraPaths", extraPaths, true)
	}


	const debug_py = vscode.commands.registerCommand('mayapy.debugPythonFile', async (uri: vscode.Uri) => {
		let activeDebugSession = vscode.debug.activeDebugSession
		if (activeDebugSession) {
			Logger.info(`activeDebugSession:${activeDebugSession}`);
			Logger.info(`name:${activeDebugSession.name}`);
			Logger.info(`type:${activeDebugSession.type}`);
			Logger.info(`id:${activeDebugSession.id}`);
			Logger.info(`configuration:${activeDebugSession.configuration}`);
			Logger.info(`configuration:${Object.keys(activeDebugSession.configuration)}`);
			Logger.info(`=======================================================`);
			let configuration = activeDebugSession.configuration;
			Logger.info(`name:${configuration.name}`);
			Logger.info(`request:${configuration.request}`);
			Logger.info(`type:${configuration.type}`);
			Logger.info(`pythonPath:${configuration.pythonPath}`);
			Logger.info(`program:${configuration.program}`);
			Logger.info(`debugOptions:${configuration.debugOptions}`);
			Logger.info(`cwd:${configuration.cwd}`);
			Logger.info(`env:${configuration.env}`);
			Logger.info(`console:${configuration.console}`);
			Logger.info(`envFile:${configuration.envFile}`);
		}

		const ptvsdPath: string = path.join(path.dirname(__dirname), "py")
		const file_name: string = path.basename(uri.fsPath, ".py");
		const fileDirname: string = path.dirname(uri.fsPath);
		
		const config = vscode.workspace.getConfiguration('mayapy');
		const hostname: string = config.get("mayaypy.hostname");
		const port: number = config.get("mayaypy.port");

		// NOTE Python 代码
		const attach_code: string = `
# 添加 ptvsd 导入路径
import sys
ptvsd_module = r"${ptvsdPath}"
if ptvsd_module not in sys.path:
	sys.path.insert(0,ptvsd_module)

# 开启 ptvsd Debug 端口
import ptvsd
ptvsd.enable_attach(address=('${hostname}', ${port}), redirect_output=True)
ptvsd.wait_for_attach()`;

		const attachFile = vscode.Uri.parse('untitled:' + path.join(vscode.workspace.rootPath, 'attach.py'));
		vscode.workspace.openTextDocument(attachFile).then(document => {
			const edit = new vscode.WorkspaceEdit();

			edit.insert(attachFile, new vscode.Position(0, 0), attach_code);
			return vscode.workspace.applyEdit(edit).then(success => {
				if (success) {
					vscode.window.showTextDocument(document);
					// NOTE 发送当前代码
					vscode.commands.executeCommand("mayacode.sendPythonToMaya")
					// NOTE 关闭当前打开的文件
					vscode.commands.executeCommand("workbench.action.closeActiveEditor")
				} else {
					vscode.window.showInformationMessage('Debug Attaching File Error!');
				}
			});
		});


		let run_code: string = `
# 加载当前文件
current_directory = r"${fileDirname}"
if current_directory not in sys.path:
	sys.path.insert(0,current_directory)

import ${file_name}
reload(${file_name})`;

		const newFile = vscode.Uri.parse('untitled:' + path.join(vscode.workspace.rootPath, 'debug.py'));
		vscode.workspace.openTextDocument(newFile).then(document => {
			const edit = new vscode.WorkspaceEdit();

			edit.insert(newFile, new vscode.Position(0, 0), run_code);
			return vscode.workspace.applyEdit(edit).then(success => {
				if (success) {
					vscode.window.showTextDocument(document);
					Logger.info(`open document`);
					
					let startDebugFlag = false
					// NOTE 检查当前 Debug 状态
					if (vscode.debug.activeDebugSession) {
						let configuration = activeDebugSession.configuration;
						Logger.info(`MayaDebugMode exist:${"MayaDebugMode" in configuration}`);
						if ("MayaDebugMode" in configuration){
							// NOTE 发送当前代码
							vscode.commands.executeCommand("mayacode.sendPythonToMaya")
							// NOTE 关闭当前打开的文件
							vscode.commands.executeCommand("workbench.action.closeActiveEditor")
						}else{
							vscode.commands.executeCommand("workbench.action.debug.stop")
							startDebugFlag = true;
						}
					} else{
						startDebugFlag = true;
					}
					
					if (startDebugFlag){
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
							// NOTE 关闭当前打开的文件
							vscode.commands.executeCommand("workbench.action.closeActiveEditor")

						});
					}


					Logger.info(`close document`);
				} else {
					vscode.window.showInformationMessage('Debug Running File Error!');
				}
			});
		});


	});

	context.subscriptions.push(debug_py);

}
