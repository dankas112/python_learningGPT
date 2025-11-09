def sum_list(user_list):
    if len(user_list) == 1:
        return user_list[0]
    elif len(user_list) < 1:
        return 0
    else:
        return user_list[0] + sum_list(user_list[1:])

nums = [10, 20, 30, 40, 50]
print("Сумма:", sum_list(nums))