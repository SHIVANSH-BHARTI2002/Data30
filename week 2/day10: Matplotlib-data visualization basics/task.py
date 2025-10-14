# Visualize the growth of sales over months using a line chart and customize titles and axes.
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [45, 50, 58, 65, 70, 78, 85, 90, 95, 105, 110, 125]

plt.plot(months,sales)
plt.title("Growth of Sales over months")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("sales_growth.png")
print("Plot saved as sales_growth.png")
