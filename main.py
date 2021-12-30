import json
user=input("enter login or signup")
dict={}
if user=="signup":
    dic={}
    user_data=[]
    name=input("enter the user name")
    print("Hiii.....")
    print(name)
    print("welcome.....")
    passward=input("enter passward")
    cl="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sl="abcdefghijklmnopqrstuvwxyz"
    num="0123456789"
    spch="!@#$%^&"
    if len(passward)>=8:
        i=0
        a=0
        b=0
        c=0
        d=0
        while i<len(passward):
            if passward[i] in cl:
                a=a+1
            elif passward[i] in sl:
                b=b+1
            elif passward[i] in num:
                c=c+1
            elif passward[i] in spch:
                d=d+1
            i=i+1
        if a>=1 and b>=1 and c>=1 and d>=1:
            print("ur passward is strong")
            with open("data.json","r")
            
            passward2=input("again enter the passward for conformation")
            if passward==passward2:
                dic["username"]=name
                dic["passward"]=passward
                user_data.append(dic)
                print(user_data)
#             if passward!=passward2:
#                 print("both passward are not same")
#                 passward2=input("enter the same passward")
#             else:
#                 print("both are saame")
#                 print("succcessfully registered")
#                 age=int(input("enter your age"))
#                 gender=input("male or female")
#                 mail=input("enter your mail")
#                 ph=int(input("enter 10 digit phone number"))
#                 dic["name"]=name
#                 dic["age"]=age
#                 dic["gender"]=gender
#                 dic["mail"]=mail
#                 dic["ph"]=ph
#                 dic["passward"]=passward
#                 with open("signup.json","a+") as file:
#                     json.dump(dic,file,indent=4)
#                 print(dic)
#                 if name not in "signup.json":
#                     print("congrats",name,"you are signed up successfully")
#                 else:
#                     print("user name already exist")
#         else:
#             ("ur passward is not a strong passward")
#     else:
#         print("please enter 8 digit passward")
#         passward=input("enter ur passward")
# elif user=="login":
#     name2=input("enter your name")
#     passward2=input("enter your passward")
#     if name==name2 and passward==passward2:
#         print("login successfully>.........")
#     else:
#         print("invalid")

    