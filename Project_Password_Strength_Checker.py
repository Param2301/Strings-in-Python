# My Password Checker Program


password = input("Enter a password: ")


if len(password) < 8:
    print("Your password is too short! It needs to be at least 8 characters.")
else:
    
    has_uppercase = False
    for char in password:
        if char.isupper():
            has_uppercase = True
    
    
    has_lowercase = False
    for char in password:
        if char.islower():
            has_lowercase = True
    

    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
    

    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/\\"
    has_special = False
    for char in password:
        if char in special_chars:
            has_special = True
    

    if has_uppercase and has_lowercase and has_digit and has_special:
        print("Your password is strong! ")
    else:
        print("Your password is not strong enough!")
        
       
        if not has_uppercase:
            print("- You need at least one uppercase letter")
        if not has_lowercase:
            print("- You need at least one lowercase letter")
        if not has_digit:
            print("- You need at least one number")
        if not has_special:
            print("- You need at least one special character (@, #, $ etc.)")

score = 0

if len(password) >= 8:
    score = score + 1
if len(password) >= 10:
    score = score + 1

if has_uppercase:
    score = score + 2
if has_lowercase:
    score = score + 2
if has_digit:
    score = score + 2
if has_special:
    score = score + 3

print("Password strength score: " + str(score) + "/10")

if score <= 3:
    print("Strength: Weak ")
elif score <= 6:
    print("Strength: Medium ")
else:
    print("Strength: Strong ")

print("Thanks for using my password checker!")