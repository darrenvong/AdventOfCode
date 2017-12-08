import numpy as np

def get_first_value_larger_than_input(num_input=277678):
    spiral_grid = np.zeros((2000, 2000), np.int64)


def get_next_square_coordinate(step_limit=3):
    """Pattern seems to be that it goes x number of steps right/up, then
    x + 1 steps left/down, then x + 2 steps right up and so on."""
    curX, curY = (0, 0)
    step = 1
    direction = 1 # 1 for right/up, -1 for left/down
    yield (curX, curY) # first square
    while step <= step_limit:
        for _ in range(step):
            curX += direction
            yield (curX, curY)

        for _ in range(step):
            curY += direction
            yield (curX, curY)

        step += 1
        direction *= -1


if __name__ == '__main__':
    for coord in get_next_square_coordinate():
        print(coord)
