from credentials import Credentials
from user import User


def createAccount(fname,lname,mail,uName,pass_word):
    '''Creates user account'''
    new_user=User(first_Name=fname,last_Name=lname,user_Name=uName,e_mail=mail,pass_word=pass_word)
    return new_user

def save_Users(user):
    '''saves the user details'''
    user.save_User()

def login(pass_word):
    '''logs in the user by connecting find user'''
    new_user=User.find_User(pass_word)
    return new_user

def display_User():
    '''function that displays user credentials by calling display credentials'''
    return User.display_Users()



# Credential functions
def create_Credentials(name,Uname,password):
    '''Fucntion that creates credentials of the user '''
    new_credentials=Credentials(name=name,Uname=Uname,password=password)
    return new_credentials


def save_Cred(cred):
    '''saves user credentials using save credetials function in cred page'''
    cred.save_Credentials()

def gen_Pass():
    '''generates password for user'''
    return  Credentials.genPass()

def display_Cred():
    '''function that displays user credentials by calling display credentials'''
    return Credentials.display_Credentials()


def find_Cred(name):
    '''function to find the user credentials by allowing user to search'''
    return Credentials.find_cred(name)


def check_existing(val):
    '''function to check if the crediats exist'''
    return Credentials.check_cred_Exists(val)

def del_Cred(del_cred):
    ''''function to delete the credentials'''
    del_cred.delete_Account()

def copy_credentials(name):
    return Credentials.copy_Cred(name)

def main():
    print("hello Welcome to password locker.What is your name")
    user_name=input()
    print('\n')
    print(f"Hello {user_name} please sign in to access or save passwords")
    print('\n')
    while True:
        print("Do you have an account? Use LI to let me know that you want to login")
        print('\n')
        print("Dont have an account? Use CA to tell me to create an accout for you")
        print('\n')
        print("Dont have an account? Use VC to tell me to show you your  account ")
        print('\n')
        print("Dont you want to Exit? Use EX to tell me to allow you leave") 

        short_code=input().upper()

        if short_code=='VC':
            if display_User():
                    for useR in display_User():
                        print(f" You have {useR.first_Name} account with username:{useR.user_Name}  and password:{useR.pass_word} and  your email is {useR.e_mail}")
                    print("-----------------------------------------------------------------------------------")
            else:
                        print('\n')
                        print("User list is currently empty create one first ")
                        print("-------------------------------------------------")
        elif short_code=='CA':
            print("Create Account")
            print("*"*5)
            print('\n')

            print("First Name....................................")
            fname=input()
            print("*"*10)
            print('\n')
        

            print("Last Name.....................................")
            lname=input()
            print("*"*20)
            print('\n')
        


            print("Email ........................................")
            email=input()
            print("*"*20)
            print('\n')
        

            print("user Name.....................................")
            uname=input()
            print("*"*20)
            print('\n')
        


            print("pass_word to Login..................................")
            pNumber=input()
            print("*"*20)
            print('\n')
            

            print("*"*200)
            save_Users(createAccount(fname,lname,uname,email,pNumber))
        
            print(f"Now you have to login {fname} use LI as instructed below")
            print('\n')
            print("----------------------------------------------------------------")

        elif short_code=='LI':
            print("Password .......")
            password=input()
            # print("pass_word number.......")
            # pNumber=input()
            
            logedUser=login(password)
            while True:
                if logedUser:


                    print('\n')
                    print(f"What do you want to do  {logedUser.first_Name}?")
                    print("\n")
                    print("For Create credentials---------------------------CC")
                    print("\n")
                    print("For Display your saved credentials----------------DC")
                    print("\n")
                    print("For Searching  credentials------------------------SC")
                    print("\n")
                    print("To Delete credentials------------------------------DL")
                    print("\n")
                    print("To Copy credentials------------------------------COPY")
                    print("\n")
                    print("To Exit---------------------------------------------EX")
                    print("\n")
                    # print("To Update  credentials-----------------------------UC")
            
                    short_code=input().upper()
                    if short_code=="CC":
                        print("New Credentials .................")
                        print("*"*50)
                        print("\n")


                        print("Name of site .................")
                        name=input().capitalize()
                        print("\n")

                        print("Username...................")
                        Uname=input()
                        print("\n")


                        print("Select either to enter password or create password")
                        print("For enter password-------------------------------EP")
                        
                        print("For Generate password ---------------------------GP")
                        com=input().upper()
                        print("\n")
                        if com=='EP':
                            print("input password")
                            passw=input()
                            print(passw)
                        elif com=='GP':
                            print("input password")
                            passw=gen_Pass()
                            passww=gen_Pass()
                            print(passw)
                        else:
                            print("I dont understand you choose eith EP or GP")
                            break
                        save_Cred(create_Credentials(name,Uname,passw))
                        print(f"New credentials of: {Uname} with password:{passw} created for {name}")
                    elif short_code=='DC':
                        if display_Cred():
                            for cred in display_Cred():
                                print(f" You have {cred.name} account with username:{cred.Uname}  and password {cred.password}")
                            print("-----------------------------------------------------------------------------------")
                        else:
                            print("Credentials are currently empty create one first ")
                            print("-------------------------------------------------")
                    elif short_code=="SC":
                        print("Name of account to search...........")
                        search_val=input().capitalize()
                        
                        # if search_val=='':
                        #     print("its empty")
                
                        
                        
                        # else:
                        if check_existing(search_val):
                            search_cred=find_Cred(search_val)
                            print(f" You have {search_cred.name} account with username:{search_cred.Uname}  and password {search_cred.password}")
                            print("-----------------------------------------------------------------------------------")
                        else:
                            print(f"Sorry we dont have a record {search_val} in our database ")
                            print("-----------------------------------------------------------------------------------")
                                
                    elif short_code=='DL':
                        del_val=input()
                        if check_existing(del_val):

                            search_cred=find_Cred(del_val)
                            del_Cred(search_cred)
                            print("-------------------------------------------------")
                            print(f"You have sucessfully deleted {del_val}")
                            print("-------------------------------------------------")
                    elif short_code=='COPY':
                        print("Name of credential to copy")
                        name=input().capitalize()
                       
                        if check_existing(name):

                            cred=copy_credentials(name)
                            print("-------------------------------------------------")
                            print("Copied sucessfully Try pasting  it somewhere")
                            print('\n')
                            print("-------------------------------------------------")
                        else:
                            print(f"Sorry {name}not found")

                    elif short_code=='EX':
                        print(f"Goodbye {fname} You are out of the Credentials store to get in again you have to login")
                        print("YOUR ACCOUNT DETAILS ARE SAFE US")
                        print("-------------------------------------------------------------------------")
                        break
                    else:
                        print('I did not understand you try again')
                        
                else:
                    print("Create account to login")
                    break
        
        elif short_code=='EX':
                print(f"goobye {user_name}")
                print("THANK YOU")
                break

        else:
                print(f"Did you really read the instructions {user_name} please retry")


            





            









if __name__=='__main__':
    main()

