import tkinter as tk



class Player_arrow_wumpus():
    def __init__(self, x, y, xw= 0, yw= 0, xt= 0, yt= 0, xd= 0, yd= 0):
        self.root = tk.Tk()
        
        self.x_player = x
        self.y_player = y

        
        self.game_board = Canvas(self.root, width=500, height=500, background='white')
        self.game_board.grid(row=0, column=0)
        self.button_board = Canvas(self.root, width=500, height=400, background='black')
        self.button_board.grid(row=1, column=0)

        self.x_arrow = self.x_player
        self.y_arrow = self.y_player

        self.x_wumpus = xw
        self.y_wumpus = yw

        self.x_teleport = xt
        self.y_teleport = yt

        self.x_death = xd
        self.y_death = yd

        self.status_player = True
        self.status_wumpus = True

        self.true_or_false = False

        self.state = DISABLED

        self.amount_of_clicks = 0

        self.count = 0 

        self.create_button()

        self.player_drawing = self.game_board.create_rectangle(self.x_player, self.y_player, (self.x_player + 100), (self.y_player - 100), fill='pink')

        self.main()



    def main(self):
        self.root.mainloop()


    def create_button(self):            
        self.up_button = Button(self.button_board, text= 'up', command= self.move_up_player)
        self.up_button.grid(row=0, column= 1)
            
        self.down_button = Button(self.button_board, text= 'down', command= self.move_down_player)
        self.down_button.grid(row=2, column= 1)

        self.left_button = Button(self.button_board, text= 'left', command= self.move_left_player)
        self.left_button.grid(row=1, column= 0)

        self.right_button = Button(self.button_board, text= 'right', command= self.move_right_player)
        self.right_button.grid(row=1, column= 3)

        self.shoot_button_arrow = Button(self.button_board, text= 'shoot', command=self.enable_shoot)
        self.shoot_button_arrow.grid(row=1, column= 1)

        self.up_button_arrow = Button(self.button_board, text= 'up arrow', state=self.state, command=self.move_up_arrow)
        self.up_button_arrow.grid(row=0, column= 0)
            
        self.down_button_arrow = Button(self.button_board, text= 'down arrow', state=self.state, command=self.move_down_arrow)
        self.down_button_arrow.grid(row=2, column= 3)

        self.left_button_arrow = Button(self.button_board, text= 'left arrow', state=self.state, command=self.move_left_arrow)
        self.left_button_arrow.grid(row=2, column= 0)

        self.right_button_arrow = Button(self.button_board, text= 'right arrow', state=self.state, command=self.move_right_arrow)
        self.right_button_arrow.grid(row=0, column= 3)     

    def enable_shoot(self):
        """disable all the movement for the player and enable shooting"""
        self.up_button.configure(state=DISABLED)
        self.down_button.configure(state=DISABLED)
        self.right_button.configure(state=DISABLED)
        self.left_button.configure(state=DISABLED)

        self.up_button_arrow.configure(state=NORMAL)
        self.down_button_arrow.configure(state=NORMAL)
        self.right_button_arrow.configure(state=NORMAL)
        self.left_button_arrow.configure(state=NORMAL)

    def move_up_player(self):
        self.y_player= self.y_player - 100
        if self.y_player == 0:
            self.y_player = 500
            self.game_board.delete(self.player_drawing)
            self.player_drawing = self.game_board.create_rectangle(self.x_player, self.y_player, (self.x_player + 100), (self.y_player - 100), fill='pink')
        self.game_board.delete(self.player_drawing)
        self.player_drawing = self.game_board.create_rectangle(self.x_player, self.y_player, (self.x_player + 100), (self.y_player - 100), fill='pink')
        
    def move_down_player(self):
        self.y_player = self.y_player + 100
        if self.y_player > 500:
            self.y_player = 100
            self.game_board.delete(self.player_drawing)
            self.player_drawing = self.game_board.create_rectangle(self.x_player, self.y_player, (self.x_player + 100), (self.y_player - 100), fill='pink')

        self.game_board.delete(self.player_drawing)
        self.player_drawing = self.game_board.create_rectangle(self.x_player, self.y_player, (self.x_player + 100), (self.y_player - 100), fill='pink')

    def move_left_player(self):
        self.x_player = self.x_player - 100
        if self.x_player < 0:
            self.x_player = 400
            self.game_board.delete(self.player_drawing)
            self.player_drawing = self.game_board.create_rectangle(self.x_player, self.y_player, (self.x_player + 100), (self.y_player - 100), fill='pink')
        self.game_board.delete(self.player_drawing)
        self.player_drawing = self.game_board.create_rectangle(self.x_player, self.y_player, (self.x_player + 100), (self.y_player - 100), fill='pink')

    def move_right_player(self):
        self.x_player = self.x_player + 100
        if self.x_player > 400:
            self.x_player = 0
            self.game_board.delete(self.player_drawing)
            self.player_drawing = self.game_board.create_rectangle(self.x_player, self.y_player, (self.x_player + 100), (self.y_player - 100), fill='pink')
        self.game_board.delete(self.player_drawing)
        self.player_drawing = self.game_board.create_rectangle(self.x_player, self.y_player, (self.x_player + 100), (self.y_player - 100), fill='pink')

    def move_up_arrow(self):
        self.x_arrow = self.x_player
        self.amount_of_clicks += 1
        self.y_arrow= self.y_arrow - 100
        self.arrow_drawing_one = self.game_board.create_oval(self.x_player, self.y_player, (self.x_player + 100), (self.y_player - 100), fill='blue')
        if self.y_arrow == 0:
            self.y_arrow = 500
            self.game_board.delete(self.arrow_drawing_one)
            self.arrow_drawing_one = self.game_board.create_oval(self.x_arrow, self.y_arrow, (self.x_arrow + 100), (self.y_arrow - 100), fill='blue')

        self.game_board.delete(self.arrow_drawing_one)
        self.arrow_drawing_one = self.game_board.create_oval(self.x_arrow, self.y_arrow, (self.x_arrow + 100), (self.y_arrow - 100), fill='blue')

        """checks how many times the button has been clicked and then normal the up button"""
        if self.amount_of_clicks > 2:
            """makes the movment for player possible"""
            self.up_button.configure(state=NORMAL)
            self.down_button.configure(state=NORMAL)
            self.right_button.configure(state=NORMAL)
            self.left_button.configure(state=NORMAL)

            self.y_arrow = self.y_player
            self.x_arrow = self.x_player


            self.amount_of_clicks = 0
            """makes the movment for arrow impossible"""
            self.up_button_arrow.configure(state=DISABLED)
            self.down_button_arrow.configure(state=DISABLED)
            self.right_button_arrow.configure(state=DISABLED)
            self.left_button_arrow.configure(state=DISABLED)       

    def move_down_arrow(self):
        self.x_arrow = self.x_player
        self.amount_of_clicks += 1
        self.y_arrow = self.y_arrow + 100
        self.arrow_drawing = self.game_board.create_oval(self.x_arrow, self.y_arrow, (self.x_arrow + 100), (self.y_arrow - 100), fill='blue')

        if self.y_arrow > 500:
            self.y_arrow = 100
            self.game_board.delete(self.arrow_drawing)
            self.arrow_drawing = self.game_board.create_oval(self.x_arrow, self.y_arrow, (self.x_arrow + 100), (self.y_arrow - 100), fill='blue')

        self.game_board.delete(self.arrow_drawing)
        self.arrow_drawing = self.game_board.create_oval(self.x_arrow, self.y_arrow, (self.x_arrow + 100), (self.y_arrow - 100), fill='blue')
        """checks how many times the button has been clicked and then normal the up button"""
        if self.amount_of_clicks > 2:
            """makes the movment for player possible"""
            self.up_button.configure(state=NORMAL)
            self.down_button.configure(state=NORMAL)
            self.right_button.configure(state=NORMAL)
            self.left_button.configure(state=NORMAL)

            self.y_arrow = self.y_player
            self.x_arrow = self.x_player

            self.amount_of_clicks = 0
            """makes the movment for arrow impossible"""
            self.up_button_arrow.configure(state=DISABLED)
            self.down_button_arrow.configure(state=DISABLED)
            self.right_button_arrow.configure(state=DISABLED)
            self.left_button_arrow.configure(state=DISABLED)

    def move_left_arrow(self):
        self.y_arrow = self.y_player
        self.amount_of_clicks += 1
        self.x_arrow = self.x_arrow - 100
        self.arrow_drawing = self.game_board.create_oval(self.x_arrow, self.y_arrow, (self.x_arrow + 100), (self.y_arrow - 100), fill='blue')

        if self.x_arrow < 0:
            self.x_arrow = 400
            self.game_board.delete(self.arrow_drawing)
            self.arrow_drawing = self.game_board.create_oval(self.x_arrow, self.y_arrow, (self.x_arrow + 100), (self.y_arrow - 100), fill='blue')
        self.game_board.delete(self.arrow_drawing)
        self.arrow_drawing = self.game_board.create_oval(self.x_arrow, self.y_arrow, (self.x_arrow + 100), (self.y_arrow - 100),fill='blue')
        """checks how many times the button has been clicked and then normal the up button"""
        if self.amount_of_clicks > 2:
            """makes the movment for player possible"""
            self.up_button.configure(state=NORMAL)
            self.down_button.configure(state=NORMAL)
            self.right_button.configure(state=NORMAL)
            self.left_button.configure(state=NORMAL)

            self.y_arrow = self.y_player
            self.x_arrow = self.x_player


            self.amount_of_clicks = 0
            """makes the movment for arrow impossible"""
            self.up_button_arrow.configure(state=DISABLED)
            self.down_button_arrow.configure(state=DISABLED)
            self.right_button_arrow.configure(state=DISABLED)
            self.left_button_arrow.configure(state=DISABLED)

    def move_right_arrow(self):

        self.x_arrow = self.x_arrow + 100
        self.amount_of_clicks += 1
        self.arrow_drawing = self.game_board.create_oval(self.x_arrow, self.y_arrow, (self.x_arrow + 100), (self.y_arrow - 100), fill='blue')

        if self.x_arrow > 400:
            self.x_arrow = 0
            self.game_board.delete(self.arrow_drawing)
            self.arrow_drawing = self.game_board.create_oval(self.x_arrow, self.y_arrow, (self.x_arrow + 100), (self.y_arrow - 100), fill='blue')
        
        """checks how many times the button has been clicked and then normal the up button"""
        if self.amount_of_clicks > 2:
            """makes the movment for player possible"""
            self.up_button.configure(state=NORMAL)
            self.down_button.configure(state=NORMAL)
            self.right_button.configure(state=NORMAL)
            self.left_button.configure(state=NORMAL)

            self.y_arrow = self.y_player
            self.x_arrow = self.x_player


            self.amount_of_clicks = 0
            """makes the movment for arrow impossible"""
            self.up_button_arrow.configure(state=DISABLED)
            self.down_button_arrow.configure(state=DISABLED)
            self.right_button_arrow.configure(state=DISABLED)
            self.left_button_arrow.configure(state=DISABLED)

        self.game_board.delete(self.arrow_drawing)
        self.arrow_drawing = self.game_board.create_oval(self.x_arrow, self.y_arrow, (self.x_arrow + 100), (self.y_arrow - 100),fill='blue')






player_one = Player_arrow_wumpus(0, 500)





        


