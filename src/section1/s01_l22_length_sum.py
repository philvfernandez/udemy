grades = [80, 75, 90, 100]

total = sum(grades)
length = len(grades)

average = total / length
print(average)

## List of grades (best choice for grades because a list has the most flexibility and allows duplicates.
grades1 = [80, 75, 90, 100]

## Tuple of grades (Good if you don't have to add new items.)
grades2 = (80, 75, 90, 100)

## Set of grades (worst choice with respect to grades because you can't have any duplicates (same grade).
## Only use sets if you need to compare sets together.
grades3 = {80, 75, 90, 100}