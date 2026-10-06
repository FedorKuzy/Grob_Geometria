def divide_segment(p1, p2, m=1, n=1):
    if m < 0 or n < 0 or (m + n) <= 0:
        raise ValueError("Отношения m и n должны быть неотрицательными, а их сумма — больше 0")
    k = m / (m + n)
    return [round(a + k * (b - a), 4) for a, b in zip(p1, p2)]
