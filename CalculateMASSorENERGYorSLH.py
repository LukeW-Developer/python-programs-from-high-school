choose1=True
while choose1:
    print("")
    print("Coded by LukeW-Developer")
    print("")
    print("What do you want to find out?")
    print("'Mass'")
    print("'Specific Latent Heat'")
    print("'Thermal Energy'")
    print("")
    print("Select - Selection")
    choose1=input("You want to find out the: ")
    if choose1=="Mass":
        import decimal
        print("")
        print("Enter an amount (Thermal Energy)")
        chooseTHERMALENERGY=float(input("Thermal Energy: "))
        print("")
        print("Enter an amount (Specific Latent Heat)")
        chooseSLH=float(input("Specific Latent Heat: "))
        completeANSWERforMASS= decimal.Decimal(chooseTHERMALENERGY) / decimal.Decimal(chooseSLH)
        print("")
        print("Mass:",completeANSWERforMASS,"kg")
        print("Working out:")
        print(chooseTHERMALENERGY,"/",chooseSLH,"=",completeANSWERforMASS,"kg")

    if choose1=="Specific Latent Heat":
        import decimal
        print("")
        print("Enter an amount (Mass)")
        chooseMASS=float(input("Mass: "))
        print("")
        print("Enter an amount (Thermal Energy)")
        chooseTHERMALENERGY=float(input("Thermal Energy: "))
        completeANSWERforSLH= decimal.Decimal(chooseMASS) / decimal.Decimal(chooseTHERMALENERGY)
        print("")
        print("Specific Latent Heat:",completeANSWERforSLH,"J/kg")
        print("Working out:")
        print(decimal.Decimal(chooseMASS),"/",decimal.Decimal(chooseTHERMALENERGY),"=",completeANSWERforSLH)

    if choose1=="Thermal Energy":
        import decimal
        print("")
        print("Enter an amount (Mass)")
        chooseMASS=float(input("Mass: "))
        print("")
        print("Enter an amount (Specific Latent Heat)")
        chooseSLH=float(input("Specific Latent Heat: "))
        completeANSWERforTHERMALENERGY= decimal.Decimal(chooseMASS) * decimal.Decimal(chooseSLH)
        print("")
        print("Thermal Energy:",completeANSWERforTHERMALENERGY,"J")
        print("Working out:")
        print(decimal.Decimal(chooseMASS),"*",decimal.Decimal(chooseSLH),"=",completeANSWERforTHERMALENERGY)
