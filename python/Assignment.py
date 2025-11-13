# تكليف من درس 1 الى 10
# تكليف الاول
#قم بإنشاء ملف جديد لتبدأ كتابة الكود فيه ثم في أعلى الملف قم بكتابة Multiple Line Comment توصف فيه الملف ويمكنك كتابة ما تريد, لا توجد مشكلة
#---------
#التكليف 02
#قم بإنشاء ثلاث متغيرات تحتوي على إسمك وسنك وبلدك, ويكون نوعهم String
name = "Najat"
age = "00"
country = "Eritrea"
#قم بطباعة القيم الموجودة في المتغيرات السابقة في ثلاث أسطر تحت بعضهم وقبلهم اسم يعبر عن المتغيرات المطلوب طباعة ما في ال Output التالي بنفس الشكل\
#"Name: Osama"
#"Age: 38"
#"Country: Egypt"
print("Name: " + name)
print("Age: " + age)
print("Country: " + country)
#التكليف 04
#قم بعمل Concatenate للمتغيرات مع بعض الكلمات لتخرج بهذه الرسالة الموجودة في ال Output التالي
#"Hello, My Name Is Osama And Iam 38 Years Old and I Live in Egypt."
print("Hello, My Name Is " + name + " And Iam " + age + " Years Old and I Live in " + country + ".")
#التكليف  5
#قم بطباعة نوع كل متغير من المتغيرات التي أنشأناها في سطر منفصل ليظهر لنا ال Output التالي
#<class 'str'>
#<class 'str'>
#<class 'str'>
print(type(name))
print(type(age))
print(type(country))
#تكاليف من الدروس 11 الى 18
#التكليف 01 
#قم بإنشاء ثلاث متغيرات عبارة عن اسمك وسنك وبلدك ثم قم بطباعة الرسالة التالية مع عمل Concatenate للمتغيرات 
# مع العلامات والكلمات التالية لتحصل على نفس الرسالة في النهاية, يجب عليك إظهار الرسالة كما هي بجميع العلامات الموجودة بنفس الترتيب والمسافات
#"Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt
name = "Najat"
age = "00"
country = "Eritrea"
print("Hello '" + name + "', How You Doing \\ \"\"\" Your Age Is \"" + age + "\"\" + And Your Country Is: " + country)
#التكليف 02 
#قم بطباعة نفس الرسالة السابقة كما هي ولكن على أكثر من سطر, شاهد ال Output المطلوب
#"Hello 'Osama', How You Doing \
#""" Your Age Is "38"" +
#And Your Country Is: Egypt
print("\"Hello '" + name + "', How You Doing \\ \n\"\"\" Your Age Is \"" + age + "\"\" + \nAnd Your Country Is: " + country)
#التكليف 03 
#قم بعمل متغير name وبداخله القيمة “Elzero” ثم عن طريق ال Indexing + Slicing قم بجلب الحرف الثاني في اول سطر والحرف الثالث في ثاني سطر والحرف الأخير في السطر الثالث, يجب عليك جلب الحرف بطريقة دايناميكية حيث أن الكلمة يمكن أن تتغير, شاهد المثال لترى المطلوب
name = 'Elzero'
# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"
print('Second Letter Is "' + name[1] + '"') #هنا جلبنا الحرف الثاني
print('Third Letter Is "' + name[2] + '"')  #هنا جلبنا الحرف الثالث
print('Last Letter Is "' + name[5] + '"') #هنا جلبنا الحرف الاخير
#التكليف 04
#سوف نستعمل ما سبق ولكن سوف نستخرج أكثر من حرف وليس حرف واحد, يجب عليك كتابة ال Code لتخرج النتيجة كما في المثال التالي
# Needed Output
# "lze"
# "Ezr"
# "rzE"
name = 'Elzero'

print('"'+ name[1:4] + '" ')   # "lze"  -> أحصل على الحروف من الفهرس 1 إلى 3
print( '"'+ name[0::2] + '" ' )  # "Ezr"  -> ابدأ من الفهرس 0 وخذ كل حرفين (step=2)
print( '"'+ name[4::-2] + '" ') # "rzE"  -> ابدأ من الفهرس 4 وارجع للخلف بخطوتين
#التكليف 05
#قم بإزالة العلامات الزائدة من الكلمة لتتبقى الكلمة فقط, شاهد المثال لترى الفكرة
name = "#@#@Elzero#@#@"

# Needed Output
# Elzero
clean_name = name.strip("#@")
print(clean_name)
#التكليف 06
#قم بعمل متغير فيه أي رقم تريده ونوعه String ثم قم بوضع أصفار قبل أي رقم يتم وضعه كقيمة للمتغير على أن لا يزيد عرض الأعداد عن 4 أعداد فمثلا ال 20 تكون 0020 وال 199 تكون 0199 وال 1200 تكون كما هي 1200, شاهد المطلوب في المثال التالي
#num = "9"
#num = "15"
#num = "130"
#num = "950"
#num = "1500"

# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500
num1 = "9"
print(num1.zfill(4))
num2 = "15"
print(num2.zfill(4))
num3 = "130"
print(num3.zfill(4))
num4 = "950"
print(num4.zfill(4))
num5 = "1500"
print(num5.zfill(0))
#التكليف 07

#قم بوضع علامات @ قبل أي String يتم إعطائك له على ألا يزيد عدد الأحرف عن 20, شاهد المثال لترى الفكرة
name_one = "Osama"
name_two = "Osama_Elzero"

# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))
#التكليف 08
#قم بتحويل الحروف الكبيرة لحروف صغيرة والعكس, شاهد المثال لترى الفكرة
name_one = "OSamA"
name_two = "osaMA"

# Needed Output
# osAMa
# OSAma
print(name_one.swapcase())
print(name_two.swapcase())
#التكليف 09 
#قم بحساب كم مرة تكررت كلمة Love في ال String الذي سوف يتم إعطائه لك, شاهد المثال لتفهم
msg = "I Love Python And Although Love Elzero Web School"
# Needed Output
# 2
print(msg.count("Love"))
#التكليف 10
#قم بطابعة ال Position الخاص بالحرف z في كلمة Elzero, شاهد المثال لتفهم المطلوب
name = "Elzero"

# Needed Output
# 2
print(name.index("z"))
#التكليف 11
#قم بإستبدال الكلمة التالية “<3" بكلمة Love مرة واحدة فقط في الجملة التي سوف يتم إعطائها لك. شاهد المثال
msg = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although <3 Elzero Web School
print(msg.replace("<3", "Love", 1))
#-----------------------------------------------
