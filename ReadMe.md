تحلیل نجات یافتگان کشتی تایتانیک
مقدمه

هدف این پروژه تحلیل داده‌های مربوط به مسافران کشتی تایتانیک است. داده‌ها شامل اطلاعات جمعیتی، اجتماعی-اقتصادی و وضعیت نجات یافتگی مسافران هستند. دو مجموعه داده موجود است: train.csv و test.csv.
•	train.csv شامل جزئیات مسافران (۸۹۱ نفر) به همراه اطلاعاتی است که نشان می‌دهد آیا نجات یافته‌اند یا خیر.
•	test.csv شامل اطلاعات مشابهی است اما وضعیت نجات یافتگی مسافران را فاش نمی‌کند. هدف این است که با استفاده از الگوهایی که در داده‌های train.csv پیدا می‌شود، وضعیت نجات یافتگی مسافران در test.csv پیش‌بینی شود.
مراحل پروژه


1.	بارگذاری و پاکسازی داده‌ها:
o	بارگذاری داده‌ها از فایل‌های CSV.
o	پاکسازی داده‌ها از مقادیر گمشده و نادرست.
o	تبدیل متغیرهای دسته‌بندی به متغیرهای عددی.

2.	تحلیل اکتشافی داده‌ها:
o	بررسی توزیع متغیرهای مختلف.
o	تحلیل روابط بین متغیرها.
o	انجام آزمون‌های آماری برای بررسی تفاوت‌های معنی‌دار بین گروه‌های مختلف.

3.	مدل‌سازی و انتخاب مدل:
o	استفاده از مدل‌های مختلف ماشین‌ یادگیری برای پیش‌بینی وضعیت نجات یافتگی مسافران.
o	ارزیابی مدل‌ها با استفاده از کراس‌-والیدیشن.
o	انتخاب بهترین مدل بر اساس دقت و سایر معیارها.

4.	پیش‌بینی و تولید خروجی:
o	آموزش مدل نهایی بر روی کل داده‌های آموزش.
o	پیش‌بینی وضعیت نجات یافتگی مسافران در داده‌های تست.
o	ذخیره نتایج پیش‌بینی شده در فایل CSV برای ارسال به کگل.

ارزیابی


هدف این پروژه پیش‌بینی وضعیت نجات یافتگی مسافران کشتی تایتانیک است. برای هر مسافر در مجموعه داده‌های تست، باید مقدار ۰ یا ۱ برای متغیر Survived پیش‌بینی شود.


معیار ارزیابی

امتیاز شما درصد مسافرانی است که وضعیت نجات یافتگی آنها را به درستی پیش‌بینی کرده‌اید. این معیار به عنوان دقت (Accuracy) شناخته می‌شود.

فرمت فایل ارسال
فایل ارسال باید شامل دقیقاً ۴۱۸ ردیف به همراه یک سطر هدر باشد. فایل باید دارای دو ستون باشد:
•	PassengerId (ترتیب به هر نحوی می‌تواند باشد)
•	Survived (پیش‌بینی‌های باینری: ۱ برای نجات یافته و ۰ برای فوت شده)
مثال:

python
Copy code
PassengerId,Survived
892,0
893,1
894,0
...


پوشه‌ها و فایل‌ها
•	data/ : شامل فایل‌های داده‌ها (train.csv و test.csv).
•	notebook/ : شامل نوت‌بوک‌های Jupyter برای تحلیل اکتشافی و مدل‌سازی.
•	src/ : شامل کدهای منبع پروژه به صورت ماژولار و سازمان‌یافته.
•	main.py : فایل اصلی برای اجرای کل پروژه.
•	README.md : توضیحات پروژه (این فایل).
•	requirements.txt : شامل کتابخانه‌های مورد نیاز پروژه.


استفاده از کدها
کدهای موجود در پوشه src شامل توابع و کلاس‌هایی هستند که برای مراحل مختلف پروژه استفاده می‌شوند. شما می‌توانید با استفاده از فایل main.py کل پروژه را اجرا کنید و نتایج نهایی را تولید کنید.
________________________________________
این فایل راهنما به شما کمک می‌کند تا به راحتی با ساختار پروژه آشنا شده و بتوانید به درستی از کدها و داده‌ها استفاده کنید. اگر سوالی دارید یا به راهنمایی بیشتری نیاز دارید، لطفاً در بخش Issues پروژه در گیت‌هاب مطرح کنید.
4o
