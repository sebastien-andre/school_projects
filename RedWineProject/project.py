# Reading and Cleaning CSV Dataset
import pandas as pd
df = pd.read_csv('winequality-red.csv', sep = ';')
data_columns = ['Fixed Acidity', 'Volatile Acidity', 'Citric Acid', 'Residual Sugar',
                'Chlorides', 'Free Sulfur Dioxide', 'Total Sulfur Dioxide', 'Density',
                'pH', 'Sulphates', 'Alcohol', 'Quality']
df.columns = data_columns
df

# Calculating Statistics
import numpy as np

red_wine_stats = df.apply([np.mean, np.median, np.var, np.std, np.min, np.max])
red_wine_stats.to_csv('Red_Wine_Statistics.csv',  float_format='%.3f')
red_wine_stats

# Visualizing the Data
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#   Density vs Alcohol
fig1, ax1 = plt.subplots()
density_alcohol = df[['Density', 'Alcohol', 'Quality']].copy().sort_values('Density')
levels1, categories1 = pd.factorize(density_alcohol['Quality'])
colors1 = [plt.cm.tab10(i) for i in levels1]
handles1 = [patches.Patch(color=plt.cm.tab10(i), label=c) for i, c in enumerate(categories1)]
ax1.scatter(density_alcohol['Density'], density_alcohol['Alcohol'], c=colors1)
ax1.set_xlabel('Density')
ax1.set_ylabel('Alcohol')
ax1.set_title('Density vs Alcohol in Red Wine')
ax1.legend(handles=handles1,  title='Quality', loc=2)
ax1.grid()
fig1.savefig('Density_vs_Alcohol_in_Red_Wine.png')

#   Free Sulfur Dioxide vs Total Sulfur Dioxide
fig2, ax2 = plt.subplots()
sulfurs = df[['Free Sulfur Dioxide', 'Total Sulfur Dioxide', 'Quality']].copy().sort_values('Free Sulfur Dioxide')
levels2, categories2 = pd.factorize(sulfurs['Quality'])
colors2 = [plt.cm.tab10(i) for i in levels2]
handles2 = [patches.Patch(color=plt.cm.tab10(i), label=c) for i, c in enumerate(categories2)]
ax2.scatter(sulfurs['Free Sulfur Dioxide'], sulfurs['Total Sulfur Dioxide'], c=colors2)
ax2.set_xlabel('Free Sulfur Dioxide')
ax2.set_ylabel('Total Sulfur Dioxide')
ax2.set_title('Free Sulfur Dioxide vs Total Sulfur Dioxide in Red Wine')
ax2.legend(handles=handles2,  title='Quality', loc=2)
ax2.grid()
fig2.savefig('Free_Sulfur_Dioxide_vs_Total_Sulfur_Dioxide_in_Red_Wine.png')

#   Residual Sugar vs Density
fig3, ax3 = plt.subplots()
sugar_density = df[['Residual Sugar', 'Density', 'Quality']].copy().sort_values('Residual Sugar')
levels3, categories3 = pd.factorize(sugar_density['Quality'])
colors3 = [plt.cm.tab10(i) for i in levels3]
handles3 = [patches.Patch(color=plt.cm.tab10(i), label=c) for i, c in enumerate(categories3)]
ax3.scatter(sugar_density['Residual Sugar'], sugar_density['Density'], c=colors3)
ax3.set_xlabel('Residual Sugar')
ax3.set_xscale('log')
ax3.set_ylabel('Density')
ax3.set_title('Residual Sugar vs Density in Red Wine')
ax3.legend(handles=handles3,  title='Quality', loc=2)
ax3.grid()
fig3.savefig('Residual_Sugar_vs_Density_in_Red_Wine.png')

#   pH vs Alcohol
fig4, ax4 = plt.subplots()
ph_alcohol = df[['pH', 'Alcohol', 'Quality']].copy().sort_values('pH')
levels4, categories4 = pd.factorize(df['Quality'])
colors4 = [plt.cm.tab10(i) for i in levels4]
handles4 = [patches.Patch(color=plt.cm.tab10(i), label=c) for i, c in enumerate(categories4)]
ax4.scatter(ph_alcohol['pH'], ph_alcohol['Alcohol'], c=colors4)
ax4.set_xlabel('pH')
ax4.set_ylabel('Alcohol')
ax4.set_title('pH vs Alcohol in Red Wine')
ax4.legend(handles=handles4,  title='Quality', loc=2)
ax4.grid()
fig4.savefig('pH_vs_Alcohol_in_Red_Wine.png')

