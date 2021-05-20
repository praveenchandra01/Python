def countTriplets(arr, n, m):
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (arr[i] * arr[j] * arr[k] == m):
                    count += 1
                    print(arr[i],arr[j],arr[k])
    return count


arr = [1, 4, 6, 2, 3, 8]
m = 24
print(countTriplets(arr, len(arr), m))
