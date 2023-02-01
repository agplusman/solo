import matplotlib.pyplot as plt

impact = 7
effort = 7

data = [[impact, effort]]

fig, ax = plt.subplots()
ax.scatter(*zip(*data), c='red')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

plt.axhline(y=5, color='black', linestyle='--')
plt.axvline(x=5, color='black', linestyle='--')

plt.text(5, 8, "Low Effort, High Impact", ha='center', va='center', color='black')
plt.text(8, 5, "High Effort, High Impact", ha='center', va='center', color='black')
plt.text(2, 5, "Low Effort, Low Impact", ha='center', va='center', color='black')
plt.text(5, 2, "High Effort, Low Impact", ha='center', va='center', color='black')

plt.fill_betweenx([0, 5], [0, 5], [10, 10], color='green', alpha=0.2)
plt.fill_between([0, 5], [5, 10], [0, 0], color='green', alpha=0.2)

plt.xlabel('Impact')
plt.ylabel('Effort')

plt.annotate(f"({impact}, {effort})", (impact + 0.3, effort + 0.3), fontsize=12)

plt.show()