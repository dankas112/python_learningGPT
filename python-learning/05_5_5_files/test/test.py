with open(r'C:\Users\danii\Desktop\мое\programming\python\study\python-learning\05_5_5_files\test\test.txt', 'w', encoding='utf-8') as f:
    f.write('Hello world!!!')
    f.write('\nI becoming human')
    f.write('\nBut feel self not good')

with open(r'C:\Users\danii\Desktop\мое\programming\python\study\python-learning\05_5_5_files\test\test.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    print(f'Количество строк - {len(lines)}')

with open(r'C:\Users\danii\Desktop\мое\programming\python\study\python-learning\05_5_5_files\test\test.txt', 'a', encoding='utf-8') as f:
    f.write('\nAnd.. This is a nes line!')