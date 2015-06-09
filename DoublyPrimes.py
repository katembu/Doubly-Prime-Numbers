import math


class Doubly(object):

    def __init__(self, n=100):
        self.n = n
        self.final_list = []

    # Check if Number is Prime Number
    def is_prime(self, num):
        if num < 1:
            return False
        elif (num == 1 or num == 2):
            return True
        elif(num % 2 == 0 and num > 2):
            return False
        else:
            return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))

    def is_doubly(self, numberString):
        """
        Loop through each digit of a number(already converted to string)
        and check if each digit is Prime Number. If one digit is not
        Prime Number it returns False
        """
        for num in numberString:
            if not self.is_prime(int(num)):
                return False
        return True

    def prime_number_generator(self):
        """
        Generate Prime Numbers for range between 1 to N
        Its a simple implementation of Eratosthenes algorithm(without Sieve)
        """
        multiples = set()
        yield 1  # Start from 1 as per the Instruction.1 is not a Prime Number
        for i in range(2, self.n+1):
            if i not in multiples:
                yield i
                multiples.update(range(i*i, self.n+1, i))

    def doubly_list(self, p):
        """
        Return final list of Doubly Prime Numbers between range 1 - N
        A number is converted to string and passed to is_doubly function
        """
        self.final_list = [x for x in p if self.is_doubly(str(x))]
        return self.final_list


if __name__ == '__main__':
    N = ''
    try:
        N = int(raw_input("Enter length: "))
        if N < 1:
            print ("Length should be greater than 0")
    except ValueError:
        print("That's not an int!")


    if N and N > 0:
        # Instantiate
        doubly = Doubly(N)
        # Generate Prime Numbers between 1 - N
        p = list(doubly.prime_number_generator())
        # Get Doubly Prime Numbers
        doubly_list = doubly.doubly_list(p)
        print "Doubly List Between 1 - %s : %s " % (N, doubly_list)
