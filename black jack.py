import random
import os
os.system('cls')
balance = 4000
def game():
    global balance
    print('''
  .------.            _     _            _    _            _    
  |A_  _ |.          | |   | |          | |  (_)          | |   
  |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
  | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
  |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
  `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        `------'                           |__/           
    ''')
    print(f"your balance:${balance}")
    bet = int(input("how much you want to bet?"))
    while bet>balance:
        bet = int(input("insufficient balance:"))
    balance-=bet
    print(f"new balance:${balance}")
    stopper = []
    deck = []
    def prin(cards):
        for i in range(len(cards)):
            if i ==0:
                print(" ",end="")
            print("___   ",end="") 
        print()
        for i in range(len(cards)):
            if cards[i][0]=='10':
                print("|10 | ",end="")
            else:    
                print(f"|{cards[i][0]}  | ",end="") 
        print()
        for i in range(len(cards)):
            print(f"| {cards[i][1]} | ",end="")
        print()       
        for i in range(len(cards)):
            if cards[i][0]=='10':
                print("|_10| ",end="")
            else:    
                print(f"|__{cards[i][0]}| ",end="")
        return("")        
    for suit in ('♥','♦','♠','♣'):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
            random.shuffle(deck)
    b = [deck.pop(), deck.pop()]
    c = [deck.pop(), deck.pop()]
    fake = ['?','#']
    hidden = [c[0],fake ]
    def your_score(e):
        f = [];score=0;A_counter=0
        for i in e:
            f.append(i[0])
        for i in f:
            if i=="Q" or i=="K" or i=="J":
                f[f.index(i)]=10
            if i=="A":
                f[f.index(i)]=11;A_counter+=1         
        for i in f:
            score+=int(i)
        for i in range(A_counter):    
            if score>21:
                score-=10
        return score
    print ("your cards:")
    print(f"{prin(b)}\n\ncurrent score is {your_score(b)}") 
    print (f"computer's card :")
    print(f"\n{prin(hidden)}")  
    def replay(choice):
        global balance
        os.system('cls')
        print('''
  .------.            _     _            _    _            _    
  |A_  _ |.          | |   | |          | |  (_)          | |   
  |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
  | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
  |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
  `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        `------'                           |__/           
    ''')
        print(f"your balance:{balance}")    
        if choice=="y":
            b.append(deck.pop())
            c.append(deck.pop())
            hidden.append(fake)
        print (f"your card:")
        print(f"\n{prin(b)}\ncurrent score is {your_score(b)}") 
        print (f"computer's card :")
        print(f"\n{prin(hidden)}") 
        if your_score(b)>21 and your_score(c)>21:
              print(f"you lose${bet}!!!");stopper.append("a")
              print(f"computer's card were:") 
              print(f"\n{prin(c)}\n")
        if your_score(b)>21 and your_score(c)<=21 :
            print(f"you lose${bet}!!!")
            print(f"computer's card were:")
            print( f"\n{prin(c)}\n");stopper.append("a")  
        if choice=="n":
            if your_score(c)>21:
                print(f"congrats you won${bet}!!!!!");stopper.append("a");balance+=2*bet
                print(f"computer's card were:")
                print(f"\n{prin(c)}\n")
            elif your_score(b)>your_score(c):
                print(f"congrats you won:${bet}!!!!!");stopper.append("a");balance+=2*bet
                print(f"computer's card were:") 
                print(f"\n{prin(c)}\n")
            elif your_score(b)==your_score(c):
                print("it's a draw");stopper.append("a");balance+=bet
                print(f"computer's card were:") 
                print(f"\n{prin(c)}\n")
            else:
                print(f"you lose${bet}!!!");stopper.append("a")
                print(f"computer's card were:") 
                print(f"\n{prin(c)}\n")
    while len(stopper)==0:                  
        replay(input("do you want draw one more card type y or n:"))
game()
while True:
    cont = input("do you want to play again?(type y/n):\n")
    if cont == "y":
        if balance>0:
            os.system('cls')
            game()
        else:
            print("insufficient balance to continue :/")
            exit()    
    elif cont == "n":
        exit()
    else: 
        print("input from given choice only!!!")
        