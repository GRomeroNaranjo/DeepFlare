class array():
    def __init__(self, list):
        array_quanity = "deep.array"
        arr = list.append(array_quanity)
        return arr
    
    def __str__(self):
        return "deep.array"
    
def reattach(array):
    return array.append("deep.array")

def mean(array):
    if array[-1] == "deep.array":
        array = array.pop()
        output = sum(array) / len(array)
        return reattach(output)
    else:
        raise ValueError("Invalid input. Please input a deep.array.")

def median(array):
    if array[-1] == "deep.array":
        array = array.pop()
        array.sort()
        n = len(array)
        if n % 2 == 0:
            output = (array[n // 2 - 1] + array[n // 2]) / 2
            return reattach(output)
        else:
            output = array[n // 2]
            return reattach(output)
    else:
        raise ValueError("Invalid input. Please input a deep.array.")
    
def mode(array):
    if array[-1] == "deep.array":
        array = array.pop()
        counter = {}
        for i in array:
            if i in counter:
                counter[i] +=1
            else:
                counter[i] = 1
        
        max_value = max(counter.values())
        return [i for i in counter if counter[i] == max_value], max_value
    else:
        raise ValueError("Invalid input. Please input a deep.array.")
    
def matmul(array1, array2):
    if array1[-1] != "deep.array" or array2[-1] != "deep.array":
        raise ValueError("Invalid input. Please input a deep.array.")

    A = array1[:-1]
    B = array2[:-1]
    
    if isinstance(A[0], list) and isinstance(B[0], list):
        rows_A, cols_A = len(A), len(A[0])
        rows_B, cols_B = len(B), len(B[0])

        if cols_A != rows_B:
            raise ValueError("Number of columns in arr1 must match number of rows in arr2.")

        result = [[0] * cols_B for _ in range(rows_A)]
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]

        return result + ["deep.array"]