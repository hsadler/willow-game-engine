import arcade
from arcade.pymunk_physics_engine import PymunkPhysicsEngine
import random
import math

# Game options
SCREEN_TITLE = "Arcade + Pymunk Physics Example"
SCREEN_WIDTH = arcade.get_display_size()[0]
SCREEN_HEIGHT = arcade.get_display_size()[1]
FPS = 100

# Game objects
CIRCLES_COUNT = 1000
CIRCLE_RADIUS_MIN = 6
CIRCLE_RADIUS_MAX = 6
CIRCLE_MASS = 1.0
CIRCLE_ELASTICITY = .99
CIRCLE_FRICTION = 0.01
WALL_THICKNESS = 20

# Physics
DAMPING = 0.99
GRAVITY = -900
MIN_INITIAL_VELOCITY = 10
MAX_INITIAL_VELOCITY = 20

class MyGame(arcade.Window):
    def __init__(self, num_circles=CIRCLES_COUNT):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.set_update_rate(1/FPS)
        self.set_fullscreen(True)
        self.physics_engine = PymunkPhysicsEngine(
            gravity=(0, GRAVITY),
            damping=DAMPING,
        )
        self.shapes = arcade.SpriteList()
        self.num_circles = num_circles
    
    def setup(self):
        # Create boundary walls
        
        # Bottom wall
        bottom = arcade.SpriteSolidColor(SCREEN_WIDTH, WALL_THICKNESS, arcade.color.WHITE)
        bottom.center_x = SCREEN_WIDTH // 2
        bottom.center_y = WALL_THICKNESS // 2
        
        # Top wall
        top = arcade.SpriteSolidColor(SCREEN_WIDTH, WALL_THICKNESS, arcade.color.WHITE)
        top.center_x = SCREEN_WIDTH // 2
        top.center_y = SCREEN_HEIGHT - WALL_THICKNESS // 2
        
        # Left wall
        left = arcade.SpriteSolidColor(WALL_THICKNESS, SCREEN_HEIGHT, arcade.color.WHITE)
        left.center_x = WALL_THICKNESS // 2
        left.center_y = SCREEN_HEIGHT // 2
        
        # Right wall
        right = arcade.SpriteSolidColor(WALL_THICKNESS, SCREEN_HEIGHT, arcade.color.WHITE)
        right.center_x = SCREEN_WIDTH - WALL_THICKNESS // 2
        right.center_y = SCREEN_HEIGHT // 2
        
        # Add walls to sprite list and physics engine
        for wall in (bottom, top, left, right):
            self.shapes.append(wall)
            self.physics_engine.add_sprite(
                wall, 
                body_type=PymunkPhysicsEngine.STATIC,
                friction=0.0,
                elasticity=1.0
            )
        
        # Create specified number of circles
        for _ in range(self.num_circles):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            radius = random.randint(CIRCLE_RADIUS_MIN, CIRCLE_RADIUS_MAX)
            circle = arcade.SpriteCircle(radius, color)
            # Random position (away from walls)
            circle.center_x = random.randint(WALL_THICKNESS*2, SCREEN_WIDTH - WALL_THICKNESS*2)
            circle.center_y = random.randint(WALL_THICKNESS*2, SCREEN_HEIGHT - WALL_THICKNESS*2)
            
            self.shapes.append(circle)
            
            # Add circle to physics engine
            self.physics_engine.add_sprite(
                circle,
                mass=CIRCLE_MASS,
                friction=CIRCLE_FRICTION,
                elasticity=CIRCLE_ELASTICITY
            )
            
            # Apply random velocity
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(MIN_INITIAL_VELOCITY, MAX_INITIAL_VELOCITY)
            velocity = (speed * math.cos(angle), speed * math.sin(angle))
            self.physics_engine.set_velocity(circle, velocity)

    def on_update(self, delta_time: float):
        self.physics_engine.step(delta_time)

    def on_draw(self):
        self.clear()
        self.shapes.draw()

if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()
