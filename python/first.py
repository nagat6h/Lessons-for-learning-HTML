print("I LOVE Python")
print("I LOVE Programming")
# هذا # = علامة وصف 
# print("programming")   منع الكود من التنفيذ
print("programming") 
#--------------------------------------------------------------------
#تطبيقاتنا تحتوي على كود و بيانات
#الكود = الأسطر التي تكتبها لإدارة والتعامل مع هذه البيانات
# مثال بايثون:
print("Hello")
#لتنظيم البيانات نحتاج إلى تصنيفها (أرقام، نصوص، قيم منطقية)
# Num (أرقام) ⇒ عمر الطلاب، رقم هاتف الطالب، رواتب المعلمين
#مثال
age = 16
phone = 1551234567
salary = 5000
# String (نصوص) ⇒ أسماء الطلاب، أسماء المعلمين، أسماء الأحداث
#مثال
student_name = "Sara"
teacher_name = "Mr. Ali"
event_name = "Science Fair"

#Booleans (قيم منطقية) ⇒ هل المعلم استلم الراتب أم لا، هل عمر الطالب مناسب أم لا

# البيانات يتم تخزينها في ذاكرة الكمبيوتر

#نستخدم المتغيرات للإشارة إلى هذه البيانات
#مثال
x = 10   # x هو متغير

#المتغيرات لا تحتوي على البيانات نفسها، بل تشير فقط إلى موقعها في الذاكرة

 #الكود يستخدم البيانات لتنفيذ العمليات (إضافة، تعديل، حذف)
 # مثال بسيط:
students = ["Ali", "Sara"]
students.append("Hussain")   # إضافة
students[0] = "Omar"         # تعديل
students.remove("Sara")      # حذف
#---------------------------------------------------------
#
#يمكنك معرفة نوع البيانات لأي متغير في بايثون باستخدام الدالة type().
#--------------------------------------------------------------------------------------
#  الشرح     |                            مثال       |     الرمز | الاسم بالانجليزي  | نوع البيانات                                    
#---------------------------------------------------------------------------------------------------------------------------------------------===
# عدد صحيح      | Integer           | `int`     | `x = 10`                               | يمثل الأعداد الصحيحة مثل 1، 2، -5، 100            
# عدد عشري      | Float             | `float`   | `y = 3.14`                             | يمثل الأعداد التي تحتوي على فاصلة عشرية           
# نص            | String            | `str`      | `name = "Ali"`                         | يمثل النصوص بين علامتي اقتباس مفردتين أو مزدوجتين 
# منطقية        | Boolean           | `bool`    | `is_active = True`                     | تمثل القيم المنطقية: `True` أو `False`            
# قائمة         | List              | `list`    | `mylist = [1, 2, 3, "Python"]`         | مجموعة مرتبة من العناصر يمكن تعديلها              
# زوج مرتب      | Tuple             | `tuple`   | `mytuple = (1, 2, 3)`                  | تشبه القائمة لكنها **غير قابلة للتعديل**          
# قاموس         | Dictionary        | `dict`    | `mydict = {"name": "Sara", "age": 25}` | يحتوي على أزواج (مفتاح:قيمة)                      
#مجموعة         | Set               | `set`     | `myset = {1, 2, 3}`                    | مجموعة غير مرتبة ولا تسمح بالتكرار                
#None            | NoneType          | `None`    | `x = None`                             | تعني "لا توجد قيمة" (قيمة فارغة أو غير معرّفة)    
#---------------------------------
#  ملاحظة : (https://harmash.com/tutorials/python/variables-types)
#-----------------------------
#كل شيء في بايثون يعتبر كائن (Object) 
# (Class) يعني كل قيمة لها نوع 
#  وخصائص وعمليات ممكن تطبق عليها
 
print(type(10)) # int =>  اختصار  integer         اي رقم صحيح موجب او سالب 
print(type(100)) # int =>  اختصار  integer        اي رقم صحيح
print(type(-50))# int =>  اختصار  integer       اي رقم صحيح

print(type(100.9)) #float  => Floating point numder   عدد عشري
print(type(1.9888755)) #float  => Floating point numder   عدد عشري
print(type(-100.8777)) #float  => Floating point numder   عدد عشري
 
x = 3            # قيمته عبارة عن عدد صحيح ,x هنا قمنا بتعريف متغير إسمه
y = 1.5          #  قيمته عبارة عن عدد عشري ,y هنا قمنا بتعريف متغير إسمه
z = 4J           #   قيمته عبارة عن عدد مركب ,z هنا قمنا بتعريف متغير إسمه

print(type(x))   # x هنا طبعنا نوع قيمة المتغير
print(type(y))   # y هنا طبعنا نوع قيمة المتغير
print(type(z))   # z هنا طبعنا نوع قيمة المتغير


print(type("Hello"))  # str=> string النص
#القيم النصية
#لتعريف نص في بايثون يمكنك استخدام رمز التنصيص الفردي ' ' أو الزوجي " " و لا يوجد أي فارق بينهما.
#إذا كان النص يتألف من سطر واحد يمكن استخدام الرمز ' ' أو الرمز " ".
#إذا كان النص يتألف من عدة أسطر يمكن استخدام الرمز ''' ''' أو الرمز """ """.

print(type([1,2,3,4,5,6])) # list =>list  قائمة

