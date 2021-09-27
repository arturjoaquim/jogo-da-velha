from itertools import chain, combinations


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


points_field = [2, 7, 6, 9, 5, 1, 4, 3, 8]

value_fields = [
    "Circles",
    "Squares",
    "Circles",
    "Circles",
    "Circles",
    "Squares",
    "Squares",
    "Squares",
    "Circles"
]

circles_points = []
squares_points = []

for i in range(9):
    if value_fields[i] == "Circles":
        circles_points.append(points_field[i])
    elif value_fields[i] == "Squares":
        squares_points.append(points_field[i])
    else:
        pass


def checkValues(iterator):
    combination_list = list(iterator)
    combination_list = [combination for combination in combination_list if len(combination) == 3]

    return [combination for combination in combination_list if sum(combination) == 15]

    #for combination in combination_list:
        # print(sum(combination))
     #   if sum(combination) == 15:
      #      return True


combination_list_circles = powerset(circles_points)
combinations_list_squares = powerset(squares_points)

print(checkValues(combination_list_circles))
print(checkValues(combinations_list_squares))
