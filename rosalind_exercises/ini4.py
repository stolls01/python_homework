#Given: Two positive integers a and b (a<b<10000).
#Return: The sum of all odd integers from a through b, inclusively.

a =
b =

integer_list = list(range(a, b+1))

if (a % 2) == 0:
    odd_integers = integer_list[1::2]
else:
    odd_integers = integer_list[0::2]

odd_integer_sum = 0
for integer in odd_integers:
    odd_integer_sum = odd_integer_sum + integer

print(odd_integer_sum)