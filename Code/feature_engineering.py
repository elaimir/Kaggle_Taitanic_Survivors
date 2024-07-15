import pandas as pd
from sklearn.preprocessing import StandardScaler

# تابعی برای آماده‌سازی ویژگی‌ها از داده‌های آموزشی و تست
def prepare_features(train, test):
    # انتخاب ویژگی‌های مورد نظر
    features = ["Pclass", "Sex", "SibSp", "Parch"]
    
    # ایجاد داده‌های دسته‌بندی شده (one-hot encoded)
    X_train = pd.get_dummies(train[features])
    X_test = pd.get_dummies(test[features])
    
    # اطمینان از هم‌ترازی ستون‌ها در داده‌های آموزشی و تست
    X_train, X_test = X_train.align(X_test, join='left', axis=1)
    
    # نرمال‌سازی داده‌ها
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test
