import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset Titanic
titanic = sns.load_dataset('titanic')

# Calcular as quantidades de sobreviventes e não sobreviventes por sexo
quantidade_mulheres = titanic[titanic['sex'] == 'female'].shape[0]
quantidade_mulheres_vivas = titanic[(titanic['sex'] == 'female') & (titanic['survived'] == 1)].shape[0]

quantidade_homens = titanic[titanic['sex'] == 'male'].shape[0]
quantidade_homens_vivos = titanic[(titanic['sex'] == 'male') & (titanic['survived'] == 1)].shape[0]

# Calcular as proporções
proporcao_mulheres_vivas = quantidade_mulheres_vivas / quantidade_mulheres

proporcao_homens_vivos = quantidade_homens_vivos / quantidade_homens

# Exibir os resultados
eixo_x = ['Mulheres', 'Homens']
eixo_y = [proporcao_mulheres_vivas, proporcao_homens_vivos]

print(eixo_x)
print(eixo_y)

plt.bar(eixo_x, eixo_y)
plt.ylabel('Proporção de Sobreviventes')
plt.xlabel('Sexo')
plt.title('Proporção de Sobreviventes por Sexo')
plt.tight_layout()

print(titanic.head())
plt.show()


