import seaborn as sns
import matplotlib.pyplot as plt

# تابع برای رسم هیستوگرام برای اعمال مختلف
def plot_histograms(data, columns):
    for col in columns:
        sns.histplot(data[col], kde=True)
        plt.title(f'{col} Distribution')
        plt.show()

# تابع برای رسم نمودار تعداد اعضا برای داده‌های دسته‌ای
def plot_count(data, x, hue=None):
    sns.countplot(x=x, hue=hue, data=data)
    plt.title(f'{x} Count')
    plt.show()

# تابع برای رسم نمودار heatmap ارتباطات متغیرها
def plot_correlation_heatmap(data, columns):
    correlation_matrix = data[columns].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

# تابع برای رسم نمودارهای اضافی مانند Scatter plot، Pie chart، Violin plot و Swarm plot
def plot_additional(data):
    # Scatter plot
    plt.scatter(x=data['Age'], y=data['Fare'])
    plt.title('Scatter Plot')
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.show()

    # Pie chart
    fare_by_pclass = data.groupby('Pclass')['Fare'].sum()
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(fare_by_pclass, labels=fare_by_pclass.index, autopct='%1.1f%%', startangle=140)
    ax.legend(wedges, fare_by_pclass.index, title="Pclass", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.title('Pie Chart')
    plt.show()

    # Violin plot
    sns.violinplot(x='Pclass', y='Age', data=data)
    plt.title('Violin Plot of Age by Class')
    plt.show()

    # Swarm plot
    sns.stripplot(x='Pclass', y='Age', data=data)
    plt.title('Swarm Plot of Age by Class')
    plt.show()
