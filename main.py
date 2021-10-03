import sympy
import metode

x = sympy.symbols('x')

print("==========Proyek Mencari Akar Persamaan==========")
g_x = input('Masukkan Persamaan Disini: ')
x0 = float(input('Tebakaan awal (x0): '))
E = float(input('Toleransi terhadap error (Ea): '))
N = int(input('Banyak Langkah Maksimal: '))
print('Pilih 1 untuk Metode Newton Raphson dan Pilih 2 untuk Metode Secant')
metoda = int(input('Pilih Metode 1 atau 2:'))

g_x = sympy.sympify(g_x)
h_x = sympy.diff(g_x)

if metoda == 1:
    try:
        metode.newtonMethod(g_x, h_x, x0, E, N)
    except Exception as e:
        print(e)
        x1 = float(input('Tebakan awal (x1) untuk secant method: '))
        metode.secant(g_x, x0, x1, E, N)
elif metoda == 2:
    x1 = float(input('Tebakan awal (x1) untuk secant method: '))
    print("\n")
    try:
        metode.secant(g_x, x0, x1, E, N)
    except Exception as e:
        print(e)
        metode.newtonMethod(g_x, h_x, x0, E, N)
else:
    print("Mohon maaf, hanya dapat memilih Metode 1 atau Metode 2")
