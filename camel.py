# Implement a program that promps the user for the name in camel case and convert it to snake case.
text = input("camelCase: ").strip()
new_text = ""
for i in text:
    if i.islower():
        new_text += i
    else:
        new_text += "_" + i.lower()
print("snake_case:",new_text)