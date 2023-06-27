import matplotlib.pyplot as plt

years= [2010, 2012, 2014, 2016, 2018, 2020]
population = [ 10, 12, 9, 8 ,7, 9]
plt.plot(years, population, marker = "o", linestyle= "--", color ="red")
plt.xlabel("Year")
plt.ylabel("Population (in billions)")
plt.title ("Population Growth Over Years")
plt.show()
