import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_198=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_198["font"] = ft
        GLabel_198["fg"] = "#333333"
        GLabel_198["justify"] = "center"
        GLabel_198["text"] = "Registro"
        GLabel_198["relief"] = "ridge"
        GLabel_198.place(x=200,y=40,width=70,height=25)

        GLabel_265=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_265["font"] = ft
        GLabel_265["fg"] = "#333333"
        GLabel_265["justify"] = "center"
        GLabel_265["text"] = "Nombre"
        GLabel_265.place(x=70,y=80,width=70,height=25)

        GLabel_206=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_206["font"] = ft
        GLabel_206["fg"] = "#333333"
        GLabel_206["justify"] = "center"
        GLabel_206["text"] = "Apellido"
        GLabel_206.place(x=70,y=130,width=70,height=25)

        GLabel_706=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_706["font"] = ft
        GLabel_706["fg"] = "#333333"
        GLabel_706["justify"] = "center"
        GLabel_706["text"] = "Email"
        GLabel_706.place(x=70,y=180,width=70,height=25)

        GLabel_849=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_849["font"] = ft
        GLabel_849["fg"] = "#333333"
        GLabel_849["justify"] = "center"
        GLabel_849["text"] = "Telefono"
        GLabel_849.place(x=70,y=230,width=70,height=25)

        GLabel_355=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_355["font"] = ft
        GLabel_355["fg"] = "#333333"
        GLabel_355["justify"] = "center"
        GLabel_355["text"] = "Nacionalidad"
        GLabel_355.place(x=50,y=290,width=70,height=25)

        GLineEdit_501=tk.Entry(root)
        GLineEdit_501["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_501["font"] = ft
        GLineEdit_501["fg"] = "#333333"
        GLineEdit_501["justify"] = "center"
        GLineEdit_501["text"] = ""
        GLineEdit_501.place(x=150,y=80,width=184,height=30)

        GLineEdit_718=tk.Entry(root)
        GLineEdit_718["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_718["font"] = ft
        GLineEdit_718["fg"] = "#333333"
        GLineEdit_718["justify"] = "center"
        GLineEdit_718["text"] = ""
        GLineEdit_718.place(x=150,y=130,width=182,height=30)

        GLineEdit_943=tk.Entry(root)
        GLineEdit_943["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_943["font"] = ft
        GLineEdit_943["fg"] = "#333333"
        GLineEdit_943["justify"] = "center"
        GLineEdit_943["text"] = ""
        GLineEdit_943.place(x=150,y=180,width=180,height=30)

        GLineEdit_484=tk.Entry(root)
        GLineEdit_484["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_484["font"] = ft
        GLineEdit_484["fg"] = "#333333"
        GLineEdit_484["justify"] = "center"
        GLineEdit_484["text"] = ""
        GLineEdit_484.place(x=150,y=230,width=181,height=30)

        GListBox_544=tk.Listbox(root)
        GListBox_544["borderwidth"] = "1px"
        GListBox_544["cursor"] = "spider"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_544["font"] = ft
        GListBox_544["fg"] = "#333333"
        GListBox_544["justify"] = "center"
        GListBox_544.place(x=150,y=290,width=181,height=30)
        GListBox_544["exportselection"] = "1"
        GListBox_544["listvariable"] = "C"
        GListBox_544["selectmode"] = "multiple"
        GListBox_544["setgrid"] = "True"

        GLabel_177=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_177["font"] = ft
        GLabel_177["fg"] = "#333333"
        GLabel_177["justify"] = "center"
        GLabel_177["text"] = "Sexo"
        GLabel_177.place(x=60,y=340,width=70,height=25)

        GRadio_395=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_395["font"] = ft
        GRadio_395["fg"] = "#333333"
        GRadio_395["justify"] = "center"
        GRadio_395["text"] = "Masculino"
        GRadio_395.place(x=140,y=340,width=86,height=25)
        GRadio_395["command"] = self.GRadio_395_command

        GRadio_476=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_476["font"] = ft
        GRadio_476["fg"] = "#333333"
        GRadio_476["justify"] = "center"
        GRadio_476["text"] = "Femenino"
        GRadio_476.place(x=240,y=340,width=86,height=25)
        GRadio_476["command"] = self.GRadio_476_command

        GButton_249=tk.Button(root)
        GButton_249["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_249["font"] = ft
        GButton_249["fg"] = "#000000"
        GButton_249["justify"] = "center"
        GButton_249["text"] = "INICIAR"
        GButton_249.place(x=170,y=390,width=70,height=25)
        GButton_249["command"] = self.GButton_249_command

    def GRadio_395_command(self):
        print("command")


    def GRadio_476_command(self):
        print("command")


    def GButton_249_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
