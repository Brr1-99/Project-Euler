"""
Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
"""

with open("61-70/triangle.txt") as file:
    arr = []
    for line in file:
        arr.append(list(map(int, line.split(" "))))

for row in range(len(arr)-2, -1, -1):
  for col in range(len(arr[row])):
    arr[row][col] += max(arr[row+1][col], arr[row+1][col+1])

print(f'The maximum value of the triangle is : {arr[0][0]}')