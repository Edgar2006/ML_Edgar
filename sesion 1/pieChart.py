import matplotlib.pyplot as plt

cat = ["category a", "category b", "category c", "category d","category i"]

pers = [25,60,32,3, 10]

exp = [0,0.2,0,0,0.2]

color = ["red", "blue", "orange", "green","skyblue"]

plt.pie(pers, explode = exp, labels = cat, colors = color, shadow = True)
plt.title("qwerty")
plt.legend(cat)
plt.show()

