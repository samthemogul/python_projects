'''
Write a program to print the sum of the following series
a. 1 + ½ + 1/3 +. …. + 1/n
b. 1/1 + 2^2/2 + 3^3/3 + ……. + n^n/n
'''

nth_term = int(input("You want to find the sum to what term?:"))

def first_series(nth_term):
    a = 1
    sum1 = 0
    while a <= nth_term:
        sum1 += 1/a
        a += 1
    print(sum1)


def second_series(nth_term):
    b = 1
    sum2 = 0
    while b <= nth_term:
        sum2 += (b ** b) / b
        b += 1
    print(sum2)




first_series(nth_term)
second_series(nth_term)