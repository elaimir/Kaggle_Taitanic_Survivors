import pandas as pd
from scipy import stats
from scipy.stats import chi2_contingency

# تابع برای محاسبه آماره‌های آماری مختلف برای داده‌ها
def calculate_statistics(data):
    # محاسبه تست t برای مقایسه میانگین سن بازماندگان و غیربازماندگان
    survived_age = data[data['Survived'] == 1]['Age']
    not_survived_age = data[data['Survived'] == 0]['Age']
    t_stat, p_value = stats.ttest_ind(survived_age.dropna(), not_survived_age.dropna())
    print(f"t-statistic: {t_stat}, p-value: {p_value}")

    # محاسبه میانگین سن بازماندگان و غیربازماندگان
    mean_survived_age = survived_age.mean()
    mean_not_survived_age = not_survived_age.mean()
    print(f"Mean age of survivors: {mean_survived_age}")
    print(f"Mean age of non-survivors: {mean_not_survived_age}")

    # تبدیل متغیر جنسیت به عددی و محاسبه جدول توام متغیرهای بازماندگان بر اساس جنسیت
    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
    contingency_table = pd.crosstab(data['Survived'], data['Sex'])

    # انجام تست chi-square برای ارزیابی ارتباط بین بازماندگی و جنسیت
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    print(f"Chi2 Statistic: {chi2}")
    print(f"P-value: {p}")

    # محاسبه درصد بازماندگی بر اساس جنسیت
    total_men = data[data['Sex'] == 0]
    total_women = data[data['Sex'] == 1]
    survived_men = total_men[total_men['Survived'] == 1]
    survived_women = total_women[total_women['Survived'] == 1]

    men_survived_percent = (len(survived_men) / len(total_men)) * 100
    women_survived_percent = (len(survived_women) / len(total_women)) * 100
    print(f"Percentage of male survivors: {men_survived_percent:.2f}%")
    print(f"Percentage of female survivors: {women_survived_percent:.2f}%")
