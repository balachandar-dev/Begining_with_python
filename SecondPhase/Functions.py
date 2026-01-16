def greet():
    print("Hi")

greet()

def add():
    5 + 4

add()

def check_temperature(temperature, is_raining=True): 
    if is_raining:
        print(f"raining, {temperature}'C")
    else:
        print(f"not raining, {temperature}'C")

check_temperature(16, False)
check_temperature(25, True)
check_temperature(is_raining=False, temperature=30)
check_temperature(24)

def calculate_value(price, tax, discount):
    tax_rate = price * tax
    final_price = price + tax - discount
    print(f"final price is {final_price}")

calculate_value(90, 0.25, 10)

def add(a, b): 
    return a + b

added_value = add(10, 5)

print(f"added value is {added_value}")

multiply_two_values = add(10, 5) * add(3, 4)

print(f"multiple value is {multiply_two_values}")

if add(10, 23) > 20:
    print("failed")
else:
    print("success")
