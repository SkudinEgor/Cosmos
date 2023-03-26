import PySimpleGUI as psg
llist = [
    [psg.Text("Write your username"), psg.InputText(key="fieldname", default_text="Name")],
    [psg.OptionMenu(values=(1350, 968, 1077), key="width", default_value=1350), psg.OptionMenu(values=(600, 650, 799, 750), key="height", default_value=750)], 
    [psg.Text("Write your colour"), psg.OptionMenu(values=("red", "green", "blue"), key="fieldcolor", default_value="blue")],  
    [psg.Button("Start", button_color="green"), psg.Button("Exit", button_color="red")]
]
menu = psg.Window("Cosmos", llist)
while 1 == 1:
    read = menu.read()
    event = read[0]   
    value =  read[1]
    print(value)
    if event == "Start" or event == psg.WIN_CLOSED or event == "Exit":
        break
menu.close()