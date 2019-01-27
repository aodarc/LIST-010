string = "козак з казок"

def palindrome(string):
    string = string.lower().replace(" ","")

    if string == string[::-1]:
        print("Yes")
    else:
        print("No")

palindrome(string)