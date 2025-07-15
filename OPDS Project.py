import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Create visualizations folder if it doesn't exist
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# Re-creating the dataset
data = {
    'Age Group': ['Under 15', '16-21', '22-29', '30-36', '37+'],
    'Daily Usage (hours)': [1.5, 6.5, 5.2, 3.5, 2.8],
    'Awareness Level': [20, 50, 70, 65, 55],
    '2FA Adoption (%)': [15, 50, 75, 70, 60],
    'Victimization (%)': [35, 40, 20, 25, 30],
    'Attended Workshops (%)': [5, 25, 50, 40, 30],
    'Smartphone Usage (hours)': [1.2, 6.0, 5.5, 3.8, 2.5],
    'Computer Usage (hours)': [0.5, 1.2, 2.5, 1.8, 1.5],
    'Firewall Usage (%)': [10, 30, 50, 60, 40],
    'Antivirus Usage (%)': [20, 40, 70, 80, 60]
}
df = pd.DataFrame(data)

# Plot: Daily Technology Usage Across Generations
plt.figure(figsize=(10, 6))
plt.bar(df['Age Group'], df['Daily Usage (hours)'], color='lightblue', edgecolor='black')
plt.title('Daily Technology Usage by Age Group', fontsize=16)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Daily Usage (hours)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('visualizations/daily_technology_usage.png', dpi=300, bbox_inches='tight')
plt.show()

# Plot: Smartphone vs Computer Usage
plt.figure(figsize=(10, 6))
plt.bar(df['Age Group'], df['Smartphone Usage (hours)'], color='skyblue', label='Smartphone')
plt.bar(df['Age Group'], df['Computer Usage (hours)'], color='orange', bottom=df['Smartphone Usage (hours)'], label='Computer')
plt.title('Smartphone vs Computer Usage by Age Group', fontsize=16)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Total Usage (hours)', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('visualizations/smartphone_vs_computer_usage.png', dpi=300, bbox_inches='tight')
plt.show()

# Plot: Awareness Level vs Victimization
x = np.arange(len(df['Age Group']))
plt.figure(figsize=(10, 6))
plt.bar(x - 0.2, df['Awareness Level'], 0.4, label='Awareness Level', color='green')
plt.bar(x + 0.2, df['Victimization (%)'], 0.4, label='Victimization (%)', color='red')
plt.xticks(x, df['Age Group'])
plt.title('Awareness Level vs Victimization by Age Group', fontsize=16)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('visualizations/awareness_vs_victimization.png', dpi=300, bbox_inches='tight')
plt.show()

# Plot: Participation in Cyber Safety Workshops
plt.figure(figsize=(10, 6))
plt.bar(df['Age Group'], df['Attended Workshops (%)'], color='purple', edgecolor='black')
plt.title('Participation in Cyber Safety Workshops by Age Group', fontsize=16)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('visualizations/workshop_participation.png', dpi=300, bbox_inches='tight')
plt.show()

# Correlation Heatmap
correlation_matrix = df[['Daily Usage (hours)', 'Awareness Level', '2FA Adoption (%)', 'Victimization (%)']].corr()
plt.figure(figsize=(10, 8))
plt.imshow(correlation_matrix, cmap='coolwarm', alpha=0.8)
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, fontsize=10, rotation=45, ha='right')
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, fontsize=10)
plt.title('Correlation Heatmap', fontsize=14)
plt.savefig('visualizations/correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()

# Plot: Two-Factor Authentication Adoption by Age Group
plt.figure(figsize=(10, 6))
plt.plot(df['Age Group'], df['2FA Adoption (%)'], marker='o', color='blue', linewidth=2, markersize=8)
plt.title('Two-Factor Authentication Adoption Across Generations', fontsize=16)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('2FA Adoption (%)', fontsize=12)
plt.grid()
plt.savefig('visualizations/2fa_adoption_trends.png', dpi=300, bbox_inches='tight')
plt.show()

# Plot: Cyber Risk Mitigation Measures
plt.figure(figsize=(10, 6))
plt.bar(df['Age Group'], df['Firewall Usage (%)'], color='orange', label='Firewall Usage')
plt.bar(df['Age Group'], df['Antivirus Usage (%)'], bottom=df['Firewall Usage (%)'], color='teal', label='Antivirus Usage')
plt.title('Cyber Risk Mitigation Measures by Age Group', fontsize=16)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('visualizations/risk_mitigation_measures.png', dpi=300, bbox_inches='tight')
plt.show()