print(type((1,2,3,4,5,))) # tuple => tuple والـ Tuple يشبه List لكن ما ينفع نغيره بعد ما نعمله (يعني غير قابل للتعديل).

print({"one" : 1, "tow" : 2, "three" : 3}) # dict =>Dictionary  لشكل { } مع أزواج (مفتاح  : قيمة) زي كلمة و معناها

print(type(2 == 2)) #bool =>Boolean   True التعبير 2 == 2 يسوي مقارنة: هل 2 يساوي 2؟
print(2 == 4) # False التعبير 2 == 4 يسوي مقارنة: هل 2 يساوي 4؟
#--------------------------------------------------------------
#------المتغيرات ( variables ) ------
#------------
# Syntax => [variable  Name] [Assignment operator] [value]
# يعني قواعد كتابة الكود Syntax       (  اسم المتغير   علامة يساوي = القيمة اللي نخزنها)
#  الصيغة العامة لكتابة المتغير في بايثون هي
#  اسم المتغير = القيمة
# قواعد اختيار اسم المتغير (Name Convention and Rules)
#1-  (a-z أو A-Z)  يجب أن يبدأ اسم المتغير بحرف   [
#  _أو شرطة تحتية 
#  احصل على خادم Python الخاص بك
#أسماء المتغيرات صحيحة
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" 
#2-  لا يمكن أن يبدأ المتغير برقم أو رمز خاص
# مثال   @name = "Ali"
# [3] يمكن أن يحتوي المتغير على أرقام أو شرطة تحتية في الوسط أو النهاية
#مثال
#2myvar = "John"
# [4]  لا يمكن أن يحتوي اسم المتغير على رموز مثل: @ # % ! - + / *
# مثال   my-name = "Ali"      my$name = "Sara"
# [5]  بايثون حساسة لحالة الأحرف (Case Sensitive)
#يعني المتغير name مختلف عن Name أو NAME
#مثال:
name = "Ali"
Name = "Omar"
print(name)   # Ali
print(Name)   # Omar

#-------------------------------------
myVariable = " My value "
print(myVariable)  #(في بايثون، لا تستطيع تعريف متغير بدون إسناد قيمة او معلومة  إليه أثناء تعريفه)

name = "Najat Hussain"    # كلمة واحدة => عادي
myName = "نجاة حسين"  # كلمتين => camelCase
my_name = "Najat Idris" # كلمتين => snake_case
print(name)
print(myName)
print(my_name)
#--------------------------------------
# ---المتغيرات ( variables )--
# ------------------
# Source Code : الكود الأصلي الذي تكتبه في الكمبيوتر
# Translation : تحويل الكود الأصلي إلى لغة الآلة
# Compilation : ترجمة الكود قبل وقت التشغيل
# Run-Time : الفترة التي يستغرقها البرنامج لتنفيذ الأوامر
# Interpreted : الكود يتم ترجمته أثناء التنفيذ مباشرة
# ----------------------------------------------------
x = 10        # وضع قيمة رقمية في المتغير
x = "Hello"   # تغيير قيمة المتغير إلى نص (كتابة)
print(x)      # طباعة قيمة المتغير
#في بايثون يمكن للمتغير أن يغيّر نوعه بسهولة
# عندما نطبع x سيظهر "Hello" لأن آخر قيمة تم إسنادها 
#--------
# الكلمات المحجوزة
help('keywords')
#قائمة بالكلمات المفتاحية في بايثون. أدخل أي كلمة مفتاحية للحصول على مزيد من المساعدة
#  الكلمة    |            المعنى                            
# ---------           | ----------------------------------- 
#**True**             | تمثّل القيمة المنطقية "صحيح"        
#**False**            | تمثّل القيمة المنطقية "خطأ"         
#**None**             | تعني "لا شيء" — قيمة فارغة أو غائبة 
#**if / elif / else** | بنية الشرط: تنفيذ كود بناءً على شرط            
#**for**              | حلقة تكرار (loop) على عناصر تسلسل              
# **while**           | حلقة تكرار تعتمد على شرط                       
#**break**            | إيقاف الحلقة فورًا                             
#**continue**         | تخطي الدورة الحالية في الحلقة                  
# **pass**            | لا يفعل شيئًا (يستخدم كعنصر نائـب placeholder) 
# **def**             | تعريف دالة                                      
#**return**           | إعادة قيمة من دالة                              
#**lambda**           | تعريف دالة صغيرة بدون اسم (دالة مجهولة)         
#**class**            | تعريف فئة (كائن object جديد)                    
# **global**          | إعلان أن المتغير عام (خارج الدالة)              
#**nonlocal**         | استخدام متغير من نطاق خارجي (داخل دالة متداخلة) 
#**import**           | استيراد مكتبة أو وحدة             
# **from**            | استيراد من وحدة محددة             
# **as**              | إعادة تسمية عند الاستيراد (alias) 
# **and**             | "و" منطقية                               
# **or**              | "أو" منطقية                              
# **not**             | نفي منطقي                                
# **is**              | مقارنة الهوية (هل المتغيران نفس الكائن؟) 
#**in**               | للتحقق من وجود عنصر داخل تسلسل           
#**try**              | بدء كتلة اختبار أخطاء                           
#**except**           | التعامل مع الخطأ عند حدوثه                      
# **finally**         | تنفيذ كود مهما كانت النتيجة (حدث خطأ أم لا)     
# **raise**           | إطلاق استثناء (خطأ مخصص)                        
# **assert**          | تحقق من شرط أثناء التنفيذ (للاختبار أو التصحيح) 
# **async**           | تعريف دالة غير متزامنة           
# **await**           | انتظار نتيجة من دالة غير متزامنة 
# **with**            | يستخدم لإدارة الموارد (مثل فتح ملف) ويغلقها تلقائيًا    
#**yield**            | لإرجاع قيمة مؤقتة من مولّد (generator) دون إنهاء الدالة 
#**del**              | حذف متغير أو عنصر من قائمة           
#**assert**           | التحقق من شرط (غالبًا أثناء التطوير) 
#----------------------------------
a, b, c = 1, 2, 3   # لا يمكن أن يكون عدد المتغيرات ≠ عدد القيم، وإلا سيحدث خطأ
print(a)
print(b)
print(c)
#---------------------------

