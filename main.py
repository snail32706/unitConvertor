import tkinter as tk
import numpy as np


class Unit_Convertor_Math:
    
    def __init__(self, inputNumber, unit1, unit2):
        self.num = inputNumber
        self.unit1 = unit1
        self.unit2 = unit2
        self.check_input()

    def check_input(self):
        if not isinstance(self.num, (float, int)):
            return 'type Error! Argument "num" must be int or float.'
        if self.unit1 not in ["K", "Hz", "nm"]:
            return 'type Error! Argument " unit1" must be "K", "Hz", "nm"'
        if self.unit2 not in ["eV", "J"]:
            return 'type Error! Argument " unit2" must be "eV", "J"'
        return True
    
    def unit_convertor(self):

        if self.check_input() != True:
            print(self.check_input())

        e = 1.6e-19
        k = 1.38e-23    # (J/K)
        h = 6.626e-34   # (J*s)
        hc = 1240       # (eV*nm)

        def Hz_to_eV(num):
            return h * num / e

        def Hz_to_J(num):
            return h * num

        def nm_to_eV(num):
            return hc / num

        def nm_to_J(num):
            return hc / num * e

        def K_to_eV(num):
            return num * k / e

        def K_to_J(num):
            return num * k

        conversion_functions = {
            ('Hz', 'eV'): Hz_to_eV,
            ('Hz', 'J'): Hz_to_J,
            ('nm', 'eV'): nm_to_eV,
            ('nm', 'J'): nm_to_J,
            ('K', 'eV'): K_to_eV,
            ('K', 'J'): K_to_J,
        }

        func = conversion_functions[(self.unit1, self.unit2)]
        return func(self.num), self.unit2

class UnitConverterUI:
    
    def __init__(self, master):
        self.master = master
        master.title("Physical Unit Convertor")
        master.geometry('500x300')
        
        self.heading = tk.Label(master , text = "Energy Conversion" , font = 'Verdana 25 bold')
        self.heading.place(x=120 , y=20)

        # 輸入框
        self.input_entry = tk.Entry(master, bg='#f3f3f3', fg='black')
        self.input_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER, width=260, height=30)
        
        # 選擇對話筐 1
        self.select1_var = tk.StringVar()
        self.select1_var.set("K")
        self.select1_optionmenu = tk.OptionMenu(master, self.select1_var, "K", "Hz", "nm")
        self.select1_optionmenu.place(relx=0.38, rely=0.47, anchor=tk.CENTER, width=90, height=30)
        
        self.word = tk.Label(master , text = "to" , font = 'Verdana 12')
        self.word.place(relx=0.5, rely=0.47, anchor=tk.CENTER)
        
        # 選擇對話筐 2
        self.select2_var = tk.StringVar()
        self.select2_var.set("eV")
        self.select2_optionmenu = tk.OptionMenu(master, self.select2_var, "eV", "J")
        self.select2_optionmenu.place(relx=0.62, rely=0.47, anchor=tk.CENTER, width=90, height=30)
        
        # 按鈕
        self.start_button = tk.Button(master, text="Start", command=self.convert_units, bg="#ffff4e", relief=tk.RAISED, borderwidth=2)
        self.start_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER, width=50, height=35)

        # 輸出框
        self.output_entry = tk.Entry(master, bg="#D3D3D3", fg='black')
        self.output_entry.place(relx=0.5, rely=0.79, anchor=tk.CENTER, width=260, height=58)
        

    def convert_units(self):

        input_value  = float(self.input_entry.get())
        select1_unit = self.select1_var.get()
        select2_unit = self.select2_var.get()
        
        output_value, _ = Unit_Convertor_Math(input_value, select1_unit, select2_unit).unit_convertor()
        output_value = str(output_value)

        show_out  = f"{input_value} {select1_unit} = {output_value[0:8]} {select2_unit}"
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, show_out)


if __name__ == '__main__':
    root = tk.Tk()
    app = UnitConverterUI(root)
    root.mainloop()
