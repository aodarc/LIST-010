#name = input("Enter decorator name: ")
#text = input("Enter text for function: ")

def tag(name):
    def decorator(foo):
        def wrapper(text):
            if name.isdigit():   
                return "Error"
            return (f"<{name.lower()}>" f"{foo(text)}" f"</{name.lower()}>")
        return wrapper
    return decorator


# @decorato
# def foo(text):
#     if name.isalpha():
#         return (text.upper())
#     else:
#         print("Error")

TEST_CASES = [
		({'name':'span'}, 'lorem ipsum', '<span>LOREM IPSUM</span>'),
		({'name':'div'}, 'lorem ipsum', '<div>LOREM IPSUM</div>'),
		({'name':'STRONG'}, 'lorem ipsum', '<strong>LOREM IPSUM</strong>'),
		({'name':'123'}, 'lorem ipsum', 'error'),
	]

for case in TEST_CASES:
    @tag(**case[0])
    def foo(text):
            return text.upper()
		

    assert foo(case[1]) == case[2], 'My error'






   


