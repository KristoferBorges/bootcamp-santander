import seaborn as sns
import pandas as pd

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
print(f"Mulheres:")
print(f"Quantidade: {quantidade_mulheres}")
print(f"Vivas: {quantidade_mulheres_vivas} ({proporcao_mulheres_vivas:.2%})\n")

print(f"Homens:")
print(f"Quantidade: {quantidade_homens}")
print(f"Vivos: {quantidade_homens_vivos} ({proporcao_homens_vivos:.2%})")

if (quantidade_homens_vivos > quantidade_mulheres_vivas):
    print("\nOs homens sobreviveram mais do que as mulheres")
else:
    print("\nAs mulheres sobreviveram mais do que os homens")

