Admins = ["sasa","peter","joseph","mena"]
login = input("please enter your name :- ").lower().replace(" ","")
isvalid = "invalid input"

if login in Admins:
    while isvalid == "invalid input" :
        print("-"*100)
        print(" you can just write the first letter of \"update\" or \"delete\" ".center(100,"-"))
        print("-"*100)
        option = input(f"welcome back {login}, wanna delete or update your user name :- ").lower().replace(" ","")

        if option == "delete" or option == "d":

            Admins.remove(login)
            print("name deleted successfuly .")
            isvalid = "valid"

        elif option == "update" or option == "u":

            New_Admin_Name = input("please enter your new user name :- ").lower().replace(" ","")
            Admins [Admins.index(login)] = New_Admin_Name
            print("name updated successfuly .")
            isvalid = "valid"

        else:
            print(isvalid) 
else:
    while isvalid == "invalid input" :
        add_a_new_admin = input("badly you are not admin,wanna be an admin ? yes\"y\"or no \"n\" :- ").lower().replace(" ","")
        
        if add_a_new_admin == "yes" or add_a_new_admin == "y" or add_a_new_admin == "no" or add_a_new_admin == "n":

            isvalid = "valid"
            if add_a_new_admin == "yes" or add_a_new_admin == "y":

                newAdmin = input("please enter your name just your 1st name :- ").lower().replace(" ","")
                Admins.append(newAdmin)
                print("added successfuly .")

            elif add_a_new_admin == "no" or add_a_new_admin == "n":

                print("thanks for your visiting .")