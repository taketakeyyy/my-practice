
if __name__ == "__main__":
    n = int(input())
    r0 = int(input())
    r1 = int(input())
    minv = r0 if r0 <= r1 else r1
    maxv = r1 - r0
    for i in range(2, n):
        r = int(input())
        maxv = max(maxv, (r-minv))
        minv = min(minv, r)
    print(maxv)
