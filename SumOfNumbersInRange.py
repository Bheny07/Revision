# Define the range
start = 20
end = 25

# Initialize sum
sum_of_integers = 0

# Output integers and calculate sum
print("Integers from", start, "to", end, "inclusive:")
for i in range(start, end + 1):
    print(i)
    sum_of_integers += i

# Output the sum
print("Sum of the integers from", start, "to", end, "inclusive:",
      sum_of_integers)
