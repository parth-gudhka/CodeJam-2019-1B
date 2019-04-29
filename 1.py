from numpy import zeros


def main():
    t = int(input())
    for i in range(1, t + 1):
        # for i in range(2):
        test_case = input()
        p, q = map(int, test_case.split())
        # people = []
        people = []
        for j in range(p):
            case = input().split()
            people.append(
                {
                    "x": int(case[0]),
                    "y": int(case[1]),
                    "dir": case[2]
                }
            )
        matrix = zeros([q + 1, q + 1])
        for person in people:
            if person["dir"] == "W":
                for c in range(person["x"]):
                    for d in range(q + 1):
                        matrix[c][d] += 1
            elif person["dir"] == "E":
                for c in range(person["x"] + 1, q + 1):
                    for d in range(q + 1):
                        matrix[c][d] += 1
            elif person["dir"] == "N":
                for c in range(q + 1):
                    for d in range(person["y"] + 1, q + 1):
                        matrix[c][d] += 1
            elif person["dir"] == "S":
                for c in range(q + 1):
                    for d in range(person["y"]):
                        matrix[c][d] += 1
        max = 0
        x = 0
        y = 0
        for c in range(q + 1):
            for d in range(q + 1):
                if (matrix[c][d] > max):
                    x = c
                    y = d
                    max = matrix[c][d]
        # print(max, x, y)
        print(matrix)
        print("Case #" + str(i) + ": " + str(x) + " " + str(y))
        # print(people)
        # print(p, q)


if __name__ == '__main__':
    main()
