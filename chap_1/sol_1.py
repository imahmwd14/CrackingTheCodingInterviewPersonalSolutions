string = "afhgsdfnbgsmdfg"


def unique(string):
    arr = [0] * (ord('z') - ord('a'))

    for c in string:
        i = ord(c) - ord('a')

        if arr[i] == 1:
            return False

        arr[i] = 1

    return True


if __name__ == '__main__':
    print(unique(string))
    print(unique('a'))
    pass
