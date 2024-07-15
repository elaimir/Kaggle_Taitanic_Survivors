from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, roc_auc_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# تابعی برای ارزیابی عملکرد مدل با استفاده از معیارهای مختلف
def evaluate_model(model, X, y):
    # تقسیم داده‌ها به دو قسمت آموزش و تست
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    # آموزش مدل روی داده‌های آموزشی
    model.fit(X_train, y_train)
    
    # پیش‌بینی برچسب‌ها برای داده‌های تست
    y_pred = model.predict(X_test)
    
    # محاسبه دقت مدل
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")
    
    # گزارش دقیقی از معیارهای دیگر ارزیابی
    print(classification_report(y_test, y_pred))
    
    # ماتریس اشتباهات
    print(confusion_matrix(y_test, y_pred))

    # محاسبه نمودار ROC و نمودار AUC
    y_pred_prob = model.predict_proba(X_test)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
    roc_auc = roc_auc_score(y_test, y_pred_prob)

    # نمایش نمودار ROC
    plt.figure()
    plt.plot(fpr, tpr, label=f'ROC curve (area = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc='lower right')
    plt.show()
