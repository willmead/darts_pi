import random


def calculate_pi(num_darts):
    darts_in_circle = 0.0
    darts_total = 0.0

    for i in range(num_darts):
        darts_total += 1

        x = random.random() * 2 - 1
        y = random.random() * 2 - 1

        if x ** 2 + y ** 2 < 1:
            darts_in_circle += 1

    print(f"{darts_in_circle} / {darts_total} x 4 = {4 * darts_in_circle/darts_total}")


calculate_pi(100_000_000)
