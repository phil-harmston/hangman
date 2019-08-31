# Imports needed to code the project
from curses import wrapper
import curses
import random
import string
import json
import functools

"""Use this function to input a custom word then choose option "C" When playing the game"""
def custom_word():
    my_word = "UTAH"
    return my_word

# Used to ease the menu at the beginning of the game.
def erase_menu(stdscr, menu_y):
    stdscr.clear()
    stdscr.border()

# Displays the menu at the beginning of the game.
def display_menu(stdscr, menu_y):
    erase_menu(stdscr, menu_y)
    stdscr.addstr(menu_y +0, 30, '1.) "E" -- EASY MODE')
    stdscr.addstr(menu_y +1, 30, '2.) "A" -- AVERAGE MODE')
    stdscr.addstr(menu_y +2, 30, '3.) "H" -- HARD MODE')
    stdscr.addstr(menu_y +3, 30, '4.) "C" -- CUSTOM WORD')   
    stdscr.addstr(menu_y +4, 30, '5.) "Q" -- PRESS "Q" TO QUIT')
    
    

# Draws the hangman tree in ascii
def draw_game(stdscr):
    
    stdscr.move(2, 5)
    stdscr.addstr('===============')
    for y in range(3,15):
        stdscr.move(y, 5)
        stdscr.addstr('|')
    stdscr.move(y,2 )
    stdscr.addstr('=======')
    stdscr.refresh()

# Draw the fat head using o
def draw_head(stdscr):
    stdscr.move(2, 19)
    stdscr.addstr('oo')
    stdscr.move(3, 18)
    stdscr.addstr('o   o')
    stdscr.move(4, 17)
    stdscr.addstr('o     o')
    stdscr.move(5, 18)
    stdscr.addstr('o   o')
    stdscr.move(6, 19)
    stdscr.addstr('o o')
    stdscr.refresh()

# Draw the body of the person
def draw_body(stdscr):
    stdscr.move(7, 20)
    for y in range(7,12):
        stdscr.move(y, 20)
        stdscr.addstr('|')
    stdscr.refresh()

# Draw the arms and legs of the person
def draw_right_arm(stdscr):
    stdscr.move(8, 20)
    stdscr.addstr('_______')
    
def draw_left_arm(stdscr):
   stdscr.move(8, 14)
   stdscr.addstr('_______')

def draw_right_leg(stdscr):
    stdscr.move(11, 20)
    stdscr.addstr('_______')
    for y in range(12,14):
        stdscr.move(y, 26)
        stdscr.addstr('|')
    
def draw_left_leg(stdscr):
    stdscr.move(11, 14)
    stdscr.addstr('_______')
    for y in range(12,14):
        stdscr.move(y, 14)
        stdscr.addstr('|')

#function opens the file to use and returns the list to the level functions.
def open_file():
    
    with open("dict.json", 'r') as file:
        words = json.load(file)
    return words


# returns words less than 14 and greater than 9 in length
def hard_list():
    hard_word = []
    words = open_file()
    
    for key in words:
        if len(key) < 14 and len(key) > 9:
            hard_word.append(key)
           
    my_word = random.choice(hard_word)

   
    return my_word

# returns words less than 9 greater than 5
def med_list():
    med_word = []
    words = open_file()
    
    for key in words:
        if len(key) < 9 and len(key) > 5:
            med_word.append(key)
    my_word = random.choice(med_word)
    
    return my_word

# returns the words less than 7 and greater than 4
def easy_list():
    easy_word = []
    words = open_file()
    
    for key in words:
        if len(key) < 7 and len(key) > 4:
            easy_word.append(key)
    my_word = random.choice(easy_word)
    
    return my_word
    

# Function used to compare the lists if true returns true else false
# this is how we see if the user won the game or not.
def wordfound(word, my_word):
    if functools.reduce(lambda i, j : i and j, map(lambda m,k: m==k, word, my_word),True):
        return True
    else:  
        return False

