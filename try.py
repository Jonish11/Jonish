
print("enter marks")
English = int(input("English:"))
Math = int(input("Math:"))
Social = int(input("Social:"))
Science = int(input("Science:"))
Nepali = int(input("Nepali:"))

total = (English+Math+Social+Science+Nepali)
print("Total Marks is:", total)

if English>=35 and Math>=35 and Social>=35 and Science>=35 and Nepali>=35:
    print("Result: PASS")

    per=(English+Math+Social+Science+Nepali)/5
    print("PErcentage:", per)

    if per>=75:
        print("Distinction")
    elif per>=60:
        print("First Division")
    elif per>=45:
        print("Second Division")
    elif per>=35:
        print("Thirs Division")   

else:
    print("You are Fail in:")

    if English<35:
        print("English")
    if Math<35:
        print(" Math")
    if Social<35:
        print("Social")
    if Science<35:
        print("Science")
    if Nepali<35:
        print("Nepali")