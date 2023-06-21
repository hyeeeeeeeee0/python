#main.py 
from collision_detection import *

class Character(Sprite):
    def __init__(self, x, y, width, height, image, jump=False):
        super().__init__(x, y, width, height, image)
        self.jump = jump

    def hop(self, distance=300):
        self.y += distance

wizard = Character(-128, 200, 128, 128, "wizard.gif")
goblin = Sprite(128, 200, 108, 128, "goblin.gif")

pacman = Character(-128, 0, 128, 128, "pacman.gif", jump=False)
cherry = Sprite(128, 0, 128, 128, "cherry.gif")

bar = Sprite(0, -350, 128, 24, "bar.gif")
ball = Sprite(0, -150, 32, 32, "ball.gif")

# 스프라이트 모음 리스트
sprites = [wizard, goblin, pacman, cherry, bar, ball]

# 고블린 이동
def move_goblin():
    goblin.x -= 64

    if goblin.x < -300:
        goblin.x = 128

# 팩맨 이동
def move_pacman():
    pacman.x += 30

    if pacman.x > 300:
        pacman.x = -128

# 팩맨 점프
def jump_pacman(distance=300):
    if not pacman.jump:
        pacman.hop(distance)
        pacman.jump = True

    def reset_jump():
        pacman.hop(-300)
        pacman.jump = False

    wn.ontimer(reset_jump, 500)  # 500ms(0.5초) 후에 점프 리셋

# 야구공 이동
def move_ball():
    ball.y -= 24

    if ball.y < -400:
        ball.y = -150

# 이벤트 처리
wn.listen()
wn.onkeypress(move_goblin, "Left")  # 왼쪽 방향 화살표 입력
wn.onkeypress(move_pacman, "Right")  # 오른쪽 방향 화살표 입력
wn.onkeypress(jump_pacman, "space")  # 스페이스 키 입력
wn.onkeypress(move_ball, "Down")  # 아래방향 화살표 입력

while True:

    # 각 스프라이트 위치 이동 및 도장 찍기
    for sprite in sprites:
        sprite.render(pen)

    # 충돌 여부 확인
    if wizard.is_overlapping_collision(goblin):
        wizard.image = "x.gif"

    if pacman.is_distance_collision(cherry):
        cherry.image = "x.gif"

    if bar.is_aabb_collision(ball):
        ball.image = "x.gif"

    # 이미지 복원
    if cherry.image == "x.gif" and not pacman.is_distance_collision(cherry):
        cherry.image = "cherry.gif"
        
    if wizard.image == "x.gif" and not wizard.is_overlapping_collision(goblin):
        wizard.image = "wizard.gif"

    if ball.image == "x.gif" and not bar.is_aabb_collision(ball):
        ball.image = "ball.gif"

    wn.update()  # 화면 업데이트
    pen.clear()  # 스프라이트 이동흔적 삭제
