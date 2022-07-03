from abc import ABCMeta, abstractmethod

# interface 
class ArithmeticCalculator(metaclass=ABCMeta):
    
    @abstractmethod
    def sum_divisors_of(self):
        raise NotImplementedError

class Calculator(ArithmeticCalculator):
    
    def sum_divisors_of(self, n):
        divisors = [i for i in range(1, n+1) if n % i == 0]
        sum_of_divisors = sum(divisors)
        return sum_of_divisors
    

a = Calculator()
num = int(input('Enter a number: '))
print(f'The sum of divisors of {num} is:', a.sum_divisors_of(num))
