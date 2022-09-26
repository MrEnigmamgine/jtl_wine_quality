import matplotlib.pyplot as plt
import seaborn as sns

def abv_boxen_by_quality(df):
    plt.figure(figsize=[10,5])
    sns.boxenplot(data=df, x='quality', y='alcohol')
    plt.title('%ABV is most important variable to consider when making a wine.')
    plt.show()