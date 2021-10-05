import random

movies=['CASINO ROYALE','MARVEL','HARRY POTTER','TITANIC','TWILIGHT','FAST AND FURIOUS','STAR TREK','INDIANA JONES','KINGSMAN','LORD OF THE RINGS','HOBBIT','THE CHRONICALS OF NARNIA','TRANSFORMERS','INSIDIOUS','JOHNNY ENGLISH','SHERLOCK HOLMES','INTERSTELLAR','INCEPTION','FINAL DESTINATION','JAMES BOND','LARA CROFT TOMB RAIDER','NATIONAL TREASURE','FIFTY SHADES','ZATHURA','MEN IN BLACK','DAN BROWN','CONJURING','ANNABELLA','IT','THE RING','THE GRUDGE','HOME ALONE','BABYS DAY OUT','CARS','ICE AGE','THE JUNGLE BOOK','PIRATES OF THE CARRIBEAN','HUNGER GAMES','MAZE RUNNER','KISSING BOOTH','TO ALL BOYS I HAVE LOVED BEFORE','STAR WARS','I ROBOT','MARTIAN','KNOWING','LIFE OF PI','AMERICAN PIE','PASSENGERS','AVATAR','WOLF OF WALL STREET','SHUTTER ISLAND',
'PERKS OF BEING A WALLFLOWER','EXAM']

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
            
        else:
            temp.append('*')
            
    qn=''.join(str(x) for x in temp)
    return qn
    

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
        
        
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list = list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
            
        else:
            if qn_list[i]=='*':
                temp.append('*')
                
            else:
                temp.append(ref[i])
                
    qn_new=''.join(str(x) for x in temp)
    return qn_new


def play():
    p1name=input('Player 1! Please enter your name: ')
    p2name=input('Player 2! Please enter your name: ')
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            print(p1name,'Your turn ')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said=True
            while not_said:
                letter=input('Your letter: ').upper()
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn, picked_movie,letter)
                    print(modified_qn)
                    d=int(input('Press 1 to guess the movie or 2 to unlock another letter :'))
                    
                    if d==1:
                        ans=input('Your answer: ').upper()
                        if ans==picked_movie:
                            pp1=pp1+1
                            print('Correct')
                            not_said=False
                            print(p1name, 'Your score: ',pp1)
                            
                        else:
                            print('Wrong answer. Try again.')
                            
                else:
                    print(letter,'not found')
                    
            c=int(input('Press 1 to continue or 0 to quit: '))
            if c==0:
                print(p1name, 'Your score: ',pp1)
                print(p2name, 'Your score: ',pp2)
                print('Thanks for playing.')
                print('Have a nice day.')
                willing=False
                    
        else:
            print(p2name,'Your turn ')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said=True
            while not_said:
                letter=input('Your letter: ').upper()
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn, picked_movie,letter)
                    print(modified_qn)
                    d=int(input('Press 1 to guess the movie or 2 to unlock another letter :'))
                    
                    if d==1:
                        ans=input('Your answer: ').upper()
                        if ans==picked_movie:
                            pp2=pp2+1
                            print('Correct')
                            not_said=False
                            print(p2name, 'Your score: ',pp2)
                            
                        else:
                            print('Wrong answer. Try again.')
                            
                else:
                    print(letter,'not found')
                    
            c=int(input('Press 1 to continue or 0 to quit: '))
            if c==0:
                print(p1name, 'Your score: ',pp1)
                print(p2name, 'Your score: ',pp2)
                print('Thanks for playing.')
                print('Have a nice day.')
                willing=False
        
        turn=turn+1
        
        
play()
        