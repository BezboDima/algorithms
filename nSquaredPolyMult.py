# GROUP: Ryan Kardoes, Dmitry Bezborodov
# Basic O^2 implementation of multiplication
def poly_mult(coA: list, coB: list):
    ans = [0] * (len(coA) + len(coB) - 1)
    for x, a in enumerate(coA):
        for y, b in enumerate(coB):
            ans[x+y] += (a*b)
    return ans

A = [7,2,3]
B = [4,-1,2]

print(poly_mult(A, B))