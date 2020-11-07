def read_file(filename):
    data = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
            for line in f:    
                data.append(line.strip())
    return data


def convert(data):
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for d in data: 
        s = d.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for msg in s[2:]:
                    allen_word_count += len(msg)
        elif name =='Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:               
                for msg in s[2:]:
                    viki_word_count += len(msg)
    print('Allen說了', allen_word_count, '個字') 
    print('Allen傳了', allen_sticker_count, '個貼圖', allen_image_count, '張圖片')
    print('Vike說了', viki_word_count, '個字') 
    print('Vike傳了', viki_sticker_count, '個貼圖', viki_image_count, '張圖片')            

def write_file(filename, data):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for d in data:
            f.write(d + '\n')


def main():
    data = read_file('LINE-Viki.txt')
    data = convert(data)
    # write_file('output.txt',data)

main()