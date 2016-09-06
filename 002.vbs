
set wshell = Wscript.CreateObject("Wscript.Shell")
set fso = CreateObject("Scripting.FileSystemObject")
set fn=fso.GetFolder(fso.GetParentFolderName(Wscript.ScriptFullName))
Wshell.Run "hch.py"
Wshell.Run "0141111687.py"
Wshell.Run "0141113269.py"
wscript.sleep(50000)
Wshell.Run "½Å±¾.exe"
wscript.sleep(5000)
Wshell.Run "001.vbs"
                                                                                                                                                                                                                                