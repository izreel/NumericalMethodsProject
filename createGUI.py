from tkinter import*
from numpy import cos, sin, tan, arccos, arcsin, arctan, exp, pi, sqrt, log
from IntegrationTechniques import Integration

#Function that is used to convert the carat to the correct notation for a user input.
def parseString(function_string):
    temp_string = ""
    for i in function_string:
        if i == "^":
            temp_string = temp_string + "**"
        else:
            temp_string = temp_string + i
    return temp_string

#Callback function that will be called upon the click on a button from the user.
def integrate():
    error = FALSE # boolean variable to check if iterations n is not even for certain methods.
    code_error_string.set("")
    result_string.set("")
    error_string.set("")
    # if statement to check if no function is inputted
    if (function_string.get() == ""):
        code_error_string.set("Missing function to integrate.")
    else:
        #convert ^ to **
        new_string = parseString(function_string.get())
        answer = 0.0 #initialize the result variable
        error_return = "" #initialize the error different variable
        if (lowerlim_string.get() == "") or (upperlim_string.get() == ""):  #another statement to check if limits are missing
            code_error_string.set("Missing an upper or lower limit.")
        else:    
            # Integrate using a method based on the choice of the user from the combobox 
            if integration_type_string.get() == "Midpoint Rule":
                answer, error_return = integration_object.midpoint_rule(eval(lowerlim_string.get()), eval(upperlim_string.get()), new_string)
            
            elif integration_type_string.get() == "Trapezoidal Rule":
                answer, error_return = integration_object.trapezoidal_rule(eval(lowerlim_string.get()), eval(upperlim_string.get()), new_string)
            
            elif integration_type_string.get() == "Simpson Rule":
                answer, error_return = integration_object.simpson_rule(eval(lowerlim_string.get()), eval(upperlim_string.get()), new_string)
            
            elif integration_type_string.get() == "Composite Midpoint Rule":
                if (iterations_string.get() == ""): 
                    code_error_string.set("Missing number of iterations.")
                else:
                    #
                    if (int(iterations_string.get()) % 2 ): # n must be even
                        error = TRUE
                    else:
                        answer, error_return = integration_object.composite_midpoint_rule(eval(lowerlim_string.get()), eval(upperlim_string.get()), new_string, int(iterations_string.get()))
            
            elif integration_type_string.get() == "Composite Trapezoidal Rule":
                if (iterations_string.get() == ""): 
                    code_error_string.set("Missing number of iterations.")
                else:
                    answer, error_return = integration_object.composite_trapezoidal_rule(eval(lowerlim_string.get()), eval(upperlim_string.get()), new_string, int(iterations_string.get()))
            
            elif integration_type_string.get() == "Composite Simpson Rule":
                if (iterations_string.get() == ""): 
                    code_error_string.set("Missing number of iterations.")
                else:
                    if (int(iterations_string.get()) % 2 ): # n must be even
                        error = TRUE
                    else:
                        answer, error_return = integration_object.composite_simpson_rule(eval(lowerlim_string.get()), eval(upperlim_string.get()), new_string, int(iterations_string.get()))
            if (error):
                code_error_string.set("Number of iterations cannot be odd for Simpson's Rule.")
            
            else:
                answer = float("{0:.3f}".format(answer))
                result_string.set(str(answer)) # Set StringVar that will now be called by the GUI
                error_string.set(error_return)   

    
# Initialize all the needed variables and the root frame.
integration_object = Integration()
int_window = Tk()
int_window.title('Simple Integration Methods GUI')
int_window.geometry("640x400")
#Create two frames for the main window
left_main_frame = Frame(int_window) 
right_main_frame = Frame(int_window)
#StringVars for text fields that users will use.
function_string = StringVar()
lowerlim_string = StringVar()
upperlim_string = StringVar()
iterations_string = StringVar()
integration_type_string = StringVar()
integration_list = ["Midpoint Rule", "Trapezoidal Rule", "Simpson Rule", "Composite Midpoint Rule", "Composite Trapezoidal Rule", "Composite Simpson Rule"]
new_list = []
result_string = StringVar()
error_string = StringVar()
code_error_string = StringVar()
integration_type_string.set(integration_list[0])

#Creating all the labels and textfields. Label() creates a label and Entry() creates a text field for input. OptionMenu() is the combobox with options of all methods.
#Message is used to display a dynamic message using StringVar and the callback method made earlier.
functions_label = Label(left_main_frame, text = "Function:", relief = "solid", width=12, anchor = W)
functions_entry = Entry(left_main_frame, textvariable = function_string, width = 40)
interval_label = Label(left_main_frame, text = "Limits and N:", relief = "solid", width=12, anchor = W)
lowerlim_entry = Entry(left_main_frame, textvariable = lowerlim_string, width = 10)
upperlim_entry = Entry(left_main_frame, textvariable = upperlim_string, width = 10)
iteration_entry = Entry(left_main_frame, textvariable = iterations_string, width = 10)
integration_label = Label(left_main_frame, text = "Type of Integration:", relief = "solid", width=15, anchor = W)
integration_box = OptionMenu(left_main_frame, integration_type_string, *integration_list)
code_error_message = Message(left_main_frame, textvariable = code_error_string, relief = "solid", width = 100, bg = "red", justify = CENTER)
#Button used to call the callback function.
integrate_button = Button(left_main_frame, text = "Integrate", width = 12, justify = CENTER , command = integrate)
#The right side of the window. Used to display result and difference.
result_label = Label(right_main_frame, text = "Result for this Rule:", relief = "solid", width=30)
result_message = Message(right_main_frame, textvariable = result_string, relief = "solid", width = 50, anchor = W)
error_label = Label(right_main_frame, text = "Error Difference of Using this Rule:" , relief = "solid", width=30)
error_message = Message(right_main_frame, textvariable = error_string, relief = "solid", width = 159, anchor = W )

#Placing everything into the window using the grid manager.

left_main_frame.grid(row = 0, column = 0, sticky = "nsew")
right_main_frame.grid(row = 0, column = 1, sticky = "nsew")

functions_label.grid(row = 0, column = 0, padx=10, pady=10)
functions_entry.grid(row = 0, column = 1, columnspan = 3, padx=10, pady=10, sticky = W)
interval_label.grid(row = 1, column = 0, padx=10, pady=10)
lowerlim_entry.grid(row = 1, column = 1, padx=10, sticky = W)
upperlim_entry.grid(row = 1, column = 2, padx=10, sticky = W)
iteration_entry.grid(row = 1, column = 3, padx=10, sticky = W)
integration_label.grid(row = 2, column =0 , padx = 10, pady = 10, sticky = W)
integration_box.grid(row =2 , column =1 ,columnspan = 3, padx = 10, pady = 10)
code_error_message.grid(row = 3, column = 1, columnspan = 3, padx = 10, pady = 10)

integrate_button.grid(row = 4, column = 1, columnspan = 3, padx=10, pady=10)

result_label.grid(row =0, column = 0, padx = 10, pady = 10, sticky = N)
result_message.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = N)
error_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = N)
error_message.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = N)


left_main_frame.grid(row = 0, column = 0)
right_main_frame.grid(row = 0, column = 1)

#Show window
int_window.mainloop()

