def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"

    if a == b and b == c:
        triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    is_right = False

    if a * a + b * b == c * c:
        is_right = True
    if a * a + c * c == b * b:
        is_right = True
    if b * b + c * c == a * a:
        is_right = True

    if is_right:
        return triangle_type + " and Right"

    return triangle_type


if __name__ == "__main__":
    print("3, 3, 3:", classify_triangle(3, 3, 3))
    print("5, 5, 8:", classify_triangle(5, 5, 8))
    print("4, 5, 6:", classify_triangle(4, 5, 6))
    print("3, 4, 5:", classify_triangle(3, 4, 5))
    print("1, 2, 3:", classify_triangle(1, 2, 3))
