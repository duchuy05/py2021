# f = open('demo.txt', 'r')
# content = f.readline(29)
# print(content)

# f.close()

courses = [
    ("Javascript", 200),
    ("Python", 290),
    ("C++", 210),
]

courses.append(("Django", 400))
print(courses)
filtered = list(map(lambda item: item[1], courses))
print(filtered)

print("He said \"this is not a good software\", please access D:\\LionKing")

def myFunction(a, b):
    print('Value', a + b)


myFunction(190, 130)

list = [[1,2,4,3], [14,24], [23, 24, 53]]
print(list[1][1])

itera = [1, 2, 3, 3]
print(sum(itera, 12))
