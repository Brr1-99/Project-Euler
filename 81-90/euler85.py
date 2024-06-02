"""
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""

def count_rectangles(height: int, width: int) -> int:
    total_count = ((height + 1)* height/2) *((width + 1)* width/2)
    return total_count


print(count_rectangles(63, 44))