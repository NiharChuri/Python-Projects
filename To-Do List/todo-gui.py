import FreeSimpleGUI.window
import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Enter a task: ")
textInput = fsg.InputText(tooltip="Enter a Task")
addTodoBtn  =fsg.Button("Add to list")
window = fsg.Window("To-Do App", layout=[[label, textInput], [addTodoBtn]])
window.read()
window.close()