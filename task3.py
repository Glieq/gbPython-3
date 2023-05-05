# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая
# буква имеет определенную ценность. В случае с английским алфавитом очки распределяются
# так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.

# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь,
# Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу,
# которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*

# ноутбук
# 12
word = input("Введите слово: ")
word = word.upper()
sum = 0
one_point = list('АВЕИНОРСТ')
two_points = list('ДКЛМПУ')
three_points = list('БГЁЬЯ')
four_points = list('ЙЫ')
five_points = list('ЖЗХЦЧ')
eight_points = list('ШЭЮ')
ten_points = list('ФЩЪ')
for letter in word:
    for one_points_letter in one_point:
        if (letter == one_points_letter):
            sum += 1
    for two_points_letter in two_points:
        if (letter == two_points_letter):
            sum += 2
    for three_points_letter in three_points:
        if (letter == three_points_letter):
            sum += 3
    for four_points_letter in four_points:
        if (letter == four_points_letter):
            sum += 4
    for five_points_letter in five_points:
        if (letter == five_points_letter):
            sum += 5
    for eight_points_letter in eight_points:
        if (letter == eight_points_letter):
            sum += 8
    for ten_points_letter in ten_points:
        if (letter == ten_points_letter):
            sum += 10
print(sum)
