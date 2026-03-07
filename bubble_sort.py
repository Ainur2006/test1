def bubble_sort(incoming_list: list = []) -> list:
    if not incoming_list:
        return None
    swap = True
    count_step = len(incoming_list) - 1
    while swap:
        swap = False
        for i in range(count_step):
            if incoming_list[i] > incoming_list[i + 1]:
                incoming_list[i], incoming_list[i + 1] = (
                    incoming_list[i + 1],
                    incoming_list[i],
                )  # меняем местами пары чисел, большее становится правее
                swap = True  # если произошла замена, то меняем значение "swap"
        count_step -= 1  # уменьшаем счётчик, т.к. большее число в конце списка
    return incoming_list


list = [
    2,
    5,
    2,
    8,
    76,
    4,
    6,
]

print(bubble_sort(list))
print()
