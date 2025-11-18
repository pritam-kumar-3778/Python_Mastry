color = input("Enter a traffic color : ")

match color:
    case "Green":
        print("Go")
    case "red":
        print("Stop")
    case "yellow":
        print("Look")
    case _:
        print("Wrong Input")


# default case id denoated as under score ( _ ), If none of the case is match then default will run.