import os
import glob
import pandas as pd

# Получаем список всех csv файлов в папке "Wallets"
path = os.path.join(os.path.dirname(__file__), 'Wallets', '*.csv')
files = glob.glob(path)

# Создаем пустой датафрейм для объединения данных
df = pd.DataFrame()

# Объединяем все файлы в один датафрейм
for file in files:
    temp_df = pd.read_csv(file)
    df = pd.concat([df, temp_df])

# Сохраняем результат в файл "merged.csv"
df.to_csv('merged.csv', index=False)