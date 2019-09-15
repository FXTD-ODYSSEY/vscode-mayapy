/*---------------------------------------------------------
 * Copyright (C) Microsoft Corporation. All rights reserved.
 *--------------------------------------------------------*/

import * as vscode from 'vscode';

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

	// NOTE Python Extension API 测试
	let pythonExt = vscode.extensions.getExtension('ms-python.python');
	// let api = pythonExt.exports;
	let pythonConfig = vscode.workspace.getConfiguration("python")
	let pythonPath = pythonConfig.get("pythonPath")

	Logger.info(`pythonPath: ${pythonPath}`);


	// Logger.info(`pythonExt.id: ${pythonExt.id}`);
	// Logger.info(`pythonExt.extensionPath: ${pythonExt.extensionPath}`);
	// Logger.info(`api: ${Object.keys(api)}`);
	// api.ready.then(values => {
	// 	Logger.info(`=====================================`);
	// 	Logger.info(`==========extension ready============`);
	// 	Logger.info(`=====================================`);
	// 	Logger.info(`values : ${typeof values}`);
	// 	Logger.info(`values : ${Object.keys(values)}`); 
	// 	Logger.info(`values.length : ${Object.keys(values).length}`); 
	// 	for (const key in values) {
	// 		Logger.info(`key : ${key}`); 
	// 		Logger.info(`typeof : ${typeof key}`); 
	// 		Logger.info(`hasOwnProperty : ${values.hasOwnProperty(key)}`); 
	// 	}
	// 	Logger.info(`=====================================`); 
	// 	Logger.info(`=====================================`); 
	// 	Logger.info(`=====================================`); 
	// 	let pythonConfig = vscode.workspace.getConfiguration("python")
	// 	let pythonPath = pythonConfig.get("pythonPath")
	// 	Logger.info(`pythonConfig : ${pythonConfig}`); 
	// 	Logger.info(`pythonConfig keys : ${Object.keys(pythonConfig)}`); 
	// 	for (const key in pythonConfig) {
	// 		Logger.info(`key : ${key}`);
	// 		Logger.info(`typeof : ${typeof key}`);
	// 		Logger.info(`hasOwnProperty : ${values.hasOwnProperty(key)}`);
	// 	}
	// 	Logger.info(`pythonPath : ${pythonPath}`); 
	// })

}
