# binary_search
# O(log2 n)
USER_ID = [range(1, 1001)]


def binary_search(check_list: list, item: int | float) -> int:
    low = 0
    high = len(check_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = check_list[mid]

        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1


if __name__ == '__main__':
    INDEX_USER_49 = binary_search(USER_ID, 49)
    print(INDEX_USER_49)
