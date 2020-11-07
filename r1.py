def read_file(filename):
    data = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
            for line in f:    
                data.append(line.strip())
    return data

def convert(data):
    new = []
    person = None # 預設person是沒有值的
    for d in data: 
        if d == 'Allen':
            person = 'Allen'
            continue
        elif d == 'Tom':
            person = 'Tom'
            continue

        if person: # 如果person有值，則繼續運行
            new.append(person + ': ' + d)
    return new

def write_file(filename, data):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for d in data:
            f.write(d + '\n')

def main():
    data = read_file('input.txt')
    data = convert(data)
    write_file('output.txt',data)

main()