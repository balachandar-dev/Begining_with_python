# condition

temperature = 22

is_raining = True

if temperature > 35:
    print("Very Hot")
elif temperature > 20:
    print("Hot")
else:
    print("Cold")

if temperature > 35 or temperature < 20 and not is_raining:
    print("Not comfortable")
else:
    print("Comfortable")

#loops

for i in range(5):
    print(i)

for i in range(5,14):
    print(i)

for j in range(2, 10, 3):
    print(j)