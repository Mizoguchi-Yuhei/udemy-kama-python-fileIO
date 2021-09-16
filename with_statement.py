# try:
#     f = open("pep8_introduction.txt")
#     for line in f:
#         print(line, end="")
# finally:
#     f.close()

# print("hello\n")
# print("world\n")
#
# print("hello", end="")
# print("world", end="")

# with statement
with open("pep8_introduction.txt") as f:
    for line in f:
        print(line, end="")
