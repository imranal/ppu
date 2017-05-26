import matplotlib.pylab as plt
import matplotlib.ticker as ticker

x = [0, 0.5, 1, 2, 3, 3.5, 4, 4.5, 5, 7.5, 8.5, 9]
y = [2,  2,  2, 3, 1,  2,  2,  2,  2,  1,   1,  0]

fig, ax = plt.subplots(1)

width = 0.5
ax.bar(x, y, width, color="pink")
ax.set_xlabel('score')
ax.set_ylabel('antall')

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

plt.show()

avg = 0
for i in range(len(x) - 1):
    avg += x[i]*y[i]
avg = avg/sum(y)
print(avg)
