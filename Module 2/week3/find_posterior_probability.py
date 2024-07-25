import pandas as pd
import numpy as np
df = pd.read_excel('Book1.xlsx', keep_default_na=False)


# Cach 1
def find_posterior_probability(df, c: str, events: list):
    filtered = df[df['Class'] == c]
    res = len(filtered)/len(df)
    cur_col = 0
    print(f'Class: {c}')
    for event in events:

        res *= len(filtered[filtered[filtered.columns[cur_col]]
                   == event])/len(filtered)
        print(
            f'current col: {filtered.columns[cur_col]}, {len(filtered[filtered[filtered.columns[cur_col]] == event])}')
        cur_col += 1
    print(res)
    return res


cs = ['On Time', 'Late', 'Very Late', 'Cancelled']

for c in cs:
    find_posterior_probability(df, c, ['Weekday', 'Winter', 'High', 'Heavy'])


# Cach 2: lam theo thay ...
def create_train_data():
    return np.array([['Sunny', 'Hot', 'High', 'Weak', 'no'],
                     ['Sunny', 'Hot', 'High', 'Strong', 'no'],
                     ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
                     ['Rain', 'Mild', 'High', 'Weak', 'yes'],
                     ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
                     ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
                     ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
                     ['Overcast', 'Mild', 'High', 'Weak', 'no'],
                     ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
                     ['Rain', 'Mild', 'Normal', 'Weak', 'yes']], dtype='<U8')


train_data = create_train_data()


def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    prior_probability[0] = np.mean(train_data[:, -1] == 'no')
    prior_probability[1] = 1 - prior_probability[0]
    return prior_probability


def compute_conditional_probability(train_data):
    conditional_probability = [[], []]
    list_x_name = []
    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
    # your code here ********************
    for i in range(len(list_x_name)):
        x_conditional_probability_no = []
        x_conditional_probability_yes = []
        filtered_no = train_data[train_data[:, -1] == 'no']
        filtered_yes = train_data[train_data[:, -1] == 'yes']
        for j in list_x_name[i]:
            proba_no = np.mean(filtered_no[:, i] == j)
            proba_yes = np.mean(filtered_yes[:, i] == j)
            x_conditional_probability_no.append(proba_no)
            x_conditional_probability_yes.append(proba_yes)
        conditional_probability[0].append(x_conditional_probability_no)
        conditional_probability[1].append(x_conditional_probability_yes)
    return conditional_probability, list_x_name


conditional_probability, list_x_name = compute_conditional_probability(
    train_data)


def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]


x1 = get_index_from_value("Sunny", list_x_name[0])
print("P( ’Outlook’= ’ Sunny ’| Play Tennis ’= ’Yes ’) = ",
      np.round(conditional_probability[1][0][x1], 2))


def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probability(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)

    return prior_probability, conditional_probability, list_x_name


prior_probability, conditional_probability, list_x_name = train_naive_bayes(
    train_data)


def prediction_play_tennis(name, list_x_name, prior_probability, conditional_probability):

    x1 = get_index_from_value(name[0], list_x_name[0])
    x2 = get_index_from_value(name[1], list_x_name[1])
    x3 = get_index_from_value(name[2], list_x_name[2])
    x4 = get_index_from_value(name[3], list_x_name[3])

    index = [x1, x2, x3, x4]

    p0 = 0
    p1 = 0

    # your code here ***********************
    p0 += prior_probability[0]
    p1 += prior_probability[1]

    col = 0
    for i in index:
        p0 *= conditional_probability[0][col][i]
        p1 *= conditional_probability[1][col][i]
        col += 1

    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred


pred = prediction_play_tennis(['Sunny', 'Cool', 'High', 'Strong'],
                              list_x_name, prior_probability, conditional_probability)
if (pred):
    print("Ad should go!")
else:
    print("Ad should not go!")
