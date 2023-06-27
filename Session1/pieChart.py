import matplotlib.pyplot as plt

categories = ['Category 1', 'Category 2', 'Category3', 'Category 4', 'Category 5']

percentages = [25, 30, 15, 10, 20]
explode = [0, 0.1, 0, 0, 0.1]
colors = ['red', 'blue','pink', 'orange','green']
plt.pie(percentages, explode = explode, labels = categories, colors = colors, shadow = True)
plt.title("Percentage Distribution")
plt.legend(categories)
plt.show()

