import seaborn as sns
import matplotlib.pyplot as plt
import os

# ایجاد پوشه images در صورت عدم وجود
if not os.path.exists('images'):
    os.makedirs('images')

# بارگذاری داده‌ها
train_cleaned = pd.read_csv('traint.csv')
test_cleaned = pd.read_csv('testt.csv')

# مثال‌هایی از ذخیره نمودارها
sns.histplot(train_cleaned['Age'], kde=True)
plt.title('Age Distribution')
plt.savefig('images/age_distribution.png')
plt.close()

sns.histplot(train_cleaned['Fare'], kde=True)
plt.title('Fare Distribution')
plt.savefig('images/fare_distribution.png')
plt.close()

# تحلیل متغیرهای دسته‌بندی
sns.countplot(x='Pclass', data=train_cleaned)
plt.title('Passenger Class Distribution')
plt.savefig('images/passenger_class_distribution.png')
plt.close()

train_cleaned['Sex'] = train_cleaned['Sex'].map({0: 'male', 1: 'female'})
sns.countplot(x='Survived', hue='Sex', data=train_cleaned)
plt.title('Survival by Gender')
plt.savefig('images/survival_by_gender.png')
plt.close()

sns.barplot(x='Pclass', y='Fare', data=test_cleaned)
plt.title('Average Fare by Class')
plt.savefig('images/average_fare_by_class.png')
plt.close()

correlation_matrix = train_cleaned[['Age', 'Fare', 'Pclass']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('images/correlation_heatmap.png')
plt.close()

plt.scatter(x=train_cleaned['Age'], y=train_cleaned['Fare'])
plt.title('Scatter Plot')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.savefig('images/scatter_plot.png')
plt.close()

fare_by_pclass = train_cleaned.groupby('Pclass')['Fare'].sum()
fig, ax = plt.subplots()

wedges, texts, autotexts = ax.pie(fare_by_pclass, labels=fare_by_pclass.index, autopct='%1.1f%%', startangle=140)
ax.legend(wedges, fare_by_pclass.index, title="Pclass", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.title('Pie Chart')
plt.savefig('images/pie_chart.png')
plt.close()

sns.violinplot(x='Pclass', y='Age', data=train_cleaned)
plt.title('Violin Plot of Age by Class')
plt.savefig('images/violin_plot.png')
plt.close()

sns.stripplot(x='Pclass', y='Age', data=train_cleaned)
plt.title('Swarm Plot of Age by Class')
plt.savefig('images/swarm_plot.png')
plt.close()

correlation_matrix = train_cleaned[['Age', 'Fare', 'Pclass']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('images/correlation_heatmap_2.png')
plt.close()

sns.kdeplot(data=test_cleaned['Age'].dropna(), shade=True)
plt.title('KDE Plot of Age')
plt.savefig('images/kde_plot.png')
plt.close()
