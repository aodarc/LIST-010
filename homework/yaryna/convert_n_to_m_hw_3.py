import string

def convert_to_10(converted_number):
    len_dict_converted_number = len(dict_converted_number)
    number_in_10=0
    for key in dict_converted_number:
       converted_number_to_10 =int(dict_converted_number.get(key))*n**(len_dict_converted_number- key-1)
       number_in_10 += converted_number_to_10
    return number_in_10 
    

def convert_to_m(number_in_10):
    list_of_rest = []
    whole_part = 37
    while whole_part > m:
        whole_part = number_in_10 // m
        rest = number_in_10 - whole_part*m
        number_in_10 = whole_part
        list_of_rest.append(rest)
    else:
        list_of_rest.append(whole_part)
    list_of_rest.reverse()

    replace_keys = {value: key for key, value in replace_value.items()}
    for element in list_of_rest:
        if element in replace_keys:
             list_of_rest[list_of_rest.index(element)]=replace_keys.get(element)

    number_in_m =""
    for i in range(len(list_of_rest)):
        number_in_m += str(list_of_rest[i])
    return str(number_in_m)
  
converted_number=input("Enter integer number: ")
n=int(input("Enter first notation: "))
m=int(input("Enter second notation: "))
replace_value = {s: i for i, s in enumerate(string.ascii_uppercase, start=10)}
converted_number = converted_number.upper()
lst_converted_number = list(converted_number)
for element in lst_converted_number:
    if element in replace_value:
        lst_converted_number[lst_converted_number.index(element)]=replace_value.get(element)
dict_converted_number = {i:lst_converted_number[i] for i in range(len(lst_converted_number))}





if ("." in converted_number) or ("-" in converted_number) or ("[" in converted_number) or ("]" in converted_number):
    print("False")
elif m==1:
    number_in_10 = convert_to_10(converted_number)
    print("0"*number_in_10)
for element in lst_converted_number:
    if int(element) >=n:
        print("False")
else:
    number_in_10 = convert_to_10(converted_number)
    print(convert_to_m(number_in_10))


 