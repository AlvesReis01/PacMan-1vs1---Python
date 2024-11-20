import turtle
# initialize the window
screen = turtle.Screen()
screen.title("Pac Man 2 vs 2 - Turtle")
screen.bgcolor("lightblue")
screen.setup(width=590, height=740)

# Defining their general basic attributes and behaviors by SuperClass


class Players:
    def __init__(self, color, start_x, start_y):
        self.Points = 0
        self.turtle = turtle.Turtle()
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(start_x, start_y)
        self.turtle.shape("turtle")

    # Receives the direction of movement and check the collision adjusting the angle and calculating the new x and y
    def Movement_Player(self, Direction, Check_Collision):
        angles = {"up": 90, "down": 270, "left": 180, "right": 0}
        Direction_X, Direction_Y = {
            "up": (0, 10),
            "down": (0, -10),
            "left": (-10, 0),
            "right": (10, 0),
        }[Direction]

        self.turtle.setheading(angles[Direction])
        New_X = self.turtle.xcor() + Direction_X
        New_Y = self.turtle.ycor() + Direction_Y

        if not Check_Collision(New_X, New_Y):
            self.turtle.goto(New_X, New_Y)
# Both classes inherit their attributes from the Players class, adjusting only the colors and initial positions.


class Player1(Players):
    def __init__(self):
        super().__init__(color="blue", start_x=-150, start_y=0)


class Player2(Players):
    def __init__(self):
        super().__init__(color="red", start_x=150, start_y=0)


class Map:
    # Sets the block size on the map
    BLOCK_SIZE = 20

    # Defining the map
    # 1 - Solid Block
    # 2 - Empty Space
    def __init__(self):
        self.map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        # Screen Dimensions
        self.map_width = 590
        self.map_height = 640

    # Draw the Map
    def MapaLoad(self):
        self.Drawing_Map()

    # Function that draw one single block per time on the map
    def Drawing_Block(self, x, y, Color):
        Block = turtle.Turtle()
        Block.hideturtle()
        Block.speed(0)
        Block.penup()
        Block.goto(x - self.map_width // 2, y + self.map_height // 2)
        Block.pendown()
        Block.fillcolor(Color)
        Block.begin_fill()
        for _ in range(4):
            Block.forward(self.BLOCK_SIZE)
            Block.right(90)
        Block.end_fill()

    # Go through the map and draw the block
    def Drawing_Map(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == 1:
                    self.Drawing_Block(x * self.BLOCK_SIZE, -y * self.BLOCK_SIZE, "black")

    # Checks if the position (x, y) is colliding with a solid block
    def check_collision(self, x, y):
        Map_X = int((x + self.map_width // 2) // self.BLOCK_SIZE)
        Map_Y = int((-y + self.map_height // 2) // self.BLOCK_SIZE)
        if 0 <= Map_Y < len(self.map) and 0 <= Map_X < len(self.map[0]):
            return self.map[Map_Y][Map_X] == 1
        return True  # Fora do mapa, considerado colisão


class Game:
    # Instances all the classes.
    def __init__(self):
        self.velocidade = 1
        self.player1 = Player1()
        self.player2 = Player2()
        self.map = Map()
        self.score_display = turtle.Turtle()  # Turtle para o placar
        self.score_display.hideturtle()
        self.score_display.penup()
        self.score_display.color("black")
        self.Scoreboard()

    def Menu(self):
        self.map.MapaLoad()
        self.Controls()
    # Defines the controls for the players
    
    def Controls(self):
        screen.listen()
        #  Player1
        screen.onkey(lambda: self.Update_Score_Player1(1), "w")  # Exemplo para incrementar a pontuação
        screen.onkey(lambda: self.player1.Movement_Player("down", self.map.check_collision), "s")
        screen.onkey(lambda: self.player1.Movement_Player("left", self.map.check_collision), "a")
        screen.onkey(lambda: self.player1.Movement_Player("right", self.map.check_collision), "d")

        # Player2
        screen.onkey(lambda: self.Update_Score_Player2(1), "Up")  # Exemplo para incrementar a pontuação
        screen.onkey(lambda: self.player2.Movement_Player("down", self.map.check_collision), "Down")
        screen.onkey(lambda: self.player2.Movement_Player("left", self.map.check_collision), "Left")
        screen.onkey(lambda: self.player2.Movement_Player("right", self.map.check_collision), "Right")
    # Lambda facilita a implementação das teclas sem criar uma função separada para cada uma

    # atualiza o placar
    def Scoreboard(self):
        self.score_display.clear()
        self.score_display.goto(0, 330)  # Ajuste a posição conforme necessário
        score_text = f"Player 1: {self.player1.Points}   |   Player 2: {self.player2.Points}"
        self.score_display.write(score_text, align="center", font=("Arial", 16, "bold"))

    def Update_Score_Player1(self, points):
        self.player1.Points += points
        self.Scoreboard()

    def Update_Score_Player2(self, points):
        self.player2.Points += points
        self.Scoreboard()


game = Game()
game.Menu()
screen.mainloop()
