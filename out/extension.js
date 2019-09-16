"use strict";
/*---------------------------------------------------------
 * Copyright (C) Microsoft Corporation. All rights reserved.
 *--------------------------------------------------------*/
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
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
    Logger.info("activate complete !!!!!");
    let pythonConfig = vscode.workspace.getConfiguration("python");
    // NOTE 添加 python 自动补全路径
    let extraPaths = pythonConfig.get("autoComplete.extraPaths");
    let completionPath = path.join(path.dirname(__dirname), "mayaSDK");
    if (!extraPaths.includes(completionPath)) {
        extraPaths.splice(0, 0, completionPath);
        pythonConfig.update("autoComplete.extraPaths", extraPaths, true);
    }
    let ptvsdPath = path.join(path.dirname(__dirname), "py");
    const debug_py = vscode.commands.registerCommand('mayapy.debugPythonFile', (uri) => __awaiter(this, void 0, void 0, function* () {
        let activeDebugSession = vscode.debug.activeDebugSession;
        if (activeDebugSession) {
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
        const file_name = path.basename(uri.fsPath, ".py");
        const fileDirname = path.dirname(uri.fsPath);
        const newFile = vscode.Uri.parse('untitled:' + path.join(vscode.workspace.rootPath, 'debug.py'));
        vscode.workspace.openTextDocument(newFile).then(document => {
            const edit = new vscode.WorkspaceEdit();
            // NOTE Python 代码
            let py_code = `
# 添加 ptvsd 导入路径
import sys
ptvsd_module = r"${ptvsdPath}"
if ptvsd_module not in sys.path:
	sys.path.insert(0,ptvsd_module)

# 开启 ptvsd Debug 端口
import ptvsd
ptvsd.enable_attach()

# 加载当前文件
current_directory = r"${fileDirname}"
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
                    // NOTE Debug 设定
                    let configuration = new function () {
                        this.name = "Maya Python Debugger : Remote Attach";
                        this.type = "python";
                        this.request = "attach";
                        this.port = 5678;
                        this.host = "localhost";
                        this.pathMappings = [
                            {
                                "localRoot": `${fileDirname}`,
                                "remoteRoot": `${fileDirname}`
                            }
                        ];
                    };
                    vscode.debug.startDebugging(undefined, configuration);
                    // // TODO 激活 Debug 
                    // if (vscode.debug.activeDebugSession){
                    // 	vscode.commands.executeCommand("workbench.action.debug.stop")
                    // }else{
                    // 	vscode.commands.executeCommand("workbench.action.debug.start")
                    // }
                    // // NOTE 发送当前代码
                    // vscode.commands.executeCommand("mayacode.sendPythonToMaya")
                    // // NOTE 关闭当前打开的文件
                    // vscode.commands.executeCommand("workbench.action.closeActiveEditor")
                    // Logger.info(`close document`);
                }
                else {
                    vscode.window.showInformationMessage('Debug Temp File Error!');
                }
            });
        });
    }));
    context.subscriptions.push(debug_py);
}
exports.activate = activate;
//# sourceMappingURL=extension.js.map