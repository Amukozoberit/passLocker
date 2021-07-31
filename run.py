from user import User


def createAccount(fname,lname,mail,uName,phone):
    new_user=User(first_Name=fname,last_Name=lname,user_Name=uName,e_mail=mail,phone_Number=phone)
    return new_user

def save_Users(user):
    user.save_User()

def login(email):
    new_user=User.find_User(email)
    return new_user

def main():
    print("hello Welcome to password locker.What is your name")
    user_name=input()
    print(f"Hello {user_name} please sign in to access or save passwords")
    print('\n')
    print("Do you have an account? Use LI to let me know that you want to login")
    print('\n')
    print("Dont have an account? Use CA to tell me to create an accout for you")
    short_code=input().upper()


    if short_code=='LI':
        print("Sorry our database is empty")
    elif short_code=='CA':
        print("Create Account")
        print("*"*5)
        print('\n')

        print("First Name.........")
        fname=input()
        print("*"*10)
        print('\n')
       

        print("Last Name.........")
        lname=input()
        print("*"*20)
        print('\n')
      


        print("Email .........")
        email=input()
        print("*"*20)
        print('\n')
      

        print("user Name.........")
        uname=input()
        print("*"*20)
        print('\n')
     


        print("Phone Number.........")
        pNumber=input()
        print("*"*20)
        print('\n')
        

        print("*"*200)
        save_Users(createAccount(fname,lname,uname,email,pNumber))
       
        print("Now you have to login ")
        print("email.......")
        email=input()
        # print("phone number.......")
        # pNumber=input()
        logedUser=login(email)


        print(f"Welcome {logedUser.first_Name} its been tough but argh you done")




    elif short_code=='EX':
        print(f"goobye {user_name}")

    else:
        print(f"Did you really read the instructions {user_name} please retry")


       





        









if __name__=='__main__':
    main()

