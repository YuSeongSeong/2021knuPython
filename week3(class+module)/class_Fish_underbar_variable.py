#class
class FishBread:
    #클래스 변수
    banjook = "밀가루"
    #메소드 만들기
    def make_FB(self, ingredients, price):
        self.__ingredients = ingredients
        self.__price = price
    
    #붕어빵 살펴보기
    def see_FB(self):
        print(self.__ingredients, self.__price)


#class 만들기

a = FishBread()
a.make_FB("팥", 400)
print(a.__ingredients, a.__price)
a.__price = 10
a.see_FB()