# game loop for game play
def gameloop(stdscr, word):
# always start with 6 lives lives are reduce and shown by adding parts to the hangman
    lives = 6
    # holds the user letter selection
    my_word = []
    
    # the game starts off with underscores until a letter is found
    for l in word:
        my_word.append('_')

    while(1):
        # Get input from the user        
        s =''
        c = stdscr.getkey(1,1)  #get key from the user
        # uppercase for comparison
        c = c.upper()
        word = word.upper()
        # special exit charactor for dev purposes exit any time by pressing shift ~
        if c == "~":
            exit()

        if c in word:
            # find the letter in the word and show it.
            for index, letter in enumerate(word):
                if letter == c:
                    my_word[index] = letter
                        
                
            

        # if the letter is not in the word reduce lives by one and hang our hangman
        # each time the game is redrawn so all parts must be redrawn.  This probably needs fixed.
        else:
            lives = lives -1
            if lives == 5:
                draw_head(stdscr)
            if lives == 4:
                draw_head(stdscr)
                draw_body(stdscr)
            if lives == 3:
                draw_head(stdscr)
                draw_body(stdscr)
                draw_left_arm(stdscr)
            if lives == 2:
                draw_head(stdscr)
                draw_body(stdscr)
                draw_left_arm(stdscr)
                draw_right_arm(stdscr)
            if lives == 1:
                draw_head(stdscr)
                draw_body(stdscr)
                draw_left_arm(stdscr)
                draw_right_arm(stdscr)
                draw_left_leg(stdscr)
            if lives ==0:
                draw_head(stdscr)
                draw_body(stdscr)
                draw_left_arm(stdscr)
                draw_right_arm(stdscr)
                draw_left_leg(stdscr)
                draw_right_leg(stdscr)
        
        # creates a string to show the word on the screen after each selection
        stdscr.addstr(20, 15, s.join(my_word))

        # checks to see if the game was won
        if wordfound(word, my_word):
                    win_loose(stdscr, word, game_results=1)
        
        # if lives equal 0 the game was lost
        if lives == 0:
            win_loose(stdscr, word, game_results = 0)
        
# prints the appropriate results of the game win or loose.          
def win_loose(stdscr, word, game_results):
            stdscr.move(18,10)
            stdscr.clrtoeol()
            if game_results == 0:
                stdscr.addstr(18, 10, "I'm sorry, better luck on the next one. Press \"N\" to play again")

                stdscr.move(19, 10)
                answer = 'The word was {} . '.format(word)
                stdscr.addstr(19, 10, answer)
            else:
                stdscr.addstr(18, 10, "Good job,  Press \"N\" to play again")
                answer = 'The word was {} . '.format(word)
                stdscr.addstr(19, 10, answer)
            
            # allows the user to play again if desired.
            c = stdscr.getkey(1,1)  #get key from the user
            c = c.upper()
            if c == 'N':
                print_board(stdscr)


def print_board(stdscr):  
    # sets up the game
    stdscr.clear()  # Clear the screen
    stdscr.border()
    stdscr_y, stdscr_x = stdscr.getmaxyx()
    menu_y = (stdscr_y+5) - 20
    
    # prints the opening menu
    display_menu(stdscr, menu_y)
    c = stdscr.getkey(1,1)  #get key from the user
    stdscr.addstr(c)
    c = c.upper()
    
    if c =='E': #Easy mode
        word = easy_list() 
    if c == 'A':
        word = med_list()    
    if c == 'H':
        word = hard_list()
    if c == 'C':
        word = custom_word()
    if c == 'Q':
        exit()

    # clears the menu on game start
    erase_menu(stdscr, menu_y)
    
    # draws the game and prompts for inpute
    draw_game(stdscr)
    stdscr.addstr(18, 10, 'Choose a letter in the word')
    stdscr.move(20, 15)

    stdscr.addstr('_'*len(word))
    stdscr.refresh()
    gameloop(stdscr, word)

# main function for game play
def main(stdscr):
    print_board(stdscr)
    
    
# if not a module then play the game.
if __name__=="__main__":
    # wraps cursor see cursor doc for more info.
    curses.wrapper(main)
   