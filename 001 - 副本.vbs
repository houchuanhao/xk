
set wshell = Wscript.CreateObject("Wscript.Shell")
set fso = CreateObject("Scripting.FileSystemObject")
set fn=fso.GetFolder(fso.GetParentFolderName(Wscript.ScriptFullName))
wscript.sleep(50000)
Wshell.Run "change1.py"
Wshell.Run "change2.py"
                                 