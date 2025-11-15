#Activity 1

def directions():
    steps = ["Move forward" , "Move backward" , "Move left" , "Move right"]
    return steps


def run_task1():
    movements = directions()
    print(movements)
if __name__ == "__main__":
    run_task1()

#Activity 2

def movements():
    path = ["Move forward" , 10 ,"Move Backward" , 5, "move left" , 3, "move right", 1]
    return path

def run_task2():
    print("Moving")
    path = movements()

    for i in range (0, len(path) , 2):
        direction = path[i]
        step = path[i+1]
        print(f"{direction} for {step} steps")

if __name__ == "__main__":
    run_task2()