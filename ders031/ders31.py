# data = []

# with open('students.txt') as f:
#     rf = f.read()
#     data.append(rf)

# print(data)

# --------------------------

# with open('students.txt') as f:
#     lines = f.readlines() # the ouput is always a list.

# print(lines)

# for line in lines:
#     print(line)


# # -------------
# print('erfan\n')
# print('berke',end="")
# print('\tyusuf')
# print('meltem')
# # -------------

# --------------------soru1-----------------------

# DESIRED OUTPUT :
# [[10, 20, 30],[50, 60 70],[90,100,110]]

# \n --> line feed (new line)

# def soru1():
#     result = []
#     with open('soru1.txt') as f:
#         group = []
#         for line in f:
#             # if line is a number
#             if line != '\n':
#                 group.append(int(line.strip('\n')))
#             else:
#                 # if line is feed line
#                 result.append(group)
#                 group = []
#         result.append(group)
#     return result

# print(soru1())

# -------------------------------------

with open('soru1.txt') as f:
    groups = f.read().rstrip().split('\n\n')
    nums = [list(map(int,group.split())) for group in groups]
    print(nums)