# أحرف الهروب (Escape Sequences)
# هي رموز خاصة داخل النصوص (Strings) تُكتب باستخدام شرطة مائلة للخلف \
# \b  => رجوع للخلف (Backspace)
print("Hello\bworld") #سيتم إزالة o
# \newline  => الهروب إلى سطر جديد + \
print("Hello\
    I Love \
    python")
# \\  => طباعة علامة Backslash \
print("I Love Back slash\\")
# \'  => طباعة علامة اقتباس مفرد '
print('I Love single Quote\'test\'')
# \"  => طباعة علامة اقتباس مزدوج "
print("I Love single Quote\"test\"")
# \n  => نزول إلى سطر جديد (Line Feed)
print("Hello world\nSecond Line")
# \r  => عودة إلى بداية السطر (Carriage Return)
print("123456\rabcd")  #1 2 3 4 تم استبدالها بـ a b c d

# \t  => مسافة تبويب أفقية (Tab)
print("Hello\tPython")
# \xhh  => يُستخدم في بايثون لتمثيل حرف واحد باستخدام قيمته الست عشرية (Hexadecimal)
#https://www.ibm.com/docs/en/ste/8.4.1?topic=information-hex-decimal-symbol-values
print("\x4E\x61\x6A\x61\x74")
# ----------------------------
#-----Concatenation = جمع النصوص معًا لتكوين نص واحد---
msg="I Love"
lang="Python"
print(msg + " " + lang) 
full= msg + " " + lang
print(full)
a = "first\
second\
Third"
b = "A\
B\
C"
print(a + "\n " + b)
#print("Hello" + 1) #لا يمكنه دمج نص  مع عدد مباشرة     
# لكن هناك حلول ح نتعلمها بعدين
#------------------------------------
#----( strings)  سلاسل نصية
myStringOon = 'This is singie Quote'
myStringTwo = "This is singie Quote"
print(myStringOon)
print(myStringTwo)

myStringThree = 'This is singie Quote "test"'
myStringFour = "This is singie Quote 'test'"
print(myStringThree)
print(myStringFour)

myStringFive = '''First
second 'test' "test"
Third'''
print(myStringFive)

myStringSix = """First
second "test" \\\ 'test'
Third"""
print(myStringSix)
#----------------------------------------------
#فهرسة وتقطيع النصوص في بايثون (Strings – Indexing and Slicing)
#1. All Data in Python is Object
#كل البيانات في بايثون هي كائنات (Objects)
#2. Object Contain Elements
#الكائن يحتوي على عناصر (مثل حروف السلسلة النصية).
#3. Every Element Has Its Own Index
#كل عنصر له رقم فهرس خاص به (Index).
#4. Python Use Zero Based Indexing (Index Start From Zero)
#بايثون تستخدم فهرسة تبدأ من الصفر يعني أول عنصر رقمه 0
#5. Use Square Brackets To Access Element
#نستخدم الأقواس المربعة [] للوصول إلى عنصر معيّن
#6. Enable Accessing Parts Of Strings, Tuples or Lists
#تُمكّنك من الوصول إلى أجزاء من النصوص أو الـ tuples أو القوائم
#------------------
#الفهرسة (الوصول إلى عنصر واحد)
myString = "I Love Python"
print(myString[0])  # Index 0 => I   (i)اي يسوي حرف 
print(myString[9])  # Index 9 => t   (t)اي يسوي حرف 
print(myString[-1])  # Index -1 => first character form end        اي يسوي الحرف الأول من النهاية
print(myString[-6])  # Index -6 => 6th character form end   
#سلسلة( الوصول إلى عناصر متعددة)
#[Start:End][الابداية: النهاية]
#[Start:End: steps]     [ الابداية: النهاية : الخطوات]
#start → من أين تبدأ (الفهرس الأول الذي تبدأ منه)
#end → إلى أين تنتهي (يتوقف قبل هذا الفهرس)
#step → كم خطوة يتخطى

print(myString[8:11])#yth
print(myString[3:5])# ov
print(myString[:10])# if start is not here will start from 0 (I Love Pyt )( إذا لم يتم تحديد البداية، ستبدأ من 0)
print(myString[5:])# if end is not here will go to the end (e Python)(إذا لم يكن النهاية هنا، فسأذهب إلى النهاية)
print(myString[:]) # البيانات الكاملة(Full Data)

print(myString[0::1])  # البيانات الكاملة(Full Data)
print(myString[::1])  # البيانات الكاملة(Full Data)

