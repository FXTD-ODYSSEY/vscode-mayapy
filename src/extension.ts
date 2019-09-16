/*---------------------------------------------------------
 * Copyright (C) Microsoft Corporation. All rights reserved.
 *--------------------------------------------------------*/

import * as vscode from 'vscode';
import * as path from 'path';

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

	let ptvsdPath: string = path.join(path.dirname(__dirname), "py")

	const debug_py = vscode.commands.registerCommand('mayapy.debugPythonFile', async (uri:vscode.Uri) => {
		let activeDebugSession = vscode.debug.activeDebugSession
		if (activeDebugSession){
			Logger.info(`activeDebugSession:${activeDebugSession}`);
			Logger.info(`name:${activeDebugSession.name}`);
			Logger.info(`type:${activeDebugSession.type}`);
			Logger.info(`id:${activeDebugSession.id}`);
			Logger.info(`workspaceFolder:${activeDebugSession.workspaceFolder}`);
			Logger.info(`configuration:${activeDebugSession.configuration}`);
			Logger.info(`configuration:${Object.keys(activeDebugSession.configuration)}`);
			Logger.info(`=======================================================`);
			let configuration = activeDebugSession.configuration;
			Logger.info(`name:${configuration.name}`);
			Logger.info(`request:${configuration.request}`);
			Logger.info(`type:${configuration.type}`);
			Logger.info(`pythonPath:${configuration.pythonPath}`);
			Logger.info(`program:${configuration.program}`);
		}

		// Logger.info(`rootPath:${vscode.workspace.rootPath}`);
		// Logger.info(`workspaceFile:${vscode.workspace
		// 	.workspaceFile}`);
		// Logger.info(`uri:${uri.fsPath}`);
		// Logger.info(`basename:${path.basename(uri.fsPath, ".py")}`);
		
		// vscode.debug.startDebugging()
		

		let file_name:string = path.basename(uri.fsPath, ".py");

		const newFile = vscode.Uri.parse('untitled:' + path.join(vscode.workspace.rootPath, 'debug.py'));
		vscode.workspace.openTextDocument(newFile).then(document => {
			const edit = new vscode.WorkspaceEdit();

			let py_code: string = `
# 添加 ptvsd 导入路径
import sys
ptvsd_module = r"${ptvsdPath}"
if ptvsd_module not in sys.path:
	sys.path.insert(0,ptvsd_module)

# 开启 ptvsd Debug 端口
import ptvsd
ptvsd.enable_attach()

# 加载当前文件
current_directory = r"${path.dirname(uri.fsPath)}"
if current_directory not in sys.path:
	sys.path.insert(0,current_directory)

import ${file_name}
reload(${file_name})
			`;

			edit.insert(newFile, new vscode.Position(0, 0), py_code);
			return vscode.workspace.applyEdit(edit).then(success => {
				if (success) {
					vscode.window.showTextDocument(document);
					Logger.info(`open document`);
					
					// TODO 激活 Debug 
					if (vscode.debug.activeDebugSession){
						vscode.commands.executeCommand("workbench.action.debug.stop")
					}else{
						vscode.commands.executeCommand("workbench.action.debug.start")
					}

					// NOTE 发送当前代码
					vscode.commands.executeCommand("mayacode.sendPythonToMaya")
					// NOTE 关闭当前打开的文件
					vscode.commands.executeCommand("workbench.action.closeActiveEditor")
					Logger.info(`close document`);
				} else {
					vscode.window.showInformationMessage('Error!');
				}
			});
		});
	});

	context.subscriptions.push(debug_py);

}
