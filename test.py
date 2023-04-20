import tkinter as tk
'''
tk add buttum.
can create a new entry.

'''
class UnitConverterUI:
    def __init__(self, master):
        self.master = master
        master.title("Physical Unit Convertor")
        master.geometry('700x550')

        # title
        heading = tk.Label(master , text = "Energy Conversion" , font = 'Verdana 30 bold')
        heading.place(relx=0.5, rely=0.07, anchor=tk.CENTER)

        # top
        self.add_entry_button = tk.Button(master, text="add", command=self.add_entry, font=("Arial", 16), bg='#87CEEB')
        self.add_entry_button.place(relx=0.17, rely=0.18, anchor=tk.CENTER, width=70, height=35)

        self.add_entry_button = tk.Button(master, text='convert', command=self.add_entry, font=("Arial", 16), bg="yellow")
        self.add_entry_button.place(relx=0.3, rely=0.18, anchor=tk.CENTER, width=110, height=35)

        output_unit = tk.Label(master, text="output unit:", font=("Arial", 14), fg="white")
        output_unit.place(relx=0.6, rely=0.18, anchor=tk.CENTER)

        self.select1_output_unit = tk.StringVar()
        self.select1_output_unit.set('eV')
        select1_menu = tk.OptionMenu(master, self.select1_output_unit, 'eV', 'J')
        select1_menu.place(relx=0.72, rely=0.18, anchor=tk.CENTER, width=70, height=30)

        # 新增空間
        self.entry_frame = tk.Frame(master)
        self.entry_frame.place(relx=0.1, rely=0.24, relwidth=0.8, relheight=0.56)

        # 最底下
        word = tk.Label(master, text="summention =", font=("Arial", 18), fg="white")
        word.place(relx=0.25, rely=0.89, anchor=tk.CENTER)

        self.summention_entry = tk.Entry(master, bg="#D3D3D3", fg='black')
        self.summention_entry.place(relx=0.56, rely=0.89, anchor=tk.CENTER, width=280, height=70)
        
    def add_entry(self):

        if self.row_count > 7:
            return

        var           = tk.BooleanVar()
        value_in      = tk.Entry(self.entry_frame)
        unit_in       = tk.OptionMenu(self.entry_frame, tk.StringVar(), "K", "Hz", "nm")
        display_value = tk.Entry(self.entry_frame)
        label_unit    = tk.Label(self.entry_frame, text="unit")

        # 放置元件
        var_checkbox  = tk.Checkbutton(self.entry_frame, variable=var)
        var_checkbox.grid(row=self.row_count, column=0, padx=5, pady=5)
        value_in.grid(row=self.row_count, column=1, padx=5, pady=5)
        unit_in.grid(row=self.row_count, column=2, padx=5, pady=5)
        display_value.grid(row=self.row_count, column=3, padx=5, pady=5)
        label_unit.grid(row=self.row_count, column=4, padx=5, pady=5)

        # 記錄元件
        self.entries.append((var, value_in, unit_in, display_value, label_unit))

        # 調整下一個元件的位置
        self.row_count += 1
        for i in range(len(self.entries) - 1):
            self.entries[i][0].grid(row=i, column=0, padx=5, pady=5)
            self.entries[i][1].grid(row=i, column=1, padx=5, pady=5)
            self.entries[i][2].grid(row=i, column=2, padx=5, pady=5)
            self.entries[i][3].grid(row=i, column=3, padx=5, pady=5)
            tk.Label(self.entry_frame, text="unit").grid(row=i, column=4, padx=5, pady=5)

        self.master.update()  # 刷新畫面
        self.entry_frame.configure(height=(self.row_count + 1) * 50)  # 調整 entry_frame 高度

        # 將焦點放到新的 value_in 上
        value_in.focus()
        print(self.entries)
        

if __name__ == '__main__':
    root = tk.Tk()
    app = UnitConverterUI(root)
    root.mainloop()
