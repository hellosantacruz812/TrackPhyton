# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, separator=','):
    participants_1 = set(str_1.split(separator))
    participants_2 = set(str_2.split(separator))
    end_list = (participants_1.intersection(participants_2))
    end_list = sorted(end_list)
    return end_list
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group))
# TODO Провеьте работу функции с разделителем отличным от запятой