print(myString[::2])  # يطبع كل حرفين (يتخطى حرف بعد كل حرف) ← النتيجة: "ILv yhn"
print(myString[::3])  # يطبع كل ثلاثة حروف (يتخطى حرفين بعد كل حرف) ← النتيجة: "Io tn"
#-----------------------------------------------
#-------- (دوال السلاسل النصية)(Strings Methods)
a = "I Love Python"
b = "      I Love Python      "
print(len(a))  # عدد الحروف في النص بدون المسافات الزائدة
print(len(b))  # عدد الحروف + المسافات الموجودة في البداية والنهاية

#strip(تزيل المسافات من البداية والنهاية)rstrip(تزيل المسافات من اليمين فقط)lstrip(تزيل المسافات من اليسار فقط)

n = "    I Love Python      "
print(n.strip())#تزيل المسافات من البداية والنهاية من الجهتين 
print(n.rstrip())#تزيل المسافات من اليمين فقط
print(n.lstrip()) #تزيل المسافات من اليسار فقط
print(len(n.strip()))
print(len(n.rstrip()))
print(len(n.lstrip()))

#-----------------------------------------------
n = "###I Love Python####"
print(n.strip())        # لا تزيل # لأنها تزيل المسافات فقط افتراضياً
print(n.rstrip("#"))    # "###I Love Python"   (تزيل # من اليمين فقط)
print(n.lstrip("#"))    # "I Love Python####"  (تزيل # من اليسار فقط)


n = "#@&@#@#I Love Python#&#&#"
print(n.strip("#@&"))   # "I Love Python"   (تزيل أي من الرموز # @ & من الجهتين)
print(n.rstrip("#@&"))  # " #@&@#@#I Love Python"  (من اليمين فقط)
print(n.lstrip("#@&"))  # "I Love Python#&#&#"     (من اليسار فقط)
#-----------------------------------------------
# title() ← تجعل أول حرف من كل كلمة كبير (Capital)
b = "I love 2b Graphics and 3g Techlogy and Python"
print(b.title())  # "I Love 2B Graphics And 3G Techlogy And Python"

# capitalize() ← تجعل أول حرف فقط من السطر كبير والباقي صغير
b = "I love 2b Graphics and 3g Techlogy and Python"
print(b.capitalize())  # "I love 2b graphics and 3g techlogy and python"

#-----------------------------------------------
# zfill() ← تضيف أصفار في اليسار حتى يصل الطول للقيمة المطلوبة
c, b, e, f = "1", "11", "111", "1111"
print(c)          # 1
print(b)          # 11
print(e)          # 111
print(f)          # 1111
print(c.zfill(4)) # 0001
print(b.zfill(4)) # 0011
print(e.zfill(4)) # 0111
print(f.zfill(4)) # 1111  (لا يضيف شيء لأنها بالفعل 4 خانات)
#-----------------------------------------------
# upper() ← يحول النص إلى حروف كبيرة
g = "najat"
print(g.upper())   # "NAJAT"

# lower() ← يحول النص إلى حروف صغيرة
h = "NAJAT"
print(h.lower())   # "najat"
#-----------------------------------------------
# دوال السلاسل النصية (الجزء الثاني)
# split() و rsplit()

a = "I Love python and PHP and MysQl"
print(a.split())   # ['I', 'Love', 'python', 'and', 'PHP', 'and', 'MysQl']
# (يفصل بالكلمات عند كل مسافة)

b = "I-Love-python-and-PHP-and-MysQl"
print(b.split("-"))  # ['I', 'Love', 'python', 'and', 'PHP', 'and', 'MysQl']
# (يفصل عند علامة - )

c = "I-Love-python-and-PHP-and-MysQl"
print(c.split("-", 3))  # ['I', 'Love', 'python', 'and-PHP-and-MysQl']
# (يفصل 3 مرات فقط من اليسار)

d = "I-Love-python-and-PHP-and-MysQl"
print(d.rsplit("-", 3)) # ['I-Love-python-and', 'PHP', 'and', 'MysQl']
# (يفصل 3 مرات فقط ولكن من اليمين)
#----------------------------------------------
# center(width, fillchar) ← يضع النص في المنتصف ويضيف رموز أو مسافات حوله
e = "Najat"
print(e.center(9))        # "  Najat  "   (بمسافات)
print(e.center(9, "#"))   # "##Najat##"   (بـ #)
print(e.center(15, "@"))  # "@@@@@Najat@@@@@"  (بـ @)
#-----------------------------------------------
# count() ← تعدد كم مرة تكرر النص المطلوب
f = "I Love python and PHP Because PHP is Easy"
print(f.count("PHP"))          # 2 (تكررت مرتين)
print(f.count("PHP", 0, 25))   # 1 (من البداية إلى الفهرس 25 فقط)
print(f.count("PHP", 0, 33))   # 2 (تكررت مرتين حتى الفهرس 33)

#-----------------------------------------------
# swapcase() ← يقلب حالة الحروف (الكبير يصير صغير والعكس)
g = "i love python"
h = "I LOVE PYTHON"
print(g.swapcase())  # I LOVE PYTHON
print(h.swapcase())  # i love python

