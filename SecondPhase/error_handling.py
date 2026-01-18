try:
    # function
    x = 10/ 0
except:
    # do this 
    print("There was an error")


try:
    with open('requirements.txt', 'r') as f:
        text = f.read()
        number = int(text)
        result = 100 / number
        print(f"Result: {result}")
except FileNotFoundError:
    print("File not found")
except ValueError: 
    print("Not a valid number")
finally:
    print("What ever happens, this will work")