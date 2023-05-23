# Вывести последнюю букву в слове
print('1 задание')

word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
print('2 задание')

from collections import Counter
word = 'Архангельск'
word = word.lower()
count = Counter(word)
print(count['а'])

# Вывести количество гласных букв в слове
print('3 задание')

word = 'Архангельск'
word = word.lower()
vowel = ['а','о','у','ы','и','е','ю','я','ё','э']
count = 0
for i in word:
    if i in vowel:
        count += 1
print(count)


# Вывести количество слов в предложении
print('4 задание')

sentence = 'Мы приехали в гости'
sentence_list = sentence.split()
print(len(sentence_list))


# Вывести первую букву каждого слова на отдельной строке
print('5 задание')

sentence = 'Мы приехали в гости'
sentence_list = sentence.split()
for word in sentence_list:
    print(word[0])


# Вывести усреднённую длину слова в предложении
print('6 задание')

sentence = 'Мы приехали в гости'
count = 0
sentence_list = sentence.split()
for word in sentence_list:
    count += len(word)
middle = count / len(sentence_list)
print(middle)