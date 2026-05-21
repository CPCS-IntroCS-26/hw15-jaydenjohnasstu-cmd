import pgzrun

# Variables
TITLE = "Volcano Crystal Hunt"
WIDTH = 800
HEIGHT = 500
velocity_y = 0
player = Rect((40, 400), (10, 10))
gravity = 1
on_ground = True
lives = 3

repeat = True
game_over = False
game_won = False

def draw():
    global repeat

    if game_won:
        screen.clear()
        screen.draw.text("You Win!", center=(400, 250), fontsize=150, color="yellow")
        repeat = False
        return
    
    if game_over:
        screen.clear()
        screen.draw.text("GAME OVER", center=(400, 250), fontsize=150, color="Red")
        repeat = False
        return
    
    if repeat == True:
        screen.clear()
        screen.draw.filled_rect(player, "orange")
        screen.draw.text(f"Volcano Crystal Hunt", (180,100), fontsize=60, color="coral")
        screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="yellow")
        screen.draw.text(f"Lives: {lives}", (10, 50), fontsize=30, color="red")
        screen.draw.filled_rect(lava, "red")

        for platform in platforms:
            screen.draw.filled_rect(platform, "tan")

        for coin in coins:
            screen.draw.filled_rect(coin, "Magenta")


lava = Rect((100, 485), (700, 15))

platforms = [
    Rect((0, 470), (100, 30)),
    Rect((150, 380), (50, 10)),
    Rect((250, 300), (50, 10)),
    Rect((100, 220), (50, 10)),
    Rect((490, 350), (50, 10)),
    Rect((600, 270), (50, 10)),
    Rect((740, 170), (50, 10)),
    Rect((637, 460), (25, 10))
]

coins = [
    Rect((170, 340), (10, 20)),
    Rect((270, 260), (10, 20)),
    Rect((120, 180), (10, 20)),
    Rect((510, 310), (10, 20)),
    Rect((620, 230), (10, 20)),
    Rect((760, 130), (10, 20)),
    Rect((645, 420), (10, 20))
]

score = 0

def update():
    # This function updates the game over and over
    global velocity_y, on_ground
    if keyboard.left:
        player.x -= 5

    if keyboard.right:
        player.x += 5

    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

    global velocity_y

    velocity_y += gravity
    player.y += velocity_y

    if keyboard.space and on_ground:
        velocity_y = -15
        on_ground = False

    for platform in platforms:
        if player.colliderect(platform) and velocity_y > 0:
            player.bottom = platform.top
            velocity_y = 0
            on_ground = True

    global lives

    global game_over



    if player.colliderect(lava):
        player.x = 40
        player.y = 400
        velocity_y = 0
        lives -= 1
        if lives == 0:
            game_over = True


    global score

    global game_won

    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1
            if score == 7:
                game_won = True

pgzrun.go()