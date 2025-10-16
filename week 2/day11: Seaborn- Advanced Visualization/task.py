# Load the tips dataset and create a boxplot showing the distribution of tips by day
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.boxplot(x="day", y="tip", data=tips)

plt.title("Distribution of Tips by Day", fontsize=14)
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Tip Amount ($)", fontsize=12)
plt.savefig("task.png")