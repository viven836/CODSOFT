import secrets
import string

print("<---WELCOME TO PASSWORD GENERATOR--->")

def generate():
    letters = string.ascii_letters
    numbers = string.digits
    characters = string.punctuation

    password = letters + numbers + characters


    pass_length = int(input("Enter passwoed lenght:"))


    pwd = ''
    for i in range(pass_length):
         pwd += ''.join(secrets.choice(password))

    print(pwd)

while True:
        print('\n')
        generate()
        print('\n')
        reply = input("Do you want to continue? yes/no: ")
        
        if reply.lower() == 'no':
            print("Thank you!")
            break

