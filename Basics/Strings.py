name = "John"

content = f"Hi there, my name is {name}!"

content.lower()
name.upper()
content.title()

contains = "Hi" in content
startsWith = content.startswith("I")

new_content = content.replace("Hello", "Hi")
print(new_content)