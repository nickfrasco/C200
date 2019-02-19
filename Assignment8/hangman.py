
import random

def insert(board, index, symbol):
    tmp = []
    for i in range(0,len(board)):
        if i == index:
            tmp.append(symbol)
        else:
            tmp.append(board[i])
    return tmp

def get_loc(letter, xlst):
    lst=[]
    for i in range(0, len(xlst)):
        if letter == xlst[i]:
            lst.append(i)
    return lst

def transfer(xlst, board, polst):
    for i in polst:
        board = insert(board,i,xlst[i])
    return board

def display_score(wl):
    print("Wins {0} and Losses {1}".format(wl[0],wl[1]))

def play(word,board,wins,losses):
    already_guessed = []
    cnt = len(list("hangman"))
    print(board)

    while cnt > 0 and "-" in board:
        letter = input("Letter: ")
        if letter not in already_guessed:
            already_guessed.append(letter)
            if letter in word:
                board = transfer(word,board,get_loc(letter,word))
                print(board)
            else:
                cnt -= 1
                print("You have {0} guesses left.".format(cnt))
        else:
            print("You've guessed {0} already...try again".format(letter))
    if "-" in board:
        print("Sorry...")
        print("The word was {0}".format(word))
        return [wins,losses+1]
    else:
        print("Yay!")
        return [wins+1,losses]




wins,losses = 0,0

w = 0
words = [list(random.choice(open("words.txt").readline().split()))]
board = list("-"*len(words[w]))
another_game = 'y'
wl = [0,0]

while another_game == 'y':
    board = list("-"*len(words[w]))
    wl = play(words[w],board,wl[0],wl[1])
    display_score(wl)
    another_game = input("Another game (y/n) ")

print("Thank you for playing. ")

