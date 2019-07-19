# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
# import math
#
# class Triangle ():
#     def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
#         self.a_x = a_x
#         self.a_y = a_y
#         self.b_x = b_x
#         self.b_y = b_y
#         self.c_x = c_x
#         self.c_y = c_y
#         self.AB = round(math.sqrt(int(math.fabs(((b_y - a_y) ** 2) + ((b_x - a_x) ** 2)))), 2)
#         self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
#         self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)
#
#     def perimetr(self):
#         self.perimetr = round((self.AB + self.BC + self.CA), 2)
#         return (self.perimetr)
#
#     def ploshad(self):
#         self.polperimetr = round(self.perimetr / 2, 2)
#         self.ploshad = round(math.sqrt(self.polperimetr*(self.polperimetr - self.AB)*(self.polperimetr - self.BC)*(self.polperimetr - self.CA)), 2)
#         return (self.ploshad)
#
#     def vysotaAB(self):
#         self.vysotaAB = round(((self.ploshad * 2 / self.AB)), 2)
#         return (self.vysotaAB)
#
#     def vysotaBC(self):
#         self.vysotaBC = round(((self.ploshad * 2 / self.BC)), 2)
#         return (self.vysotaBC)
#
#     def vysotaCA(self):
#         self.vysotaCA = round(((self.ploshad * 2 / self.CA)), 2)
#         return (self.vysotaCA)
#
# #
# # tri_coord = Triangle(1, 1, 1, 3, 5, 1)
# #
# # print('Длинна строны АВ = {}, ВС = {}, СА = {}'.format(tri_coord.AB, tri_coord.BC, tri_coord.CA))
# # print('Периметр треугольника АВС равен {}'.format(tri_coord.perimetr()))
# # print('Площадь треугольника АВС равна {}'.format(tri_coord.ploshad()))
# # print('Высота треугольника АВС, проведенная из угла A равна {}'.format(tri_coord.vysotaBC()))
# # print('Высота треугольника АВС, проведенная из угла B равна {}'.format(tri_coord.vysotaCA()))
# # print('Высота треугольника АВС, проведенная из угла C равна {}'.format(tri_coord.vysotaAB()))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math

class Trapetzium ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.d_x = d_x
        self.d_y = d_y
        self.AB = round(math.sqrt(int(math.fabs(((b_y - a_y) ** 2) + ((b_x - a_x) ** 2)))), 2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CD = round(math.sqrt(int(math.fabs(((d_y - c_y) ** 2) + ((d_x - c_x) ** 2)))), 2)
        self.DA = round(math.sqrt(int(math.fabs(((a_y - d_y) ** 2) + ((a_x - d_x) ** 2)))), 2)
        self.AC = round(math.sqrt(int(math.fabs(((c_y - a_y) ** 2) + ((c_x - a_x) ** 2)))), 2)
        self.BD = round(math.sqrt(int(math.fabs(((d_y - b_y) ** 2) + ((d_x - b_x) ** 2)))), 2)

    # def iso_trapezium(self):
    #     if self.AC == self.BD:
    #         return (' равнобедренная')
    #     else:
    #         return (' не равнобедренная')

    def perimetr(self):
        self.perimetr = round((self.AB + self.BC + self.CD + self.DA), 2)
        return (self.perimetr)

    #
    def ploshad(self):
        if self.AC == self.BD:
            if self.DA == self.BC:
                self.ploshad = round((self.AB + self.CD) * (((self.DA**2 - ((self.CD - self.AB)/2) ** 2) ** 0.5) / 2), 2)
                return (self.ploshad)
            else:
                if self.AB == self.CD:
                    self.ploshad = round((self.BC + self.DA) * (((self.AB**2 - ((self.BC - self.DA)/2) ** 2) ** 0.5) / 2), 2)
                    return (self.ploshad)
        else:
            return (' - трапеция не равнобедренная.')


trap_coord = Trapetzium (3, 5, 6, 5, 8, 1, 1, 1)

print('Длины строн равнобедренной трапеции равны:\n АВ = {}\n ВС = {}\n СD = {}\n DA = {}'.format(trap_coord.AB, trap_coord.BC, trap_coord.CD, trap_coord.DA))
print('Периметр равнобедренной трапеции равен {}'.format(trap_coord.perimetr()))
print('Площадь равнобедренной трапеции равна {}'.format(trap_coord.ploshad()))


#