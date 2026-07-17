# while True:
#     try:
#         user_input = input("Enter Your Age (type exit to quit.): ")
#         if user_input.lower() == 'exit':  # exIT,exIt, Exit
#             print('Your quit the program')
#             break

#         age = int(user_input) # kritik noktamiz
#         if age >= 18 and age <= 90:
#             print("Age Set Successfully")
#             break
#         else:
#             print('age must be between 18 and 90')
#     except:
#         print('Please Enter Valid Number')


# ----------------- 

# while True:
#     try:
#         user_input = input("Enter Your Age (type exit to quit.): ")
#         if user_input.lower() == 'exit':  # exIT,exIt, Exit
#             print('Your quit the program')
#             break

#         age = int(user_input) # berke
#         if age < 18 or age > 90: # 100
#             raise ValueError('Age Must Be Between 18 and 90')
#         else:
#             print("Age Set Successfully")
#             break
        
#     except ValueError as ve:
#         print(ve)
#     except ZeroDivisionError as zde:
#         print(zde)

# ----------------- 

# # when one of the except blocks run the others won't run

# while True:
#     try:
#         user_input = input("What is your age? (type 'exit' to quit): ")
#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break
#         age = int(user_input)
#         print(age)
#         10 / age
#     except ValueError:
#         print("please enter a number")
#     except ValueError:
#         print("I will never see here")
#     except ZeroDivisionError:
#         print("please enter value higher than zero! ")
#     else:
#         print("thank you! ")
#         break


# -------- bundle --------- 

# def division(num1:int,num2:int):
#     try:
#         return num1/num2
#     except (TypeError,ValueError,ZeroDivisionError) as e:
#         return f"Oops. error: {e}"

# print(division('1',2))
# print(division(1,0))


# --------------------------


# while True:
#     try:
#         age = int(input("what's your age? "))
#         10/age
#     except ValueError:
#         print("please enter a number")
#         continue
#     except ZeroDivisionError:
#         print("please enter age higher than 0")
#         break
#     else:
#         print("thank you")
#         break
#     finally:
#         print("ok im finally done.")
#     print("can you here me")
#     break


# --------------------------
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

while True:
    try:
        print("Type 1 to select .txt")
        print("Type 2 to select .csv")
        file_type = input("please enter your file type: ") # .txt
        
        file_name = input("please enter your file name: ") # names
        if file_type == '1':
            file_type = '.txt' # ✅
        elif file_type == '2':
            file_type = '.csv'
        else:
            raise ValueError("You should select 1 or 2")
        file_name += file_type # names + .txt = "names.txt"
        full_path = BASE_DIR / file_name
        with open(full_path) as f:
            for line in f:
                print(line)
        break
    except FileNotFoundError as fnfe:
        print(fnfe)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f'Opps unkown error: {e}')