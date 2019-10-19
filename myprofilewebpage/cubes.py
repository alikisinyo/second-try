# 4. write a program that prints the first 20 numbers and their cubes.
a = 0
b = 0
for i in range(1, 21):
    a = str(i * i)
    b = str(i * i * i)
    print(str(i) + "...", a + "...", b)



