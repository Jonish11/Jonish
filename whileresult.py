num_of_students = int(input("Enter number of students: "))
x = 1

while x <= num_of_students:
    print(f"========Students: {x}===========")
    for a in range(1):
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
    print("Percentage:", per)

    if per>=75:
        print("Distinction")
    elif per>=60:
        print("First Division")
    elif per>=45:
        print("Second Division")
    elif per>=35:
        print("Thirs Division")   

    else:
        print("Result: Fail")

    if English<35:
        print("You are Fail in English")
    if Math<35:
        print("You are Fail in Math")
    if Social<35:
        print("You are Fail in Social")
    if Science<35:
        print("You are Fail in Science")
    if Nepali<35:
        print("You are Fail in Nepali")  

    x += 1