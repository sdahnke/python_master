from pywinauto import Application

## app.UntitledNotepad.menu_select("Datei->Speichern")
## app.AboutNotepad.OK.click()
## app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)

app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" ')
app.Dialog.Wait('ready')
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces=True)
