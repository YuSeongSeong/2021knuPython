#해달이의 집에서 학교까지의 거리
# 숫자 두개를 입력 받아 둘 중 큰 값에서 작은 값을 뺴서 거리를 구하는 프로그램 작성

#결과
# 첫 번째 수가 클 떄
# 첫 번쨰 수를 입력 : 55
# 두 번쨰 수를 입력: 4
# 51

# 두 번쨰 수가 클 떄
# 첫 번쨰 수를 입력하세요: 12
# 두 번쨰 수를 입력하세요: 33
# 21

# 두 수를 입력 받자
input1 = input("첫 번쨰 수를 입력하세요 ")
input2 = input("두 번쨰 수를 입력하세요 ")

# 거리를 출력하기 위해 두 수의 대소비교
if input1 > input2:
    print(int(input1) - int(input2))
else:
    print(int(input2) - int (input1)) 
