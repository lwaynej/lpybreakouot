import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Breakout"

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
PADDLE_Y = 40
PADDLE_SPEED = 5


class BreakoutGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.paddle_x = SCREEN_WIDTH / 2
        self.left_pressed = False
        self.right_pressed = False

    def on_draw(self):
        self.clear()
        paddle_rect = arcade.rect.XYWH(self.paddle_x, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)
        arcade.draw_rect_filled(paddle_rect, arcade.color.WHITE)

    def on_update(self, delta_time):
        if self.left_pressed:
            self.paddle_x -= PADDLE_SPEED
        if self.right_pressed:
            self.paddle_x += PADDLE_SPEED

        # Keep paddle within the screen
        half = PADDLE_WIDTH / 2
        if self.paddle_x < half:
            self.paddle_x = half
        if self.paddle_x > SCREEN_WIDTH - half:
            self.paddle_x = SCREEN_WIDTH - half

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False


def main():
    BreakoutGame()
    arcade.run()


if __name__ == "__main__":
    main()
