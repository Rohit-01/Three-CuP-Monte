from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    
    guess=[]
    
    while True: 
        guess=input("Pick a CUP number: 0,1 or 2 \n")

        if guess not in ['0','1','2']:
            print("Please Enter any one of number mentioned above โ")
        else:
            break
       
    return int(guess)   

def check_guess(mylist, guess):
    if mylist[guess]=='o':
        print("Congratulation! ๐") 
        print("Its the correct cup! โ")
    
    else:
        print("Worng Guess! โนโน")
        
        print( mylist)
        
#Initial list
mylist=[' ','o',' ']

#Shuffled list
mixed_list=shuffle_list(mylist)

#User guess
guess=player_guess()

#Check Guess
check_guess(mixed_list,guess)