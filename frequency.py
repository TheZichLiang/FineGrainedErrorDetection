import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Load the CSV files
train_data = pd.read_csv('csv_data/train.csv')
validation_data = pd.read_csv('csv_data/validation.csv')
test_data = pd.read_csv('csv_data/test.csv')

# Function to filter data based on language pair
def get_language_data(lang):
    if lang.lower() == "en-de":
        return (
            train_data.iloc[:6992],
            validation_data.iloc[:1000],
            test_data.iloc[:998]
        )
    elif lang.lower() == "en-zh":
        return (
            train_data.iloc[6992:13964],
            validation_data.iloc[1000:1996],
            test_data.iloc[998:1995]
        )
    elif lang.lower() == "ru-en":
        return (
            train_data.iloc[33898:],
            validation_data.iloc[4842:],
            test_data.iloc[4993:]
        )

# Select language pair
language_pair = "ru-en"
train, validation, test = get_language_data(language_pair)

# Combine datasets
data = pd.concat([train, validation, test])

# Ensure proper columns
data.columns = ['', 'original', 'translation', 'mean']

# Convert 'mean' column to numeric
data['mean'] = pd.to_numeric(data['mean'], errors='coerce')

# Drop NaN values in the mean column
data = data.dropna(subset=['mean'])

# Plot histogram of mean scores
plt.figure(figsize=(10, 6))
counts, bins, _ = plt.hist(data['mean'], bins=30, alpha=0.6, label='Frequency', color='blue', edgecolor='black')

# Calculate normal distribution
mean = data['mean'].mean()
std_dev = data['mean'].std()
x = np.linspace(bins.min(), bins.max(), 500)
normal_dist = norm.pdf(x, mean, std_dev)

# Scale normal distribution to match histogram
bin_width = bins[1] - bins[0]  # Width of a bin
normal_dist_scaled = normal_dist * len(data['mean']) * bin_width

# Plot normal distribution
plt.plot(x, normal_dist_scaled, color='red', label='Normal Distribution')
plt.xlabel('Mean Score')
plt.ylabel('Frequency')
plt.title(f'Frequency of Scores for {language_pair} Translations')
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("ru-en_binned.png", dpi=300, bbox_inches='tight')
plt.show()