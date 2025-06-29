import arcade


class Wall:
    sprite: arcade.Sprite

    def __init__(self, x, y, width, height, color):
        self.sprite = arcade.SpriteSolidColor(width, height, color)
        self.sprite.center_x = x
        self.sprite.center_y = y


class Ball:
    sprite: arcade.SpriteCircle

    # color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # radius = random.randint(CIRCLE_RADIUS_MIN, CIRCLE_RADIUS_MAX)
    # circle = arcade.SpriteCircle(radius, color)
    # # Random position (away from walls)
    # circle.center_x = random.randint(WALL_THICKNESS*2, SCREEN_WIDTH - WALL_THICKNESS*2)
    # circle.center_y = random.randint(WALL_THICKNESS*2, SCREEN_HEIGHT - WALL_THICKNESS*2)
    
    # self.shapes.append(circle)
    
    # # Add circle to physics engine
    # self.physics_engine.add_sprite(
    #     circle,
    #     mass=CIRCLE_MASS,
    #     friction=CIRCLE_FRICTION,
    #     elasticity=CIRCLE_ELASTICITY
    # )
    
    # # Apply random velocity
    # angle = random.uniform(0, 2 * math.pi)
    # speed = random.uniform(MIN_INITIAL_VELOCITY, MAX_INITIAL_VELOCITY)
    # velocity = (speed * math.cos(angle), speed * math.sin(angle))
    # self.physics_engine.set_velocity(circle, velocity)

    def __init__(self, x, y, radius, color):
        self.sprite = arcade.SpriteCircle(radius, color)
        self.sprite.center_x = x
        self.sprite.center_y = y
        self.sprite.color = color
