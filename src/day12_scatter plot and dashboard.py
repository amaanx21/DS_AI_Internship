#TASK 1: Correlation Checker
import matplotlib.pyplot as plt
study_hours=[1,2,3,4,5,6,7,8]
scores=[50,55,65,70,75,85,90,95]
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.title("Scatter Plot")
plt.scatter(study_hours,scores)
plt.show()

#TASK 2: The Comparison dashboard
import matplotlib.pyplot as plt
print("TASK 2")
plt.subplot(1,2,1)
plt.bar(['Electronics','Clothing','Home'],[300,450,200])
plt.title("Bar Chart")
plt.xlabel("Categoties")
plt.ylabel("Values")
plt.show()
plt.subplot(1,2,2)
plt.plot([1,2,3,4,5],[2000,4500,4000,7500,9000])
plt.title("Line Plot")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

