def main():
    t = int(input())
    for i in range(1, t + 1):
    # for i in range(2):
        test_case = input()
        n, k = map(int, test_case.split())
        # print(k)
        c = list(map(int, input().split()))
        d = list(map(int, input().split()))

        num = 0

        # Find num here
        for p in range(n):
            for q in range(p, n):
                c_max = max(c[p:q+1])
                d_max = max(d[p:q+1])
                # print(c_max, d_max)
                if (abs(c_max - d_max) <= k):
                    # print(p, q, c_max, d_max)
                    num += 1

        #
        # num = i
        print("Case #" + str(i) + ": " + str(num))


if __name__ == '__main__':
    main()
