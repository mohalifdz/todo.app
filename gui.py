# https://pypi.org/
# https://pypi.org/project/PySimpleGUI/

import functions
import PySimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo')
add_button = sg.Button('Add')

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
# the layout up, can be modified depends on what to be group in position
window.read()
window.close()