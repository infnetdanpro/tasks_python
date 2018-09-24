def square(a):
    perim_quad = a * 4
    s_quad = a * a
    diag_quad = a*(2**0.5)

    return_cort = (perim_quad, s_quad, diag_quad)

    return (return_cort)


if __name__ == "__main__":
    calc_quad = int(input())
    print(square(calc_quad))