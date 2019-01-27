name = input("Enter decorator name: ")
text = input("Enter text for function: ")

def decorator(foo,name = name):
    def wrapper(text):
        return (f"<{name.lower()}>" f"{foo(text)}" f"</{name.lower()}>")
    return wrapper

if name.isalpha() is True:
    @decorator
    def foo(text):
        return (text.upper())
else:
    print("Error")

print(foo(text))



   


