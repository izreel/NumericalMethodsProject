from tkinter import*
from IntegrationTechniques import Integration

def parseString(function_string):
    temp_string = ""
    for i in function_string:
        if i == "^":
            temp_string = temp_string + "**"
        else:
            temp_string = temp_string + i
    print(temp_string)
    return temp_string



def integrate():
    new_string = parseString(function_string.get())
   
    if integration_type_string.get() == "Midpoint Rule":
        print(integration_object.midpoint_rule(int(lowerlim_string.get()), int(upperlim_string.get()), new_string, int(iterations_string.get())))
    

integration_object = Integration()
int_window = Tk()
int_window.title('Simple Integration Methods GUI')
left_main_frame = Frame(int_window)
right_main_frame = Frame(int_window)
function_string = StringVar()
lowerlim_string = StringVar()
upperlim_string = StringVar()
iterations_string = StringVar()
integration_type_string = StringVar()
integration_list = ["Midpoint Rule", "Trapezoidal Rule", "Simpson Rule", "Trapezoidal Rule", "Composite Trapezoidal Rule", "Composite Simpson Rule"]
new_list = []
result_string = StringVar()
error_string = StringVar()
integration_type_string.set(integration_list[0])

functions_label = Label(left_main_frame, text = "Function:", relief = "solid", width=12, anchor = W)
functions_entry = Entry(left_main_frame, textvariable = function_string, width = 40)
interval_label = Label(left_main_frame, text = "Limits and N:", relief = "solid", width=12, anchor = W)
lowerlim_entry = Entry(left_main_frame, textvariable = lowerlim_string, width = 10)
upperlim_entry = Entry(left_main_frame, textvariable = upperlim_string, width = 10)
iteration_entry = Entry(left_main_frame, textvariable = iterations_string, width = 10)
integration_label = Label(left_main_frame, text = "Type of Integration:", relief = "solid", width=12, anchor = W)
integration_box = OptionMenu(left_main_frame, integration_type_string, *integration_list)



integrate_button = Button(left_main_frame, text = "Integrate", width = 12, justify = CENTER , command = integrate)

result_label = Label(right_main_frame, text = "Result for Midpoint Rule:", relief = "solid", width=30, anchor = W)
result_message = Message(right_main_frame, textvariable = result_string, relief = "solid", width = 30)
error_label = Label(right_main_frame, text = "% Error of Midpoint Rule:" , relief = "solid", width=30, anchor = W)
error_message = Message(right_main_frame, textvariable = error_string, relief = "solid", width = 15)

functions_label.grid(row = 0, column = 0, padx=10, pady=10)
functions_entry.grid(row = 0, column = 1, columnspan = 3, padx=10, pady=10, sticky = W)
interval_label.grid(row = 1, column = 0, padx=10, pady=10)
lowerlim_entry.grid(row = 1, column = 1, padx=10, sticky = W)
upperlim_entry.grid(row = 1, column = 2, padx=10, sticky = W)
iteration_entry.grid(row = 1, column = 3, padx=10, sticky = W)
integration_label.grid(row = 3, column =0 , padx = 10, pady = 10)
integration_box.grid(row = 3, column =1 ,columnspan = 3, padx = 10, pady = 10)

integrate_button.grid(row = 4, column = 1, columnspan = 3, padx=10, pady=10)

result_label.grid(row = 0, padx=10, pady=10)
result_message.grid(row = 0, column = 1, padx = 10, pady = 10)
error_label.grid(row = 1, padx=10, pady=10)
error_message.grid(row = 1, column = 1, padx = 10, pady = 10)


left_main_frame.grid(row = 0, column = 0)
right_main_frame.grid(row = 0, column = 1)

int_window.mainloop()

#print(integration_object.composite_simpson(0, 10, parseString(function_string.get()), 10))