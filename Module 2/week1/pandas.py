import pandas as pd
df = pd.read_csv('.Module 2\week1\advertising.csv')

# 15
df[df['Sales'] == max(df['Sales'])]

# 16
df['TV'].mean()

# 17
len(df[df['Sales'] >= 20])

# 18
df[df['Sales'] >= 15]['Radio'].mean()

# 19
df[df['Newspaper'] > df['Newspaper'].mean()]['Sales'].sum()

# 20
avg = df['Sales'].mean()


def scoring(sales, avg):
    if sales > avg:
        return 'Good'
    elif sales == avg:
        return 'Average'
    else:
        return 'Bad'


df['Sales'].apply(lambda row: scoring(row, avg))[7:10]

# 21
df['distance_to_avg'] = abs(df['Sales'] - avg)
closest_to_avg = list(
    df[df['distance_to_avg'] == min(df['distance_to_avg'])]['Sales'])[0]
df['Sales'].apply(lambda row: scoring(row, closest_to_avg))[7:10]
