import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.main.lab import problem1


def main():
    result = problem1()
    print(result)


if __name__ == "__main__":
    main()
