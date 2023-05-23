# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from collections import Counter
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
print(1)
names = [item['first_name'] for item in students]
cnt = Counter(names)
for name, count in cnt.items():
    print(f'{name}: {count}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
print(2)
names = [item['first_name'] for item in students]
cnt = Counter(names)
most_popular_name = cnt.most_common(1)[0]
most_popular_name = most_popular_name[0]
print(f'most popular name is {most_popular_name}')



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
print(3)
count = 0
for i in range(len(school_students)):
    names = [item['first_name'] for item in school_students[i]]
    cnt = Counter(names)
    most_popular_name = cnt.most_common(1)[0]
    most_popular_name = most_popular_name[0]
    count += 1
    print(f'most popular name in class №{count} is {most_popular_name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for i in school:
    count_girls = 0
    count_boys = 0
    names = [item['first_name'] for item in i['students']]
    for j in names:
        if is_male[j] == True:
            count_boys += 1
        else: count_girls += 1
    number = i['class']
    print(f'class {number}: girls {count_girls}, boy {count_boys}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
max_boys = 0
max_girls = 0
name_max_boys = None
name_max_girls = None
for i in school:
    number = i['class']
    count_girls = 0
    count_boys = 0
    names = [item['first_name'] for item in i['students']]
    for j in names:
        if is_male[j] == True:
            count_boys += 1
        else: count_girls += 1
    if count_boys > max_boys:
        max_boys = count_boys
        name_max_boys = number
    if count_girls > max_girls:
        max_girls = count_girls
        name_max_girls = number

print(f'most girl in class {name_max_girls} - {max_girls}')
print(f'most boys in class {name_max_boys} - {max_boys}')


