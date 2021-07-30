#class
class FishBread:
    #클래스 변수
    banjook = "밀가루"
    #메소드 만들기
    def make_FB(self, ingredients, price):
        self.ingredients = ingredients
        self.price = price
    
    #붕어빵 살펴보기
    def see_FB(self):
        print(self.ingredients, self.price)
    
    #클래스 메소드
    def see_banjook(cls):
        print(cls.banjook)

#class 만들기
a = FishBread()
b = FishBread()

a.see_banjook()
b.see_banjook()

FishBread.banjook = "콩가루"
a.banjook = "쌀가루"

a.see_banjook()
b.see_banjook()


