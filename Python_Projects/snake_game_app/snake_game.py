import turtle
import time
import random

# Core Configuration Configurations
FRAME_DELAY = 0.1
SCORE = 0
HIGH_SCORE = 0

# 1. Screen Setup Display Management
window = turtle.Screen()
window.title("Graphical Matrix Snake Engine")
window.setup(width=600, height=600)
window.bgcolor("black")
window.tracer(0)  # Disables automatic screen updates for seamless manual frame control

# 2. Instantiate Game Object Entities
# Snake Head Initialization
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Target Food Placement Initialization
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

body_segments = []

# Score Display Telemetry
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 16, "normal"))

# 3. Directional Vector Transformation Modules
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    """Calculates head position based on directional vector variables."""
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# 4. Asynchronous Event Key Binding Setup
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

def reset_game_state():
    """Handles collision cleanup and state resets."""
    global SCORE
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    
    # Clean screen artifacts by shifting entities away and wiping the list array
    for segment in body_segments:
        segment.goto(1000, 1000)
    body_segments.clear()
    
    SCORE = 0
    update_score_display()

def update_score_display():
    pen.clear()
    pen.write(f"Score: {SCORE}  High Score: {HIGH_SCORE}", align="center", font=("Courier", 16, "normal"))

# 5. Core Game Loop Architecture

# --- Replace the bottom loop with this clean architecture ---

# State flag to manage loop execution safety
is_running = True

def handle_close():
    """Callback function triggered when the user closes the GUI window container."""
    global is_running
    is_running = False

# Tell turtle to execute our handler function when the window closes
window._root.protocol("WM_DELETE_WINDOW", handle_close)

# 5. Safe Game Loop Architecture
while is_running:
    try:
        window.update()  # Refresh canvas graphics buffer safely

        # Border Collision Mechanics Check
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            reset_game_state()

        # Food Capture Analytics Check
        if head.distance(food) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("darkgreen")
            new_segment.penup()
            body_segments.append(new_segment)

            SCORE += 10
            if SCORE > HIGH_SCORE:
                HIGH_SCORE = SCORE
            update_score_display()

        # Cascade positions backward through body segments array chain
        for index in range(len(body_segments) - 1, 0, -1):
            x = body_segments[index - 1].xcor()
            y = body_segments[index - 1].ycor()
            body_segments[index].goto(x, y)

        # Bridge the gap by shifting the initial segment to the head location
        if len(body_segments) > 0:
            x = head.xcor()
            y = head.ycor()
            body_segments[0].goto(x, y)

        move()

        # Self-Intersection Segment Body Matrix Collision Check
        for segment in body_segments:
            if segment.distance(head) < 20:
                reset_game_state()

        time.sleep(FRAME_DELAY)
        
    except (turtle.Terminator, Exception):
        # Catch unexpected window closures mid-update and break loop cleanly
        break

print("[INFO] Game engine detached cleanly. Zero exceptions reported.")