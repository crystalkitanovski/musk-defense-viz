import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('seaborn')
sns.set_palette("husl")

# Create the data
data = {
    'Year': [2012, 2016, 2020, 2022, 2023, 2024],
    'Value_Billions': [0.4, 0.83, 2.89, 1.43, 1.22, 0.95],
    'Event': ['First SpaceX NASA Contract', 
              'Air Force GPS Contract',
              'Space Force Launch Contract',
              'Starlink Military Support',
              'DOD Starshield Contract',
              'DOGE Formation Announced'],
    'Category': ['Space', 'Defense', 'Defense', 'Defense', 'Defense', 'Government']
}

df = pd.DataFrame(data)

# Create the figure and axis with specific size
plt.figure(figsize=(12, 6))

# Create the main bar plot
bar_plot = sns.barplot(data=df, 
                      x='Year', 
                      y='Value_Billions',
                      palette='Blues_r')

# Customize the plot
plt.title("Elon Musk's Growing Defense & Government Impact (2012-2024)", 
         fontsize=14, 
         pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Contract Value (Billions USD)', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add value labels on top of each bar
for i, v in enumerate(df['Value_Billions']):
    bar_plot.text(i, v + 0.1, f'${v}B', 
                 ha='center', 
                 fontsize=10)

# Add event annotations
for i, (event, val) in enumerate(zip(df['Event'], df['Value_Billions'])):
    plt.text(i, val/2, event, 
             ha='center', 
             rotation=90, 
             fontsize=8,
             color='white')

# Add a footnote
plt.figtext(0.99, 0.01, 'Data compiled from public contracts and announcements. Values are approximate.',
            ha='right', 
            fontsize=8, 
            style='italic')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot
plt.savefig('musk_defense_timeline.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
