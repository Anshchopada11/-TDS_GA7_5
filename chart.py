# chart.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn styling for a professional look
sns.set_style("whitegrid")
sns.set_context("talk")  # Suitable for presentations

# Generate synthetic data
np.random.seed(42)  # For reproducibility

channels = ['Email', 'Chat', 'Phone', 'Social Media']
n = 200  # Number of data points per channel

data = {
    'Channel': np.repeat(channels, n),
    'ResponseTime': np.concatenate([
        np.random.normal(loc=8, scale=2, size=n),   # Email
        np.random.normal(loc=3, scale=1, size=n),   # Chat
        np.random.normal(loc=5, scale=1.5, size=n), # Phone
        np.random.normal(loc=6, scale=2, size=n)    # Social Media
    ])
}

df = pd.DataFrame(data)

# Clip negative values to 0 (response time can't be negative)
df['ResponseTime'] = df['ResponseTime'].clip(lower=0)

# Create figure with 512x512 px size
plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512 px

# Create violin plot
sns.violinplot(
    x='Channel',
    y='ResponseTime',
    data=df,
    palette='Set2',
    inner='quartile'
)

# Add labels and title
plt.title('Customer Support Response Time by Channel', fontsize=16)
plt.xlabel('Support Channel')
plt.ylabel('Response Time (minutes)')

# Save the chart
plt.tight_layout()
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
