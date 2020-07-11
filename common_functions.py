def newl(x=1):
    for i in range(x):
        print("")
        i+= 1


def eq(midtext="", LeaveLines=1):
    newl(LeaveLines)
    print("===============================" + str(midtext) + "===============================")
    newl(LeaveLines)