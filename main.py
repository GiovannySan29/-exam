def averageStudent():
    average = 0
    for j in range(1,6):
        average += int(input(f"Ingrese nota {j}: "))
    average = average / 5
    return average

def  resul(rogram,listProgram):
    exists = False
    for i in listProgram:
        for l in i:
            if l == program:
                exists = True
    return exists            



age=0
enrolled=0
name=0
promEdad=0
opcion=0
edadValid=0
alum=0
numAlumnos=0
programlist=[]
existsProgram=False
menuenrollment=0
sex = 0
newStudent=0
countWomen=0
countMen=0
student=[] 
academicprogram=0 

while menuenrollment == 0:
    menu=input("¿Qué desea hacer? - admision(admi) - matrícula(matri): ")
    if menu == "matricula" :
        menuenrollment = 1
        while True:
            try:
                numAlum = int(input("Enter number of students: "))
                if numAlum < 0:
                    print("Error! enter a valid option.")
                else:
                    break
            except ValueError:
                print("Error! enter a valid option.")
        for i in range(numAlum):
            name = 0
            while name == 0: 
                name = input("Enter name: ")
                if name.isalpha():
                    name = 1
                
            academicprogram=0        
            while academicprogram == 0:
                program = input("Enter academic program: ")
                if program.isalpha():
                    academicprogram = 1
            
            programss = resul(program,programlist)
            if programss == False:
                programlist.append({program})
            sex = 0
            while sex == 0:
                sex = input("Enter sex - m(mujer), h(hombre)")
                if sex == "m" or sex == "M":  
                    countWomen+=1
                    sex = 1
                elif sex == "h" or sex == "H":
                    countMen+=1
                    sex = 1
                else:
                    print("Error! enter a valid option.")
                    sex = 0
            average =averageStudent()        
            student.append({"name":name, "program":program , "average":average, "sexo":sex}) 
    else:
        if menu == "Matricula" or menu == "matricula":
            opcion = 0
            while True:
                name = 0
                while name == 0: 
                    name = input("Enter name: ")
                    if name.isalpha():
                        name = 1
                    else:
                        print("Error! enter a valid option.")
                        name = 0
                while True:
                    try:
                        age = int(input("Enter age:"))
                        if age < 0:
                            print("Error! enter a valid option.")
                        else:
                            break
                    except ValueError:
                        print("Error! enter a valid option..") 
                sex = 0
                promEdad = promEdad + age  
                while sex == 0:
                    sex = input("Enter sex - m(mujer), h(hombre)")
                    if sex == "m" or sex == "M":  
                        countWomen+=1
                        sex = 1
                    elif sex == "h" or sex == "H":
                        countMen+=1
                        sex = 1
                    else:
                        print("Error! enter a valid option.")
                        sex = 0
                enrolled +=1
                while True:
                    try:
                        newStudent=int(input("If you want to enter a new student press 1 or press any key to exit!!"))  
                        if newStudent < 0:                                  
                            print("Error! enter a valid option.")
                        else:
                            break
                    except ValueError:
                        print("Error! enter a valid option.")
                menu = 1
                if newStudent != 1:
                    break
            promEdad = promEdad /enrolled
            print("The average age of the enrolled students is: " + str(promEdad))
            print("The number of students enrolled is: " + str(enrolled))
            print("The average number of women enrolled is: " + str(countWomen))
            print("The average number of man enrolled is: " + str(countMen))
        else:
            print("Error! enter a valid option.")
            menu = 0