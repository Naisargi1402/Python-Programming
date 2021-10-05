import random

def choose():
    words=['rainbow', 'computer', 'science', 'photograph', 'life', 'car', 'baseball', 'football']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
    
    
def thank(p1,p2,pp1,pp2):
    print(p1,' Your score is :',pp1)
    print(p2,' Your score is :',pp2)
    print('Thanks for playing.')
    print('Have a nice day !')



p1=input('Player 1, Please enter your name: ')
p2=input('Player 2, Please enter your name: ')
pp1=0
pp2=0
turn=0
while(1):
    picked_word=choose()
    qn=jumble(picked_word)
    print(qn)
    if turn%2==0:
        print(p1,'Your turn. ')
        ans=input('What is on my mind? ')
        if ans==picked_word:
            pp1=pp1+1
            print('Your score is: ',pp1)
        else:
            print('Better luck next time! I thought: ',picked_word)
        
        
    else:
        print(p2,'Your turn. ')
        ans=input('What is on my mind? ')
        if ans==picked_word:
            pp2=pp2+1
            print('Your score is: ',pp2)
        else:
            print('Better luck next time! I thought: ',picked_word)
    c=int(input('Press 1 to continue and 0 to quit: '))
    if c==0:
        thank(p1,p2,pp1,pp2)
        break
    turn=turn+1
        

