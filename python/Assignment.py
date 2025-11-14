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
#تكليفات الدروس من 19 إلى 20
#التكليف 1
#قم بطباعة جميع أنواع ال Numbers كل واحد في سطر منفصل
print(type(10))
print(type(10.1))
print(type(10+10j))
#التكليف 2
#قم بطباعة الجزء ال Imaginary من ال Complex Number التالي “1+2j” في السطر الأول وفي السطر الثاني قم بطباعة جزء ال Real
1+2j
# Print Imaginary Part Here
# Print Real Part Here
print(1+2j.imag)
print(1+2j.real)
#التكليف 3
#قم بتحويل الرقم 10 ل Floating Point Number مع وضع عشر أرقام بعد العلامة العشرية
num = 10
# Needed Ouput
# 10.0000000000
# تحويل إلى Float وعرض 10 أرقام بعد العلامة العشرية
print(f"{float(num):.10f}")
#التكليف 4
#قم بتحويل الرقم 159.650 ل Integer ثم قم بطباعته في أول سطر ثم في تاني سطر تقوم بطباعة نوعه والـاكد أنه Integer
num = 159.650

# Needed Output
# 159
# <class 'int'>
print(int(num))
print(type(num))  #    <class 'float'>  طلع  مو <class 'int'>

#التكليف 5
#قم بوضع العلامة الحسابية المناسبة بدل علامة الإستفهام لتكون النتيجة صحيحة في الأمثلة التالية
#100 - 115 = -15
print(100 - 115) # -15
#50 * 30 = 1500
print(50 * 30) # 1500
#21 % 4 = 1
print(21 % 4) # 1
#110 // 11 = 10
print(110 // 11)
#97 ? 20 = 4
print(97 // 20) # 4

#تكليفات الدروس من  21 إلى 23
#التكليف 1
#قم بعمل قائمة List تحتوي على أسماء أصدقائك ويكون فيها على الأقل 5 أسماء والمطلوب في السطر الأول والثاني طباعة إسم أول صديق في القائمة بطريقتين ثم في السطر الثالث والرابع تقوم بطباعة إسم آخر صديق في القائمة بطريقتين
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two
print(friends[0])# Osama
print(friends[-5])# Osama
print(friends[4])# Mahmoud
print(friends[-1])# Mahmoud
#التكليف 2
#من القائمة السابقة قم بطباعة الأسماء الفردية في السطر الأول وفي السطر الثاني قم بطباعة الأسماء الزوجية
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"
print(f'"{friends[0]}", "{friends[2]}", "{friends[4]}"')
print(f'"{friends[1]}", "{friends[3]}"')
#التكليف 3
#قم بطباعة مجموعة الأسماء رقم 2 و 3 و 4 في السطر الأول ثم الأسم الأخير والذي قبله في السطر الثاني مع العلم أن ال Code يجب أن يعمل في حالة قمنا بتغيير عدد العناصر الموجودة في القائمة
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"
print(f'"{friends[1]}", "{friends[2]}", "{friends[3]}"')
print(f'"{friends[3]}", "{friends[4]}"')

#التكليف 4
#قم بتحديث آخر أسمين في القائمة لإسم “Elzero”
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]
friends[-1] = "Elzero" # تحديث آخر أسمين في القائمة
friends[-2] = "Elzero" # تحديث آخر أسمين في القائمة
print(friends)

#التكليف 5
#قم بإضافة إسم من أصدقائك للقائمة في أول القائمة أولا ثم قم بإضافة إسم آخر في نهاية القائمة
friends = ["Osama", "Ahmed", "Sayed"]

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.insert(0, "Nasser") # إضافة اسم في بداية القائمة
friends.append("Salem") # إضافة اسم في نهاية القائمة
print(friends)

#التكليف 06
#قم بحذف أول إسمين من القائمة ثم بعدها في سطر آخر قم بإزالة آخر إسم من القائمة
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]
friends.remove("Nasser") # حذف أول إسمين من القائمة 
friends.remove("Osama") # حذف أول إسمين من القائمة
print(friends)
friends.pop() # إزالة آخر إسم من القائمة
print(friends) 
#التكليف 7
#قم بإنشاء قائمتين آخريين فيهم المزيد من الأصدقاء ثم قم بضمهم على أول قائمة لتخرج بالقائمة النهائية فيها جميع الأصدقاء
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)

#التكليف8
#قم بترتيب الأسماء في القائمة في السطر الأول من A إلى Z وفي السطر الثاني من Z إلى A
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']
friends.sort() # ترتيب الأسماء في القائمة من A إلى Z
print(friends)
friends.sort(reverse=True) # ترتيب الأسماء في القائمة من Z إلى A
print(friends)
#التكليف9
#قم بحساب عدد الأسماء الموجودة في القائمة
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# Needed Output
# 6
print(len(friends)) # طباعة عدد الأسماء الموجودة في القائمة


#التكليف 10
#قم بعمل قائمة فيها لغات البرمجة المشهورة وداخلها قائمة فرعية فيها أسماء أطر عمل مشهورة ثم في السطر الأول قم بطباعة إسم اول اطار عمل في القائمة الفرعية وفي السطر الثاني إسم آخر إطار عمل في القائمة الفرعية مع مراعاة أن القائمة الفرعية يمكن أن تزيد ولكنها دائما آخر عنصر في القائمة الرئيسية
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

# Needed Output
# Django
# Web
print(technologies[4][0])
print(technologies[4][2])
#-----------------------------------------------
#تكليفات الدروس من 24 إلى 25
#التكليف 1





