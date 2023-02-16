def build_pyramid(n, row=0, line=""):
    if row == n:
        return

    if len(line) == 2 * n - 1:
        print(line)
        return build_pyramid(n, row + 1)

    if len(line) >= n - row - 1 and len(line) <= n + row - 1:
        line += "*"
    else:
        line += " "

    build_pyramid(n, row, line)

n = int(input("Enter the height of the pyramid: "))
build_pyramid(n)
