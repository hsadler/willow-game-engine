import arcade


class Wall:
    sprite: arcade.Sprite

    def __init__(self, x, y, width, height, color):
        self.sprite = arcade.SpriteSolidColor(width, height, color)
        self.sprite.center_x = x
        self.sprite.center_y = y


class Ball:
    sprite: arcade.SpriteCircle

    def __init__(self, x, y, radius, color):
        self.sprite = arcade.SpriteCircle(radius, color)
        self.sprite.center_x = x
        self.sprite.center_y = y
        self.sprite.color = color
