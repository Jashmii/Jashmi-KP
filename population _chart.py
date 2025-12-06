import matplotlib.pyplot as plt

age_groups = ['0–14 years', '15–64 years', '65+ years']
population_percentage = [25, 67, 8]

plt.figure(figsize=(10,6))
plt.bar(age_groups, population_percentage)

for i, v in enumerate(population_percentage):
    plt.text(i, v + 1, f"{v}%", ha='center')

plt.title('Population Distribution by Age (Sample Dataset)')
plt.xlabel('Age Groups')
plt.ylabel('Population Percentage')
plt.savefig("population_chart.png", dpi=300, bbox_inches='tight')
plt.show()