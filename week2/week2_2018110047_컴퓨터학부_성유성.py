# 문제 : 해달이는 1부터 100까지의 숫자를 분류하려 한다
# 리스트 "mul2"에는 2의 배수, 리스트 "mul3"에는 3의 배수, 
# 리스트 "mul6"에는 6의 배수를 넣고
# 나머지 수는 모두 더해서 출력하려고 한다. 해달이를 도와주자
# 사용할 개념 : 리스트, for, range, if, %, append, +=

mul2 = []
mul3 = []
mul6 = []
others = 0

# 풀이 코드
for i in range(1,101):
    if i % 6 == 0:
        mul6.append(i)
    elif i % 3 == 0:
        mul3.append(i)
    elif i % 2 == 0:
        mul2.append(i)
    else:
        others += i

print("mul2 = ",mul2)
print("mul3 = ",mul3)
print("mul6 = ",mul6)
print("others = ",others)

# 결과 값
# "mul2 = [2, 4, 8, ..., 100]"
# "mul3 = [3, 6, 9, ..., 99]"
# "mul6 = [6, 12, 18, ..., 96]"
# "others = 1633"