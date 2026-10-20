#Name:
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

height = int(input("whats your height in inches"))
weight = int(input("whats your weight in pounds"))
Bmi = (weight / height ** 2) * 703
print(Bmi)

if Bmi < 18.5:
    print("underweight")
elif Bmi >= 18.5 and Bmi <= 24.9:
    print("normal weight")
elif Bmi >= 25 and Bmi <= 29.9:
    print("overweight")
else:
    print("obese")