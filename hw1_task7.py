a = int(input("Количество километров в 1-й день: "))
b = int(input("Количество километров в последний день: "))
day = 1
print(day, "-й день: ", a)
while a < b:
    day = day + 1
    a = 0.1 * a + a
    print(day, "-й день: ", a)
print("Ответ: на", day, "-й день спортсмен достиг результата - не менее", b, "километров")