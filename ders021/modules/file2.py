from file1 import multi_10

def add_ten(num):
    return num + 10

# main : file2
# Eger burasi ana akis ise


print("file2.py: ",__name__)

if __name__ == "__main__":
    print(add_ten(3))
    print(multi_10(5))