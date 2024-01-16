from tkinter import *

window=Tk()
window.minsize(width=350,height=100)


#weight label
weight_label=Label(text="Enter your weight")
weight_label.pack()

#weight entry
weight_entry=Entry()
weight_entry.pack()

#height label
height_label=Label(text="Enter your height")
height_label.pack()

#height entry
height_entry=Entry()
height_entry.pack()

#texts

myList=[]
#calculate
def calculate_bmi():
    myList.append(weight_entry.get())
    myList.append(height_entry.get())
    print(myList)
    weight_int=float(myList[0])
    height_int=float(myList[1])
    bmi_person=weight_int/(((height_int/100)*(height_int/100)))
    print(bmi_person)
    obeseString =f"Your BMI is {bmi_person},you are obese."
    if bmi_person>=40:
        obese_label=Label(text=obeseString)
        obese_label.pack()
#button
calculate_button=Button(text="calculate",command=calculate_bmi)
calculate_button.pack()





window.mainloop()