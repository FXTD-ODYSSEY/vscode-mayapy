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

	let pythonConfig = vscode.workspace.getConfiguration("python")
	let pythonPath = pythonConfig.get("pythonPath")

	// NOTE 添加 python 自动补全路径
	let extraPaths: Array<string> = pythonConfig.get("autoComplete.extraPaths")
	let completionPath: string = path.join(path.dirname(__dirname), "mayaSDK")
	if (!extraPaths.includes(completionPath)){
		extraPaths.splice(0, 0, completionPath);
		pythonConfig.update("autoComplete.extraPaths", extraPaths,true)
	}



}
