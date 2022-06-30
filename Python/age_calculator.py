# collect date from the user .

age = input("please enter yor age :- ")
age = age.replace(" ","")
age = int(age)
print("-"*100)
print("you can write just the first letter of the time unit".center(100,"-"))
print("-"*100)
The_operator = input("please enter the time unit you want(\"weeks\",\"days\",\"months\") :- ")
The_operator = The_operator.lower().replace(" ","")

if The_operator == "days" or The_operator == "d":
   print(f"you lived for {age*365:,}")

elif The_operator == "weeks" or The_operator == "w":
    print(f"you lived for {age*52:,}")

elif The_operator == "months" or The_operator == "m":
    print(f"you lived for{age * 12:,}")
