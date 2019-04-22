def cs_service_bot():
    print("Hello, Welcome to the DNS Cable Company's Service Portal.\nAre you a new or existing customer?\n")
    print("[1] New Customer\n")
    print("[2] Existing Customer\n")
    response = input("Please enter the number corresponding to your choice: ")
    if response == "1":
        return new_customer()
    elif response == "2":
        return existing_customer()
    else:
        print("Sorry, we didn't understand your selection")
        print(cs_service_bot())

def existing_customer():
    print("""
\nWhat kind of support do you need?\n
[1] Television Support.\n
[2] Internet Support.\n
[3] Speak to a support representative.\n
""")
    response = input("please enter the number corresponding to your choice: ")
    if response == "1":
        return television_support()
    elif response == "2":
        return internet_support()
    elif response == "3":
        return live_rep("support")
    else:
        print("Sorry, we didn't understand your selection")
        print(existing_customer())

def new_customer():
    print("""\nWe're excited to have you join the DNS family, how can we help you?\n
          [1] Sign up for service.\n
          [2] Schedule a home visit.\n
          [3] Speak to a sales representative.\n
          """)
    response = input("please enter the number corresponding to your choice: ")
    if response == "1":
        return sign_up()
    elif response == "2":
        return home_visit()
    elif response == "3":
        return live_rep("sales")
    else:
        print("Sorry, we didn't understand your selection")
        print(new_customer())

def television_support():
    print("What is the nature of your problem?\n"
    "[1] I can't access certain channels.\n"
    "[2] My picture is blurry.\n"
    "[3] I keep losing service.\n"
    "[4] Other issues\n")
    response = input("What is the nature of your problem? ")
    if response == "1":
        print("Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.")
        return did_that_help()
    elif response == "2":
        print("Try adjusting the antenna above your television set.")
        return did_that_help()
    elif response == "3":
        print("Is it raining outside? If so, wait until it is not raining and then try again.")
        return did_that_help()
    elif response == "4":
        return live_rep("support")
    else:
        print("Sorry, we didn't understand your selection")
        print(television_support())

def internet_support():
    print("What is the nature of your problem?\n"
    "[1] I can't connect to the internet.\n"
    "[2] My connection is very slow.\n"
    "[3] I cant access certain sites.\n"
    "[4] Other issues\n")
    response = input("What is the nature of your problem? ")
    if response == "1":
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        return did_that_help()
    elif response == "2":
        print("Make sure that all cell phones and other peoples computers are not connected to the internet, so that you can have all the bandwidth.")
        return did_that_help()
    elif response == "3":
        print("Move to a different region or install a VPN. Some areas block certain sites.")
        return did_that_help()
    elif response == "4":
        return live_rep("support")
    else:
        print("Sorry, we didn't understand you selection")
        print(internet_support())

def did_that_help():
    response = input("Has the solution given, solved the problem you had? ")
    if response == ("Yes" or "yes"):
        print("Thank you!")
    elif response == ("No" or "no"):
        print("Would you like to;\n"
              "[1] Talk to a live representative?\n"
              "[2] Schedule a home visit?\n")
        answer = input(": ")
        if answer == "1":
            return live_rep("support")
        elif answer == "2":
            return home_visit("support")
        else:
            print("Sorry, we didn't understand your selection")
            print(did_that_help)
    else:
        print("Sorry, we didn't understand your selection")
        print(did_that_help())


cs_service_bot()

