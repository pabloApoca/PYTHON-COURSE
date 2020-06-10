demo_list = [1 , "hello" , 1.34 , True, [1,2,3]]
colors= ["red", "blue", "green"]

# numbers_list = list((1,2,3,4))
# print(numbers_list)
# print(type(numbers_list))

# r = list(range(1,11))
# print(r)

# print(type(colors))
# print(len(colors))
# print(colors[2])

# print("green" in colors)

# print(colors)
# colors[1]="yellow"
# print(colors)

# # # print(dir(colors))
# # colors.append(("violet", "yellow"))
# # print(colors)

# colors.extend(["violet", "yellow"])
# print(colors)

# colors.extend(["black", "pink"])

#colors.insert(1, "violet")
colors.insert(len(colors), "violet")
print(colors)

# colors.pop()
#colors.pop(1)
# colors.remove("green")
#colors.clear()
#colors.sort(reverse=True)
print(colors.index("red"))

print(colors)

print(colors.count("red"))

