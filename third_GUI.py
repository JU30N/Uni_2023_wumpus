from tkinter import *

root = Tk()

game_board = Canvas(root, width=500, height=500, background='white')
game_board.grid(row=0, column=0)
button_board = Canvas(root, width=500, height=400, background='black')
button_board.grid(row=1, column=0)










class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive_or_dead = True
        self.player_drawing = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')


    def status(self):
        return self.alive_or_dead
    
    def dead(self):
        self.alive_or_dead = False
        return self.alive_or_dead
    
   

    def get(self):
        """returns a list of the players coordinates"""
        return self.x, self.y

    def move_up(self):
        self.y = self.y - 100
        if self.y == 0:
            self.y = 500
            game_board.delete(self.player_drawing)
            self.player_drawing = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')

        game_board.delete(self.player_drawing)
        self.player_drawing = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')


    def move_down(self):
        self.y = self.y + 100
        if self.y > 500:
            self.y = 100
            game_board.delete(self.player_drawing)
            self.player_drawing = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')

        game_board.delete(self.player_drawing)
        self.player_drawing = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')

    def move_left(self):
        self.x = self.x - 100
        if self.x < 0:
            self.x = 400
            game_board.delete(self.player_drawing)
            self.player_drawing = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')
        game_board.delete(self.player_drawing)
        self.player_drawing = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')

    def move_right(self):
        self.x = self.x + 100
        if self.x > 400:
            self.x = 0
            game_board.delete(self.player_drawing)
            self.player_drawing = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')
        game_board.delete(self.player_drawing)
        self.player_drawing = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')


class Drawing():

    def draw_player(self, x, y):
        self.player_drawing = game_board.create_rectangle(x, y, (x + 100), (y - 100), fill='pink')

    def redraw(self, x, y):
        game_board.delete(self.player_drawing)
        self.player_drawing = game_board.create_rectangle(x, y, (x + 100), (y - 100), fill='pink')

        


class Arrow():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.arrow_amount = 5
        self.arrow = game_board.create_oval(self.x, self.y, (self.x + 100), (self.y - 100), fill='black')
        game_board.delete(self.arrow)


    def remove_arrow_amount(self):
        self.arrow_amount = self.arrow_amount - 1
        if self.arrow_amount == 0:
            return False
        return True

    def shoot(self):
        print("shoot")
    
    def move_up(self):
        self.y = self.y - 100
        if self.y == 0:
            self.y = 500
            game_board.delete(self.arrow)
            self.arrow = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')
        game_board.delete(self.arrow)
        self.arrow = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')

    def move_down(self):
        self.y = self.y + 100
        if self.y > 500:
            self.y = 100
            game_board.delete(self.arrow)
            self.arrow = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')
        game_board.delete(self.arrow)
        self.arrow = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')

    def move_left(self):
        self.x = self.x - 100
        if self.x < 0:
            self.x = 400
            game_board.delete(self.arrow)
            self.arrow = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')
        game_board.delete(self.arrow)
        self.arrow = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')

    def move_right(self):
        self.x = self.x + 100
        if self.x > 400:
            self.x = 0
            game_board.delete(self.arrow)
            self.arrow = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')
        game_board.delete(self.arrow)
        self.arrow = game_board.create_rectangle(self.x, self.y, (self.x + 100), (self.y - 100), fill='pink')




class Wumpus():
    pass
class scents():
    pass

def shooting_arrow(input = 0):
    if input == "z":
        return DISABLED
    else:
        return ACTIVE




class Clicks():
    def __init__(self):
        self.count = 0
        self.button_state = NORMAL
    def add(self):
        self.count = self.count + 1

    def get(self):
        if self.count > 4:
            return False
        else:
            return True
    
    def get_state(self):
        return self.button_state

    def change_state(self):
        if self.button_state == NORMAL:
            self.button_state = DISABLED
        else:
            self.button_state = NORMAL

def main():
    clicks_amount = Clicks()
    if not clicks_amount.get():
        clicks_amount.change_state()
    up_button_arrow = Button(button_board, text= 'up arrow', command=clicks_amount.add(), state=clicks_amount.get_state())
    up_button_arrow.grid(row=0, column= 0)
        
    down_button_arrow = Button(button_board, text= 'down arrow', command=clicks_amount.add(), state=clicks_amount.get_state())
    down_button_arrow.grid(row=2, column= 3)

    left_button_arrow = Button(button_board, text= 'left arrow', command=clicks_amount.add(), state=clicks_amount.get_state())
    left_button_arrow.grid(row=2, column= 0)

    right_button_arrow = Button(button_board, text= 'right arrow', command=clicks_amount.add(), state=clicks_amount.get_state())
    right_button_arrow.grid(row=0, column= 3)

    


def switch():
    if up_button["state"] == NORMAL:
        up_button["state"] = DISABLED
        down_button["state"] = DISABLED
        left_button["state"] = DISABLED
        right_button["state"] = DISABLED
        up_button["text"] = "disabled"
        down_button["text"] = "disabled"
        left_button["text"] = "disabled"
        right_button["text"] = "disabled"
        main()
        

    elif up_button["state"] == DISABLED:
        up_button["state"] = NORMAL
        down_button["state"] = NORMAL
        left_button["state"] = NORMAL
        right_button["state"] = NORMAL
        up_button["text"] = "up"
        down_button["text"] = "down"
        left_button["text"] = "left"
        right_button["text"] = "right"    


player_one = Player(0, 500)
arrow_one = Arrow(0, 500)

    
print("one")
        
up_button = Button(button_board, text= 'up', command= player_one.move_up)
up_button.grid(row=0, column= 1)
    
down_button = Button(button_board, text= 'down', command= player_one.move_down)
down_button.grid(row=2, column= 1)

left_button = Button(button_board, text= 'left', command= player_one.move_left)
left_button.grid(row=1, column= 0)

right_button = Button(button_board, text= 'right', command= player_one.move_right)
right_button.grid(row=1, column= 3)

shoot_button_arrow = Button(button_board, text= 'shoot', command=switch)
shoot_button_arrow.grid(row=1, column= 1)




        






    
root.mainloop()