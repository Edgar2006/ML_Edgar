import matplotlib.pyplot as plt

products = ["Product 1", "Product2", "Product3", "Product4"]

sales = [350,780,280,520]

plt.bar(products, sales, color = ["red", "blue", "green", "orange"])

plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales Data")
plt.show()

