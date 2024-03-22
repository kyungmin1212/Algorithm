from collections import Counter

def solution(s):
    s = s.replace("{","")
    s = s.replace("}","")
    s = s.replace(","," ")
    s_list = s.split(" ")
    counter = Counter(s_list)

    return [int(k) for k,v in counter.most_common()]