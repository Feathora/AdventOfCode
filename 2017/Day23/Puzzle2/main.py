# def solve(input):
#     a = 1
#     b = 0
#     c = 0
#     d = 0
#     e = 0
#     f = 0
#     g = 0
#     h = 0

#     b = 99
#     c = b
#     if a != 0:
#         while True:
#             b = b * 100 + 100000
#             c = b + 17000

#             f = 1
#             d = 2

#             while True:
#                 e = 2

#                 while True:
#                     g = d * e - b

#                     if g == 0:
#                         f = 0

#                     e += 1
#                     g = e - b
#                     if g == 0:
#                         break
                
#                 d += 1
#                 g = d - b
#                 if g == 0:
#                     break
            
#             if f == 0:
#                 h += 1

#             g = b - c
#             if g == 0:
#                 break

#             b += 17

#     print(h)

b = 109900

c = 126900



def prime(num):

	i = 2

	while i * i <= num:

		if num % i == 0:

			return False

		i += 1

	return True



res = 0

for b in range(109900, c + 1, 17):

	if not prime(b):

		res += 1

print(res)