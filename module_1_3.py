# from pprint import pprint, pp
#
# name = 'Elena'
# print('Name: ' + name)
# age = 44
# print('Age:', age)
# age = age + 2
# print('New Age:', age)
# is_student = True
# print('Is Student:', is_student)
#
#
# homework_count = 12
# hours_spent_count = 1.5
# course_title = 'Python'
# time_for_one_task = hours_spent_count / homework_count
# print('Курс:', course_title + ',', 'всего задач:', str(homework_count) + ',', 'затрачено часов:', str(hours_spent_count)
#       + ',', 'среднее время выполнения', time_for_one_task, 'часа.')
#
# example = 'homework'
# print(example[0])
# print(example[-1])
# print(example[len(example) // 2 :])
# print(example[::-1])
# print(example[1::2])


date_task = {}
for i in range (1, 4) :
    date = input ('Введите дату: ')
    task = input ('Введите задачу: ')
    date_task[date] = task
for key in date_task :
    print(key + ' ' + date_task[key])
