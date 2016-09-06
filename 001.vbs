
set wshell = Wscript.CreateObject("Wscript.Shell")
set fso = CreateObject("Scripting.FileSystemObject")
set fn=fso.GetFolder(fso.GetParentFolderName(Wscript.ScriptFullName))
Wshell.Run "hch.py"
Wshell.Run "0141111687.py"
Wshell.Run "0141113269.py"
delay(500000)
Wshell.Run "½Å±¾.exe"
Wshell.Run "002.vbs"
                                 