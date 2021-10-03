from sympy import *

x = symbols('x')


def newtonMethod(g_x, h_x, x0, E, N):
    step = 1
    flag = 1
    Ea = 1
    print('\nMetode Newton-Raphson')
    print("Iterasi \t    x1 \t\t   f(x1) \t    Ea")
    while Ea > E:
        if h_x.subs(x, x0) == 0.0:
            raise Exception("\nEror, dikarenakan karena sistem terbagi dengan 0!")
        x1 = x0 - g_x.subs(x, x0) / h_x.subs(x, x0)
        Ea = abs(g_x.subs(x, x1))

        print('%d \t\t %0.6f \t %0.6f \t %0.6f' % (step, x1, g_x.subs(x, x1), Ea))
        x0 = x1
        step += 1

        if step > N:
            flag = 0
            break
    if flag == 1:
        print('\nDidapat Akar yang Terdekat adalah %0.8f' % x1)
    else:
        raise Exception("\nTidak Konvergen ataupun Banyak Langkah Maksimal yang Di-input Masih Kurang Banyak")


def secant(g_x, x0, x1, e, N):
    step = 1
    Ea = 1
    print('Metode Secant')
    print("Iterasi \t    x1 \t\t   g(x1) \t    Ea")
    while Ea > e:
        if g_x.subs(x, x0) == g_x.subs(x, x1):
            raise Exception("\nEror, dikarenakan sistem terbagi dengan 0!")
        x2 = x1 - ((x1 - x0) * g_x.subs(x, x1) / (g_x.subs(x, x1) - g_x.subs(x, x0)))
        Ea = abs((x2 - x1) / x2) * 100
        print('   %d \t\t %0.6f \t %0.6f \t %0.6f' % (step, x2, g_x.subs(x, x2), Ea))

        x0 = x1
        x1 = x2
        step += 1

        if step > N:
            raise Exception("\nTidak Konvergen Alias Menjauhi Titik Akar")
    print('\nDidapat Akar yang Terdekat adalah %0.8f' % x2)
