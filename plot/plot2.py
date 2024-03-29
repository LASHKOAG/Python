from matplotlib import pyplot as plt

movies = ["Энни Холл", "Бен-Гур", "Касабланка", "Ганди", "Вестсайдская история"] 
num_oscars = [5,11,3,8,10]


xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)

#добавить подпись к оси Y
plt.ylabel("Количество наград")

#добавить название диаграммы
plt.title("Мои любимые фильмы")

plt.xticks = ([i + 0.5 for i, _ in enumerate(movies)], movies)



#добавить подпись к оси X
#plt.xlabel("Годы")

#вывод на экран
plt.show()