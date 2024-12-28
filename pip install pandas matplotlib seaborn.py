
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.DataFrame({
    "Age_Group": ["0-20 Years", "21-40 Years", "41-60 Years", "61+ Years"],
    "Population_Million": [516, 378, 245, 161]
})

# Plot the bar chart
plt.figure(figsize=(8, 6))
colors = ['violet', 'indigo', 'blue', 'green']
plt.bar(data['Age_Group'], data['Population_Million'], color=colors)

# Add titles and labels
plt.title("India's Population Distribution by Age in 2022", fontsize=14)
plt.xlabel("Age Group", fontsize=12)
plt.ylabel("Population (in Millions)", fontsize=12)

# Add values on top of bars
for i, val in enumerate(data['Population_Million']):
    plt.text(i, val + 10, str(val), ha='center', fontsize=10)

# Show the plot
plt.show()
