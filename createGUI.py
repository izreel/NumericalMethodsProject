from tkinter import*


int_window = Tk()
int_window.title('Simple Integration Methods GUI')
left_main_frame = Frame(int_window)
right_main_frame = Frame(int_window)
function_string = StringVar()

functions_label = Label(left_main_frame, text = "Function:", bd = 1, relief = "solid", width=12, anchor = W)
functions_entry = Entry(left_main_frame, bd = 1, textvariable = function_string)
interval_label = Label(left_main_frame, text = "Intervals and n:", bd = 1, relief = "solid", width=12, anchor = W)
integrate_button = Button(left_main_frame, text = "Integrate", width = 10, justify = CENTER )

result_label = Label(right_main_frame, text = "Result:", bd = 1, relief = "solid", width=12, anchor = W)
error_label = Label(right_main_frame, text = "% Error:" , bd = 1, relief = "solid", width=12, anchor = W)

functions_label.grid(row = 0, padx=10, pady=10)
functions_entry.grid(row = 0, column = 1, padx=10, pady=10)
interval_label.grid(row = 1, padx=10, pady=10)
integrate_button.grid(row = 3, column = 1, padx=10, pady=10)

result_label.grid(row = 0, padx=10, pady=10)
error_label.grid(row = 1, padx=10, pady=10)

left_main_frame.grid(row = 0, column = 0)
right_main_frame.grid(row = 0, column = 1)

def parseString(function_string):
    temp_string = ""
    for i in function_string:
        if i == "^":
            temp_string = temp_string + "**"
        else:
            temp_string = temp_string + i
    print(temp_string)

int_window.mainloop()
parseString(function_string.get())

