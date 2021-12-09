class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def divide_by_null(a, b):
        try:
            return (a / b)
        except:
            return f"Na 0 delit nelzya"


d = Division(21, 66)
print(Division.divide_by_null(21, 0))
print(Division.divide_by_null(21, 30))
print(d.divide_by_null(66, 6))
