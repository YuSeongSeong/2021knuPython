#입출력
name = input("이름을 입력: ")
age = input("나이를 입력: ")
print(f"{name}님의 나이는 {age}세 입니다.")
age = int(age) + 10 #형변환
print(f"{name}님의 10년 뒤 나이는 {age}세 입니다")
