print("Het_Kothari_60004230270")

def histogram(I):
    count_dict = {}
    for num in I:
        count_dict[num] = count_dict.get(num,0)+1

    sorted_pairs = sorted(count_dict.items(), key=lambda x: (x[1], x[0]))

    return sorted_pairs


print(histogram([13, 12, 11, 13, 14, 13, 7, 7, 13, 14, 12]))
print(histogram([7, 12, 11, 13, 7, 11, 13, 14, 12]))
print(histogram([13, 7, 12, 7, 11, 13, 14, 13, 7, 11, 13, 14, 12, 14, 14, 7]))
