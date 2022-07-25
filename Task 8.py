# Напишите программу, удаляющую из текста все слова, содержащие "абв"

print(''.join(input().lower().split('абв')))

print(' '.join([i for i in input().lower().split() if 'абв' not in i]))