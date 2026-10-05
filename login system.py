username = "your username here"
password = "your password here"

option1 = "Change Password"
option2 = "View Account"
option3 = "Logout"

login_attempts = 0
is_success = True

while login_attempts < 3:
    name = input("Username: ")
    user_password = input("Password: ")

    if username == name and password == user_password:

        while is_success:
            print("1.", option1)
            print("2.", option2)
            print("3.", option3)

            choice = input("Choose an option: ")

            if choice == "3":
                is_success = False
                break

            elif choice == "2":
                print(username)
                print("The account is active.")

            elif choice == "1":
                new_password = input("New password: ")

                if new_password == user_password:
                    print("Password is the same as the old one")

                elif new_password == "":
                    print("Password is empty, try again")

                else:
                    password = new_password
                    user_password = new_password
                    print("Update successful")

            else:
                print("Invalid option.")

        break

    elif username != name and password == user_password:
        print("Incorrect Username")
        login_attempts += 1

    elif username == name and password != user_password:
        print("Incorrect Password")
        login_attempts += 1

    else:
        print("Login Failed")
        login_attempts += 1

    if login_attempts == 3:
        print("Account Locked, visit. Please see the administrator to unlock your account.")
