print(f"hello i have a story to tell you about a girl who moved back to her home town after a struggle inlife and has battle scars to show it i cant wait to share with you. ")
print(f"before i start i need to ask a few questions and i need your response. ")
print(f"after typing in your response make sure to press the enter key.")
input(f"\npress the enter key to continue....")
hometown = input("\nwhat is your hometown?: ")
returnfrom = input("where are you returning home from?: ")
help = input("will you help the person: ")
fighting = input("will you stay and fight: ")
doingboth = input("will you both fight for your home and help the person: ")
print(f"\nlets start the story now!!!!")
print(f"\nthere was this nice women with blonde hair she has battle scars from previous struggles in life. ")
print(f"\nshe was  returning to her hometown and had to renavigate what was once her home. ")
print(f"\nshe is back in her hometown trying to find her footing and reestablish herself and find out where she can help. ")
print(f"\nshe is asked by this person for help but she is unsure if she should  because they doubted her ablitys in life before. ")
shouldshehelp = input(f"\nshould she help this person type yes or no: ")
if shouldshehelp == "yes":
    print(f"\nshe puts her pride and ego aside and helps the person. ")
else:
    print("f\nshe does not give in and stands her ground. ")
shouuldshestay = input(f"\nshould she stay and fight for her hometown? type yes or no: ")
while shouldshestay.lower() != "yes" and shouldshestay.lower() != "no":
    shouldshestay = input(f"please type yes or no: ")   
if shouldshestay == "yes":
    print(f"\nshe will be in for a long fight but she stays where she is from and fights to reestablish herself. ")
else:
    print(f"\nshe goes someplace else and starts a new living elsewhere. ")
    if shouldshehelp == "yes" and shouldshestay == "yes":
        print(f"\nsheputs her pride aside and she stays and fights for her home. ")
 elif shouldshehelp == "no" and shouldshestay == "no":
    print(f"\nshe put her feelings first and decided to make living elsewhere. ")