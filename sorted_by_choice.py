# sorted by choice
USER_ID = [1220, 222, 883, 2, 64, 21, 43, 1, 45, 66, 8787, 42, 453]

def sorted_by_choice(check_list: list, reversed: bool = False) -> list:
    new_list = list()

    for i in range(len(check_list)):
        new_list.append(
            check_list.pop(
                check_list.index(
                    max(check_list) if reversed else min(check_list)
                )
            )
        )
    
    return new_list


NEW_SORTED_USER_ID = sorted_by_choice(USER_ID)
print(NEW_SORTED_USER_ID)
