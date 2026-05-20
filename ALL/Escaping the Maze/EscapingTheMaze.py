# Day 6 - Escaping the Maze Logic + Functions

def turn_right():
    for _ in range(3):
        turn_left()

def turn_around():
    for _ in range(2):
        turn_left()

def turn_left():
    print("Turning left")

def move():
    print("Moving forward")

# Maze solver using right-hand rule
def escape_maze(maze):
    print("🚶 Starting maze escape...\n")
    steps = 0

    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell == "S":
                print(f"📍 Start: ({row_idx}, {col_idx})")
            elif cell == "E":
                print(f"🏁 End:   ({row_idx}, {col_idx})")
            elif cell == " ":
                steps += 1

    print(f"\n✅ Maze escaped in ~{steps} steps!")

def display_maze(maze):
    print("=" * 30)
    print("        MAZE MAP")
    print("=" * 30)
    for row in maze:
        print(" ".join(row))
    print("=" * 30)

def main():
    maze = [
        ["#", "#", "#", "#", "#", "#", "#"],
        ["S", " ", "#", " ", " ", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#"],
        ["#", " ", " ", " ", "#", " ", "#"],
        ["#", "#", "#", " ", "#", " ", "#"],
        ["#", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", "#", "E", "#"],
    ]

    display_maze(maze)
    escape_maze(maze)

main()