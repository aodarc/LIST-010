string = "Mom! Mom! Are you sleeping?! you!!"

string = string.lower()
string = string.replace("-"," ")
string = string.replace(",","")
string = string.replace("!","")
string = string.replace("?","")
string = string.replace(".","")


list_of_string = string.split(" ")

def most_frequent(list_of_string):

    d = {item:list_of_string.count(item) for item in list_of_string }

    max_value = max(d.values())
    most_frequent_word = sorted(key for key in d if d[key] == max_value)
    print(most_frequent_word )

most_frequent(list_of_string)