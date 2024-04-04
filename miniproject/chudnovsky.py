from decimal import Decimal, getcontext


def binary_split(a, b):
    if b == a + 1:
        Pab = -(6 * a - 5) * (2 * a - 1) * (6 * a - 1)
        Qab = 10939058860032000 * a ** 3
        Rab = Pab * (545140134 * a + 13591409)
    else:
        m = (a + b) // 2
        Pam, Qam, Ram = binary_split(a, m)
        Pmb, Qmb, Rmb = binary_split(m, b)

        Pab = Pam * Pmb
        Qab = Qam * Qmb
        Rab = Qmb * Ram + Pam * Rmb
    return Pab, Qab, Rab


def chudnovsky(n):
    """Chudnovsky algorithm."""
    P1n, Q1n, R1n = binary_split(1, n)
    return (426880 * Decimal(10005).sqrt() * Q1n) / (13591409 * Q1n + R1n)


print(chudnovsky(2))  # 3.141592653589793238462643384

getcontext().prec = 100
for n in range(2, 10):
    print(f"{n=} {chudnovsky(n)}")  # 3.14159265358979323846264338...
