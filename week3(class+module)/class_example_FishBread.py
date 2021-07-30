#class
class FishBread:
    #메소드 만들기
    def make_FB(self, ingredients, price):
        self.ingredients = ingredients
        self.price = price
    
    #붕어빵 살펴보기
    def see_FB(self):
        print(self.ingredients, self.price)

#class 만들기
a = FishBread()
b = FishBread()

a.make_FB("팥", 400)
b.make_FB("슈크림",500)
a.see_FB()
b.see_FB()



