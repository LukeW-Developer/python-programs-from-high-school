selectdigit1=True
while selectdigit1:
    print("")
    print("Coded by LukeW-Developer")
    print("")
    print("Choose 'Letters' or 'Numbers'")
    print("Digit 1 - Selection")
    selectdigit1=input("Digit 1 - Your Option: ")
    
    print("")
    print("Digit 2 - Selection")
    selectdigit2=input("Digit 2 - Your Option: ")

    if selectdigit1=="Numbers":
        print("")

        if selectdigit2=="Numbers":
            print("Choose a Number")
            print("Choose a Number (Digit 1)")
            digit1=int(input("Digit 1 - Number - Enter your answer: "))
            
            print("")
            print("Choose a Number (Digit 2)")
            digit2=int(input("Digit 2 - Number - Enter your answer: "))
            
            digit1complete= digit1 * 16
            print("")
            print("Full Answer is:",digit1complete + digit2)
            print("Working Out:")
            print(digit1,"x 16 =",digit1complete)
            print(digit1complete,"+",digit2,"=",digit1complete + digit2)

        if selectdigit2=="Letters":
            print("")
            print("Choose a Number (Digit 1)")
            digit1=int(input("Digit 1 - Number - Enter your answer: "))
            
            print("")
            print("Choose a Letter (Digit 2)")
            digit2=input("Digit 2 - Letter - Enter your answer: ")
            digit1complete= digit1 * 16
            
            # is the person entering a value that is beyond singular digits?
            if digit2=="A":
                digit2complete= 10
            elif digit2=="B":
                digit2complete= 11
            elif digit2=="C":
                digit2complete= 12
            elif digit2=="D":
                digit2complete= 13
            elif digit2=="E":
                digit2complete= 14
            elif digit2=="F":
                digit2complete= 15
            else:
                print("")
                print("ERROR! You entered something that wasnt a Letter!")
                print("Please enter a letter thats A-F!")
                continue
            
            print("")
            print("Full Answer is:",digit1complete + digit2complete)
            print("Working Out:")
            print("A-F are 10-15")
            print(digit1,"x 16 =",digit1complete)
            print(digit1complete,"+",digit2complete,"=",digit1complete + digit2complete)


    if selectdigit1=="Letters":
        print("")

        if selectdigit2=="Numbers":
            print("")
            print("Choose a Letter (Digit 1)")
            digit1=input("Digit 1 - Letter - Enter your answer: ")

            print("")
            print("Choose a Number (Digit 2)")
            digit2=int(input("Digit 2 - Number - Enter your answer: "))
            if digit1=="A":
                digit1complete= 10
                digit1fullcomplete= 10 * 16
            elif digit1=="B":
                digit1complete= 11
                digit1fullcomplete= 11 * 16
            elif digit1=="C":
                digit1complete= 12
                digit1fullcomplete= 12 * 16
            elif digit1=="D":
                digit1complete= 13
                digit1fullcomplete= 13 * 16
            elif digit1=="E":
                digit1complete= 14
                digit1fullcomplete= 14 * 16
            elif digit1=="F":
                digit1complete= 15
                digit1fullcomplete= 15 * 16
            else:
                print("")
                print("ERROR! You entered something that wasnt a Letter! (Digit 1)")
                print("Please enter a letter thats A-F!")
                continue
                
            print("Full Answer is:",digit1fullcomplete + digit2)
            print("Working Out:")
            print("A-F are 10-15")
            print(digit1complete,"x 16 =",digit1fullcomplete)
            print(digit1fullcomplete,"+",digit2,"=",digit1fullcomplete + digit2)
            

        if selectdigit2=="Letters":
            print("")
            print("Choose a Letter (Digit 1)")
            digit1=input("Digit 1 - Letter - Enter your answer: ")

            print("")
            print("Choose a Letter (Digit 2)")
            digit2=input("Digit 2 - Letter - Enter your answer: ")
            if digit1=="A":
                digit1complete= 10
                digit1fullcomplete= 10 * 16
            if digit1=="B":
                digit1complete= 11
                digit1fullcomplete= 11 * 16
            if digit1=="C":
                digit1complete= 12
                digit1fullcomplete= 12 * 16
            if digit1=="D":
                digit1complete= 13
                digit1fullcomplete= 13 * 16
            if digit1=="E":
                digit1complete= 14
                digit1fullcomplete= 14 * 16
            if digit1=="F":
                digit1complete= 15
                digit1fullcomplete= 15 * 16

            if digit2=="A":
                digit2complete= 10
            elif digit2=="B":
                digit2complete= 11
            elif digit2=="C":
                digit2complete= 12
            elif digit2=="D":
                digit2complete= 13
            elif digit2=="E":
                digit2complete= 14
            elif digit2=="F":
                digit2complete= 15
            else:
                print("")
                print("ERROR! You entered something that wasnt a Letter!")
                print("Please enter a letter thats A-F!")
                continue

            print("")
            print("Full Answer is:",digit1fullcomplete + digit2complete)
            print("Working Out:")
            print("A-F are 10-15")
            print(digit1complete,"x 16 =",digit1fullcomplete)
            print(digit1fullcomplete,"+",digit2complete,"=",digit1fullcomplete + digit2complete)
