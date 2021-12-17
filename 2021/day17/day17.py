target = {"x": (185, 221), "y": (-122, -74)}
t_target = {"x": (20, 30), "y": (-10, -5)}


def in_target(x, y, target):
    """Check if inside target"""
    return (
        x >= target["x"][0]
        and x <= target["x"][1]
        and y >= target["y"][0]
        and y <= target["y"][1]
    )


def out_of_bounds(x, y, target):
    """Check if passed target"""
    return x > target["x"][1] or y < target["y"][0]


def throw(v0_x, v0_y, target):
    """Simulate the throw"""
    x, y = 0, 0
    vx, vy = v0_x, v0_y
    ys = []
    while not in_target(x, y, target):
        x += vx
        y += vy
        ys.append(y)
        if vx != 0:
            vx -= 1
        vy -= 1
        if out_of_bounds(x, y, target):
            return None
    return max(ys)


def solve(target):
    """Try for a bunch of init velocities"""
    ys = []
    for v0_x in range(0, target["x"][1] + 1):
        # Randomly choose 130 :P
        for v0_y in range(target["y"][0], 130):
            y = throw(v0_x, v0_y, target)
            if y is not None:
                ys.append(y)
    return ys


# PART 1
def part1(target):
    ys = solve(target)
    return max(ys)


assert part1(t_target) == 45
print(part1(target))


# PART 2
def part2(target):
    ys = solve(target)
    return len(ys)


assert part2(t_target) == 112
print(part2(target))
