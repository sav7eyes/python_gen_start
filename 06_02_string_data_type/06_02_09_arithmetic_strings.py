str1, str2, str3 = input(), input(), input()
len_min = min(len(str1), len(str2), len(str3))
len_max = max(len(str1), len(str2), len(str3))
len_max = max(len(str1), len(str2), len(str3))
len_mid = (len(str1) + len(str2) + len(str3)) - len_min - len_max

if len_mid - len_min == len_max - len_mid:
    print('YES')
else:
    print('NO')
