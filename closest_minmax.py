def smallest_subarray_size(A):
    max_val = A[0]
    min_val = A[0]
    min_max_indices = []

    for i in range(len(A)):
        if A[i] > max_val:
            max_val = A[i]
        if A[i] < min_val:
            min_val = A[i]

    for i in range(len(A)):
        if A[i] == max_val or A[i] == min_val:
            min_max_indices.append(i)

    return min_max_indices[-1] - min_max_indices[0] + 1


A = []
input_str = input("Enter the elements of array A : ")
input_list = input_str.split()
for i in range(len(input_list)):
    A.append(int(input_list[i]))

output = smallest_subarray_size(A)
print(output)

