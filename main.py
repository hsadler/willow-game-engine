import math
import random
import arcade
from arcade.pymunk_physics_engine import PymunkPhysicsEngine

import settings
from gameobjects import Wall, Ball


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, settings.SCREEN_TITLE)
        self.set_update_rate(1/settings.FPS)
        self.set_fullscreen(True)
        self.physics_engine = PymunkPhysicsEngine(
            gravity=(0, settings.GRAVITY),
            damping=settings.DAMPING,
        )
        self.sprites = arcade.SpriteList()
        self.num_circles = settings.BALL_COUNT

    def create_walls(self):
        # Bottom wall
        bottom = Wall(
            x=settings.SCREEN_WIDTH // 2,
            y=settings.WALL_THICKNESS // 2,
            width=settings.SCREEN_WIDTH,
            height=settings.WALL_THICKNESS,
            color=arcade.color.WHITE,
        )
        # Top wall
        top = Wall(
            x=settings.SCREEN_WIDTH // 2,
            y=settings.SCREEN_HEIGHT - settings.WALL_THICKNESS // 2,
            width=settings.SCREEN_WIDTH,
            height=settings.WALL_THICKNESS,
            color=arcade.color.WHITE,
        )
        # Left wall
        left = Wall(
            x=settings.WALL_THICKNESS // 2,
            y=settings.SCREEN_HEIGHT // 2,
            width=settings.WALL_THICKNESS,
            height=settings.SCREEN_HEIGHT,
            color=arcade.color.WHITE,
        )
        # Right wall
        right = Wall(
            x=settings.SCREEN_WIDTH - settings.WALL_THICKNESS // 2,
            y=settings.SCREEN_HEIGHT // 2,
            width=settings.WALL_THICKNESS,
            height=settings.SCREEN_HEIGHT,
            color=arcade.color.WHITE,
        )
        for wall in [bottom, top, left, right]:
            self.sprites.append(wall.sprite)
            self.physics_engine.add_sprite(
                wall.sprite,
                body_type=PymunkPhysicsEngine.STATIC,
                friction=0.0,
                elasticity=1.0
            )

    def create_balls(self):
        for _ in range(self.num_circles):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            radius = random.randint(settings.BALL_RADIUS_MIN, settings.BALL_RADIUS_MAX)
            ball = Ball(
                random.randint(settings.WALL_THICKNESS*2, settings.SCREEN_WIDTH - settings.WALL_THICKNESS*2),
                random.randint(settings.WALL_THICKNESS*2, settings.SCREEN_HEIGHT - settings.WALL_THICKNESS*2),
                radius,
                color
            )
            self.sprites.append(ball.sprite)
            # Add circle to physics engine
            self.physics_engine.add_sprite(
                ball.sprite,
                mass=settings.BALL_MASS,
                friction=settings.BALL_FRICTION,
                elasticity=settings.BALL_ELASTICITY
            )
            # Apply random velocity
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(settings.BALL_MIN_INITIAL_VELOCITY, settings.BALL_MAX_INITIAL_VELOCITY)
            velocity = (speed * math.cos(angle), speed * math.sin(angle))
            self.physics_engine.set_velocity(ball.sprite, velocity)
    
    def setup(self):
        # Create walls
        self.create_walls()
        # Create balls
        # self.create_balls()

    def on_update(self, delta_time: float):
        self.physics_engine.step(delta_time)

    def on_draw(self):
        self.clear()
        self.sprites.draw()

if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()
