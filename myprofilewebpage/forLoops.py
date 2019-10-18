# a forLoop loops over a given range
# the i below represents each individual member of that group(range)
# in range the last value is excluded
for i in range(0, 100):
    print(i)

for e in range(5, 10):
    print(e)

# for a range the introduction of a third value in a range block introduces a skip reference
for e in range(5, 10, 3):
    print(e)
# in the example above it will skip 3 values

house = {"utensils": ["spoon", "knife", "plate", "fork"],
         "clothes": ["bedding", "jackets", "umbrella"]
         }
for i in house:
    print(i)
# this prints the keys stored in the dictionaries
    for i in house:
        print(house[i])
# this prints the key values

students = ["ali", "juma", "kassim", "andrew", "eugene"]
for s in students:
    s += " kamau"
    print(s)

total = 0
subject = [23, 45, 67 , 89 , 56]
for x in subject:
    total += x
print(total)

# questions
# 1. write a program that prints you name 100 times using a WHILE AND LOOP
# 2. write a program that outputs 100 lines numberes 1 to 100 and has you name in it
# 3. write a program that uses a for loop to print the numbers 8,11,14,17,20......86,89
# 4. write a program that prints the first 20 numbers and their cubes.
# example of 4
#   1...1...1
#   2...4...8
#   3...9...27
# -->20...400...8000
# ---------------------->use both a for loop and while loop <--------------------------
