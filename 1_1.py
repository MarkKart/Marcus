import numpy as np

a = np.array([[2.3, 5.1, 4.7],
              [3.5, 6.7, 1.5],
              [8.4, 3.1, 9.2]])

b = np.array([[4.3, 8.1, 6.1],
              [3.7, 6.2, 1.5],
              [2.4, 5.7, 4.7]])


rows1, columns1 = np.shape(a)
rows2, columns2 = np.shape(b)

print("Массив a содержит",rows1, "строк и",columns1,"столбцов")
print("Массив b содержит",rows2, "строк и",columns2,"столбцов")

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a ** 2)
print(a % 2)

print('ASDASDASD')
c = np.cos(a)
print(c)
d = np.sin(b)
print(d)
print('ASDASDASD')
c = np.cos(a)
print(c)
d = np.sin(b)
print(d)
