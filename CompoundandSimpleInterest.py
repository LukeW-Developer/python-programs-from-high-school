choose1=True
while choose1:
    print("")
    print("Coded by LukeW-Developer")
    print("")
    print("What do you want to find out?")
    print("'1. Compound Interest'")
    print("'2. Simple Interest'")
    print("")
    
    print("Select - Selection")
    choose1=input("You want to find out the: ")
    
    if choose1=="1":
        
        import math
        print("")
        print("Money (1k for example)")
        chooseA=float(input("Money: "))
        
        print("")
        print("Percentage (5% for example)")
        chooseB=float(input("PercentageB: "))
        
        print("")
        print("Time (Years for example. E.g. 2)")
        chooseC=int(input("Time: "))
        
        part1Convertor= chooseB/100
        if chooseB < 100:
            part2Convertor= part1Convertor
            prechosenWorkingOutNumber=1
            chosenReplacedWorkingOutNumber=part1Convertor
        elif chooseB > 100:
            part2Convertor=part1Convertor
        else:
            print("Error!")
            
        fullAnswer= chooseA*part2Convertor**chooseC
        print("")
        print("Answer:",fullAnswer)
        print("Working Out:")
        if chooseB < 100:
            print(prechosenWorkingOutNumber,"+",chosenReplacedWorkingOutNumber,"=",part2Convertor)
        elif chooseB > 100:
            print(chooseB,"=",part2Convertor)
        print(chooseA,"x",part2Convertor,"(to the power of,",chooseC,"=",fullAnswer)

        for i in range(1, chooseC+1):
            print("Year",i,'=',chooseA*part2Convertor**i)

    if choose1=="2":
        import math

        # Note: simple interest isnt fully working, need to fix the percentage system soon
        print("")
        print("Money (1k for example)")
        chooseA=float(input("Money: "))
        
        print("")
        print("Percentage (5% for example)")
        chooseB=float(input("PercentageB: "))
        
        print("")
        print("Time (Years for example. E.g. 2)")
        chooseC=int(input("Time: "))

        part1Convertor= chooseB/100
        if chooseB < 100:
            part2Convertor= part1Convertor
            prechosenWorkingOutNumber=1
            chosenReplacedWorkingOutNumber=part1Convertor
        elif chooseB > 100:
            part2Convertor= part1Convertor-1
        else:
            print("Error!")
        
        fullAnswer= chooseA*part2Convertor*chooseC
        print("")
        print("Answer:",fullAnswer)
        print("Working Out:")
        if chooseB < 100:
            print(prechosenWorkingOutNumber,"+",chosenReplacedWorkingOutNumber,"=",part2Convertor)
        elif chooseB > 100:
            print(chooseB,"=",part2Convertor)
        print(chooseA,"x",part2Convertor,"times by,",chooseC,"=",fullAnswer)

        for i in range(1, chooseC+1):
            partialAnswer=part2Convertor*i
            print("Year",i,'=',chooseA+partialAnswer)
