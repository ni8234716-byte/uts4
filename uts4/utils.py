import math

def persegi():
    s = float(input("Masukkan sisi: "))
    print("Luas Persegi =", s * s)

def persegi_panjang():
    p = float(input("Masukkan panjang: "))
    l = float(input("Masukkan lebar: "))
    print("Luas Persegi Panjang =", p * l)

def segitiga():
    a = float(input("Masukkan alas: "))
    t = float(input("Masukkan tinggi: "))
    print("Luas Segitiga =", 0.5 * a * t)

def jajar_genjang():
    a = float(input("Masukkan alas: "))
    t = float(input("Masukkan tinggi: "))
    print("Luas Jajar Genjang =", a * t)

def layang_layang():
    d1 = float(input("Masukkan diagonal 1: "))
    d2 = float(input("Masukkan diagonal 2: "))
    print("Luas Layang-layang =", 0.5 * d1 * d2)

def belah_ketupat():
    d1 = float(input("Masukkan diagonal 1: "))
    d2 = float(input("Masukkan diagonal 2: "))
    print("Luas Belah Ketupat =", 0.5 * d1 * d2)

def trapesium():
    a = float(input("Masukkan sisi atas: "))
    b = float(input("Masukkan sisi bawah: "))
    t = float(input("Masukkan tinggi: "))
    print("Luas Trapesium =", 0.5 * (a + b) * t)

def lingkaran():
    r = float(input("Masukkan jari-jari: "))
    print("Luas Lingkaran =", math.pi * r * r)

def heksagon():
    s = float(input("Masukkan sisi: "))
    print("Luas Heksagon =", (3 * math.sqrt(3) / 2) * s * s)

def pentagon():
    s = float(input("Masukkan sisi: "))
    print("Luas Pentagon =", (5 * s * s) / (4 * math.tan(math.pi / 5)))