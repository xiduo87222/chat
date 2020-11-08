data = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        data.append(line.strip())

for d in data:
    s = d.split(' ')
    time = s[0][:5] # 取s[0]的前五個字串
    name = s[0][5:]
    print('時間', time, '人名', name)

