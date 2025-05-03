# Step 1: Read the integer N
N = int(input("Step1: please set the number of elements (N) you want to include: "))

# Step 2: Read N numbers
numbers = []
for i in range(N):
    number = int(input(f"Step2: Please enter the {i + 1}th number: "))
    numbers.append(number)

# Step 3: Read the integer X
X = int(input("Step3: please enter the integer you are looking for: "))

# Step 4: Check if X is in the list and output the index or -1
if X in numbers:
    index = numbers.index(X) + 1  # Adding 1 to convert from 0-based to 1-based index
    print(index)
else:
    print(-1)
