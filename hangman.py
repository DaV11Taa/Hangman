from random import randint# Do not delete this line
from HangManWords.hangmanWordBase import definitons

oldOne = ""

def displayIntro():
    print("_______________________________________________\n _                                             \n| |                                            \n| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  \n| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n| | | | (_| | | | | (_| | | | | | | (_| | | | |\n|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n                    __/ |                      \n                   |___/                       \n_______________________________________________")
    print("_____________________Rules_____________________\nTry to guess the hidden word one letter at a   \ntime. The number of dashes are equivalent to   \nthe number of letters in the word. If a player \nsuggests a letter that occurs in the word,     \nblank places containing this character will be \nfilled with that letter. If the word does not  \ncontain the suggested letter, one new element  \nof a hangman’s gallow is painted. As the game  \nprogresses, a segment of a victim is added for \nevery suggested letter not in the word. Goal is\nto guess the word before the man hangs!        \n_______________________________________________")

def displayEnd(result):
    if '+' in str(result) :
        print(f"Hidden word was:  {str(result).removesuffix('+')}\n________________________________________________________________________\n          _                                  _                          \n         (_)                                (_)                         \n__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    \n\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   \n \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      \n  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      \n           | |   (_)    | |                  | (_)                      \n        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ \n       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|\n      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   \n       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   \n________________________________________________________________________")
    else:
        print(f"Hidden word was:  {str(result)}\n __     __           _           _   _                                    \n \ \   / /          | |         | | | |                                   \n  \ \_/ /__  _   _  | | ___  ___| |_| |                                   \n   \   / _ \| | | | | |/ _ \/ __| __| |                                   \n    | | (_) | |_| | | | (_) \__ \ |_|_|                                   \n    |_|\___/ \__,_| |_|\___/|___/\__(_)                                   \n        _______ _                                        _ _          _ _ \n       |__   __| |                                      | (_)        | | |\n          | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |\n          | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |\n          | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|\n          |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)\n__________________________________________________________________________")
    
def displayHangman(state):
    state = int(state)
    if int(state) == 0:
        print(f"                 \n     ._______.   \n     |/      |   \n     |      (_)  \n     |      \|/  \n     |       |   \n     |      / \  \n     |           \n ____|___        \n                 ")
    elif int(state) == 1:
        print(f"                 \n     ._______.   \n     |/      |   \n     |      (_)  \n     |      \|/  \n     |       |   \n     |           \n     |           \n ____|___        \n                 ")
    elif int(state) == 2:
        print(f"                 \n     ._______.   \n     |/      |   \n     |      (_)  \n     |       |   \n     |       |   \n     |           \n     |           \n ____|___        \n                 ")
    elif int(state) == 3:
        print(f"                 \n     ._______.   \n     |/      |   \n     |      (_)  \n     |           \n     |           \n     |           \n     |           \n ____|___        \n                 ")
    elif int(state) == 4:
        print(f"                 \n     ._______.   \n     |/      |   \n     |           \n     |           \n     |           \n     |           \n     |           \n ____|___        \n                 ")
    elif int(state) == 5:
        print(f"                 \n     ._______.   \n     |/          \n     |           \n     |           \n     |           \n     |           \n     |           \n ____|___        \n                 ")

def getWord():
    global oldOne
    #file = open('./HangManWords/hangman-words.txt', 'r')
    file = open('./HangManWords/wordlist.txt', 'r')
    worldlist = list(file.readlines())
    file.close()
    chosenWord = str(worldlist[randint(0,len(worldlist)-1)].replace('\n',''))
    
    #to change the word if it is the same as it was on the last turn.
    while chosenWord == oldOne:
        chosenWord = str(worldlist[randint(0,len(worldlist)-1)].replace('\n',''))

    oldOne = chosenWord
    return chosenWord


def valid(c):
    if len(str(c)) > 1 or len(str(c)) == 0: 
        return False 
    if ord('a') <= ord(c) <= ord('z') and len(str(c)) == 1:
        return True
    else:
        return False

def showDefinition(word):
    print(f'Definition:\n{definitons.get(word)}')

def convent(text):
    covered = ''
    for i in range(0,len(text)):
        covered = covered + '#'
    return covered

def checkandreplace(Covered,trygess,letter):
    Ctrytogess_list = list(Covered)
    indices = [i for i, lett in enumerate(trygess) if lett == letter]
    for i in range(0,len(indices)):
        Ctrytogess_list[indices[i]] = letter

 
    Covered = "".join(Ctrytogess_list)
    return Covered

def play(trytogess):
    Ctrytogess = convent(trytogess)
    lives = 5
    letter = ''
    while True:
        displayHangman(lives)
        if lives == 0:
            break
        print(f'Guess the word:  {Ctrytogess}')
        while True:
            letter = input('Enter the letter: ')
            if valid(letter): break
        if letter in trytogess:
            Ctrytogess = checkandreplace(Ctrytogess, trytogess, letter)
        else:
            lives = lives - 1
        if Ctrytogess == trytogess:
            trytogess = trytogess + '+'
            break
    return trytogess

def hangman():
    while True:
        displayIntro()
        trytogess = getWord()
        showDefinition(trytogess)
        result = play(trytogess)
        displayEnd(result)
        choice = input('Do you want to play again? (yes/no)\n')
        while True :
            if choice == 'no' or choice == 'not' or choice == 'n':
                return
            if choice == 'yes' or choice =='y':
                break
            choice = input('Do you want to play again? (yes/no)\n')
  
if __name__ == "__main__":
    hangman()
