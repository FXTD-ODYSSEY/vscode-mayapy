## 1.0.4  |  2019-9-19

- ISSUE : Pop up an untitled python file need to save or don't save ?   
    > something different in the vscode extension debug mode, after I publish the extension  
    > I create an untitled file and use the `mayacode.sendPythonToMaya` commnad run the code in maya  
    > However, there is not thing need to save in extension debug mode.    
    > so to fix the bug, I refer to the `mayacode` source code and use the temp file to fix the bug.    
- change the Debug configuration attribute `MayaDebugMode` to `MayaDebugFile` which save the current debug file


## 1.0.3  |  2019-9-19

- fix the readme markdown dsiplay issue

## 1.0.2  |  2019-9-19

- split the origin cmds completion file to multiple py file for faster intellisense  
- imporve the readme document content and add the gif to explain how extension work  

## 1.0.1  |  2019-9-19

- post the extension on the marketplace

## 1.0.0  |  2019-9-18

- depend on the `python extension` and the `mayaCode extension`
- add the autocomplete python file for intellisense
- integrate the ptvsd debug module for python remote debugging in Maya

