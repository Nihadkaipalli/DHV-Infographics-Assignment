import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("df_cleaned.csv")

countries = ['United States', 'Pakistan', 'India', 'Indonesia', 'Mexico']
years = [1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020]
df_filtered = data[(data['Country Name'].isin(countries)) & (data['Year'].isin(years))]
India_data = df_filtered[df_filtered['Country Name'] == 'India']

# Setting a different background color
plt.style.use('dark_background')
plt.figure(figsize=(12, 9))

# Creating a custom color palette
custom_palette = sns.color_palette("Paired", len(countries))

plt.suptitle("Factors Affecting Population", fontfamily='Algerian', fontsize=35, color='white',weight='bold')

# Subplot 1: Bar Plot - Population
ax1 = plt.subplot(2, 2, 1)
sns.barplot(data=df_filtered, x='Year', y='Population, total', hue='Country Name', palette=custom_palette)
plt.title('Population (Total %)', fontsize=14, color='white',fontfamily='Times New Roman')
plt.xlabel('Years',  fontsize=12, color='white', fontfamily='Times New Roman')
plt.ylabel('Population (Total %)', fontsize=12, color='white', fontfamily='Times New Roman')
plt.legend(title='Countries', bbox_to_anchor=(1.05, 1), loc='upper left', frameon=False, fontsize=10)
plt.tick_params(axis='x', colors='white',labelsize=8)
plt.tick_params(axis='y', colors='white',labelsize=8)
plt.grid(True, linestyle='--', alpha=0.6)

# Subplot 2: Line Plot - Neonatal Mortality Rate
ax2 = plt.subplot(2, 2, 2)
sns.lineplot(data=df_filtered, x='Year', y='Mortality rate, neonatal (per 1,000 live births)', hue='Country Name', marker='o', palette=custom_palette, legend=False)
plt.title('Neonatal Mortality Rate', fontsize=14, color='white',fontfamily='Times New Roman')
plt.xlabel('Years', fontsize=12, color='white', fontfamily='Times New Roman')
plt.ylabel('Mortality rate, neonatal',  fontsize=12, color='white', fontfamily='Times New Roman')
plt.tick_params(axis='x', colors='white',labelsize=8)
plt.tick_params(axis='y', colors='white',labelsize=8)
plt.grid(True, linestyle='--', alpha=0.6)

# Subplot 3: Line Plot - Life Expectancy Trends
ax3 = plt.subplot(2, 2, 3)
sns.lineplot(data=df_filtered, x='Year', y='Life expectancy at birth, total (years)', hue='Country Name', marker='o', palette=custom_palette, legend=False)
plt.title('Life Expectancy Rate', fontsize=14, color='white',fontfamily='Times New Roman')
plt.xlabel('Years', fontsize=12, color='white', fontfamily='Times New Roman')
plt.ylabel('Life Expectancy (years)',  fontsize=12, color='white', fontfamily='Times New Roman')
plt.tick_params(axis='x', colors='white',labelsize=8)
plt.tick_params(axis='y', colors='white',labelsize=8)
plt.grid(True, linestyle='--', alpha=0.6)

# Subplot 4: Pie Chart - Death Rate of India
ax4 = plt.subplot(2,2,4)
# Filter data for India and specific years
india_years = [1990, 1995, 2000, 2005, 2010, 2015, 2020]
India_data = df_filtered[(df_filtered['Country Name'] == 'India') & (df_filtered['Year'].isin(india_years))]
sns.barplot(x='Death rate, crude (per 1,000 people)', y='Year', data=India_data, palette=custom_palette, orient='h')
plt.xlabel('Death rate, crude (per 1,000 people)', fontsize=12, color='white', fontfamily='Times New Roman')
plt.ylabel('Year',  fontsize=12, color='white', fontfamily='Times New Roman')
plt.grid(True, linestyle='--', alpha=0.6)
plt.title('Death rate of India', fontsize=14, color='white',fontfamily='Times New Roman')
plt.tick_params(axis='x', colors='white',labelsize=8)
plt.tick_params(axis='y', colors='white',labelsize=8)

plt.figtext(1.02,0.09,'    The provided code orchestrates an exploratory\ndata analysis workflow focusing on various factors\nwhich affects population across multiple countries.'
                
                '\n\n    The first graph vividly showcasing the trajectory\nof population growth of Countries over the years. The\ngraph illustrates the compelling story of demographic \nshifts, vividly portraying the remarkable expansion of \npopulations of these countries over successive years.'
                '\n\n    The second plot illustrates the neonatal mortality rates \n in selected countries over the specified years. The \n varying trend lines signify a decline in neonatal \n mortality rates across these nations. This decline in \n Neonatal deaths seems to correspond with an increase \n in population.'
                '\n\n    The third line plot demonstrates the life expectancy \n trends at birth in the selected countries over the specified \n years. Rising patterns imply population growth. The life \n expectancy in these countries has been on the rise,\n attributed to advancements in healthcare and overall \n quality of life.'
                '\n\n    The final horizontal bar plot showcases Indias crude \n death rate across various years.A consistent decline in the \n death rate is observable over the years,aligning with India \n being the worlds most populous country. An intriguing \n observation is the slight increase in the death rate in 2020,\n attributed to the impact of the Covid-19 pandemic compared\n to previous years.'
                '\n\n    By systematically examining these factors, it offers valuable\n insights into the complex interplay of variables impacting\n population growth.This comprehensive analysis helps in \n understanding the intricate relationships and potential drivers \n that contribute to the fluctuations and trends observed in \n populations worldwide.', ha='left',fontsize=12,color='#d7e6ed', fontfamily='Times New Roman',bbox=dict(facecolor='black',edgecolor='white', alpha=0.5))

plt.figtext(1.02,0.92,'Student Name : Mohammed Nihad Kaipalli\nStudent ID : 22081746',ha='left',fontsize=15,color='#d7e6ed', fontfamily='Rockwell',bbox=dict(facecolor='black',edgecolor='white', alpha=0.5))
plt.tight_layout(rect=[0,0.03,1,0.95])

plt.savefig('22081746.png', dpi=300, bbox_inches='tight')






