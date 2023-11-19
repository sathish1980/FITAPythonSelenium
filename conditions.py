def Signal(signalLightColor,vehicle):
    if(signalLightColor=="Green"):
        pass
    elif(signalLightColor == "Red" or vehicle=="ambulance"):
        if(vehicle=="ambulance"):
            print("Give a way i am ambulance")
        else:
            print("you have to stop")
    elif (signalLightColor == "Orange"):
        print("get ready!!!!")
    else:
        print("You have entered incorrect color")
    print("outside condition")

Signal("Red","ambulance");