def gcd(a, b):
    """a,bの最大公約数をユークリッドの互除法で解く"""
    if b == 0: return a
    return gcd(b, a%b)


def solve():
    p1 = (1, 11)
    p2 = (5, 3)

    diff_x = abs(p1[0]-p2[0])
    diff_y = abs(p1[1]-p2[1])

    ans = gcd(max(diff_x, diff_y), min(diff_x, diff_y))-1

    print(ans)


if __name__ == "__main__":
    solve()