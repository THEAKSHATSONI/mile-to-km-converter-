from tkinter import*

# # making Screen
# window = Tk()
# window.title("Mile to Km Converter")
# window.minsize(width=300,height=300)
#
# # # making layout
# lable = Label(text="")
# lable.grid(row=0,column=0)
#
#
# # # taking Input
# input = Entry(width=10)
# input.place(x=120,y=50)
# input.get()
#
# # Making "Miles" text
# miles = Label(text="Miles")
# miles.place(x=210,y=50)
#
#
# # Making "is equal text" text
# is_ = Label(text="is equal to")
# is_.place(x=10,y=100)
#
#
# def mile_to_km():
#     print('Sucessful')
#     # 1 mile = 1.609344 kilometers
#     new_input = round(float(input.get())*1.609344,2)
#     zero.config(text = new_input)
#
#
#
#
# # Making "0" text
# zero = Label(text="0")
# zero.place(x=150,y=100)
#
#
# # Making "Km" text
# Km = Label(text="Km")
# Km.place(x=210,y=100)
#
#
# # # making Button
# button =Button(text ="Calculate",command=mile_to_km)
# button.place(x=120,y=150)
#
#
# # For making the screen visible
# window.mainloop()


# different code

def miles_to_km():
    miles = miles_input.get()
    km = float(miles)*1.609
    Kilometer_result_label.config(text=f"{km}")


window =Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20,pady=20)

miles_input = Entry(width=9)
miles_input.grid(column=1,row=0)

miles_lable = Label(text="Mles")
miles_lable.grid(column=2,row=0)

is_equal_lable = Label(text="is equal to")
is_equal_lable.grid(column=0,row=1)

Kilometer_result_label = Label(text="0")
Kilometer_result_label.grid(column=1,row=1)

Kilometer_label = Label(text="Km")
Kilometer_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=1,row=2)

window.mainloop()