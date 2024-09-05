from typing import List

# GROUP: Ryan Kardoes, Dmitry Bezborodov
# Function is responsible for adding and subtraction polynomials
def add_poly(coef_a: List[float], coef_b: List[float], negative=False):
    ans = []
    ac = coef_a.copy()
    bc = coef_b.copy()

    # if polynomials are not the same size we are adding 0 coeficients to lower degree polynomioals
    while(len(ac) != len(bc)):
        if(len(ac) > len(bc)):
            bc.append(0)
        if(len(ac) < len(bc)):
            ac.append(0)

    if negative:
        for a, b in zip(ac, bc):
            ans.append(a-b)
    else:
        for a, b in zip(ac, bc):
            ans.append(a+b)
    return ans

# Function responsible for multiplication of polynomial by degree
def exp_multy(coef: List[float], exp: int):
    #shifts elements of polynomial by exp
    ans = [0] * (exp + len(coef))
    for i in range(len(coef)):
        ans[i + exp] = coef[i]
    return ans

# Recursive function to multiply polynomials 
# Polynomials represented as an array where element is a coefficient and index is a degree
def poly_multy(coef_a: List[float], coef_b: List[float]):

    # base case
    n = len(coef_a)
    if(n == 1):
        return [coef_a[0] * coef_b[0]]
    
    # break down ploynomials to a1 and a0, b1, and b0
    coef_a1 = coef_a[(n)//2:]
    coef_a0 = coef_a[:(n)//2]

    coef_b1 = coef_b[(n)//2:]
    coef_b0 = coef_b[:(n)//2]


    # A1(x) * B1(x)
    coef_a1_multy_coef_b1 = poly_multy(coef_a1, coef_b1)

    # A1(x) + A0(x)
    coef_a1_a0 = add_poly(coef_a1, coef_a0)

    # B1(x) + B0(x)
    coef_b1_b0 = add_poly(coef_b1, coef_b0)

    # (A1(x) + A0(x)) * (B1(x) + B0(x))
    coef_a1_a0_multy_coef_b1_b0 = poly_multy(coef_a1_a0, coef_b1_b0)

    # A0(x) * B0(x)
    coef_a0_multy_coef_b0 = poly_multy(coef_a0, coef_b0)

    # (A1(x) + A0(x)) * (B1(x) + B0(x)) - # A1(x) * B1(x) - # A0(x) * B0(x))
    subtraction = add_poly(coef_a1_a0_multy_coef_b1_b0, coef_a1_multy_coef_b1, negative=True)
    subtraction = add_poly(subtraction, coef_a0_multy_coef_b0, negative=True)

    # x^n(A1(x) * B1(x))
    if(n % 2 != 0): n -= 1
    first = exp_multy(coef_a1_multy_coef_b1, n)

    # x^n//2(A1(x) + A0(x)) * (B1(x) + B0(x)) - # A1(x) * B1(x) - # A0(x) * B0(x))
    second = exp_multy(subtraction, n//2)

    # A0(x) * B0(x)
    third = coef_a0_multy_coef_b0

    # Add 3 parts together
    ans = add_poly(add_poly(first, second), third)

    return ans


A = [3,45,7,-1]
B = [5,8,0,-4]
print("Polynomials are in reverse representattion")
print("First Poly: ", A)
print("Second Poly: ", B)

print("Answer: ", poly_multy(A,B))
