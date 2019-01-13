string = "козак з казок"

def palindrome(string):
    string = string.lower().replace(" ","")
    list_of_string = list(string)

    list_of_string_2 = list(string)
    list_of_string_2.reverse()

    if list_of_string == list_of_string_2:
        print("Yes")
    else:
        print("No")

palindrome(string)