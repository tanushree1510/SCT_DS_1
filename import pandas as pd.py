import pandas as pd


# Create the dataset
data = pd.DataFrame({
    "Age_Group": ["0-20 Years", "21-40 Years", "41-60 Years", "61+ Years"],
    "Population_Million": [516, 378, 245, 161]
})

# Save the dataset to a CSV file
data.to_csv("population_data.csv", index=False)

print("Dataset saved as 'population_data.csv'")
