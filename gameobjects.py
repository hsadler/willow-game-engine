import arcade


class Wall:
    sprite: arcade.Sprite

    def __init__(self, x, y, width, height, color):
        self.sprite = arcade.Sprite(color)
        self.sprite.center_x = x
        self.sprite.center_y = y
        self.sprite.width = width
        self.sprite.height = height
        self.sprite.color = color


class Ball:
    sprite: arcade.SpriteCircle

    def __init__(self, x, y, radius, color):
        self.sprite = arcade.SpriteCircle(radius, color)
        self.sprite.center_x = x
        self.sprite.center_y = y
        self.sprite.color = color
