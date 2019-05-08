from tkinter import*


int_window = Tk()
int_window.title('Simple Integration Methods GUI')
left_main_frame = Frame(int_window)
right_main_frame = Frame(int_window)

testL = Label(left_main_frame, text = "Left")

functions_label = Label(right_main_frame, text = "Function:", bd = 1, relief = "solid", width=12, anchor = W)
interval_label = Label(right_main_frame, text = "Intervals and n:", bd = 1, relief = "solid", width=12, anchor = W)
method_label = Label(right_main_frame, text = "Methods:", bd = 1, relief = "solid", width=12, anchor = W)
testL.grid(row = 0)
functions_label.grid(row = 0, padx=10, pady=10)
interval_label.grid(row = 1, padx=10, pady=10)
method_label.grid(row = 2,padx=10, pady=10)

left_main_frame.grid(row = 0, column = 0)
right_main_frame.grid(row = 0, column = 1)




int_window.mainloop()