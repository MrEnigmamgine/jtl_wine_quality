import matplotlib.pyplot as plt
import seaborn as sns

def abv_boxen_by_quality(df):
    plt.figure(figsize=[10,5])
    sns.boxenplot(data=df, x='quality', y='alcohol')
    plt.title('%ABV is most important variable to consider when making a wine.')
    plt.show()

def not_us_legal(row):
    legal = True
    if row.total_sulfur_dioxide > 350: legal = False
    if row.type == 'red':
        if row.volatile_acidity > 1.4: legal = False
    else:
        if row.volatile_acidity > 1.5: legal = False
    return not legal

def not_eu_legal(row):
    legal = False
    sugar = row.residual_sugar
    so2 = row.total_sulfur_dioxide
    acetic = row.volatile_acidity
    if row.type == 'red':
        if acetic > 1.2: 
            return not legal
        if sugar < 5 and so2 > 150: 
            return not legal
        if 5 < sugar < 35 and so2 > 250: 
            return not legal
    else:
        if acetic > 1.08: 
            return not legal
        if sugar < 5 and so2 > 200: 
            return not legal
        if 5 < sugar < 35 and so2 > 250: 
            return not legal
        if 35 < sugar and so2 > 400: 
            return not legal
    return legal