### تحلیل نجات یافتگان کشتی تایتانیک

#### مقدمه

هدف این پروژه تحلیل داده‌های مربوط به مسافران کشتی تایتانیک است. داده‌ها شامل اطلاعات جمعیتی، اجتماعی-اقتصادی و وضعیت نجات یافتگی مسافران هستند. دو مجموعه داده موجود است: train.csv و test.csv.
- **train.csv** شامل جزئیات مسافران (۸۹۱ نفر) به همراه اطلاعاتی است که نشان می‌دهد آیا نجات یافته‌اند یا خیر.
- **test.csv** شامل اطلاعات مشابهی است اما وضعیت نجات یافتگی مسافران را فاش نمی‌کند. هدف این است که با استفاده از الگوهایی که در داده‌های train.csv پیدا می‌شود، وضعیت نجات یافتگی مسافران در test.csv پیش‌بینی شود.

#### مراحل پروژه

1. **بارگذاری و پاکسازی داده‌ها:**
   - بارگذاری داده‌ها از فایل‌های CSV.
   - پاکسازی داده‌ها از مقادیر گمشده و نادرست.
   - تبدیل متغیرهای دسته‌بندی به متغیرهای عددی.

2. **تحلیل اکتشافی داده‌ها:**
   - بررسی توزیع متغیرهای مختلف.
   - تحلیل روابط بین متغیرها.
   - انجام آزمون‌های آماری برای بررسی تفاوت‌های معنی‌دار بین گروه‌های مختلف.

3. **مدل‌سازی و انتخاب مدل:**
   - استفاده از مدل‌های مختلف ماشین‌ یادگیری برای پیش‌بینی وضعیت نجات یافتگی مسافران.
   - ارزیابی مدل‌ها با استفاده از کراس‌-والیدیشن.
   - انتخاب بهترین مدل بر اساس دقت و سایر معیارها.

4. **پیش‌بینی و تولید خروجی:**
   - آموزش مدل نهایی بر روی کل داده‌های آموزش.
   - پیش‌بینی وضعیت نجات یافتگی مسافران در داده‌های تست.
   - ذخیره نتایج پیش‌بینی شده در فایل CSV برای ارسال به کگل.

#### ارزیابی

هدف این پروژه پیش‌بینی وضعیت نجات یافتگی مسافران کشتی تایتانیک است. برای هر مسافر در مجموعه داده‌های تست، باید مقدار ۰ یا ۱ برای متغیر Survived پیش‌بینی شود.

#### معیار ارزیابی

امتیاز شما درصد مسافرانی است که وضعیت نجات یافتگی آنها را به درستی پیش‌بینی کرده‌اید. این معیار به عنوان دقت (Accuracy) شناخته می‌شود.

#### فرمت فایل ارسال

فایل ارسال باید شامل دقیقاً ۴۱۸ ردیف به همراه یک سطر هدر باشد. فایل باید دارای دو ستون باشد:
- PassengerId (ترتیب به هر نحوی می‌تواند باشد)
- Survived (پیش‌بینی‌های باینری: ۱ برای نجات یافته و ۰ برای فوت شده)

مثال:

```csv
PassengerId,Survived
892,0
893,1
894,0
...
```

#### پوشه‌ها و فایل‌ها
- `data/` : شامل فایل‌های داده‌ها (train.csv و test.csv).
- `notebook/` : شامل نوت‌بوک‌های Jupyter برای تحلیل اکتشافی و مدل‌سازی.
- `src/` : شامل کدهای منبع پروژه به صورت ماژولار و سازمان‌یافته.
- `main.py` : فایل اصلی برای اجرای کل پروژه.
- `README.md` : توضیحات پروژه (این فایل).
- `requirements.txt` : شامل کتابخانه‌های مورد نیاز پروژه.

#### استفاده از کدها

کدهای موجود در پوشه `src` شامل توابع و کلاس‌هایی هستند که برای مراحل مختلف پروژه استفاده می‌شوند. شما می‌توانید با استفاده از فایل `main.py` کل پروژه را اجرا کنید و نتایج نهایی را تولید کنید.

### اضافه کردن کارهای آماری

در انتهای پروژه، تعدادی تحلیل‌های آماری اضافی انجام شده‌اند:
- محاسبه میانگین سنی مسافران نجات یافته و فوت شده.
- انجام آزمون t برای بررسی تفاوت میانگین سنین.
- محاسبه نسبت نجات یافتگان بر اساس جنسیت.
- انجام آزمون کای-دو برای بررسی رابطه بین جنسیت و نجات یافتگی.

### English Version

### Titanic Survival Analysis

#### Introduction

The goal of this project is to analyze the data of Titanic passengers. The data includes demographic, socio-economic, and survival status information of the passengers. There are two datasets: train.csv and test.csv.
- **train.csv** contains details of 891 passengers along with their survival status.
- **test.csv** contains similar information but does not reveal the survival status of the passengers. The aim is to predict the survival status of the passengers in test.csv using the patterns found in train.csv.

#### Project Steps

1. **Data Loading and Cleaning:**
   - Loading data from CSV files.
   - Cleaning data by handling missing and incorrect values.
   - Converting categorical variables to numerical ones.

2. **Exploratory Data Analysis (EDA):**
   - Analyzing the distribution of various variables.
   - Exploring relationships between variables.
   - Performing statistical tests to identify significant differences between different groups.

3. **Modeling and Model Selection:**
   - Using various machine learning models to predict the survival status of passengers.
   - Evaluating models using cross-validation.
   - Selecting the best model based on accuracy and other metrics.

4. **Prediction and Output Generation:**
   - Training the final model on the entire training dataset.
   - Predicting the survival status of passengers in the test dataset.
   - Saving the predicted results to a CSV file for submission to Kaggle.

#### Evaluation

The goal of this project is to predict the survival status of Titanic passengers. For each passenger in the test set, you must predict a 0 or 1 value for the Survived variable.

#### Evaluation Metric

Your score is the percentage of passengers you correctly predict. This is known as accuracy.

#### Submission File Format

The submission file must contain exactly 418 rows plus a header row. The file should have exactly two columns:
- PassengerId (sorted in any order)
- Survived (binary predictions: 1 for survived, 0 for deceased)

Example:

```csv
PassengerId,Survived
892,0
893,1
894,0
...
```

#### Folders and Files
- `data/` : Contains the data files (train.csv and test.csv).
- `notebook/` : Contains Jupyter notebooks for EDA and modeling.
- `src/` : Contains source code for the project, organized in a modular manner.
- `main.py` : The main script to run the entire project.
- `README.md` : Project documentation (this file).
- `requirements.txt` : Contains the required libraries for the project.

#### Using the Code

The code in the `src` folder includes functions and classes used in different stages of the project. You can run the entire project using the `main.py` script to generate the final results.

### Additional Statistical Analysis

At the end of the project, some additional statistical analyses were performed:
- Calculation of the mean age of survived and non-survived passengers.
- Performing a t-test to check the difference in mean ages.
- Calculation of survival percentages based on gender.
- Performing a chi-square test to check the relationship between gender and survival.

---

این فایل راهنما به شما کمک می‌کند تا به راحتی با ساختار پروژه آشنا شده و بتوانید به درستی از کدها و داده‌ها استفاده کنید. اگر سوالی دارید یا به راهنمایی بیشتری نیاز دارید، لطفاً در بخش Issues پروژه در گیت‌هاب مطرح کنید.




