# file = open("students.txt")
# print(file)

# print(file.read(11))
# print('----------')
# file.seek(0) # imleci sifirlamak icin kullanilir.
# print('----------')
# print(file.read())
# file.seek(0)
# print('----------')
# print(file.readline())
# print(file.readline())

# file.close()

# ------------------------------

# names = []

# with open('students.txt') as f:
#     while True:
#         line = f.readline()
#         print(f'{line=}')

#         # boslugu gordu zaman durdur
#         if line == '':
#             break
#         # satır sonundaki \n karakterini temizle
#         names.append(line.rstrip())

# print(names)

# ------------------------------

# names = []
# with open('students.txt') as f:
#     for line in f:
#         names.append(line.strip())

# print(names)
# ------------------------------
# # expected output:
# # berkenin puani 90
# # meltemin puani 80
# # ...

# with open('students_scores.txt') as f:
#     for line in f:
#         # item = line.strip().split('-')
#         # print(item[0],item[1])
#         name,score = line.strip().split('-')
#         print(f'{name}in puani {score}')

# ------------------------------
# from statistics import mean
# def find_avg_score():
#     with open('students_scores.txt') as f:
#         scores = []
#         for line in f:
#             name,score = line.strip().split('-')
#             scores.append(float(score))
#         return mean(scores)
# print(find_avg_score())


def find_avg_score1():
    with open('students_scores.txt') as f:
        total_score = 0
        count = 0
        for line in f:
            item = line.strip().split('-')
            total_score += float(item[1])
            count += 1
        return total_score/count
print(find_avg_score1())