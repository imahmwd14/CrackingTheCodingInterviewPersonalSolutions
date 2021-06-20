def count_chars(string):
    arr = [0] * (ord('z') - ord('a'))
    for c in string:
        i = ord(c) - ord('a')
        arr[i] = arr[i] + 1
    return arr


def are_identical(arr0, arr1):
    """
    assuming they have the same size
    """
    for n in range(len(arr0)):
        if arr0[n] != arr1[n]:
            return False
    return True


def are_permutations(string0, string1):
    if len(string0) != len(string1):
        return False
    else:
        return are_identical(
            count_chars(string0),
            count_chars(string1)
        )


if __name__ == '__main__':
    print(are_permutations("aba", "baa"))
    print(are_permutations("aba", "bba"))
