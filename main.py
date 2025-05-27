import itertools
import argparse

def knapsack(path):
    try:
        with open(path) as f:
            line = f.readline().strip().split(' ')
            capacity = int(line[0])
            n = int(line[1])

            values = [int(a) for a in f.readline().strip().split(',')]
            weights = [int(a) for a in f.readline().strip().split(',')]
    except Exception as e:
        print(e)
        raise


    if not n > 0:
        raise ValueError("invalid n")
    if n != len(values) or n != len(weights):
        raise ValueError("invalid n")


    max_value = 0
    max_items = [0] * n
    iterations = 0

    for iterations, current_items in enumerate(itertools.product([0, 1], repeat=n)):
        current_value = 0
        current_weight = 0

        for i, bit in enumerate(current_items):
            if bit == 1:
                current_value += values[i]
                current_weight += weights[i]
            if current_weight > capacity:
                break

        if current_weight > capacity:
            if iterations % 1_000_000 == 0:
                print(f"{iterations=}")
                print()
            continue

        if current_value > max_value:
            max_value = current_value
            max_items = current_items
            print(f"{iterations=}")
            print(f"{max_value=}")
            print(f"{max_items=}")
            print()
        elif iterations % 1_000_000 == 0:
            print(f"{iterations=}")
            print()

    print(f"{iterations=}")
    print(f"{max_value=}")
    print(f"{max_items=}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-input", required=True, type=str, help="Input file path")

    arg = parser.parse_args()
    knapsack(arg.input)

if __name__ == '__main__':
    main()






