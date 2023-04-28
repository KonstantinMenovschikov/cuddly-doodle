import pandas as pd

# Чтение исходного файла
df = pd.read_csv('adress.csv')

# Поиск дубликатов
duplicates = df[df.duplicated()]

# Сохранение дубликатов в файл
duplicates.to_csv('duplicates.csv', index=False)

# Удаление дубликатов из исходного файла
df.drop_duplicates(inplace=True)

# Сохранение нового файла без дубликатов
df.to_csv('adress_no_duplicates.csv', index=False)