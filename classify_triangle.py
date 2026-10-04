"""Classify triangles by their side lengths."""


def classify_triangle(side_a, side_b, side_c):
    """Return the type of triangle for three side lengths."""
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return "Invalid input"

    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        return "Not a triangle"

    if side_a == side_b and side_b == side_c:
        triangle_type = "Equilateral"
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    is_right = False

    if side_a * side_a + side_b * side_b == side_c * side_c:
        is_right = True
    if side_a * side_a + side_c * side_c == side_b * side_b:
        is_right = True
    if side_b * side_b + side_c * side_c == side_a * side_a:
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
