def sum_list(user_list):
    if len(user_list) == 0:
        return 0
    else:
        return user_list[0] + sum_list(user_list[1:])


nums = [1, 2, 3, 4, 5]
print("Сумма:", sum_list(nums))

