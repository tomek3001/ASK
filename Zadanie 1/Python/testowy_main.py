import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
import keyboard

kivy.require('1.11.1')
# https://kivy.org/doc/stable/tutorials/pong.html


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            speedup = 1.1
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * speedup
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(0)
    player2 = ObjectProperty(0)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        if self.player1.score | self.player2.score < 1:
            self.ball.move()

            # odbijanie od paletek
            self.player1.bounce_ball(self.ball)
            self.player2.bounce_ball(self.ball)

            # odbijanie z góry i z dołu
            if (self.ball.y < 0) or (self.ball.top > self.height):
                self.ball.velocity_y *= -1

            # odbijanie z lewej i prawej
            if (self.ball.x < 0) or (self.ball.right > self.width):
                self.ball.velocity_x *= -1

            # punkty za nieodbicie
            if self.ball.x < self.x:
                self.player2.score += 1
                self.serve_ball(vel=(4, 0))

            if self.ball.x + self.ball.width > self.width:
                print()
                self.player1.score += 1
                self.serve_ball(vel=(-4, 0))

            mov_speed = 4

            if keyboard.is_pressed('w')\
                    & (self.player1.y + self.player1.height
                       < self.y + self.height - (mov_speed + 1)):
                self.player1.center_y += mov_speed
            if keyboard.is_pressed('s')\
                    & (self.player1.y > self.y + (mov_speed + 1)):
                self.player1.center_y -= mov_speed
            if keyboard.is_pressed('up')\
                    & (self.player2.y + self.player2.height
                       < self.y + self.height - (mov_speed + 1)):
                self.player2.center_y += mov_speed
            if keyboard.is_pressed('down')\
                    & (self.player2.y > self.y + (mov_speed + 1)):
                self.player2.center_y -= mov_speed

        else:
            self.remove_widget(PongPaddle)
            self.remove_widget(PongBall)


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
