class EvenNumbers:
    def __init__(self):
        self.even_numbers = None 

    def get_even_numbers(self): 
        if self.even_numbers is None: 
            print("Creating  Even Numbers...")
            self.even_numbers = [x for x in range(2, 21, 2)]

        print("Return Even Numbers") 
        return self.even_numbers
    
if __name__=="__main__":
    nums = EvenNumbers()
    print(nums.even_numbers)
    print("*"*40)
    print(nums.get_even_numbers())

    print("*"*40)
    print(nums.get_even_numbers())

    print("*"*40)
    print(nums.get_even_numbers()) 