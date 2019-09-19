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
const net_1 = require("net");
const net = require('net');
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
    function debug_ptvsd(attach_code) {
        const attachFile = vscode.Uri.parse('untitled:' + path.join(vscode.workspace.rootPath, 'attach.py'));
        return vscode.workspace.openTextDocument(attachFile).then(document => {
            const edit = new vscode.WorkspaceEdit();
            edit.insert(attachFile, new vscode.Position(0, 0), attach_code);
            return vscode.workspace.applyEdit(edit).then(success => {
                if (success) {
                    vscode.window.showTextDocument(document).then(() => {
                        // NOTE 发送当前代码
                        vscode.commands.executeCommand("mayacode.sendPythonToMaya");
                        // NOTE 关闭当前打开的文件
                        vscode.commands.executeCommand("workbench.action.closeActiveEditor");
                        vscode.window.showInformationMessage(`Attempt to import the ptvsd module in maya,
						please wait for a while and try again`);
                    });
                }
                else {
                    vscode.window.showInformationMessage('Debug Attaching File Error!');
                }
            });
        });
    }
    function debug_run(run_code) {
        const debugFile = vscode.Uri.parse('untitled:' + path.join(vscode.workspace.rootPath, 'debug.py'));
        return vscode.workspace.openTextDocument(debugFile).then(document => {
            const edit = new vscode.WorkspaceEdit();
            edit.insert(debugFile, new vscode.Position(0, 0), run_code);
            return vscode.workspace.applyEdit(edit).then(success => {
                if (success) {
                    vscode.window.showTextDocument(document).then(() => {
                        // NOTE 发送当前代码
                        vscode.commands.executeCommand("mayacode.sendPythonToMaya");
                        // NOTE 关闭当前打开的文件
                        vscode.commands.executeCommand("workbench.action.closeActiveEditor");
                    });
                }
                else {
                    vscode.window.showInformationMessage('Debug Running File Error!');
                }
            });
        });
    }
    function debug_func(uri) {
        const ptvsdPath = path.join(path.dirname(__dirname), "py");
        const file_name = path.basename(uri.fsPath, ".py");
        const fileDirname = path.dirname(uri.fsPath);
        const config = vscode.workspace.getConfiguration('mayapy');
        const hostname = config.get("hostname");
        const port = config.get("port");
        // NOTE 连接 ptvsd 代码
        const attach_code = `
import sys
ptvsd_module = r"${ptvsdPath}"
if ptvsd_module not in sys.path:
	sys.path.insert(0,ptvsd_module)

import ptvsd
ptvsd.enable_attach(("${hostname}",${port}))
print("Mayapy Python Debugger : ptvsd module ready\\n")`;
        const run_code = `
current_directory = r"${fileDirname}"
if current_directory not in sys.path:
	sys.path.insert(0,current_directory)

print("Mayapy Python Debugger : debug ${file_name} module\\n")
if '${file_name}' not in globals():
	import ${file_name}
else:
	reload(${file_name})
`;
        let activeDebugSession = vscode.debug.activeDebugSession;
        // NOTE 检查当前 Debug 状态
        if (activeDebugSession) {
            let configuration = activeDebugSession.configuration;
            // NOTE 确认是MayaDebug状态
            if ("MayaDebugMode" in configuration) {
                // NOTE 发送当前代码
                debug_run(run_code);
            }
            else {
                Logger.error(`please stop the current debug mode and try again`);
            }
        }
        else {
            let options = {
                "host": hostname,
                "port": port
            };
            let socket = new net_1.Socket();
            new Promise((resolve, reject) => {
                try {
                    socket.on('error', ex => {
                        reject(ex);
                    });
                    socket.connect(options, () => {
                        resolve(options);
                    });
                }
                catch (ex) {
                    reject(ex);
                }
            }).then((resolve) => {
                socket.destroy();
                Logger.info(`resolve : ${resolve}`);
                Logger.info(`${Object.keys(resolve)}`);
                // NOTE 设置 Debug 设定 | 开启 Debug 模式
                let configuration = {
                    "name": "Maya Python Debugger : Remote Attach",
                    "type": "python",
                    "request": "attach",
                    "port": port,
                    "host": hostname,
                    "pathMappings": [
                        {
                            "localRoot": `${fileDirname}`,
                            "remoteRoot": `${fileDirname}`
                        }
                    ],
                    "MayaDebugMode": true
                };
                vscode.debug.startDebugging(undefined, configuration).then(() => {
                    debug_run(run_code);
                });
            }, (reject) => {
                socket.destroy();
                Logger.info(`reject : ${reject}`);
                debug_ptvsd(attach_code);
            });
        }
    }
    const debug_py = vscode.commands.registerCommand('mayapy.debugPythonFile', (uri) => __awaiter(this, void 0, void 0, function* () {
        const mayaCodeConfig = vscode.workspace.getConfiguration('mayacode');
        const mayahost = mayaCodeConfig.get('hostname');
        const mayaport = mayaCodeConfig.get("mel.port");
        // NOTE 检测 Maya 端口是否开启
        let maya_socket = net.createConnection(mayaport, mayahost).on("error", (e) => {
            maya_socket.destroy();
            // NOTE 端口未开启 提示错误
            Logger.error(`
			Unable to connect to port localhost on Host 7001 in Maya
			Please run the mel command in the maya script editor ↓↓↓
			
			commandPort -n "${mayahost}:${mayaport}" -stp "mel" -echoOutput;

			`);
        }).on("connect", (e) => {
            maya_socket.destroy();
            debug_func(uri);
        }).on("data", (e) => {
            maya_socket.destroy();
        }).on("timeout", (e) => {
            maya_socket.destroy();
        });
    }));
    context.subscriptions.push(debug_py);
}
exports.activate = activate;
//# sourceMappingURL=extension.js.map