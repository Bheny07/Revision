def compare_numbers(A, B):
    if A == B:
        print("The numbers are equal.")
    else:
        print("The higher value is:", max(A, B))


while True:
    numb1 = float(input("Enter the first number "))
    if numb1 == 0:
        break
    numb2 = float(input("Enter the second number "))
    if numb2 == 0:
        break
    compare_numbers(numb1, numb2)
