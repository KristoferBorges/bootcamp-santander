import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel('Netflix.xlsx')

eixo_x = df['Localização'].value_counts().sort_index().keys()
curtidas_por_localizacao = df.groupby('Localização')['Curtidas'].sum()
eixo_y = [curtidas_por_localizacao[localizacao] for localizacao in eixo_x]

print(eixo_x)
print(eixo_y)

plt.bar(eixo_x, eixo_y)
plt.xticks(rotation=70)
plt.ylabel('Curtidas')
plt.xlabel('Localização')
plt.title('Curtidas por Localização')
plt.tight_layout()

plt.show()
