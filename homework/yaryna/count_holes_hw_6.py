holes = {"0":1,"4":1,"6":1,"8":2,"9":1}

string = str(input("Enter sequence:"))

def count_holes(string):
    string = string.replace("-","")
    #if isinstance(string,int) == True  or string.isdigit()==True:
    if string.isdigit()==True:
        list_of_string = list(string.lstrip('0'))
        res = 0
        for element in list_of_string:
            res += holes.get(element,0)
        print(res)
    else:
        print("Error")




count_holes(string)
