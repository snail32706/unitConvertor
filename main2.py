import tkinter as tk
import numpy as np
import mathTool as mathTool

class UnitConverterUI:
    
    def __init__(self, master):
        self.master = master
        master.title("Physical Unit Convertor")
        master.geometry('700x550')

        # title
        heading = tk.Label(master , text = "Energy Conversion" , font = 'Verdana 30 bold')
        heading.place(relx=0.5, rely=0.07, anchor=tk.CENTER)

        # top
        self.add_sum_button = tk.Button(master, text="clear", command=self.clear_total, font=("Arial", 16), bg='#87CEEB')
        self.add_sum_button.place(relx=0.17, rely=0.18, anchor=tk.CENTER, width=70, height=35)

        self.add_clear_button = tk.Button(master, text='convert', command=self.calculate_total, font=("Arial", 16), bg="yellow")
        self.add_clear_button.place(relx=0.3, rely=0.18, anchor=tk.CENTER, width=110, height=35)

        output_unit = tk.Label(master, text="output unit:", font=("Arial", 14), fg="white")
        output_unit.place(relx=0.6, rely=0.18, anchor=tk.CENTER)

        self.select1_output_unit = tk.StringVar()
        self.select1_output_unit.set('eV')
        select1_menu = tk.OptionMenu(master, self.select1_output_unit, "eV", "J")
        select1_menu.place(relx=0.72, rely=0.18, anchor=tk.CENTER, width=70, height=30)

        # 新增空間
        self.entry_frame = tk.Frame(master)
        self.entry_frame.place(relx=0.1, rely=0.24, relwidth=0.8, relheight=0.56)

        self.vector_num = 8
        for i in range(self.vector_num):
            self.__dict__[f'var_checkbox{i+1}'] = tk.BooleanVar()
            self.__dict__[f'var_checkbox{i+1}'].set(False)
            checkbox = tk.Checkbutton(self.entry_frame, variable=self.__dict__[f'var_checkbox{i+1}'], onvalue=True, offvalue=False)
            checkbox.grid(row=i, column=0, padx=5, pady=5)

            self.__dict__[f'entry_in{i+1}'] = tk.Entry(self.entry_frame, bg="white", fg="black")
            self.__dict__[f'entry_in{i+1}'].grid(row=i, column=1, padx=5, pady=5)

            self.__dict__[f'unit{i+1}'] = tk.StringVar()
            self.__dict__[f'unit{i+1}'].set("K")
            select_menu = tk.OptionMenu(self.entry_frame, self.__dict__[f'unit{i+1}'],  "K", "Hz", "nm")
            select_menu.grid(row=i, column=2, padx=5, pady=5)

            self.__dict__[f'entry_out{i+1}'] = tk.Entry(self.entry_frame, bg="black", fg="white")
            self.__dict__[f'entry_out{i+1}'].grid(row=i, column=3, padx=5, pady=5)

            self.__dict__[f'label{i+1}'] = tk.Label(self.entry_frame, text="eV", font=("Arial", 12), fg="white")
            self.__dict__[f'label{i+1}'].grid(row=i, column=4, padx=5, pady=5)

        # 最底下
        word = tk.Label(master, text="summention =", font=("Arial", 18), fg="white")
        word.place(relx=0.25, rely=0.89, anchor=tk.CENTER)

        self.summention_entry = tk.Entry(master, bg="#D3D3D3", fg='black')
        self.summention_entry.place(relx=0.56, rely=0.89, anchor=tk.CENTER, width=280, height=70)

        self.summention_unit = tk.Label(master, text="eV", font=("Arial", 18), fg="white")
        self.summention_unit.place(relx=0.79, rely=0.89, anchor=tk.CENTER)
        
        
    def get_checkbox(self):
        
        select_list = []
        for i in range(self.vector_num):
            select_list.append(self.__dict__[f'var_checkbox{i+1}'].get())
        return select_list

    def get_inputVlaue(self):
        
        entry_input_value = []
        for i in range(self.vector_num):
            entry_input_value.append(self.__dict__[f'entry_in{i+1}'].get())
        return entry_input_value

    def get_selectUnit(self):
        
        unit_input_list = []
        for i in range(self.vector_num):
            unit_input_list.append(self.__dict__[f'unit{i+1}'].get())
        return unit_input_list
        
    def calculate_total(self):
        checkbox = self.get_checkbox()
        vlue_in  = self.get_inputVlaue()
        unit_in  = self.get_selectUnit()
        unit_out = self.select1_output_unit.get()
        totle = 0
        
        for i in range(self.vector_num):
            '''
            output_value type: float or str.
            if vlue_in[i] isn't int or float return ''.
            '''
            output_value, _unit = mathTool.Unit_Convertor_Math(vlue_in[i], unit_in[i], unit_out).unit_convertor()

            self.__dict__[f'entry_out{i+1}'].delete(0, tk.END)
            self.__dict__[f'entry_out{i+1}'].insert(0, output_value)

            self.__dict__[f'label{i+1}'].config(text=f'{unit_out}')
            
            if checkbox[i] == True:
                if isinstance(output_value, str):
                    continue
                totle += output_value

        self.summention_entry.delete(0, tk.END)
        self.summention_entry.insert(0, totle)
        self.summention_unit.config(text=f'{unit_out}')

    def clear_total(self):

        for i in range(self.vector_num):
            self.__dict__[f'var_checkbox{i+1}'].set(False)

            self.__dict__[f'entry_in{i+1}'].delete(0, tk.END)
            self.__dict__[f'entry_out{i+1}'].delete(0, tk.END)
        self.summention_entry.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    app = UnitConverterUI(root)
    root.mainloop()
