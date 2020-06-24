
def bmi():
    kg, feet, inches = input("Enter your weight in kg and height in feet and inches the form x,y,z ").split(",")
    kg, feet, inches = float(kg) , float(feet), float(inches)
    m = ((feet * 0.3048) + (inches * 0.0254))
    m2 = m*m
    bmi = kg/m2
    print("The calculated BMI is " , bmi)

def waist_hip_ratio():
    waist, hip = input("Enter your waist and hip measurements in inches in the form x,y ").split(",")
    waist, hip = float(waist), float(hip)
    ratio = round(waist/hip,4)
    print("The calculated waist to hip ratio is" , ratio)

def one_rep_max():
    weight, reps = input("Enter a weight and how many reps you can achieve with this weight in the form x,y ").split(",")
    weight, reps = float(weight), float(reps)
    max = round((weight / (1.0278 - 0.0278* reps)),1)
    print("Your one rep max is",max,"kg")


def start():
        full_analysis = input("Would you like a full analysis of all your measurements?(Yes/No) ").lower()
        if full_analysis == "yes":
            print("BMI:"), bmi()
            print("Waist Hip Ratio:"), waist_hip_ratio()
            print("One Rep Max:"), one_rep_max()
        elif full_analysis == "no":
            choose()

def choose():
    choice = input("Please enter one of the following. BMI, WHR(Waist Hip Ratio), 1RM(One rep max)").upper()
    if choice == "BMI":
        bmi()
    elif choice == "WHR":
        waist_hip_ratio()
    elif choice == "1RM":
        one_rep_max()
    choose()

start()
