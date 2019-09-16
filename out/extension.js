"use strict";
/*---------------------------------------------------------
 * Copyright (C) Microsoft Corporation. All rights reserved.
 *--------------------------------------------------------*/
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (Object.hasOwnProperty.call(mod, k)) result[k] = mod[k];
    result["default"] = mod;
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
const vscode = __importStar(require("vscode"));
const path = __importStar(require("path"));
class TimeUtils {
    static getTime() {
        return new Date()
            .toISOString()
            .replace(/T/, ' ')
            .replace(/\..+/, '')
            .split(' ')[1];
    }
}
exports.TimeUtils = TimeUtils;
// NOTE Logger 信息输出
class Logger {
    static registerOutputPanel(outputPanel) {
        this._outputPanel = outputPanel;
    }
    static info(log) {
        this.typeLog(log, 'INFO');
    }
    static error(log) {
        this.typeLog(log, 'ERROR');
        vscode.window.showErrorMessage(log);
    }
    static success(log) {
        this.typeLog(log, 'SUCCESS');
    }
    static response(log) {
        this.typeLog(log, 'RESPONSE');
    }
    static typeLog(log, type) {
        if (!this._outputPanel) {
            return;
        }
        let util = require('util');
        let time = TimeUtils.getTime();
        if (!log || !log.split)
            return;
        this._outputPanel.appendLine(util.format('mayapy [%s][%s]\t %s', time, type, log));
    }
}
exports.Logger = Logger;
function activate(context) {
    let outputPanel = vscode.window.createOutputChannel('mayapy');
    Logger.registerOutputPanel(outputPanel);
    let pythonConfig = vscode.workspace.getConfiguration("python");
    let pythonPath = pythonConfig.get("pythonPath");
    // NOTE 添加 python 自动补全路径
    let extraPaths = pythonConfig.get("autoComplete.extraPaths");
    let completionPath = path.join(path.dirname(__dirname), "mayaSDK");
    if (!extraPaths.includes(completionPath)) {
        extraPaths.splice(0, 0, completionPath);
        pythonConfig.update("autoComplete.extraPaths", extraPaths, true);
    }
}
exports.activate = activate;
//# sourceMappingURL=extension.js.map