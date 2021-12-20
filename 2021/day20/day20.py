import numpy as np


def read_data(filename):
    with open(filename, "r") as f:
        algo, img = f.read().strip().replace(".", "0").replace("#", "1").split("\n\n")

    algo = algo.replace("\n", "")
    img = np.asarray([list(row) for row in img.split("\n")])
    return algo, img


t_algo, t_img = read_data("test_input.txt")
algo, img = read_data("input.txt")


def padd(img, fill):
    return np.pad(img, 2, constant_values=fill)


def enhance(img, algo, fill):
    img = padd(img, fill)
    n, m = img.shape
    new = np.full((n, m), fill)
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            pool = img[i - 1 : i + 2, j - 1 : j + 2].flatten()
            idx = int("".join(pool), 2)
            new[i, j] = algo[idx]

    return new[1 : n - 1, 1 : m - 1]


def solve(img, algo, steps):
    for i in range(steps):
        if algo[0] == "0":
            fill = "0"
        else:
            fill = "0" if i % 2 == 0 else "1"
        img = enhance(img, algo, fill)
    return np.sum(img == "1")


assert solve(t_img, t_algo, 2) == 35
print(solve(img, algo, 2))

assert solve(t_img, t_algo, 50) == 3351
print(solve(img, algo, 50))
