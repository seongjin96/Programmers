import math

def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    a = [str1[i:i+2] for i in range(0, len(str1) - 1)]
    b = [str2[i:i+2] for i in range(0, len(str2) - 1)]

    same_list = []
    all_list = []
    
    for txt in a:
        if txt.isalpha() and txt in b:
            same_list.append(txt)
            all_list.append(txt)
            b.remove(txt)
        elif txt.isalpha():
            all_list.append(txt)
    for txt in b:
        if txt.isalpha():
            all_list.append(txt)
    
    A = B = 0
    if len(same_list) == 0 and len(all_list) == 0:
        A = B = 1
    else:
        A = len(same_list)
        B = len(all_list)
    
    answer = math.trunc(A/B * 65536)
    
    return answer