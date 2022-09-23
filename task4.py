#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.
path = 'vhod.txt'
data = open(path, 'r')

new_a = ''
for line in data:
    for i in line:
        if (line.count(i) == 1):
            new_a += i
        elif (i not in new_a):
            count = line.count(i)
            new_a += i
            new_a += str(count)
data.close
with open('vihod.txt', 'w') as data_2:
    data_2.write(new_a)
