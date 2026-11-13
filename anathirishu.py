password=input("Enter password:")

if (len(password)>=8 and
    any(check.isupper()for check in password)and
    any(check.islower()for check in password)and
    any(check.isdigit()for check in password)and
    any(check in"@#$%*&"for check in password)):
    print("strong password")
else:
    print("weak password")
 
