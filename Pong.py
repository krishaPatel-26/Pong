import turtle
import time

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score and lives
score_a = 0
score_b = 0
lives_a = 3
lives_b = 3
WINNING_SCORE = 10  

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a} (Lives: {lives_a})  Player B: {score_b} (Lives: {lives_b})", 
          align="center", font=("Courier", 20, "normal"))

# Paddle movement
paddle_speed = 8
keys_pressed = {
    "w": False,
    "s": False,
    "up": False,
    "down": False
}

# Track if ball was just hit to avoid multiple score increases
just_hit_a = False
just_hit_b = False

# Functions
def set_key_pressed(key, value):
    keys_pressed[key] = value

def paddle_a_up():
    set_key_pressed("w", True)

def paddle_a_down():
    set_key_pressed("s", True)

def paddle_b_up():
    set_key_pressed("up", True)

def paddle_b_down():
    set_key_pressed("down", True)

def paddle_a_up_release():
    set_key_pressed("w", False)

def paddle_a_down_release():
    set_key_pressed("s", False)
    
def paddle_b_up_release():
    set_key_pressed("up", False)

def paddle_b_down_release():
    set_key_pressed("down", False)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeyrelease(paddle_a_up_release, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeyrelease(paddle_a_down_release, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeyrelease(paddle_b_up_release, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeyrelease(paddle_b_down_release, "Down")

def update_paddles():
    # Move paddle A
    if keys_pressed["w"] and paddle_a.ycor() < 250:
        paddle_a.sety(paddle_a.ycor() + paddle_speed)
    if keys_pressed["s"] and paddle_a.ycor() > -240:
        paddle_a.sety(paddle_a.ycor() - paddle_speed)
    
    # Move paddle B
    if keys_pressed["up"] and paddle_b.ycor() < 250:
        paddle_b.sety(paddle_b.ycor() + paddle_speed)
    if keys_pressed["down"] and paddle_b.ycor() > -240:
        paddle_b.sety(paddle_b.ycor() - paddle_speed)

def update_display():
    pen.clear()
    pen.write(f"Player A: {score_a} (Lives: {lives_a})  Player B: {score_b} (Lives: {lives_b})", 
             align="center", font=("Courier", 20, "normal"))
    
def check_winner():
    # COMMON PONG: First to WINNING_SCORE points wins
    if score_a >= WINNING_SCORE:
        return "Player A"
    elif score_b >= WINNING_SCORE:
        return "Player B"
    # Optional: Also check lives (if you want hybrid system)
    elif lives_a <= 0:
        return "Player B"
    elif lives_b <= 0:
        return "Player A"
    return None

def reset_ball():
    ball.goto(0, 0)
    ball.dx = 2.5 if ball.dx > 0 else -2.5
    ball.dy = 2.5 if ball.dy > 0 else -2.5

# Main game loop
try:
    last_time = time.time()
    game_over = False
    
    while True:
        if game_over:
            break
            
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time
        
        # Update paddles based on key states
        update_paddles()
        
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        # Border checking - Top and bottom
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
        
        # Border checking - Left and right (LOSE LIFE when ball gets past you)
        # When ball goes past Player B (right side)
        if ball.xcor() > 390:
            lives_b -= 1  # Player B loses a life (failed to save)
            update_display()
            
            winner = check_winner()
            if winner:
                pen.clear()
                pen.goto(0, 0)
                pen.write(f"{winner} WINS!", align="center", font=("Courier", 36, "normal"))
                wn.update()
                time.sleep(3)
                game_over = True
                continue
                
            reset_ball()
            # Reset hit flags
            just_hit_a = False
            just_hit_b = False
        
        # When ball goes past Player A (left side)
        elif ball.xcor() < -390:
            lives_a -= 1  # Player A loses a life (failed to save)
            update_display()
            
            winner = check_winner()
            if winner:
                pen.clear()
                pen.goto(0, 0)
                pen.write(f"{winner} WINS! First to {WINNING_SCORE}", align="center", font=("Courier", 36, "normal"))
                wn.update()
                time.sleep(3)
                game_over = True
                continue
                
            reset_ball()
            # Reset hit flags
            just_hit_a = False
            just_hit_b = False
        
        # Paddle and ball collisions - THIS IS WHERE YOU "SAVE" THE BALL AND GET POINTS
        # Paddle A (Player A saves the ball)
        if (-350 < ball.xcor() < -340) and \
           (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
            ball.setx(-340)  # Ensure ball doesn't get stuck
            ball.dx *= -1.05  # Slight speed increase on bounce
            
            # Add some paddle-induced spin
            paddle_center = paddle_a.ycor()
            hit_position = ball.ycor() - paddle_center
            ball.dy += hit_position * 0.02
            
            # Player A successfully saved the ball - GETS A POINT!
            if not just_hit_a:  # Only add score once per hit
                score_a += 1
                update_display()
                just_hit_a = True
                just_hit_b = False  # Reset other player's hit flag
                
                # Check for winner after scoring
                winner = check_winner()
                if winner:
                    pen.clear()
                    pen.goto(0, 0)
                    pen.write(f"{winner} WINS! First to {WINNING_SCORE}", align="center", font=("Courier", 36, "normal"))
                    wn.update()
                    time.sleep(3)
                    game_over = True
                    continue
        
        # Paddle B (Player B saves the ball)
        elif (340 < ball.xcor() < 350) and \
             (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
            ball.setx(340)  # Ensure ball doesn't get stuck
            ball.dx *= -1.05  # Slight speed increase on bounce
            
            # Add some paddle-induced spin
            paddle_center = paddle_b.ycor()
            hit_position = ball.ycor() - paddle_center
            ball.dy += hit_position * 0.02
            
            # Player B successfully saved the ball - GETS A POINT!
            if not just_hit_b:  # Only add score once per hit
                score_b += 1
                update_display()
                just_hit_b = True
                just_hit_a = False  # Reset other player's hit flag
                
                # Check for winner after scoring
                winner = check_winner()
                if winner:
                    pen.clear()
                    pen.goto(0, 0)
                    pen.write(f"{winner} WINS! First to {WINNING_SCORE}", align="center", font=("Courier", 36, "normal"))
                    wn.update()
                    time.sleep(3)
                    game_over = True
                    continue
        
        # Reset hit flags when ball moves away from paddles
        if ball.xcor() > 0 and just_hit_a:
            just_hit_a = False
        if ball.xcor() < 0 and just_hit_b:
            just_hit_b = False
        
        # Limit ball speed
        max_speed = 5
        if abs(ball.dx) > max_speed:
            ball.dx = max_speed if ball.dx > 0 else -max_speed
        if abs(ball.dy) > max_speed:
            ball.dy = max_speed if ball.dy > 0 else -max_speed
        
        # Update the screen
        wn.update()
        
        # Control frame rate for smoother animation
        time.sleep(0.01)
        
except turtle.Terminator:
    print("Game closed")
except Exception as e:
    print(f"An error occurred: {e}")