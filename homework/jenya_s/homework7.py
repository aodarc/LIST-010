def magic_range():

    min_lim, max_lim = None, None

    for i in range(-200, 1000):
        if min_lim is None and i is i and i+1 is i+1:
            min_lim = i+1
            
        if max_lim is None and i+1 is i+1 and i+2 is not i+2:
            max_lim = i+1
        
    return "[{};{})".format(min_lim, max_lim+1)

print(magic_range())
