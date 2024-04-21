import random
from random import *
def useless():
    return 0.5
def main():
    alphabet = "a, b, c, d ,e, f, g, h, i, j, k, l, m, n, o, p, q, r, s ,t, u, v, w, x, y, z,A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
    special_chars = "@,?,!,_,-,*,#,$,%,&"
    numbers = "1,2,3,4,5,6,7,8,9"
    user_wants_password = True
    alpha_len = int(input("how many letters? "))
    special_len = int(input("how many special chars? "))
    number_len = int(input("how many numbers? "))
    while user_wants_password:
        password = ""
        for i in range(alpha_len):
            letters = alphabet[randrange(alpha_len)]
            password = password + letters
        for i in range(special_len):
            specials = special_chars[randrange(special_len)]
            password = password + specials
        for i in range(number_len):
            number = numbers[randrange(number_len)]
            password = password + number

        print(password)
        user_wants_password = False



main()