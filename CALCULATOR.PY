def take_in():
     while True:
        try:
            user_input = input("Enter two numbers (separated by space): ")
            in1 = list(map(int, user_input.split()))

            if len(in1) != 2:
                raise ValueError("Please enter exactly two integers.")
            a = in1[0]
            b = in1[1]
            return a, b

        except ValueError as e:
            print(f"Only enter integers: {e}")


def add():
    x,y= take_in()
    addn = x+y
    print(f"Addition:{addn}")

def sub():
    x,y= take_in()
    subn = x-y
    print(f"subtraction:{subn}")

def multipy():
    x,y= take_in()
    multi = x*y
    print(f"Multiplication:{multi}")

def divide():
    x,y= take_in()
    div = x/y
    print(f"Division:{div}")



print("<------CALCULATOR----->")
while True:
    print("What do you want to do?")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")


    n =input("Enter choice:")

    match n:
        case '1':
            add()
            print()
            

        case '2':
            sub()
            print()

        case '3':
            multipy()
            print()
        
        case '4':
            divide()
            print()

        case '5':
            print("Exiting...")
            break

        case _:
            print("Wrong choice!")