#-----------------------------------
# startswith() ← يتحقق هل النص يبدأ بقيمة معينة
# الفهرس → 0 1 2 3 4 5 6 7 8 9 10 11 12 
# I   L o v e   p y t h  o  n  → الأحرف 
i = "I Love python"
print(i.startswith("I"))         # True  (يبدأ بـ I)
print(i.startswith("h"))         # False (لا يبدأ بـ h)
print(i.startswith("p", 7, 12))  # True  (من الفهرس 7 إلى 12 يبدأ بـ p)
print(i.startswith("n", 12))     # True (لأن النص ابتداءً من الفهرس 12 يبدأ بـ "n".)
#-----------------------------------------------
# endswith() ← يتحقق هل النص ينتهي بقيمة معينة
j = "I Love python"
print(j.endswith("n"))         # True  (ينتهي بـ n)
print(j.endswith("S"))         # False (لا ينتهي بـ S)
print(j.endswith("e", 2, 6))   # True  (من الفهرس 2 إلى 6 ينتهي بـ e)
print(j.endswith("I", 0))      # False (لا ينتهي بـ I من البداية)
#------------------------
#index( sudstring , start , end) 
u = "I Love python" 
print(u.index("p"))          # تطبع 7 => مكان 'p' في النص
print(u.index("p", 0, 10))   # تطبع 7 => البحث فقط بين المواقع 0 و 10
# print(u.index("p", 0, 5))  # لو شغلتها => Error لأن 'p' مش موجودة في هذا النطاق

#find( sudstring , start , end)  
o = "I Love python"
print(o.find("p"))        # 7 => مكان 'p'
print(o.find("p", 0, 10)) # 7 => نفس النتيجة
print(o.find("p", 0, 5))  # -1 => 'p' مش موجودة في هذا النطاق
# ملاحظة: الفرق بين index و find:
# index() يعطي Error لو النص مش موجود
# find() يعطي -1 لو النص مش موجود

q = "Najat"
print(q.rjust(10))      # "     Najat"  => 5 فراغات على اليسار
print(q.rjust(10, "#")) # "#####Najat"  => 5 رموز # على اليسار

# ljust() => النص على اليسار، الفراغات أو الرموز على اليمين
w = "Najat"
print(w.ljust(10))      # "Najat     "  => يضيف 5 فراغات على اليمين لتصبح الطول 10
print(w.ljust(10, "#")) # "Najat#####"  => يضيف 5 رموز # على اليمين

# splitlines() => يقسم النص إلى قائمة حسب السطور
qw = """First line
second Line
Third Line"""
print(qw.splitlines())  # ['First line', 'second Line', 'Third Line']  => يقسم عند كل سطر جديد
qe = "First line\nsecond Line\nThird Line"
print(qe.splitlines())  # نفس النتيجة لأن \n يعني سطر جديد



# expandtabs() => يستبدل التاب (\t) بعدد معين من الفراغات
qr = "Hello\tWorld\tI\tLove\tPythen"
print(qr.expandtabs(2)) # كل \t تصبح فراغين فقط

# istitle() => يتحقق إذا كانت كل كلمة تبدأ بحرف كبير وباقي الحروف صغيرة
one = "I Love Python And 3G"
two = "I Love python And 3g"
print(one.istitle()) # True  => لأن كل كلمة تبدأ بحرف كبير
print(two.istitle()) # False => لأن كلمة "python" تبدأ بحرف صغير

# isspace() => يتحقق إذا كان النص يحتوي فقط على فراغات
three = " "
four = ""
print(three.isspace()) # True  => لأنه يحتوي فقط على فراغ
print(four.isspace())# False => لأنه فارغ (لا يحتوي على شيء)

# islower() => يتحقق إذا كانت كل الحروف صغيرة
five = "i love python"
six = "I Love Python"
print(five.islower())
print(six.islower())

# isidentifier() => يتحقق إذا كانت الكلمة صالحة لتكون اسم متغير في بايثون
seven = "najat_hes"
eight = "NajatHes100"
nint = "Najat--Hes100"
print(seven.isidentifier())
print(eight.isidentifier())
print(nint.isidentifier())

# isalnum() => يتحقق إذا كانت كل الحروف أرقام أو حروف فقط (بدون رموز)
qt = "AaaaaBbbbb"
qy = "AaaaaBbbbb1111"
print(qt.isalnum()) # True  => فقط حروف
print(qy.isalnum()) # True  => حروف وأرقام فقط (مسموح)
# # isalnum() => يتحقق إذا كانت كل الحروف أرقام أو حروف فقط (بدون رموز)
#--------------------------
#replace( old Value, New Value,  count) => يستبدل نص معين بنص آخر
qu = "Hello One Two Three One Four One"
print(qu.replace("One", "1"))          # Hello 1 Two Three 1 Four 1
print(qu.replace("One", "1", 1))       # Hello 1 Two Three One Four One
print(qu.replace("One", "1", 2))       # Hello 1 Two Three 1 Four One

#join(iterable) => يدمج عناصر قائمة أو tuple أو أي iterable إلى نص واحد
myList = ["Najat", "Hussain", "Idris"]
print("-".join(myList))   # Najat-Hussain-Idris
print(" ".join(myList))   # Najat Hussain Idris
print(", ".join(myList))    # Najat, Hussain, Idris
print(type(", ".join(myList)))  # <class 'str'>  => النتيجة نص
#-----------------------------------------
##---------تنسيق السلاسل (Strings Formatting) --------
name = "Najat"
age = 00
rank = 10 

