import re
def register():
    db = open("access_register.txt", "r")
    a = input("enter your username:")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])
    pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    result=re.findall(pattern,a)
    if result:
      print("username created")    

    b = input("Create your password with atleast one capital letter one integer and one special character: ")
    s = False

    pattern1="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"  
 
    result1=re.findall(pattern1,b)
    if result1:
      s=True

    if s:
        c = input("Confirm Password: ")
        while (c != b):
            print("Password not match, Try Again")
            c = input("Try Again: ")

    else:
        print("Try again")
        register()

    file = open("access_register.txt", "a")
    file.write(a + "," + b + "\n")
    file.close()
    login()

def login():
    X=input("Enter your username to login: ")
    X = X.strip()
    db = open("access_register.txt", "r")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])

    if X in d:
        Y=input("Please Enter your password: ")
        Y=Y.strip()
        file1=open("access_register.txt","r").readlines()
        for x in file1:
            x=x.strip()
            info=x.split(",")
            if X==info[0] and Y==info[1]:
                print("Welcome in the digital world")
            else:
                F = input("Forgot Password [Y/N] : ")

                if F == "N":
                    print("try")
                    login()

                if F == "Y":
                    b = input("Create your new password with atleast one capital letter one integer and one special character: ")
                    s = False

                    pattern1="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"  
                    result1=re.findall(pattern1,b)
                    if result1:
                     s=True
                    if s:
                        c = input("Confirm Password: ")
                        while (c != b):
                            print("Password not match, Try Again")
                            c = input("Try Again: ")

                    else:
                        print("Sorry,Try again to login")
                        login()

                    file = open("access_register.txt", "w")
                    file.write(X + "," + b + "\n")
                    file.close()

    else:
        print("Unregister user you need to register first")
        register()

def welcome():
    print("WELCOME IN THE DIGITAL WORLD")
    print("For accessing you need to login and if new user than you need to register")
    W=input("Login|Register[L/R]: ")
    if W=="L":
        login()
    elif W=="R":
        register()
    else:
        print("Enter in proper manner only please")
        welcome()
welcome()
 
 