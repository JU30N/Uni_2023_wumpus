from tkinter import *
from tkinter import messagebox
root = Tk() 







class Game():
    def __init__(self):
        
        self.button_board = Canvas(root, bg= "red", width= 500, height=200)
        self.game_board = Canvas(root, bg="white", width = 400, height=500)
        self.button_board.grid(row=1, column= 0)
        self.game_board.grid(row=0, column= 0)
     
        self.shoot_arrow = True

        self.amount_of_moves = 0

        self.player_x = 0
        self.player_y = 0

        self.arrow_x = self.player_x
        self.arrow_y = self.player_y

        self.wumpus_x = 0
        self.wumpus_y = 400

        self.wumpus_x_smell_1 = 0
        self.wumpus_y_smell_1 = 300
        self.wumpus_x_smell_2 = 100
        self.wumpus_y_smell_2 = 400

        self.teleport_smell_x_1 = 100
        self.teleport_smell_y_1 = 0
        self.teleport_smell_x_2 = 200
        self.teleport_smell_y_2 = 100
        self.teleport_smell_x_3 = 300
        self.teleport_smell_y_3 = 0

        self.teleport_x = 200
        self.teleport_y = 0

        self.teleport_to_x = 300
        self.teleport_to_y = 0

        self.death_x = 300
        self.death_y = 200
        self.death_x_1 = 300
        self.death_y_1 = 100
        self.death_x_2 = 200
        self.death_y_2 = 200
        self.death_x_3 = 300
        self.death_y_3 = 300

        self.shooting_mode = False
        self.shooting_clicks = 0
        self.amount_of_arrows = 3

        self.player_drawing = self.game_board.create_rectangle(0, 0, 100, 100, fill="black")
        
        
    def add_to_moves(self):
        self.amount_of_moves = self.amount_of_moves + 1
    
    def get_to_moves(self):
        return f"{self.amount_of_moves}"
    
    def __str__(self):
        return f"{self.amount_of_arrows}"

    def test(self):
        print("hello")

    def up_move_player(self):
            self.add_to_moves()
            if self.shooting_mode:
                if self.shooting_clicks < 3:
                    self.up__move_arrow()
                    return
                self.shooting_mode = False
                self.game_board.delete(self.arrow_drawing)

            self.player_y = self.player_y - 100
            if self.player_y < 0:
                self.player_y = 400
            self.game_board.moveto(self.player_drawing, self.player_x, self.player_y)
            self.check_player_vs_other_locations(self.player_x, self.player_y)
            print(self.player_x, self.player_y)
            if self.amount_of_arrows == 0:
                    messagebox.showinfo("show", "game lost")
                    quit()

            
    def down__move_player(self):
            self.add_to_moves()
            if self.shooting_mode:
                if self.shooting_clicks < 3:
                    self.down__move_arrow()
                    return
                self.shooting_mode = False
                self.game_board.delete(self.arrow_drawing)

            self.player_y = self.player_y + 100
            if self.player_y > 400:
                self.player_y = 0
            self.game_board.moveto(self.player_drawing, self.player_x, self.player_y)
            self.check_player_vs_other_locations(self.player_x, self.player_y)
            print(self.player_x, self.player_y)
            if self.amount_of_arrows == 0:
                    messagebox.showinfo("show", "game lost")
                    quit()


    def right__move_player(self):
            self.add_to_moves()
            if self.shooting_mode:
                if self.shooting_clicks < 3:
                    self.right__move_arrow()
                    return
                self.shooting_mode = False
                self.game_board.delete(self.arrow_drawing)
                if self.amount_of_arrows == 0:
                    messagebox.showinfo("show", "game lost")
                    quit()

                

            self.player_x = self.player_x - 100
            if self.player_x < 0:
                self.player_x = 300
            self.game_board.moveto(self.player_drawing, self.player_x, self.player_y)
            self.check_player_vs_other_locations(self.player_x, self.player_y)
            print(self.player_x, self.player_y)
            if self.amount_of_arrows == 0:
                messagebox.showinfo("show", "game lost")
                quit()

    def left__move_player(self):
            self.add_to_moves()
            if self.shooting_mode:
                if self.shooting_clicks < 3:
                    self.left__move_arrow()
                    return
                self.shooting_mode = False
                self.game_board.delete(self.arrow_drawing)

            self.player_x = self.player_x + 100
            if self.player_x > 300:
                self.player_x = 0
            self.game_board.moveto(self.player_drawing, self.player_x, self.player_y)
            self.check_player_vs_other_locations(self.player_x, self.player_y)
            print(self.player_x, self.player_y)
            if self.amount_of_arrows == 0:
                messagebox.showinfo("show", "game lost")
                quit()



    def down__move_arrow(self):
            self.arrow_y = self.arrow_y + 100
            if self.arrow_y > 400:
                self.arrow_y = 0
            print(self.arrow_x, self.arrow_y)
            self.shooting_clicks = self.shooting_clicks + 1
            print(self.shooting_clicks)
            self.game_board.moveto(self.arrow_drawing, self.arrow_x, self.arrow_y)
            self.check_arrow_vs_wumpus_location(self.arrow_x, self.arrow_y)
            
    def up__move_arrow(self):         
            self.arrow_y = self.arrow_y - 100
            if self.arrow_y < 0:
                self.arrow_y = 400
            print(self.arrow_x, self.arrow_y)
            self.shooting_clicks = self.shooting_clicks + 1
            print(self.shooting_clicks)
            self.game_board.moveto(self.arrow_drawing, self.arrow_x, self.arrow_y)
            self.check_arrow_vs_wumpus_location(self.arrow_x, self.arrow_y)

    def right__move_arrow(self):
            self.arrow_x = self.arrow_x - 100
            if self.arrow_x < 0:
                self.arrow_x = 300
            print(self.arrow_x, self.arrow_y)
            self.shooting_clicks = self.shooting_clicks + 1
            print(self.shooting_clicks)
            self.game_board.moveto(self.arrow_drawing, self.arrow_x, self.arrow_y)
            self.check_arrow_vs_wumpus_location(self.arrow_x, self.arrow_y)

    def left__move_arrow(self):
            self.arrow_x = self.arrow_x + 100
            if self.arrow_x > 300:
                self.arrow_x = 0
            print(self.arrow_x, self.arrow_y)
            self.shooting_clicks = self.shooting_clicks + 1
            print(self.shooting_clicks)
            self.game_board.moveto(self.arrow_drawing, self.arrow_x, self.arrow_y)
            self.check_arrow_vs_wumpus_location(self.arrow_x, self.arrow_y)
  
    def check_arrow_vs_wumpus_location(self, location_x, location_y):
        if location_x == self.wumpus_x and location_y == self.wumpus_y:
            with open("high_score_GUI", "a",) as file:
                score = self.get_to_moves()
                file.write(score)
                file.write("\n")
                
            messagebox.showinfo("show", "game won")
            quit()

    

    def change_mode(self):
        self.add_to_moves()
        self.shooting_mode = True
        self.shooting_clicks = 0
        self.amount_of_arrows = self.amount_of_arrows - 1
        self.arrow_x = self.player_x
        self.arrow_y = self.player_y
        if self.amount_of_arrows < 0:
            self.shooting_mode = False
        else:
            self.val_one = self.arrow_x + 100
            self.val_two = self.arrow_y + 100
            self.arrow_drawing = self.game_board.create_oval(self.arrow_x, self.arrow_y, self.val_one, self.val_two, fill="green")
        self.change_text()

    def change_text(self):
        if self.amount_of_arrows < 0:
            amount_of_arrows.config(text="0")

        else:
            amount_of_arrows.config(text=self.amount_of_arrows)


        







    def check_player_vs_other_locations(self, location_x, location_y):
        if location_x == self.wumpus_x and location_y == self.wumpus_y:
            messagebox.showinfo("show", "game lost")
            quit()
        elif location_x == self.wumpus_x_smell_1 and location_y == self.wumpus_y_smell_1:
            print("scary")
            self.wumpus_drawing = self.game_board.create_rectangle(0, 300, 50, 350, fill="blue")

        elif location_x == self.wumpus_x_smell_2 and location_y == self.wumpus_y_smell_2:
            print("scary")
            self.wumpus_drawing = self.game_board.create_rectangle(100, 400, 150, 450, fill="blue")



        elif location_x == self.teleport_x and location_y == self.teleport_y:
            print("teleported1")
            root.after(2000)
            self.player_x = self.teleport_to_x
            self.player_y = self.teleport_to_y
            self.game_board.moveto(self.player_drawing, self.player_x, self.player_y)

        elif location_x == self.teleport_smell_x_1 and location_y == self.teleport_smell_y_1:
            print("u smell")
            smell_teleport = self.game_board.create_rectangle(100, 0, 150, 50, fill="green")
        
        elif location_x == self.teleport_smell_x_2 and location_y == self.teleport_smell_y_2:
            print("u smell")
            smell_teleport = self.game_board.create_rectangle(200, 100, 250, 150, fill="green")
        
        elif location_x == self.teleport_smell_x_3 and location_y == self.teleport_smell_y_3:
            print("u smell")
            smell_teleport = self.game_board.create_rectangle(350, 0, 300, 50, fill="green")


        elif location_x == self.death_x_1 and location_y == self.death_y_1:
            print("u can smell death")
            smell_death = self.game_board.create_rectangle(300, 100, 350, 150, fill="yellow")

        elif location_x == self.death_x_2 and location_y == self.death_y_2:
            print("u can smell death")
            smell_death = self.game_board.create_rectangle(200, 200, 250, 250, fill="yellow")

        elif location_x == self.death_x_3 and location_y == self.death_y_3:
            print("u can smell death")
            smell_death = self.game_board.create_rectangle(300, 300, 350, 350, fill="yellow")
        
        elif location_x == self.death_x and location_y == self.death_y:
            print("ur death")
            messagebox.showinfo("show", "game lost")
            quit()

        
        

  
    
game = Game()

upp_button = Button(game.button_board, text="up", command=game.up_move_player)
down_button = Button(game.button_board, text="down", command=game.down__move_player)
right_button = Button(game.button_board, text="left", command=game.right__move_player)
left_button = Button(game.button_board, text="right", command=game.left__move_player)

shoot_button = Button(game.button_board, text="shoot", command=game.change_mode)



amount_of_arrows = Label(game.button_board, text="3")


upp_button.grid(row=0, column=1)
down_button.grid(row=2, column=1)
right_button.grid(row=1, column=0)
left_button.grid(row=1, column=3)
shoot_button.grid(row=1, column= 4)
amount_of_arrows.grid(row=1, column=1)


root.mainloop()