import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('seaborn-v0_8')
sns.set_theme()

# Create the data
data = {
    'Year': [2012, 2016, 2020, 2022, 2023, 2024],
    'Value_Billions': [0.4, 0.83, 2.89, 1.43, 1.22, 0.95],
    'Event': ['First SpaceX\nNASA Contract', 
              'Air Force\nGPS Contract',
              'Space Force\nLaunch Contract',
              'Starlink\nMilitary Support',
              'DOD Starshield\nContract',
              'DOGE Formation\nAnnounced'],
    'Category': ['Space', 'Defense', 'Defense', 'Defense', 'Defense', 'Government']
}

df = pd.DataFrame(data)

# Create the figure and axis with specific size
plt.figure(figsize=(12, 8))

# Create the main bar plot with colorblind-friendly color
bar_plot = sns.barplot(
    data=df, 
    x='Year', 
    y='Value_Billions',
    hue='Year',
    legend=False,
    color='#2b83ba'  # Colorblind-friendly blue
)

# Customize the plot
plt.title("Elon Musk's Growing Defense & Government Impact (2012-2024)", 
         fontsize=14, 
         pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Contract Value (Billions USD)', fontsize=12)

# Rotate x-axis labels
plt.xticks(rotation=45)

# Add value labels at the top of each bar
for i, v in enumerate(df['Value_Billions']):
    bar_plot.text(i, v + 0.1, f'${v}B', 
                 ha='center',
                 va='bottom',
                 fontsize=10,
                 color='black')

# Add event labels below the value labels
for i, (event, val) in enumerate(zip(df['Event'], df['Value_Billions'])):
    bar_plot.text(i, val/3, event,
                 ha='center',
                 va='center',
                 fontsize=9,
                 color='white',
                 fontweight='bold')

# Add a footnote
plt.figtext(0.99, 0.01, 'Data compiled from public contracts and announcements. Values are approximate.',
            ha='right', 
            fontsize=8, 
            style='italic')

# Set y-axis limit to give space for labels
plt.ylim(0, max(df['Value_Billions']) * 1.2)

# Adjust layout
plt.tight_layout()

# Save the plot
plt.savefig('musk_defense_timeline.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
