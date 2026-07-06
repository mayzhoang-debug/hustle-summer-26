# May | Lab 4 | Intro to python

#ticket 1
ages = [17, 11, 25, 13, 9]
for age in ages:
    if age >= 13:
        print("Access Granted")
    else:
        print("Too young")
#predict 17, 25, 13 will get access granted because they are greater than 13
#explain it keeps looping itself and i dont have to manually keep checking it

#ticket 2
# Set up a control variable
keep_checking = "yes"

while keep_checking == "yes":

    age = int(input("Enter an age: "))
    if age >= 13:
        print("Age is 13 or older.")
    else:
        print("Age is under 13.")

    keep_checking = input("Do you want to check another age? (yes/no): ").lower()
#predict it will not run at all 
#explain while loop instead of for loop is the right choice because while loops keeps going to a certain answer 

#ticket 3
while True:
    age_input = input("Enter an age or type 'stop': ")

    if age_input == "stop":
        print("Goodbye!")
        break

    age = int(age_input)

    if age >= 13:
        print("Access granted")
    else:
        print("Too young")
    #predict if i forgot the break command it will keep looping and crash my computer 

#ticket 4
def can_access(age):
    if age >= 13:
        return True
    else:
        return False

ages = [17, 11, 25, 13, 9]

for age in ages:
    if can_access(age):
        print(f"{age} — Access granted ✅")
    else:
        print(f"{age} — Too young ❌")
#predict the difference about the code is doesnt repeat the if else code? 
#explain the code will be easier to read 

#ticket 5
def can_access(age):
    if age >= 13:
        return True
    else:
        return False
def signup_report(ages):
    approved = 0

    print("--- StreamPass Signup Report ---")

    for number, age in enumerate(ages, start=1):
        if can_access(age):
            print(f"Signup #{number} | Age {age} — Access granted ✅")
            approved += 1
        else:
            print(f"Signup #{number} | Age {age} — Too young ❌")

    print(f"Approved: {approved} out of {len(ages)}")

signups = [22, 10, 15, 8, 19, 13]

signup_report(signups)
#predict there is 4/6
#explain functions, parameters, return values, lists, for loops, conditionals 
