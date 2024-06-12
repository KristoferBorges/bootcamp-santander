import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset Titanic
titanic = sns.load_dataset('titanic')

# mostrar o pairplot
sns.pairplot(titanic)
plt.show()