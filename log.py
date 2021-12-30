import json
name=input('enter the name: ')
print('werlcome',name,"!!!")
print("1.signup")
print("2.login")
main_dict={}
list=[]
dict={}
user_info={}
option=input('(signup or login): ')
if option=="signup":
    username=input('enter the name of the user:  ')
    password=input('enter the name of the password:  ')
    cl="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sl="abcdefghijklmnopqrstuvwxyz"
    num="0123456789"
    spch="!@#$%^&"
    if len(password)>=8:
        i=0
        a=0
        b=0
        c=0
        d=0
        while i<len(password):
            if password[i] in cl:
                a=a+1
            elif password[i] in sl:
                b=b+1
            elif password[i] in num:
                c=c+1
            elif password[i] in spch:
                d=d+1
            i=i+1
        if a>=1 and b>=1 and c>=1 and d>=1:
            print("ur passward is strong")
        try:
            with open("data.json","r") as output:
                user_data=json.load(output)        
        except:
            pass 
        comform_password=input('enter the comfirm password: ')
        if password==comform_password:            
            if  ("data.json"):
                print("Congractstulations!!!",username,"You are signed up Succesfully")
                description=input("Enter your Description: ")
                birth_date=input("enter Your Date Of Birth: ")
                Gender=input("enter your Gender: ")
                hobbies=input("Enter Your hobby: ")
                try:
                    user_info["description"]=description
                    user_info["d_o_b"]=birth_date
                    user_info["Gender"]=Gender
                    user_info["Hobbies"]=hobbies
                    dict["Username"]=username
                    dict["Password"]=password
                    dict["Profile"]=user_info
                    list.append(dict)
                    main_dict["user"]=list
                    with open("data.json","r+") as file:
                        read_file= file.read()
                        userdata=json.loads(read_file)
                        for i in userdata:
                            if i =="user":
                                x=userdata[i]
                                x.append(dict.copy())
                                main_dict["user"]=x
                                json.dumps(main_dict,file)
                                file.close()
                except:
                    with open("data.json","w") as f:
                        f.write(json.dumps(main_dict, indent=4))
        else: 
            print('both passwords are not correct ')
    else:
        print("At least password should contain one Specail number or one digit")
elif option=="login":
    username=input("enter your username: ")
    login_password=input("enter your Log in Password: ")
    with open("data.json","r") as login_file:
        login_info=json.load(login_file)
        for output_data in login_info["user"]:
            if output_data["Username"] == username and output_data["Password"]==login_password:
                print(username , "You Logged In Succesfully")
                print("PROFILE")
                print("Username",":",output_data["Username"])
                print("Gender",":",output_data["Profile"]["Gender"])
                print("Bio",":",output_data["Profile"]["description"])
                print("Dob",":",output_data["Profile"]["d_o_b"])
                break
        else:
            print("Password and username are Invalid")
else:
    print("nothing")