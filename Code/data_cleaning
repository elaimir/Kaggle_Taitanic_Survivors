import pandas as pd

# تابع clean_data برای تمیز کردن و آماده‌سازی داده‌های ورودی
def clean_data(df):
    # پر کردن مقادیر گمشده در ستون 'Age' با مقدار میانه
    df['Age'].fillna(df['Age'].median(), inplace=True)
    
    # پر کردن مقادیر گمشده در ستون 'Fare' با مقدار میانه
    df['Fare'].fillna(df['Fare'].median(), inplace=True)
    
    # پر کردن مقادیر گمشده در ستون 'Embarked' با مقدار مد
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    
    # حذف ستون‌های غیرضروری 'Cabin', 'Ticket', 'Name'
    df.drop(columns=['Cabin', 'Ticket', 'Name'], inplace=True)
    
    # تبدیل مقادیر دسته‌ای ستون 'Sex' به مقادیر عددی
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    
    # تبدیل مقادیر دسته‌ای ستون 'Embarked' به مقادیر دودویی (dummy variables)
    df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
    
    # بازگرداندن دیتافریم تمیز شده
    return df
