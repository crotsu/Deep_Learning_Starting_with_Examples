# 問1

# 1から100の和を求める
 
# whileを使う
total = 0
i = 1
while i<=100:
    total += i
    i += 1
print("total=", total)

# forを使う
total = 0
for i in range(100):
    total += i+1
print("total=", total)

# 1から100までの内，3の倍数の和を求める
total = 0
for i in range(100):
    if (i+1)%3==0:
        total += i+1
print("total=", total)
