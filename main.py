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

myList=[]
#calculate
def calculate_bmi():
    myList.append(weight_entry.get())
    myList.append(height_entry.get())
    weight_int=float(myList[0])
    height_int=float(myList[1])
    bmi_person=weight_int/(((height_int/100)*(height_int/100)))
    obeseString =f"Your BMI is {bmi_person},you are obese."
    underweight=f"Your BMI is {bmi_person},you are underweight."
    normal=f"Your BMI is {bmi_person},you are normal."
    overweight=f"Your BMI is {bmi_person},you are overweight."
    if bmi_person>=40:
        obese_label=Label(text=obeseString)
        obese_label.pack()
    elif bmi_person<=18.4:
        underweight_label=Label(text=underweight)
        underweight_label.pack()
    elif 18.5 <= bmi_person <= 24.9:
        normal_label=Label(text=normal)
        normal_label.pack()
    elif 25.0 <= bmi_person<= 39.9:
        overweight_label=Label(text=overweight)
        overweight_label.pack()
    else:
        print("Enter valid numbers.")

    myList.clear()


#button
calculate_button=Button(text="calculate",command=calculate_bmi)
calculate_button.pack()





window.mainloop()