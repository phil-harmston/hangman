from curses import wrapper
import curses
import random
import string
import json




def erase_menu(stdscr, menu_y):
        stdscr.move(menu_y, 0)
        stdscr.clrtoeol()
        stdscr.move(menu_y + 1, 0)
        stdscr.clrtoeol()
        stdscr.move(menu_y+ 2, 0)
        stdscr.clrtoeol()
        stdscr.move(menu_y + 3, 0)
        stdscr.clrtoeol()
        stdscr.border()


def display_menu(stdscr, menu_y):
    erase_menu(stdscr, menu_y)
    stdscr.addstr(menu_y, 30, '1.) "E" -- EASY MODE')
    stdscr.addstr(menu_y+1, 30, '2.) "A" -- AVERAGE MODE')
    stdscr.addstr(menu_y+2, 30, '3.) "H" -- HARD MODE')
    stdscr.addstr(menu_y+3, 30, '4.) "Q" -- PRESS "Q" TO QUIT')
    
    

# Draw the game tree for the game
def draw_game(stdscr):
    
    stdscr.move(2, 5)
    stdscr.addstr('===============')
    for y in range(3,15):
        stdscr.move(y, 5)
        stdscr.addstr('|')
    stdscr.move(y,2 )
    stdscr.addstr('=======')
    stdscr.refresh()

# Draw the head of the person
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

# Get the words from the dictionary file
def hard_list():
    hard_word = []
    with open("dict.json", 'r') as file:
        words = json.load(file)
    
    for key in words:
        if len(key) < 14 and len(key) > 9:
            hard_word.append(key)
# To hard code this comment the following line            
    my_word = random.choice(hard_word)

# Uncomment the following line
# Make sure to use the hard level to get this word otherwise
# you will still get a word from the dictionary

    #my_word = "Utah"
    
    return my_word


def med_list():
    med_word = []
    with open("dict.json", 'r') as file:
        words = json.load(file)
    
    for key in words:
        if len(key) < 9 and len(key) > 5:
            med_word.append(key)
    my_word = random.choice(med_word)
    
    return my_word

def easy_list():
    easy_word = []
    with open("dict.json", 'r') as file:
        words = json.load(file)
    
    for key in words:
        if len(key) < 7 and len(key) > 4:
            easy_word.append(key)
    my_word = random.choice(easy_word)
    
    return my_word
    

def lives_left():
    pass
 
def gameloop(stdscr, word):
   
    lives = 6
    my_word = []
    for l in word:
        my_word.append('_')

    while(1):
        
        
        s =''
        c = stdscr.getkey(1,1)  #get key from the user
        
        c = c.upper()
        word = word.upper()
        if c == "~":
            exit()
        if c in word:
            #stdscr.addstr("True")
            for index, letter in enumerate(word):
                if letter == c:
                    my_word[index] = letter
                    
                

        
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
        stdscr.addstr(20, 15, s.join(my_word))
        
        if lives == 0:
            stdscr.move(18,10)
            stdscr.clrtoeol()
            stdscr.addstr(18, 10, "I'm sorry, better luck on the next one. Press \"N\" to play again")

            stdscr.move(19, 10)
            answer = 'The word was {} . '.format(word)
            stdscr.addstr(19, 10, answer)
            c = stdscr.getkey(1,1)  #get key from the user
        #stdscr.addstr(c)
            c = c.upper()
            if c == 'N':
                print_board(stdscr)




        

    
        

def print_board(stdscr):  
    stdscr.clear()  # Clear the screen
    stdscr.border()
    stdscr_y, stdscr_x = stdscr.getmaxyx()
    menu_y = (stdscr_y+5)-10
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
    if c == 'Q':
        exit()

    
    
    
    #stdscr.refresh()
    #stdscr.clear()  # Clear the screen
   
    erase_menu(stdscr, menu_y)
    
    
    draw_game(stdscr)
    stdscr.addstr(18, 10, 'Choose a letter in the word')
    stdscr.move(20, 15)

    stdscr.addstr('_'*len(word))
        
    stdscr.refresh()
    gameloop(stdscr, word)


def de_bug():
    pass

def main(stdscr):
    print_board(stdscr)
    
    

if __name__=="__main__":
    curses.wrapper(main)
   