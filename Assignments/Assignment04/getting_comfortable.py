# Sets and List comprehensions
print([abs(x) for x in range(-2, 10) if x % 2 == 0])

set_example_one = set()
set_example_one.add(1)
set_example_one.add(21)

set_example_two = set()
set_example_two.add((1,0))

for element in set_example_one:
    print(element)
print("length of set_example_one: " + str(len(set_example_one)))
for i in range(len(set_example_two)):
    temp_val = set_example_two.pop()
    print(temp_val)
print("length of set_example_two: " + str(len(set_example_two)))
