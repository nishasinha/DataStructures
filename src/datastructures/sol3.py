# Python program for the above approach

# Function to find the original array
# from the doubled array
def find_original_array_from_mix(arr):
    if len(arr) % 2 != 0:
        print("length must be even")
        return []

    # Get the numbers and their frequency
    number_frequency = {}
    for i in range(0, len(arr)):
        if arr[i] in number_frequency:
            number_frequency[arr[i]] += 1
        else:
            number_frequency[arr[i]] = 1

    # Sort the array
    arr.sort()
    res = []
    try:
        for i in range(0, len(arr)):
            number = arr[i]
            freq = number_frequency[number]
            # print("On ", number)
            # print("Freq", freq)

            if freq > 0:
                # Element is of original array
                res.append(number)
                number_frequency[number] -= 1
                twice = 2 * number
                number_frequency[twice] -= 1
    except KeyError:
        # Twice Key missed for a number
        return []

    return res


# Driver Code


# Print the result list


# This code is contributed by _Saurabh_Jaiswal
if __name__ == '__main__':
    print("********** Main *************")
    # arr = [4, 1, 2, 2, 2, 4, 8, 4]
    # arr = [1,2,2,3,4,6,7,8,14,16]
    # res = findOriginal(arr)
    print(find_original_array_from_mix([1,3,4,2,6,8]))
    print(find_original_array_from_mix([6,3,0,1]))
    print(find_original_array_from_mix([1]))