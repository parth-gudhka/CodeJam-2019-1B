#!/bin/sh
import sys


def solve(a, b):
    w = 0
    ready = False
    print(1)
    sys.stdout.flush()
    s = int(input())
    print(s)

    # def loop(day):
    #     print(day)
    #     sys.stdout.flush()
    #     s = int(input())
    #     print(s)
    #     if (s == -1):
    #         solve()
    #     else:
    #         return
    #
    # loop(w + 1)


def main():
    T, W = map(int, input().split())
    print(T, W)
    for _ in range(1, T + 1):
        solve()


if __name__ == '__main__':
    main()
