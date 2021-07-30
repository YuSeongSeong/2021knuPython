# 문제 : 부기는 에어컨 리모컨을 프로그램으로 만들려고 한다.

# 1. 사용자에게 온도를 18 ~ 30의 숫자로 입력받아 에어컨 온도를 설정하고,
# 2. 목표 온도가 설정되면 함수를 이용해 현재 온도에서 목표 온도까지 1씩 증가/감소 하여 목표온도가 되도록 한다.
# 3. '종료'를 입력받으면 프로그램을 종료한다.
# 4. 프로그램을 종료하기 전까지는 계속 온도를 입력 받을 수 있어야한다.
# 5. 시작 온도는 20도이다.
# 사용할 개념 : 함수, 전역변수, if문, while문, string-interpolation, 연산자, break

# 현재 온도
cur_tem = 20                    

# 온도 설정 함수
def set_tem(des_tem):           
    """
    온도를 설정하는 함수
    set_tem(설정할 온도)
    """
    # 현재 온도를 전역변수로 받아온다.
    global cur_tem
    now_tem = cur_tem

    # 현재 온도와 목표 온도를 비교해서 온도 설정

    if des_tem == now_tem:
        print("현재 온도는 {}도 입니다.".format(des_tem))
    elif des_tem > now_tem:
        for i in range(now_tem,des_tem+1):
            now_tem = i
            print("현재 온도는 {}도 입니다.".format(now_tem))
        cur_tem = now_tem
        
    else:
        for i in range(now_tem,des_tem-1,-1):
            now_tem = i
            print("현재 온도는 {}도 입니다.".format(now_tem))
        cur_tem = now_tem



print("에어컨을 작동합니다.")

# 입력을 계속 받을 수 있도록 무한 반복문 사용                  
    
    # 온도 입력받기
    
    # 종료를 입력 받으면 종료
    
    # 적절한 온도 값을 입력받으면 set_tem 함수 호출
    
    # 적절한 값이 아니면 다시 입력을 받는다.
while(True):
    a = input("원하는 온도를 설정해 주세요: ")
    if a == "종료":
        print("에어컨을 종료합니다.")
        break
    elif 18 <= int(a) <= 30:
        set_tem(int(a))
    else:
        print("입력을 확인해 주세요.")

