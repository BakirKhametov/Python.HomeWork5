# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.



def algorithm_rle(data):
    count = 1
    # rle_code = ''

    if not data: 
        return ''  
    
    step = 1
    elements = [data[i:i+step] for i in range(0, len(data), )]
    print(elements)

    # for i , elements in enumerate(data):
    #         print(i, elements)
    

    for i in elements:
        if elements [i] != elements[i+1]:
            rle_code = str(count) + elements[i]
            count = count
        else:
            count = count + 1
        
        
a = algorithm_rle('ffffgggggkkkkkrrrrrv')       
print(a)





