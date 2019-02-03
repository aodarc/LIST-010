import random
from random import shuffle

list_of_words = ["happy", "exited","lucky",
                 "angry","careful","suprised",
                  "glad","sleepy","shocked",
                  "upset", "worried", "unpleasant",
                  "pessimistic","unhappy","sorry"]



def mixed_list(item):
        word_list = list(item)
        random.shuffle(word_list)
        print(word_list)

def checking(item):
    mixed_list(item)
    for i in range(0,2):
        word1= input("Enter your answer:")
        if word1==item:
            print("Great!")
            return 1
            break
        else:
            print("Wrong!") 
    else: 
        return 0   
   

res = 0
for item in list_of_words:
    res =res + checking (item) 
    print("Your score is {} ".format(res))
    
    

if res >= 13:
    print("Congratulations! Your result is {} !".format(res))
elif res >= 9 and res < 13:
    print("It was great! Your result is {} !".format(res))
else:
    print("You need to be more careful! Your result is {} !".format(res))



