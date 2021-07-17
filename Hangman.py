import math
from Hangman_Data import word, alphabet
from random import choice, sample

Hangman = [' ____\n|   |\n|\n|\n|\n|\n-------',' ____\n|   |\n|   0\n|   \n|   \n|   \n-------',' ____\n|   |\n|   0\n|   |\n|   |\n|   \n-------',' ____\n|   |\n|   0\n|  /|\n|   |\n|   \n-------',' ____\n|   |\n|   0\n|  /|\\\n|   |\n|   \n-------',' ____\n|   |\n|   0\n|  /|\\\n|   |\n|  /\n-------',' ____\n|   |\n|   0 ded\n|  /|\\\n|   |\n|  / \\\n-------'][::-1]
alphabet_dict = {i:i for i in alphabet}

def Fill(word_dict : dict, letter : str, space : dict):
    for i in word_dict[letter]:
        space[str(i)] = letter
    return space

def Play(live, alphabet_dict : dict, space : dict, word_dict : dict):
    left = len([i for i in space if space[i] == '_'])
    win = False
    loss = False
    print(Hangman[live])
    print(' '+''.join(list(space.values()))+' {} letter left'.format(left))
    print(' '.join(list(alphabet_dict.values())[0:10]))
    print(' '+' '.join(list(alphabet_dict.values())[10:19]))
    print('  '+' '.join(list(alphabet_dict.values())[19:]))
    guess = input('Enter the Letter : ')
    alphabet_dict[guess] = '_'
    if len(guess) != 1:
        print(SyntaxError)
    elif guess.lower() in list(word_dict.keys()) and guess.lower() not in list(space.values()):
        space = Fill(word_dict, guess, space)
    else:
        live -= 1
        print('Wrong!!!')
    left = len([i for i in space if space[i] == '_'])
    if left == 0:
        win = True
        print(Hangman[live])
    if live == 0:
        loss = True
        print(Hangman[live])
    return live, win, loss

def Repeat():
    Repeat_input = ord(input("Do you want to play Again?(y/n) : ").upper()[0])
    Repeat_input = (True if Repeat_input == 89 else False)
    if Repeat_input:
        Main()
    else:
        quit()

def Main():
    live = len(Hangman)-1
    now_word = choice(word)
    space = {str(i):'_' for i in range(len(now_word))}
    word_dict = {i:[j for j in range(len(now_word)) if now_word[j] == i] for i in set(list(now_word))}
    alphabet_dict = {i:i for i in alphabet}
    hint_input = ord(input("Do you want hint?(y/n) : ").upper()[0])
    hint = (True if hint_input == 89 else False)
    if hint:
        hint_list = sample(list(word_dict.keys()), math.ceil(len(word_dict)/4))
        for i in hint_list:
            space = Fill(word_dict, i, space)
            alphabet_dict[i] = '_'
    while True:
        live, win, loss = Play(live, alphabet_dict, space, word_dict)
        if win:
            print("Win!!")
            break
        if loss:
            print("Game Over!!")
            break
    print(now_word)
    Repeat()

if __name__ == '__main__':
    Main()