print("My Name is " + name )
#print("My Name is " + name + " and My Age is " + (age) ) # Error  => لا يمكن دمج نص مع رقم مباشرة
print("My Name is %s" % name)  # My Name Is Najat
print("My Name is %s" % "Najat")  # My Name Is Najat
print("My Name is %s and My Age is %d" % (name, age))  # My Name is Najat and My Age is 38
print("My Name is %s and My Age is %d and My Rank is %f" % (name, age, rank))

#%s => String  نص
#%d => Integer  عدد صحيح
#%f => Float   عدد عشري
namee = "Najat"
agee = 00
ranke = 10 
print("My Name is {} ".format("Najat")) # My Name is Najat
print("My Name is {} ".format(namee)) # My Name is Najat
print("My Name is {} and My Age is {} ".format(namee, agee)) # My Name is Najat and My Age is 00
print("My Name is {:s}  Age is {:d} & Rank is {:f} ".format(namee, agee, ranke)) # My Name is Najat  Age is 00 & Rank is 10.000000
#----------------------
#
ne = "Najat"
ln = "pthon" 
yn = 3
print("My Name is %s Iam %s Developer With %d Vears Exp" % (ne, ln, yn))# My Name is Najat Iam pthon Developer With 3 Vears Exp
print("My Name is {} Iam {} Developer With {:d} Vears Exp" .format (ne, ln, yn))# My Name is Najat Iam pthon Developer With 3 Vears Exp

# control Floating Point Number تنسيق الأعداد العشرية
myNumber = 10
print("My Number is %f" % myNumber)          # My Number is 10.000000
print("My Number is %f" % myNumber)        # My Number is 10.000000
print("My Number is %.2f" % myNumber)       # My Number is 10.00

print("My Number is {:d}" .format (myNumber))   #   My Number is 10
print("My Number is {:f}" .format (myNumber))  #    My Number is 10.000000
print("My Number is {:.2f}" .format (myNumber))  #   My Number is 10.00 
# truncate String تنسيق النصوص
mylongString = "Hello people of Elzero Web School I Love Y" 
print("Message: %s" % mylongString)  # Message: Hello people of Elzero Web School I Love Y
print("Message: %.5s" % mylongString)  # Message: Hello
print("Message: {}".format (mylongString))  # Message: Hello
print("Message: {:.13s}".format (mylongString))  # Message: Hello people
#-----------------------------------------
# format Money تنسيق النقود
myMoney = 500162350198
print("My Money is: {:d}".format (myMoney))  # My Money is: 500162350198
print("My Money is: {:_d}".format (myMoney))  # My Money    is: 500_162_350_198
print("My Money is: {:,d}".format (myMoney))  # My Money is: 500,162,350,198
#print("My Money is: {:&d}".format (myMoney))  # غلط لأن & مش رمز تنسيق صحيح        
#-------------
#rearrange ilems ترتيب العناصر  
a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))          # Hello One Two Three
print("Hello {2} {1} {0}".format(a, b, c))      # Hello Three Two One
print("Hello {1} {2} {0}".format(a, b, c))     # Hello Two Three One    
print("Hello {0} {0} {0}".format(a, b, c))    # Hello One One One

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))          # Hello 10 20 30
print("Hello {2} {1} {0}".format(x, y, z))      # Hello 30 20 10
print("Hello {1:f} {2:f} {0:f}".format(x, y, z))    # Hello 20.000000 30.000000 10.000000
print("Hello {1:.2f} {2:.4f} {0:.5f}".format(x, y, z)) # Hello 20.00 30.0000 10.00000
print("Hello {0} {0} {0}".format(x, y, z))   # Hello 10 10 10

#-----------------------------------------  
#format in version 3.6+ تنسيق النصوص في بايثون 3.6+
myName = "Najat"
myAge = 00
print(f"My Name is : {myName} and My Age is : {myAge}")  # My Name is Najat and My Age is 00
print(f"My Name is : {myName} and My Age is : {myAge}")  # My Name is NAJAT and My Age is 00
#------------------------------------------------------
#https://pyformat.info/  موقع لتنسيق النصوص في بايثون   
#https://realpython.com/python-f-strings/  شرح تنسيق النصوص في بايثون
#https://www.programiz.com/python-programming/methods/string  شرح دوال النصوص في بايثون
#https://docs.python.org/3/library/stdtypes.html#string-methods  التوثيق الرسمي لدوال النصوص في بايثون
#-----------------------------------------
#-----------  #  Numbers  اعداد
#Integers  الأعداد الصحيحة
print(type(1))
print(type(100))
print(type(10))
print(type(-1))
print(type(-100))
print(type(-10))
#float  الأعداد العشرية
print(type(1.500))
print(type(10.99))
print(type(0.99))
print(type(-0.99))
print(type(-10.1))

#complex  الأعداد المعقدة
myComplexNumber = 5+6j
print(type(myComplexNumber))
print("Real Part is: {}".format(myComplexNumber.real))
print("Imaginary Part is: {}".format(myComplexNumber.imag))

