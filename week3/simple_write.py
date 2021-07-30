#간단한 파일 출력(쓰기)
f = open('headal.txt', 'w')

for i in range(100):
    f.write(f"Hello ! {i}\n")

print("쓰기 종료")

f.close()