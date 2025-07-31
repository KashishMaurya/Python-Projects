# file = open("file.txt")
# contents = file.read()
# print(contents)
# file.close()

# read only
# with open("file.txt") as file:
#     contents = file.read()
#     print(contents)


# write / append
for i in range(10):
    with open("file.txt", "a") as file:
        file.write("\nhello!!")