#[1] you can convert from int to float or complex يعني يمكنك تحويل الرقم الصحيح إلى رقم عشري أو معقد
#[2] you can convert from float to int or complex يعني يمكنك تحويل الرقم العشري إلى رقم صحيح أو معقد
#[3]you cannot convert complex to avy typa يعني لا يمكنك تحويل الرقم المعقد إلى أي نوع آخر
#امثلة
print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+5j)
#print(int(10+5j)) # Error يعني خطأ
#print(float(10+9j)) # Error يعني خطأ
#---------------------------------------------------
# Arithmetic Operators  مشغلات العمليات الحسابية 
#[+]Addition الجمع
#[-]Subtraction الطرح
#[*]Multiplication الضرب
#[/]Division القسمة
#[%]Modulus الباقي
#[**]Exponentiation التربيع
#[//]Floor Division القسمة

#[+]Addition الجمع
print(10 + 30) # = 40 
print(-10 + 20) # = 10 
print(1 + 2.66) # = 3.66 
print(1.2 + 2.2) # = 3.4

#[-]Subtraction الطرح
print(60 - 30) # = 30
print(-30 - 20) # = -50 
print(-30 - - 20) # = -10
print(5.66 - 3.44) # = 2.22

#[*]Multiplication الضرب
print(10 * 3) # = 30
print(5+ 10 *100) # = 1005 
print((5+ 10)*100) # = 1500

#[/]Division القسمة
print(100 / 20) # = 5.0
print (int(100 / 20)) # = 5

#[%]Modulus الباقي
print(8 % 2) # = 0   ليه صفر لأن 8 / 2 = 4
print(9 % 2) # = 1  كم نشيل من 9 عشان يفضل رقم نقسمه على 2 يطلع عدد صحيح
print(20 % 5) # = 0   كم نشيل من 20 عشان يفضل رقم نقسمه على 5 يطلع عدد صحيح
print(22 % 5) # = 2  كم نشيل من 22 عشان يفضل رقم نقسمه على 5 يطلع عدد صحيح 

#[**]Exponentiation التربيع
print(2 ** 5) # = 32  2 * 2 * 2 * 2 * 2 = 32
#يعني # 
print(2*2*2*2*2)# = 32
print(5**4)# = 625  5 * 5 * 5 * 5 = 625
print(5*5*5*5)# = 625

