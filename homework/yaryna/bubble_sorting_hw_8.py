sequence = [{"value": 67},
{"value": -18},
{"value": 89},
{"value": 0},
{"value": 6},
{"value": 12},
{"value": -50},
{"value": 100},
{"value" : -100}]

def bubble_sort(seq, key = lambda elem: elem, reverse = False):
    """sort any sequence

    Keyword arguments:
    seq --  unsorted sequence
    key -- selector of sequence item used for sorting 
    reverse -- if True (default) sorted from min to max
               if False sorted from max to min

    Returns: sorted sequence 
    """
    seq_lst = list(sequence)
    ln_seq = len(seq_lst) - 1
    for i in range(ln_seq):
        for j in range(len(seq_lst)-i-1):
            if key(seq_lst[j])>key(seq_lst[j+1]):
                seq_lst[j], seq_lst[j+1] = seq_lst[j+1],seq_lst[j]
    if reverse:
        return seq_lst
    else:
        return seq_lst[::-1]


print(bubble_sort(sequence, key = lambda elem:elem["value"], reverse = True))


