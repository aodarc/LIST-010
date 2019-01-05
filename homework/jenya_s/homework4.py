def find_most_frequent(text):

    # making a new string in lowercase
    # and replacing punctuation marks in it with spaces
    sub_str = text.lower()
    translation_table = dict.fromkeys(map(ord, ",.:;!?-"), " ")
    sub_str2 = sub_str.translate(translation_table)
    
    # creating a list of separate words and getting rid of spaces
    lst = [x for x in sub_str2.split(" ") if x!=""]

    max_repeat = max(lst.count(i) for i in lst)
        
    # forming a list of most frequent words without duplicates
    final_lst = list({i for i in lst if lst.count(i) >= max_repeat})

    return sorted(final_lst)

print(find_most_frequent("Tom? WHO ARE YOU, TOm?! You are fool, I:am:Lord-wOldemOrt"))