#[//]Floor Division القسمة
print(100 // 20) # = 5
print(110 // 20) # = 5    ليه 5 لأن 110 / 20 = 5.5
print(120 // 20) # = 6    ليه 6 لأن 120 / 20 = 6.0
print(130 // 20) # = 6    ليه 6 لأن 130 / 20 = 6.5
print(139 // 20) # = 6    ليه 6 لأن 139 / 20 = 6.95
#-----------------------------------
#--------- Lists | مرتبة القوائم ------
#[1]list items are enclosed in square brackets  يعني قوائم العناصر مغلقة في الأقواس المربعة
#[2] list are ordered, to use lndex to access item يعني القوائم مرتبة، لاستخدام الفهرس للاستفادة من العنصر
#[3] list are mutable => add, delete, edit يعني القوائم قابلة للتعديل => إضافة، حذف، تعديل
#[4]nlist items is not unique يعني عناصر القوائم غير مكررة
#[5]list can have different data types يعني قوائم يمكن أن تحتوي على أنواع مختلفة


myAwesomeList = ['one', 'two', 'three', 1 , 100.5, True]
print(myAwesomeList)# ['one', 'two', 'three', 1 , 100.5, True]
print(type(myAwesomeList[1]))# <class 'str'>
print(myAwesomeList[1])# two
print(myAwesomeList[-1])# True
print(myAwesomeList[-3])# three

print(myAwesomeList[1:4])# ['two', 'three', 1]  ليه 4 لأنه يبدأ من 1 وينتهي عند 4
print(myAwesomeList[:4])# ['one', 'two', 'three', 1]  ليه 4 لأنه يبدأ من البداية وينتهي عند 4
print(myAwesomeList[1:])# ['two', 'three', 1, 100.5, True]  ليه 4 لأنه يبدأ من 1 وينتهي عند آخر القائمة
print(myAwesomeList[::1])# ['one', 'two', 'three', 1, 100.5, True]
print(myAwesomeList[::2])# ['one', 'three', 100.5]  ليه 2 لأنه يبدأ من البداية وينتهي عند آخر القائمة]
#print(myAwesomeList[150])# Error
print(myAwesomeList) # ['one', 'two', 'three', 1 , 100.5, True]
myAwesomeList[1] =2 # يعني تغير العنصر في الفهرس 1
myAwesomeList[-1] = False # يعني تغير العنصر في الفهرس -1
#myAwesomeList[:2] = []# يعني حذف العنصر في الفهرس 1 و 2]
myAwesomeList[:3] = ["A", "B", "C"] # يعني تغيير العنصر في الفهرس 1 و 2 و 3    
print(myAwesomeList)# ['one', 2, 'three', 1 , 100.5, False]

#---------------------------------------------
#---------------الخاصة بالقوائم Lists الجزء الأول --------- Methods يعني (الطريقة أو الدالة التابعة)
#Method = دالة تنتمي إلى نوع بيانات محدد (object)
#وتُكتب دائمًا بهذه الصيغة:
#object.method()

#Append()  إضافة عناصر
myfriends = ['Najat', 'Amoon', 'Noura']
myoidfriends = ['Fatom', 'Hanan', 'thane']
myfriends.append('ranh')
myfriends.append(1000)
myfriends.append(15.670)
myfriends.append(True)
myfriends.append(myoidfriends)
print(myfriends)# ['Najat', 'Amoon', 'Noura', 'ranh', 1000, 15.67, True, ['Fatom', 'Hanan', 'thane']]
print(myfriends[2])# Noura
print(myfriends[6])# True
print(myfriends[7])# ['Fatom', 'Hanan', 'thane']
print(myfriends[7][2])# thane
print(myfriends[7][1])# Hanan
print(myfriends[7][0])# Fatom

#extend()  إضافة عناصر
a = [1,2,3]
b = ['a','b','c']
c = ["one", "two", "three"]
a.extend(b)
a.extend(c)
print(a)# [1, 2, 3, 'a', 'b', 'c', 'one', 'two', 'three']

#remove()  إزالة عناصر
x = [1,2,3,4,5, "najat", True ,"najat", "najat"]

x.remove("najat")
print(x)# [1, 2, 3, 4, 5, True, 'najat', 'najat'] تحذف أول عنصر يتطابق مع القيمة المحددة

#sort()  ترتيب العناصر

#y = [1,2,100, -10 , 17 , 29 ]
y = ['A','B','C']
#y.sort() # [-10, 1, 2, 17, 29, 100] ترتيب العناصر
y.sort(reverse=True) #  [100, 29, 17, 2, 1, -10] ترتيب العناصر بالعكس
#y.sort(reverse = False)# [-10, 1, 2, 17, 29, 100] ترتيب العناصر
print(y)# [100, 29, 17, 2, 1, -10] ترتيب العناصر

#reverse()  عكس العناصر
z = [10,1, 9, 80, 100, "najat", 100] 
z.reverse()
print(z)

#----- Lists Methods Part 2--- يعني (الخاصة بالقوائم Lists الجزء الثاني)
#Clear()  حذف العناصر
qp= [1,2,3,4]
pq = qp.copy()
qp.clear()
print(qp)# [] main list يعني القائمة الرئيسية
print(pq)# [1, 2, 3, 4] copied list يعني القائمة المنسدلة    

qp.append(5)
print(qp)# [5] يعني 
print(pq)# [1, 2, 3, 4]

#count()  العدد

r = [1,2,3,4,3,9,10, 1,2,1]
print(r.count(1))# 3

# index()  العنصر
qs = [ "Amoon", "Noura" , "osama" , "Ahmed" , "Najat", "Najat"]
print(qs.index("Najat"))# 4

#insert()  إضافة عناصر
qf = [1,2,3,4,5 ,"A","B"]
#qf.insert(0,"Test")# ["Test",1,2,3,4,5 ,"A","B"]
qf.insert(-1,"Test")# [ 1, 2, 3, 4, 5, 'A', 'Test', 'B']
print(qf)

#pop()  إزالة عناصر
qn =  [1,2,3,4,5 ,"A","B"]

print(qn.pop(-3))  # 4
#------------------------------------
#------Tuples Methods Part 1-- يعني (الخاصة بالقوائم Tuples الجزء الأول)--
# tuple()  إنشاء قوائم => لكنها غير قابلة للتغيير
#[1]tuple ilems are enclosed in parenthess




#-------- من درس 24 الى درس  نرجع له بعدين


#---------Control Flow – If, Elif, Else يعني التحكم في التدفق - إذا، وإلا إذا، وإلا
uName = "Najat"
uCountry = "KSA"
cName = "python course"
cPrice = 100
if uCountry == "Egypt":
    print(f"Hello {uName} Because You From {uCountry}")
    print(f"The Course \"{cName}\" Price is: {cPrice- 80}$")
elif uCountry == "KSA":
    print(f"Hello {uName} Because You From {uCountry}")
    print(f"The Course \"{cName}\" Price is: {cPrice - 50}$")
elif uCountry == "Kuwait":
    print(f"Hello {uName} Because You From {uCountry}")
    print(f"The Course \"{cName}\" Price is: {cPrice - 40}$")    
else:
    print(f"Hello {uName} Because You From {uCountry}")
    print(f"The Course \"{cName}\" Price is: {cPrice -30}$")

    #-------------------
#------Control Flow – Nested If And Trainings يعني التحكم في التدفق - إذا متداخل وتدريبات

uname = "Najat"
issubclass="Yes"
ucountry = "Eritrea"
cname = "python course"
cprice = 100

if ucountry == "Egypt" or ucountry == "KSA" or ucountry == "qatar" or ucountry == "Eritrea": 
    if issubclass == "Yes":
        print(f"Hello {uname} Because You From {ucountry} And Subclass")
        print(f"The Course \"{cname}\" Price is: {cprice - 90}$")
    else:
        print(f"Hello {uname} Because You From {ucountry}")
        print(f"The Course \"{cname}\" Price is: {cprice - 80}$")

elif ucountry == "Kuwait" or ucountry == "Bahrain":
    print(f"Hello {uName} Because You From {ucountry}")
    print(f"The Course \"{cName}\" Price is: {cprice - 50}$") 

else:
    print(f"Hello {uname} Because You From {ucountry}")
    print(f"The Course \"{cname}\" Price is: {cprice -30}$")
#-------------------
#-Ternary Conditional Operator يعني عامل الشرط الثلاثي
country= "Eritrea"
if country == "Eritrea":
    print(f"the weather in {country} is 15")

elif country == "KSA":
    print(f"the weather in {country} is 30")
else:
    print("contry  is not in the list")

#short if     مختصر if
movieRate = 18
