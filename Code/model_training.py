from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# تابعی برای پیدا کردن بهترین مقدار max_depth برای RandomForestClassifier
def find_best_max_depth(X, y, candidate_max_leaf_nodes):
    param_grid = {'max_depth': candidate_max_leaf_nodes}
    model = RandomForestClassifier(random_state=1)
    
    # استفاده از GridSearchCV برای پیدا کردن بهترین مقدار max_depth
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X, y)
    
    # بهترین مقدار max_depth
    best_max_depth = grid_search.best_params_['max_depth']
    return best_max_depth

# تابعی برای آموزش مدل با استفاده از بهترین مقدار max_depth و ارزیابی مدل‌ها
def train_model(X, y, best_max_depth):
    # تعریف مدل‌های مختلف برای ارزیابی
    models = {
        "Logistic Regression": LogisticRegression(),
        "Random Forest": RandomForestClassifier(max_depth=best_max_depth, random_state=1),
        "SVM": SVC(probability=True),
        "KNN": KNeighborsClassifier(),
        "Gradient Boosting": GradientBoostingClassifier()
    }

    best_model = None
    best_score = 0

    # ارزیابی مدل‌ها با استفاده از cross-validation
    for model_name, model in models.items():
        cv_scores = cross_val_score(model, X, y, cv=5)
        mean_score = cv_scores.mean()
        print(f"{model_name} - Accuracy: {mean_score:.4f} (+/- {cv_scores.std():.4f})")
        
        # ذخیره بهترین مدل بر اساس دقت
        if mean_score > best_score:
            best_score = mean_score
            best_model = model

    # آموزش بهترین مدل با استفاده از کل داده‌ها
    best_model.fit(X, y)
    return best_model
