class woman():
    def __init__(self, name, weight, height, iq ):
        self.name = name
        self.weight = weight
        self.height = height
        self.iq = iq

    def eat( self ):
        self.weight += 30
        print("{}는 먹어서 몸무게가 {}kg이 되었습니다".format(self.name, self.weight))

    def study( self ):
        self.iq += 10
        print("{}는 공부를 해서 아이큐가 {}이 되었습니다".format(self.name, self.iq))

    def sleep( self ):
        self.height += 12
        print("{}는 잠을 자서 키가 {}cm 되었습니다".format(self.name, self.height))
    def show( self ):
        print("{}의 현재 아이큐는 {} 키는 {}cm 몸무게는 {}kg입니다".format(self.name, self.iq,self.height,self.weight))