# Silly osu rank code

def input_rank():
   while True:
        try:
            number = input("What rank are you in osu?")
            rank = int(number)
            if rank>0:
                break
            else:
                print("Thats not a real rank silly!")
        except ValueError:
            print("Enter a number rank")
   return rank

int_rank = input_rank()

def message(rank):
    if rank>=100000:
        return("bad")
    elif rank <100000 and rank>=10000:
        return("5 digit")
    elif rank <10000 and rank>=1000:
        return("4 digit")
    elif rank <1000 and rank>=100:
        return("3 digit")
    else:
        return("good at osu")
    return 

str_rank = message(int_rank)
   
print(f"Your osu rank is #{int_rank}. You are {str_rank}!")