with open(f'26.txt') as file:
    s, n = map(int, file.readline().split(' '))
    a = []
    for i in range(n):
        a.append(int(file.readline()))
        
counter = 0
maxx = 0



print(counter, maxx)