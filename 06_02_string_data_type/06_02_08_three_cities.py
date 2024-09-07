city1, city2, city3 = input(), input(), input()
lehgt_city1 = len(city1)
lehgt_city2 = len(city2)
lehgt_city3 = len(city3)

if len(city1) == min(lehgt_city1, lehgt_city2, lehgt_city3):
    print(city1)
elif len(city2) == min(lehgt_city1, lehgt_city2, lehgt_city3):
    print(city2)
elif len(city3) == min(lehgt_city1, lehgt_city2, lehgt_city3):
    print(city3)
if len(city1) == max(lehgt_city1, lehgt_city2, lehgt_city3):
    print(city1)
elif len(city2) == max(lehgt_city1, lehgt_city2, lehgt_city3):
    print(city2)
elif len(city3) == max(lehgt_city1, lehgt_city2, lehgt_city3):
    print(city3)
