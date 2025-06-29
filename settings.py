import arcade


# Game options
SCREEN_TITLE = "Arcade + Pymunk Physics Example"
SCREEN_WIDTH = arcade.get_display_size()[0]
SCREEN_HEIGHT = arcade.get_display_size()[1]
FPS = 60

# Physics
DAMPING = 0.99
GRAVITY = 0

# Balls
BALL_COUNT = 2
BALL_RADIUS_MIN = 6
BALL_RADIUS_MAX = 6
BALL_MASS = 1.0
BALL_ELASTICITY = 1.0
BALL_FRICTION = 0.0
BALL_MIN_INITIAL_VELOCITY = 0
BALL_MAX_INITIAL_VELOCITY = 10000

# Walls
WALL_THICKNESS = 20
