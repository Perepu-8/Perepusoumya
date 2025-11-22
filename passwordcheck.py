from string import punctuation as spl
def passwordchecker(password):
    temp=0
    if(len(password)>=8):
        temp+=1
    else:
        print("PASSWORD TOO SHORT. SHOULD CONTAIN ATLEAST 8 CHARACTERS.")
    if(any(chr.isdigit() for chr in password)):
        temp+=1
    else:
        print("PASSWORD SHOULD CONTAIN ATLEAST ONE DIGIT.")
    if(any(chr.islower() for chr in password)):
        temp+=1
    else:
        print("PASSWORD SHOULD CONTAIN ATLEAST ONE LOWERCASE LETTER.")
    if(any(chr.isupper() for chr in password)):
        temp+=1
    else:
        print("PASSWORD SHOULD CONTAIN ATLEAST ONE UPPERCASE LETTER.")
    if(any( ((chr in spl)for chr in password))):
        temp+=1
    else:
        print("PASSWORD SHOULD CONTAIN ATLEAST ONE SPECIAL CHARACTER.")
    if temp>=5:
        return "STRONG 🔥"
    elif temp>=3:
        return"MEDIUM 🙂(CAN IMPROVE)"
    else:
        return"WEAK 🚫"

Password=input("ENTER A PASSWORD: ")
data=passwordchecker(Password)
print("PASSWORD:",data)       

