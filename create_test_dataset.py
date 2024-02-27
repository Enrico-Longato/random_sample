import pandas as pd
import numpy as np

# Define unequal distributions for sector, size, and location
sector_distribution = {'Tech': 0.4, 'Finance': 0.3, 'Healthcare': 0.2, 'Retail': 0.1}
size_distribution = {'Small': 0.6, 'Medium': 0.3, 'Large': 0.1}
location_distribution = {'UD': 0.4, 'TS': 0.3, 'PN': 0.2, 'GO': 0.1}

# Number of companies
n_companies = 100000

# Generate data with unequal distributions
sector_choices = np.random.choice(list(sector_distribution.keys()), size=n_companies, p=list(sector_distribution.values()))
size_choices = np.random.choice(list(size_distribution.keys()), size=n_companies, p=list(size_distribution.values()))
location_choices = np.random.choice(list(location_distribution.keys()), size=n_companies, p=list(location_distribution.values()))

# Create dataframe
data = {'company_name': [f'Company {i}' for i in range(n_companies)],
        'sector': sector_choices,
        'size': size_choices,
        'location': location_choices}


df = pd.DataFrame(data)

df = df.sort_values(by=['location', 'sector', 'size'])

df.to_csv('test_dataset.csv', index = False)

print(f'created a dataset of {len(df)} companies')
