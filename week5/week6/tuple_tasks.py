def likelihood():
    likelyhoods = (50 , 38 , 27 , 99 , 4)
    return min(likelyhoods)

def run_task1():
    max_value = max(likelihood())
    min_value - min(likelihood())
    print(f"Minimum likelihood of failing: {min_value}%")
    print(f"Maximum likelihood of failing: {max_value}%")

if __name__ == "__main":
    run_task1()

