time=input("What time of day is it? ")

if len(time)==4:
    if int(time[0:2])>12:
        print("Good Afternoon")
    else:
        print("Good Morning")
elif len(time)<=5:
    morn_after=input("Is this in the am or pm? ")
    if morn_after.upper()=="AM":
        print("Good Morning")
    else:
        print("Good Afternoon")
elif time[-2].upper()=="AM":
    print("Good Morning")
else:
    print("Good Afternoon")

