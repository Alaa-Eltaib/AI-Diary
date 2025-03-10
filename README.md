
# Learn-Python-
Welcome to Learn-Python, a beginner-friendly  for understanding the basics of Python! 🐍✨

# Why Python 

 - Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
 - Python has syntax that allows developers to write programs with fewer lines than some other programming languages
# Indentation
في بايثون بنحط مسافات لتحديد ال Code Blocks بدل {} زي ما في (++java,c)  طبعا اجباري ان احنا نحطهم  عشان نشوف بداية ونهاية كل حاجة كنا بنحطلها {} في أي لغة تاني والكود بأي مسافة ناقصة هيديني ايرور على طول 
ومننساش بعد كتابة أي شطر في if او Loops او functions بنحط :
# Variable and Data Types
  على عكس اللغات اللي اتعلمنها (++Java , c) بايثون مش بتحتاج تعرف قيمة الحاجة قبل ما تخزنها ولكن مجرد ما بتكتب الحاجة  هي بتتعرف على نوعها مباشرة 
  مثال:
  ```python
 # Variables
  x = 10
  y = "Hello, World!“
  z = 3.14
   # Data Types 
 - print(type(x)) #<class 'int'>
 - print(type(y)) # <class 'str'>
 - print(type(z)) #<class 'float'>

```

Note :  
 بنستخدم # لما اعمل كومنت في سطر واحد وبنستخدم  """ عشان اعمل كومنت  مكون من كذا سطر 

```python
#### Comments in python 
#This is a single-line comment
"""This is amulti-line Comment """
```


# Casting
  الكاستنج هو اني احول من data type ل data type تاني

```python
x = int(1)   # x will be 1 
y = int(2.8) # y will be 2 
z = int("3") # z will be 3 
x = float(1)  # x will be 1.0 
y = float(2.8) # y will be 2.8 
z = float("3")   # z will be 3.0 
x = str("s1") # x will be 's1' 
y = str(2)    # y will be '2'
```

# Strings
- في بايثون ممكن نكتب الجملة ب single quotation marks, or double
   quotation marks. 'hello' is the same as "hello".
 - Strings are Arrays
 يعني اول حرف بيكون الانديكس بتاعه بزيرو زي الاراي عشان اجيب طول الاسترينج بستخدم فانكشن اسمها len()  ، عشان اتأكد ان الحرف او الكلمة موجودة في النص اللي عندي ولا بستخدم كلمة in 
 ```python
 a = "Hello, World!" print(a[1])
 txt = "The best things in life are Water!" 
 print(“Water"  in txt) #True
 
 ```

```python

name = "PythonProgramming"

| التعبير        | النتيجة          |    التفسير        |
| ----------- | ---------------- | ---------------------- |
| `name[0]`   | `'P'`            | أول حرف من النص        |
| `name[-1]`  | `'g'`            | آخر حرف من النص       |
| `name[-5:]` | `'mming'`        | آخر 5 أحرف من النص    |
| `name[:-5]` | `'PythonProgra'` | النص بدون آخر 5 أحرف  |
| `name[::2]` | `'PtoPormig'`    | يأخذ كل حرفين من النص |
| `name[::3]` | `'PhPrni'`       | يأخذ كل 3 أحرف         |
```

- `name[start:end]` → يقتطع النص من **start** إلى **قبل** `end`.
- `name[start:end:step]` → يقتطع النص وفقًا لخطوة **step**، أي يأخذ كل `step` حروف.
- `name[::-1]` → يعكس النص  كله .
```python
first_name = "John"
last_name = "Doe"

# Using concatenation (+)
full_name = first_name + " " + last_name
print("Hello, " + full_name + "!")  # Output: Hello, John Doe!

# Using f-strings (Python 3.6+)
print(f"Hello, {first_name} {last_name}!")  # Output: Hello, John Doe!

# Using format() method
print("Hello, {} {}!".format(first_name, last_name))  # Output: Hello, John Doe!

```

3 طرق ممكن نستخدمهم عاشن ندمج الvirables : 
- اول حاجة + -->بكتب الكلام وبحط بينهم +
-  تاني حاجة --> بدمج بينهم ب {}f  دي موجودة في بايثون 3.6 فما فوق 
- تالت حاجة --> بستخدم format 
## Operations on Strings
| Function     | Description                                      |
| ------------ | ------------------------------------------------ |
| `len()`      | إرجاع طول النص (عدد الحروف)                      |
| `strip()`    | إزالة المسافات من بداية ونهاية النص              |
| `lstrip()`   | إزالة المسافات من الجهة اليسرى                   |
| `rstrip()`   | إزالة المسافات من الجهة اليمنى                   |
| `upper()`    | تحويل النص إلى **أحرف كبيرة**                    |
| `lower()`    | تحويل النص إلى **أحرف صغيرة**                    |
| `replace()`  | استبدال جزء معين من النص بآخر                    |
| `split(",")` | تقسيم النص باستخدام الفاصلة كمحدد                |
| `count()`    | عدد مرات تكرار الكلمة داخل النص                  |
| `join()`     | دمج النصوص باستخدام فاصل محدد                    |
| `find()`     | إرجاع **index** لأول ظهور للكلمة داخل النص       |
| `startswith()` | التحقق مما إذا كان النص يبدأ بكلمة معينة (ترجع `True` أو `False`) |
| `endswith()`   | التحقق مما إذا كان النص ينتهي بكلمة معينة (ترجع `True` أو `False`) |

     
# Some Operators
  # Python Operators

## Python Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

| Operator | Name            | Example  |
|----------|----------------|----------|
| +        | Addition       | x + y    |
| -        | Subtraction    | x - y    |
| *        | Multiplication | x * y    |
| /        | Division       | x / y    |
| %        | Modulus        | x % y    |
| **       | Exponentiation | x ** y   |
| //       | Floor division | x // y   |

## Python Assignment Operators
Assignment operators are used to assign values to variables:

| Operator | Example       | Same As        |
| -------- | ------------- | -------------- |
| =        | x = 5         | x = 5          |
| +=       | x += 3        | x = x + 3      |
| -=       | x -= 3        | x = x - 3      |
| *=       | x *= 3        | x = x * 3      |
| /=       | x /= 3        | x = x / 3      |
| %=       | x %= 3        | x = x % 3      |
| //=      | x //= 3       | x = x // 3     |
| **=      | x **= 3       | x = x ** 3     |
| &=       | x &= 3        | x = x & 3      |
| =\|      | x \|= 3       | x = x \| 3     |
| ^=       | x ^= 3        | x = x ^ 3      |
| >>=      | x >>= 3       | x = x >> 3     |
| <<=      | x <<= 3       | x = x << 3     |
| :=       | print(x := 3) | x = 3 print(x) |

## Python Comparison Operators
Comparison operators are used to compare two values:

| Operator | Name                        | Example  |
|----------|-----------------------------|----------|
| ==       | Equal                       | x == y   |
| !=       | Not equal                   | x != y   |
| >        | Greater than                | x > y    |
| <        | Less than                   | x < y    |
| >=       | Greater than or equal to    | x >= y   |
| <=       | Less than or equal to       | x <= y   |

## Python Logical Operators
Logical operators are used to combine conditional statements:

| Operator | Description                                      | Example                 |
|----------|-------------------------------------------------|-------------------------|
| and      | Returns True if both statements are true       | x < 5 and x < 10       |
| or       | Returns True if one of the statements is true  | x < 5 or x < 4         |
| not      | Reverses the result, returns False if true    | not(x < 5 and x < 10)  |

## Python Identity Operators
Identity operators compare objects by memory location, not just value:

| Operator | Description                                          | Example   |
|----------|-----------------------------------------------------|-----------|
| is       | Returns True if both variables are the same object | x is y    |
| is not   | Returns True if both variables are not the same object | x is not y |

## Python Membership Operators
Membership operators test if a sequence exists within an object:

| Operator | Description                                                | Example    |
|----------|------------------------------------------------------------|------------|
| in       | Returns True if a sequence with the specified value is present in the object | x in y    |
| not in   | Returns True if a sequence with the specified value is not present in the object | x not in y |

## Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

| Operator | Name                 | Description                                                                                             | Example |
| -------- | -------------------- | ------------------------------------------------------------------------------------------------------- | ------- |
| &        | AND                  | Sets each bit to 1 if both bits are 1                                                                   | x & y   |
| \|       | OR                   | Sets each bit to 1 if one of two bits is 1                                                              | x \| y  |
| ^        | XOR                  | Sets each bit to 1 if only one of two bits is 1                                                         | x ^ y   |
| ~        | NOT                  | Inverts all the bits                                                                                    | ~x      |
| <<       | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off                        | x << 2  |
| >>       | Signed right shift   | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off | x >> 2  |
الجداول دي كلها من[[Python Operators](https://www.w3schools.com/python/python_operators.asp)]


# Control Structures
  عبارة عن if , else , elif  معندناش  else if زي جافا اسمها elif
  
```python
a = 200  
b = 33  
if b > a:  
    print("b is greater than a")  
elif a == b:  
    print("a and b are equal")  
else:  
    print("a is greater than b")
```
Short Hand If
```python
if a > b: print("a is greater than b")
```
Short Hand If ... Else
```python
a = 2  
b = 330  
print("A") if a > b else print("B")
```
This technique is known as **Ternary Operators**, or **Conditional Expressions**.
**Can use `OR` ` and` `Not`**
```python
#Test if `a` is greater than `b`, AND if `c` is greater than `a`:

a = 200  
b = 33  
c = 500  
if a > b and c > a:  
  print("Both conditions are True")
#Test if `a` is greater than `b`, OR if `a` is greater than `c`:

a = 200  
b = 33  
c = 500  
if a > b or a > c:  
  print("At least one of the conditions is True")
  #Test if `a` is NOT greater than `b`:

a = 33  
b = 200  
if not a > b:  
  print("a is NOT greater than b")

```

# Loops
 عندنا 3 جمل وهم continue  , break , pass
   continue  , break ودول نفس شغلانتهم في أي لوب 
 - break , With the break statement we can stop the loop even if the while condition is true.
 - continue, With the continue statement we can stop the current iteration, and continue with the next
 - If you need to leave a block of code empty temporarily, use the `pass` statement.
## While
 زي أي while اخدناها قبل كده فرق ريقة الكتابة بس 
```python
i = 1 
while i < 6:
    print(i) i += 1
```
## The else Statement 
ممكن استخدمها مع for او while

With the else statement we can run a block of code once when the condition no longer is true:
```python
i = 1  
while i < 6:  
  print(i)  
  i += 1  
else:  
  print("i is no longer less than 6")
```
## For Loop

لما باجي اعمل for بكتبه كده -> `for i in range(n)` لو عايزة ازود الاندكس اللي هو i او ابدا الانديكس بواحد مثلا لانه تلقائي يبدأ بزيرو اكتب كده `range(1,n+1)` انا كده خليت i=1 وخليت n ينتهي عند نفسه كأني قولت =n في c++.  الشرط ده موجود لما اكون بكتب integer 
```python
for x in range(6): 
    if x == 3: 
        break  
 print(x)
```
لو بعمل for loop ل string بيتكتب كده 
```python
for x in s:
	if x in'aeiuo':
		c+=1
print(c)
```

## Range 
 ### 🔹 `range(start, stop, step)` في بايثون

دالة `range()` تُستخدم لإنشاء تسلسل من الأرقام، وغالبًا ما تُستخدم في الحلقات التكرارية مثل `for`.

#### **المعاملات:**
- **`start`** → القيمة التي يبدأ منها التسلسل (افتراضيًا `0` إذا لم يتم تحديدها).
- **`stop`** → القيمة التي **يتوقف قبلها** التسلسل (`stop - 1` هو آخر رقم يتم توليده).
- **`step`** → مقدار التغيير بين كل رقمين متتالين.

---

###  **أمثلة على `range()`**
```python
# من 0 إلى 4 (القيمة الأخيرة لا تُحتسب)
for x in range(5):
    print(x)  
# Output: 0 1 2 3 4

# من 2 إلى 9 بزيادة 2 في كل مرة
for x in range(2, 10, 2):
    print(x)
# Output: 2 4 6 8

# العد التنازلي من 10 إلى 1
for x in range(10, 0, -1):
    print(x)
# Output: 10 9 8 7 6 5 4 3 2 1

```


# Enumerate()

عبارة عن فانكشن بستخدمها للتكرار خلال تسلسل زي (list, tuple, string) مع الاحتفاظ بكل index 
ده مفيد جدًا عندما تحتاج إلى كل من **العنصر نفسه** و **موقعه** أثناء التكرار.

```python
for index, value in enumerate(iterable):
    # تنفيذ الكود هنا (الصيغة العامة)

fruits = ["apple", "banana", "cherry"] for index, fruit in enumerate(fruits): print(f"Index: {index}, Fruit: {fruit}")
#Index: 0, Fruit: apple
#Index: 1, Fruit: banana
#Index: 2, Fruit: cherry
```
- `enumerate()`لاتجعل من السهل تتبع **الموقع** الحالي للعناصر .
- يمكن تحديد بداية الفهرس باستخدام `start` في `enumerate(iterable, start=1)`.
- بديلًا لاستخدام `range(len(iterable))`، فإن `enumerate()` تعتبر **أفضل وأوضح**.
- -----------------------------------------------------------------------
# Functions
 بنعرفها بكلمة محجوزة اسمها def ودي مختصرة من كلمة define وبرضو فيه منها نوعين نوع ب print ونوع ب return
 ```python
 def my_function():
    print("Hello from a function")

my_function()

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def add(x):
    return 10 + x

print(add(3))
print(add(5))
print(add(9))

```

بالنسبة ل Arguments لو انا معرفش عدد ال attributes اللي هبعتهم بحط *  لو بعرف خلاص ببعتهم على طول 
```python
def add_numbers(*args):
    total = sum(args)
    print(f"المجموع: {total}")

add_numbers(1, 2, 3, 4, 5)
# Output: 15
```


```python
def greet(name, age):
	print(f"HI {name}, age {age} years.")
 greet('Ahmed', 20) # Output: HI Ahmed, age 20 years.

```

ممكن كمان استخدم ** kwagras ودي بتطلعهم في شكل dictionary

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Ahmed", age=25, country="Egypt")
#output:Displaying user information:
#Name: Ahmed
#Age: 25
#Country: Egypt


```
 وممكن استخدمهم سوا *  args,  * * kwargs
 
```python
def full_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

full_info("Ahmed", 25, city="Cairo", country="Egypt")
#output:
#Positional arguments: ('Ahmed', 25)
#Keyword arguments: {'city': 'Cairo', 'country': 'Egypt'}

```
 وممكن اعمل Default Parameter
```python
def my_function(**country = "Norway"**):  
  print("I am from " + country)  
  
my_function("Sweden")  #I am from Sweden
my_function("India") # I am from India
my_function()##I am from Norway
my_function("Brazil")#I am from Brazil
```
--- Positional-Only Arguments في بايثون

في بايثون، ممكن تخلّي الدالة تقبل **حاجة واحدة بس** من نوعين: إما **positional arguments** (يعني اللي بتكتبهم زي ما هما بالترتيب) أو **keyword arguments** (اللي بتحدد اسم الباراميتر وبعدين قيمته). لو عايزة تخلّي الدالة تقبل **positional arguments بس**، بتضيفي `, /` بعد الباراميترات.
او **Combine Positional-Only and Keyword-Only**

 بدون `, /`
لو كتبت بدون `, /`، هتقبل الـ arguments بأي طريقة (positional أو keyword).
فايدة **Positional Arguments:** بسيطة وسريعة لما الترتيب واضح.
```python
def my_function(x):
    print(x)

my_function(3)      # بتطبع: 3 (positional)
my_function(x=3)    # بتطبع: 3 (keyword)

```
 مع ` ,/` (Positional-Only)

```python
def my_function(x, /):
    print(x)

my_function(3)      # بتطبع: 3 (تمام)
my_function(x=3)    # هتطلع error
```
Keyword-Only Arguments
**Keyword Arguments:** أوضح وأمرن لو الدالة كبيرة أو فيها اختيارات.
```python
def my_function(*, x, y):
    print(x + y)

my_function(x=3, y=4)   # بتطبع: 7 (تمام)
my_function(3, 4)       # هتطلع error
```
 Combine Positional-Only and Keyword-Only
 **دمج Positional-Only و Keyword-Only:** تحكم وتنظيم، عشان الكود يبقى دقيق ومنظم.
```python
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
```

## Recursion
بتنادي على نفسها 
```python
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)
------------------------------
#output
Recursion Example Results:
1
3
6
10
15
21
```






--------------------------------------------------------------------------






-----------------------------------------------------------------------
# Lambda Expressions

هي عبارة عن فانكشن مجهولة من غير اسم بتتكتب في سطر واحد وبتاخد أي عدد من arguments ولكن جواها one expression

syntax:
```python
lambda _arguments_ : _expression_

```
تعتبر اختصار لكود عكس def ، مفيدة في أي فانكشن بسيطة و تستخدم في الاغلب مع map() و filter() و sorted()`
مثال:
```python
add = lambda x, y: x + y
print(add(3, 5))  # الناتج: 8

```

## Why Use Lambda Functions?

The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
```python
def myfunc(n):  
  return lambda a : a * n  
  
mydoubler = myfunc(2)  
  
print(mydoubler(11))
```
Use lambda functions when an anonymous function is required for a short period of time.

------------------------------------------------------------------------
# list 
List items are ordered, changeable, and allow duplicate values.
Lists are used to store multiple items in a single variable
  list ,set ,tuble ,dictionary---> 5 built-in data types in python used to store data
  
يعني بتخزن كذا datatype في list واحدة عادي 
الانديكس عندي بيدأ ب 0
عادة لما نيجي نعكل ليست بنعملها زي كده 
```python
List0 = ["asd", "ali", "omar"]
print(List0) # ['asd', 'ali', 'omar'] 
print(List0[0]) # 'asd'
print(len(List0)) # 3
list1 = ["apple", "banana", "cherry"] 
list2 = [1, 5, 7, 9, 3] 
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]


```

ولكن انا ممكن استخدم الConstructor عشان اعمل ليست طيب ده ازاي بيكون كده 
```Pyhton
thislist = list(("apple", "banana", "cherry"))
print(thislist)

```

-Range of indexes

ممكن نعرض الليست عن طريق الانديكس 
```Python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]  
print(thislist[2:5])
```
ملحوظة السيرش بيدأ برقم 2 انديكس لحد 4 الخمسة مش معانا
لو كده [4:]---> يعني هعرض لحد 3 الاربعة مش معايا
لو كده [:2]--->هبدأ من 2 انديكس لحد الآخر
لو  كده [-1:-4] ---> هبدأ من انديكس -4 لحد انديكس-2 (mango -->-1)مش معايا


 - عندي فانكشن اسمها append() ودي بنضيف عنصر في نهاية الليست 

```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ['apple', 'banana', 'cherry', 'orange']
```

 - افرض هضيف عنصر في مكان معين هنا بستخدم insert()

```python
thislist = ["apple", "banana", "cherry"]  
thislist.insert(2, "watermelon")  
print(thislist)
```
 كده الليست بقيت 4 عناصر مش 3

 - extend() --> وكأني بجمع 2 lists سوا 
  بتتحط الليست الجديدة في نهاية القديمة ومش بتسخدم مع الليست لا ممكن استعملها مع أي iterable(tuples,sets,dictionaries,etc)
 ```Python
 thislist = ["apple", "banana", "cherry"]  
tropical = ["mango", "pineapple", "papaya"]  
thislist.extend(tropical)  
print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

- عندي فانكشن اسمها remove() ودي بتحذف عنصر معين

```python
List2 = ["apple", "banana", "cherry"] 
List2.remove("banana") 
print(List2) # ['apple', 'cherry']
```


- كمان فيه pop() --> دي بتمسح عنصر محدد عن طريق اني بدخل الانديكس ولكن لو مدخلتش انديكس هتمسح اخر عنصر تلقائي  وبيرجع العنصر اللي اتشال يعني 
```python
thislist = ["apple", "banana", "cherry"]  
X=thislist.pop(1)  
print(thislist)#['apple', 'cherry']
print(x)#banana

thislist1 = ["apple", "banana", "cherry"]  
thislist1.pop()  
print(thislist)#["apple", "banana"]

```

- del()---> دي بتمسح عنصر او عدد من العناصر او الليست كلها 
هنا ايه الفرق بين دي remove او pop 
remove بتعتمد على الvalue 
و del , pop بيعتمدوا على الانديكس او القيمة و pop بترجع اللي شالته بس del او remove() لا 

```python
thislist = ["apple", "banana", "cherry"]  
del thislist[0]  
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".

```


- عندي فانكشن اسمها Clear() ودي بتمسح محتويات الليست كلها

```python
List2 = ["apple", "banana", "cherry"] 
List2.clear() 
print(List2) # []
```

- loops
for x in List وده اسمه تكرار مباشر وده مش بيعدل 
for i in range(len(List))  وده اقدر اعدل القيم 
و طبقا اقدر استخدم while
```python
List3 = ["apple", "banana", "cherry"]
for x in List3: 
    print(x) # apple # banana # cherry 
List3 = ["apple", "banana", "cherry"] 
for i in range(len(List3)):
    print(List3[i]) # apple # banana # cherry

```
 - في حاجة اسمها list comprehension ودي بنستخدمها لما نيجي نعمل list جديدة بناء على واحدة قديمة ,وكمان لو حاجة مش معقدة يعني for loops بسيط
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  
  
newlist = [x for x in fruits if "a" in x]  
  
print(newlist)
----------------------
syntax
newlist = [_expression_ for _item_ in _iterable_ if _condition_ == True]
```

-  Customize Sort Function
انا ممكن اخصص سورت فانكشن بالطريقة اللي عايزها عن طريق
keyword argument `key = _function_`.
```python
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)#[50, 65, 23, 82, 100]

```
 -->By default the `sort()` method is case sensitive, resulting in all capital letters being sorted before lower case letters
--->The `reverse()` method reverses the current sorting order of the elements.
 - To copy list
> copy() method
> list() method
> use slice Operator `:` (slice) operator.
- Join two lists
 >can use Operator `+` 
> can use `extend()` method
> can use append
```pyhton
list1 = ["a", "b", "c"]  
list2 = [1, 2, 3]  
  
list3 = list1 + list2  
print(list3)
------------------------
list1 = ["a", "b" , "c"]  
list2 = [1, 2, 3]  
  
list1.extend(list2)  
print(list1)
------------------------
list1 = ["a", "b" , "c"]  
list2 = [1, 2, 3]  
  
for x in list2:  
  list1.append(x)  
  
print(list1)
```

---

# Tuple
A tuple is a collection which is ordered and **unchangeable**.
Tuples are written with round brackets.
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
  هو شبه الليست ولكن مش بيقبل التعديل ولا الحذف
  ```python 
  fruits = ("apple", "banana", "cherry")
  print(fruits)
  #output
  ('apple', 'banana', 'cherry')

  ```
ممكن اعمل tuple من عنصر واحد عن طريق اضافة `,` :
  ```python
  thistuple = ("apple",)  
print(type(thistuple))  
  
#NOT a tuple  
thistuple = ("apple")  
print(type(thistuple))
```
  
  
  الوصول للعناصر :
   ```python
print(fruits[0])   # الناتج: apple
print(fruits[-1])  # الناتج: cherry (آخر عنصر)

```
   التكرار:
```python 
for fruit in fruits:
    print(fruit)
#output
apple
banana
cherry
#هل العنصر ده موجود ولا لا 
if "banana" in fruits:
    print("Yes, 'banana' is in the tuple!")


```
Once a tuple is created, you cannot change its values. Tuples are **unchangeable**, or **immutable** as it also is called.
عشان اقدر اعدل على tuble لازم الاول احوله ل list اعدل عليه وبعدين ارجعه تاتي :
 ```python
fruits_list = list(fruits)  # تحويل tuble to list
fruits_list.append("orange")  # إضافة عنصر جديد
fruits = tuple(fruits_list)  # تحويل list to tuble
print(fruits)
#output:
('apple', 'banana', 'cherry', 'orange')

```
 لو هضيف عنصر  برضو لازم احوله ل ليست او اني اضيف tuple ل tuple تاني 

```python
thistuple = ("apple", "banana", "cherry")  
y = list(thistuple)  
y.append("orange")  
thistuple = tuple(y)


thistuple = ("apple", "banana", "cherry")  
y = ("orange",)  
thistuple += y  
  
print(thistuple)#'apple', 'banana', 'cherry', 'orange')

```
 
 معنديش حئف عنصر إلا لو هحول ل ليسا وبعدينارجعه ل tuple ولكن عندي لو هحذفه تماما :
 ```python
 del fruits

```

- *Unpacking*
هو عبارة عن اني بخرج العناصر من tuple عن طريق اني بعينها ل variable تانية 
```python
fruits = ("apple", "banana", "cherry")  
  
(green, yellow, red) = fruits  
  
print(green) #apple
print(yellow) #banana 
print(red)#cherry
```
 لو عدد variables اقل من عدد ال values ممكن نحط `*` ودي هتعملي كل اللي فاضيلن في ليست
 ```python
 fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")  
  
(green, yellow, *red) = fruits  
  
print(green)  
print(yellow)  
print(red)
#apple
#banana
#['cherry', 'strawberry', 'raspberry']
```
ولو عايزة احطهم في متغير معين اخلي عنده هو `*`

 - ممكن نكرر  عناصر tuple n من المرات عن طريق اني بحط `*` ثم الرقم 
   
```python
fruits = ("apple", "banana", "cherry")  
mytuple = fruits * 2  
  
print(mytuple)#('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
```

count():Returns the number of times a specified value occurs in a tuple.
index():Searches the tuple for a specified value and returns the position of where it was                     found.

-------------------------------------------------------------------------------

# Set
Sets are used to store multiple items in a single variable.
هي مجموعة من نفس العناصر
- الـ `Set` 
- **غير مرتبة (Unordered):** العناصر في المجموعة لا تتبع ترتيبًا محددًا، مما يعني أنك لا تستطيع الاعتماد على ترتيب معين عند التعامل معها.
- **غير قابلة للتغيير (Unchangeable):*** لا يمكن تغيير العناصر الموجودة داخل المجموعة بعد إنشائها، لكن يمكنك إزالة عناصر أو إضافة عناصر جديدة.
- **غير مفهرسة (Unindexed):** لا يمكن الوصول إلى عناصر المجموعة باستخدام فهرس (زي الليست )، لأنها لا تحتوي على ترقيم للعناصر.
- بتتكتب `{}` أو بـ `set()`. 

-  ازاي تعمل Set؟ 
```python 
thisset = {"apple", "banana", "cherry"}
print(thisset)#  {'cherry', 'banana', 'apple'}

# Note: the set list is unordered, meaning: the items will appear in a random order.

# Refresh this code to see the change in the result.
```
-لو كررت رقم، بايثون هيمسح التكرار لوحده
```python
my_set = {1, 2, 2, 3, 4, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}

```
 -True , 1 الاتنين بيعتبروا نفس الحاجة في set
 -False , 0 برضو 
 
 ```python
 thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)#{True, 2, 'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)#{False, True, 'cherry', 'apple', 'banana'}



```

-لو عايز اوصل لعنصر  مش هقدر لأن مفيش انديكس ولكن ممكن عن طريق اللوبس:

```python
thisset = {"apple", "banana", "cherry"}  
  
for x in thisset:  
  print(x)
#Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}  
  
print("banana" in thisset)

#Check if "banana" is NOT present in the set:

thisset = {"apple", "banana", "cherry"}  
  
print("banana" not in thisset)





```


## operations on set
الاضافة :
لاما ()method add  او ممكن من set مختلفة ل set تانية او من أي iterable تاني 
 ```python
 #add
my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}
#Add elements from `tropical` into `thisset`:

thisset = {"apple", "banana", "cherry"}  
tropical = {"pineapple", "mango", "papaya"}  
  
thisset.update(tropical)  
  
print(thisset)

#Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}  
mylist = ["kiwi", "orange"]  
  
thisset.update(mylist)  
  
print(thisset)





```
 لحذف عنصر بستخدم `remove()`, or the `discard()` method ممكن استعمل `()pop` ولكن دي بتمسح عشوائي وبترجع اللي مسحته لو حطيته في variable 

أما `()clear` بتمسح السيت كلها وترجعها فاضية و `del` بتمسحها تمام


```python
#مسح عنصر معين بـ remove() أو discard()

my_set.remove(3)  #If the item to remove does not exist, `remove()` will raise an error.
print(my_set)

#thisset = {"apple", "banana", "cherry"}  
  
thisset.discard("banana")  
#If the item to remove does not exist, `discard()` will **NOT** raise an error.
print(thisset)

#مسح عنصر عشوائي بـ pop()

popped_item = my_set.pop()
print(popped_item)  # هيشيل أي عنصر عشوائي
--------------------------------
thisset = {"apple", "banana", "cherry"}  
  
thisset.clear()  
  
print(thisset)#set()
-----------------------------
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) #this will raise an error because the set no longer exists


```


## Join Sets
There are several ways to join two or more sets in Python.

The `union()` and `update()` methods joins all items from both sets.

The `intersection()` method keeps ONLY the duplicates.

The `difference()` method keeps the items from the first set that are not in the other set(s).

The `symmetric_difference()` method keeps all items EXCEPT the duplicates.

- *Union*
بترجع سيت فيها عناصر من اللي موجودة في 2 ستيس وممكن نستخدم `|` بدل الميثود وهتؤدي نفس الوظيفة. وينفع نعمل كذا سيت مش اتنين بس وده عن طريق اننا بنحط `,` بين كل اتنين لو بنستخدم الميثود لكن لو بستخدم `|` بنحط كذا واحدة منهم 
السيت ينفع تعمل اتحاد من الانواع المختلفة زي الليست والتوبليس عادي ولكن ده بواسطة الميثود بس الoperator متنفعش
 ```python
set1 = {"a", "b", "c"}  
set2 = {1, 2, 3}  
  
set3 = set1.union(set2)  
print(set3)#{3, 1, 'c', 2, 'a', 'b'}
-------------------------------------------
set1 = {"a", "b", "c"}  
set2 = {1, 2, 3}   
set3 = set1 | set2  
print(set3)
----------------------------------
set1 = {"a", "b", "c"}  
set2 = {1, 2, 3}  
set3 = {"John", "Elena"}  
set4 = {"apple", "bananas", "cherry"}    
myset = set1.union(set2, set3, set4) = myset = set1 | set2 | set3 |set4
print(myset)#{banana, cherry, 'b', John, 'a', Elena, 1, apple, 3, 2, 'c'}


```
*Update*
بعمل ابديت للسيت القديمة بسيت جديدة ولكن مش برجع سيت جديدة
```python
set1 = {"a", "b" , "c"}  
set2 = {1, 2, 3}  
  
set1.update(set2)  
print(set1)#{1, 'a', 3, 2, 'b', 'c'}
```

*Intersection*
بحفظ المتشابه بس وبنرجعهم في سيت جديدة و ممكن نستخدم `&` هتؤدي نفس الوظيفة وبرضو `&` بتكون بين السيت وبعضها مش باقي الداتا تايب اما الميثود فلا 
```python
set1 = {"apple", "banana", "cherry"}  
set2 = {"google", "microsoft", "apple"}  
  
set3 = set1.intersection(set2)  
print(set3
```
intersection_update() -->دي ميثود بتعمل تقاطع وترجعه في سيت جديدة
The values `True` and `1` are considered the same value. The same goes for `False` and `0`.
*Difference*
الفرق وهو اني بشوف اللي موجود في السيت الاولى ومش موجود في السيت التانية وممكن استخدم `-` هتؤدي نفس الوظيفة وبرضو `-` بتكون بين السيت وبعضها مش باقي الداتا تايب اما الميثود فلا 
```python
set1 = {"apple", "banana", "cherry"}  
set2 = {"google", "microsoft", "apple"}  
  
set3 = set1.difference(set2)    
print(set3)#{'banana', 'cherry'}
--------------------------------------------
set1 = {"apple", "banana", "cherry"}  
set2 = {"google", "microsoft", "apple"}    
set3 = set1 - set2  
print(set3)#{'banana', 'cherry'}
```
The `difference_update()` method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

*Symmetric Differences*
ميثود بتحفظ بس العمناصر اللي مش موجودة في الاتنين سيت في نفس الوقت وممكن استخدم `^`
هتؤدي نفس الوظيفة وبرضو `^` بتكون بين السيت وبعضها مش باقي الداتا تايب اما الميثود فلا
```python
set1 = {"apple", "banana", "cherry"}  
set2 = {"google", "microsoft", "apple"}  
  
set3 = set1.symmetric_difference(set2)  
  
print(set3)#{'google', 'banana', 'microsoft', 'cherry'}
```

## Summary  of  Set Methods

| Method                        | Shortcut | Description                                                                    | الشرح                                                        |
| ----------------------------- | -------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| add()                         |          | Adds an element to the set                                                     | بيضيف حاجة جديدة للمجموعة                                    |
| clear()                       |          | Removes all the elements from the set                                          | بيفضي المجموعة خالص، بيمسح كل حاجة فيها                      |
| copy()                        |          | Returns a copy of the set                                                      | بيعمل نسخة زي المجموعة بالظبط                                |
| difference()                  | -        | Returns a set containing the difference between two or more sets               | بيطلع المجموعة اللي فيها الحاجات اللي مش مشتركة بين مجموعتين |
| difference_update()           | -=       | Removes the items in this set that are also included in another, specified set | بيمسح الحاجات اللي موجودة في مجموعة تانية من المجموعة دي     |
| discard()                     |          | Remove the specified item                                                      | بيمسح حاجة معينة لو موجودة، لو مش موجودة بيعديها             |
| intersection()                | &        | Returns a set, that is the intersection of two other sets                      | بيطلع المجموعة اللي فيها الحاجات المشتركة بين مجموعتين       |
| intersection_update()         | &=       | Removes the items in this set that are not present in other, specified set(s)  | بيخلي في المجموعة بس الحاجات المشتركة مع مجموعة تانية        |
| isdisjoint()                  |          | Returns whether two sets have a intersection or not                            | بيقولك المجموعتين دول فيهم حاجة مشتركة ولا لأ                |
| issubset()                    | <=       | Returns whether another set contains this set or not                           | بيقولك المجموعة دي جوا مجموعة تانية كلها ولا لأ              |
|                               | <        | Returns whether all items in this set is present in other, specified set(s)    | بيشوف كل حاجة في المجموعة دي موجودة في التانية ولا لأ        |
| issuperset()                  | >=       | Returns whether this set contains another set or not                           | بيقولك المجموعة دي فيها مجموعة تانية كلها ولا لأ             |
|                               | >        | Returns whether all items in other, specified set(s) is present in this set    | بيشوف كل حاجة في المجموعة التانية موجودة في دي ولا لأ        |
| pop()                         |          | Removes an element from the set                                                | بيمسح حاجة من المجموعة ومش بتختار إيه بالظبط                 |
| remove()                      |          | Removes the specified element                                                  | بيمسح حاجة معينة لو موجودة، لو مش موجودة بيطلع غلط           |
| symmetric_difference()        | ^        | Returns a set with the symmetric differences of two sets                       | بيطلع الحاجات اللي موجودة في مجموعة ومش في التانية والعكس    |
| symmetric_difference_update() | ^=       | Inserts the symmetric differences from this set and another                    | بيجدد المجموعة بالحاجات اللي مختلفة بينها وبين التانية       |
| union()                       |          | Return a set containing the union of sets                                      | بيجمع كل الحاجات من مجموعتين في مجموعة واحدة                 |
| update()                      | =        | Update the set with the union of this set and others                           | بيضيف للمجموعة كل الحاجات من مجموعات تانية                   |



  -ليه تستخدم الـ Set؟ 
  لو عايز تحذف التكرار من الليست بسرعة.  
  لو عايز تعمل عمليات زي الاتحاد والتقاطع على البيانات.  
  أسرع من array في البحث عن العناصر.

 ولو عندي list وعايز اشيل التكرار احولها ل set عن طريق ->`set(nameOfList)` مع set اقدر استخدم كذا حاجة :

- `map(function, iterable)`
    
    - بتستخدم لتطبيق دالة معينة على جميع العناصر الموجودة من غير ما استخدم for
        
    - `function` ->الحاجة اللهي هتطبق،`iterable`-> اللي هطبق عليها
        
    - ❌ميفضلش استخدمها لو شرط for معقد او لو اني هرجع اكتر من قيمة .
        
- `split()`
    
    - هي دالة بتقسم string ل list بناء على فاصل معين
        
    - مثلا لو عندي "Hello World Python" -> هتبقى كده ['Hello', 'World', 'Python']
        
    - الصيغة العامة string.split(separator, maxsplit) و الاتنين اختياري
        
    - `separator` ->عبارة عن الفاصل اللي بقسم بناء عليه
        
    - `maxsplit` ->عبارة عن اقصى عدد من عمليات الفصل
        
    - مثال:
        
        
        
        ```python
        text = "one two three four five"
        words = text.split(" ", 2)
        print(words)
        # ['one', 'two', 'three four five']
        ```
        
    - لو محددتش الاتنين دول خلاص هو هيفصل كل كلمة لوحدها و النص هيتقسم عن المسافة زي المثال اللي فوق
       


-------------------------------------------------------------------------
# Dictionary

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are _ordered_. In Python 3.6 and earlier, dictionaries are _unordered_.
  بيستخدم عشان اخزن الداتا على شكل ازواج يعني الحاجة والقيمة بتاعتها وهو بيتكون من حاجتين key  وvalue بتاعتها 
  مثال:
  ```python
person = {
    "name": "Ahmed",
    "age": 30,
    "city": "Cairo"
}

print(person["name"])  # الناتج: Ahmed
print(person["age"])   # الناتج: 30
 
```
-  (key): "name"، "age"، "city".
- (value): "Ahmed"، 30، "Cairo".

عشان احط زوج جديد يعني key-value pairs الموضوع سهل بنكتب كده 
```pyhton

person["country"] = "Egypt"
print(person)#{
#    "name": "Ahmed",
#    "age": 30,
#    "city": "Cairo",
#    "country": "Egypt"
#}

```
>Keys method to get key

The list of the keys is a _view_ of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

>Values method to get values

The list of the values is a _view_ of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
>use method items to get item

The returned list is a _view_ of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
```python
#Get a list of the keys:
x = thisdict.keys()

#Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {  
"brand": "Ford",  
"model": "Mustang",  
"year": 1964  
}  
  
x = car.keys()  
  
print(x) #dict_keys(['brand', 'model', 'year'])
  
car["color"] = "white"  
  
print(x) #dict_keys(['brand', 'model', 'year', 'color'])

---------------------------------
#Get a list of the values:
x = thisdict.values()

#Make a change in the original dictionary, and see that the values list gets updated as well:

car = {  
"brand": "Ford",  
"model": "Mustang",  
"year": 1964  
}  
  
x = car.values()  
  
print(x) #dict_values(['Ford', 'Mustang', 1964])
  
car["year"] = 2020  
  
print(x) #dict_values(['Ford', 'Mustang', 2020])
------------------------------------------------------------------------------
#Get a list of the key:value pairs
x = thisdict.items()
#Make a change in the original dictionary, and see that the items list gets updated as well:
car = {  
"brand": "Ford",  
"model": "Mustang",  
"year": 1964  
}  
  
x = car.items()  
  
print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]) 
  
car["year"] = 2020  
  
print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])





```
 عشان اغير   او اضيف value لاما بغيره على طول لاما بستخدم  method اسمها `()Update`
```python
thisdict = {  
  "brand": "Ford",  
  "model": "Mustang",  
  "year": 1964  
}  
thisdict["color"] = "red"  
print(thisdict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
```
عشان احذف عندي كذا ميثود منهم pop,del,clear,popitem
`pop()`-->
بتمسح عنصر من خلال الkey بتاعه عكس اللي كانت بتعمله في الباقي هي مش بترجع العنصر المحذوف هنا 
`popitem()`-->بتمسح اخر عنصر 
`del`--> 
يتمسح عنصر من خلال الkey بتاعه  وممكن تمسح الdictionary كله 
`clear()`--> بتفضي الديكشنري
```python
thisdict = {  
  "brand": "Ford",  
  "model": "Mustang",  
  "year": 1964  
}  
thisdict.pop("model")  
print(thisdict)#{'brand': 'Ford', 'year': 1964}
----------------------
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)#{'brand': 'Ford', 'model': 'Mustang'}
---------------------------------------
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)#{'brand': 'Ford', 'year': 1964}
-----------------------------------
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
---------------------------------
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)# {}

```


## Looping through dictionary
Print all key names in the dictionary, one by one:
```python
for x in thisdict:  
  print(x)
```
عندنا 3 طرق :
   -التكرار باستخدام Keys 
   ```python 
person = { "name": "Ahmed", "age": 30, "city": "Cairo" }
for key in person: 
    print(key)
#output:
name
age
city

```
   -التكرار باستخدام values
   ```python
   for value in person.values():
       print(value)

#output:
Ahmed
30
Cairo

```
 -التكرار باستخدام key-value pairs 
   باستخدم .items()
   ```python
   for key, value in person.items():
    print(f"{key} : {value}")
#output:
name : Ahmed
age : 30
city : Cairo

```

## Copy  a Dictionary

You cannot copy a dictionary simply by typing `dict2 = dict1`, because: `dict2` will only be a _reference_ to `dict1`, and changes made in `dict1` will automatically also be made in `dict2`. عشان كده بنستخدم ميثود اسمها copy() او dict
```python
thisdict = {  
  "brand": "Ford",  
  "model": "Mustang",  
  "year": 1964  
}  
mydict = thisdict.copy()  
print(mydict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
------------------
thisdict = {  
  "brand": "Ford",  
  "model": "Mustang",  
  "year": 1964  
}  
mydict = dict(thisdict)  
print(mydict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```
## Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.
```python
myfamily = {  
  "child1" : {  
    "name" : "Emil",  
    "year" : 2004  
  },  
  "child2" : {  
    "name" : "Tobias",  
    "year" : 2007  
  },  
  "child3" : {  
    "name" : "Linus",  
    "year" : 2011  
  }
  #or
  #Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
  child1 = {  
  "name" : "Emil",  
  "year" : 2004  
}  
child2 = {  
  "name" : "Tobias",  
  "year" : 2007  
}  
child3 = {  
  "name" : "Linus",  
  "year" : 2011  
}  
  
myfamily = {  
  "child1" : child1,  
  "child2" : child2,
```

عشان توصل لعنصر منهم بكتب اسم الdictionary و البداية 
```python
print(myfamily["child2"]["name"])
```
 to make loop using the `items()` method like this:
 ```python
 for x, obj in myfamily.items():  
  print(x)  
  
  for y in obj:  
    print(y + ':', obj[y])
```


## Methods
| Method       | Description                                                                                                 | شرح                                               |
| ------------ | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| clear()      | Removes all the elements from the dictionary                                                                | بيمسح كل حاجة جوة الدكشنري                        |
| copy()       | Returns a copy of the dictionary                                                                            | بيطلع نسخة زي الدكشنري بالظبط                     |
| fromkeys()   | Returns a dictionary with the specified keys and value                                                      | بيعمل دكشنري بمفاتيح وقيمة معينة                  |
| get()        | Returns the value of the specified key                                                                      | بيجيب قيمة المفتاح اللي بتدور عليه                |
| items()      | Returns a list containing a tuple for each key-value pair                                                   | بيطلع لستة فيها كل المفاتيح والقيم                |
| keys()       | Returns a list containing the dictionary's keys                                                             | بيطلع لستة بكل المفاتيح بس                        |
| pop()        | Removes the element with the specified key                                                                  | بيمسح العنصر اللي عنده المفتاح ده                 |
| popitem()    | Removes the last inserted key-value pair                                                                    | بيمسح آخر حاجة اتضافت للدكشنري                    |
| setdefault() | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value | بيجيب القيمة لو المفتاح موجود، لو مش موجود بيضيفه |
| update()     | Updates the dictionary with the specified key-value pairs                                                   | بيحدث الدكشنري بحاجات جديدة                       |
| values()     | Returns a list of all the values in the dictionary                                                          | بيطلع لستة بكل القيم اللي في الدكشنري             |


---------------------------------------------------------------------------
# Array
array --> مش مدعومة ببايثون بشكل مباشر ولكن ممكن تستخدم الليست مكانها
دلوقتي هنشرح ازاي نستعمل الليستس زي الاراي ولكن عشان تشتغل مع الاؤاي مباشرة ف بنستعمل مكتبة اسمها Numpy

  An array is a special variable, which can hold more than one value at a time. وكلهم من نفس النوع طبعا .
   ```python
cars = ["Ford", "Volvo", "BMW"]
print(len(cars)) # الناتج: 3
print(cars[0]) # الناتج: "Ford"
  #تعديل عنصر في  array
cars[0] = "Volly" 
print(cars[0]) # الناتج: "Volly"
# النكرار
for x in cars:
   print(x)
```
ممكن اعدلها او ادور على اللعنصر باستخدام الاندكس او اجيب `()len` 
**Note:** The length of an array is always one more than the highest array index.
لما اجي اضيف عنصر هستخدم `()append` و لو همسح هستخدم `()pop` او `()remove`
The list's `remove()` method only removes the first occurrence of the specified value.

## Array Methods

Python has a set of built-in methods that you can use on lists/arrays.

| Method    | Description                                                                  |     |
| --------- | ---------------------------------------------------------------------------- | --- |
| append()  | Adds an element at the end of the list                                       |     |
| clear()   | Removes all the elements from the list                                       |     |
| copy()    | Returns a copy of the list                                                   |     |
| count()   | Returns the number of elements with the specified value                      |     |
| extend()  | Add the elements of a list (or any iterable), to the end of the current list |     |
| index()   | Returns the index of the first element with the specified value              |     |
| insert()  | Adds an element at the specified position                                    |     |
| pop()     | Removes the element at the specified position                                |     |
| remove()  | Removes the first item with the specified value                              |     |
| reverse() | Reverses the order of the list                                               |     |
| sort()    | Sorts the list                                                               |     |
**Note:** Python does not have built-in support for Arrays, but Python Lists can be used instead.

---

# Comparison Table: List vs Tuple vs Set vs Dictionary vs Array in Python

| Feature                          | **List**                               | **Tuple**                        | **Set**                                 | **Dictionary**                              | **Array** (`array` module only)                                   |
| -------------------------------- | -------------------------------------- | -------------------------------- | --------------------------------------- | ------------------------------------------- | ----------------------------------------------------------------- |
| **Definition**                   | Ordered collection of mutable elements | Ordered but immutable collection | Unordered collection of unique elements | Unordered collection of **key-value pairs** | Array with elements of **the same type** only                     |
| **Mutable?**                     | ✅ Yes                                  | ❌ No                             | ✅ Yes                                   | ✅ Yes (keys are immutable)                  | ✅ Yes                                                             |
| **Ordered?**                     | ✅ Yes                                  | ✅ Yes                            | ❌ No                                    | ✅ No (Ordered from Python 3.7+)             | ✅ Yes                                                             |
| **Allows duplicates?**           | ✅ Yes                                  | ✅ Yes                            | ❌ No                                    | ❌ No (keys are unique, values can repeat)   | ✅ Yes                                                             |
| **Allows different data types?** | ✅ Yes                                  | ✅ Yes                            | ✅ Yes                                   | ✅ Yes (only values, keys must be immutable) | ❌ No (all elements must be of the same type)                      |
| **Can modify values?**           | ✅ Yes (Add/Remove/Modify)              | ❌ No (Immutable)                 | ✅ Yes (Add/Remove)                      | ✅ Yes (Add/Remove/Modify values)            | ✅ Yes                                                             |
| **Access by index?**             | ✅ Yes                                  | ✅ Yes                            | ❌ No (Unordered)                        | ✅ Yes (by keys)                             | ✅ Yes                                                             |
| **Best use case?**               | When you need **modifiable** data      | When you need **fixed** data     | When you need **unique values**         | When you need **key-value mapping**         | When you need **high-performance numerical operations**           |
| **Creation syntax**              | `my_list = [1, 2, 3]`                  | `my_tuple = (1, 2, 3)`           | `my_set = {1, 2, 3}`                    | `my_dict = {"key": "value"}`                | `from array import array` <br> `my_array = array("i", [1, 2, 3])` |


# Error Handling

- `try-except` للتعامل مع الأخطاء بسلاسة.
-  `try` تتيح لك اختبار جزء من الكود للتحقق من وجود أخطاء.
-  `except` تتيح لك التعامل مع الخطأ إذا حدث.
- `finally` تتيح لك تنفيذ كود معين **بغض النظر** عما إذا كان قد حدث خطأ أم لا.

## مثال على `try-except`
الكود التالي سيؤدي إلى  (Exception) لأن المتغير `x` غير معرّف:
```python
try:
    print(x)
except:
    print("Exception!")

```

## Finally

حتى لو حدث خطأ، فإن الكود داخل `finally` سيتم تنفيذه دائمًا:


```python

try:  
	print(x)
except:     
	print("wrong") 
finally:    
	print("code is finshed")

#output:
wrong
code is finshed

```

----------------------------------------------------------------------
# OOP

## Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
**How to create class**
use the keyword `class`
```python
class MyClass:  
  x = 5
```
**create Object**
```python
p1=MyClass()
print(p1.x)#5
```
### The __ init __ () Function
- All classes have a function called `__init__()`, which is always executed when the class is being initiated.
+ Use the `__init__()` function to assign values to object properties, or other operations that are necessary to do when the object is being created
- is called automatically
```pyhton
class Person:  
  def __init__(self, name, age):  
    self.name = name  
    self.age = age  
  
p1 = Person("John", 36)  
  
print(p1.name)  #John
print(p1.age)#36
```
### The __ str __ () function
- like `to string `in java
- function controls what should be returned when the class object is represented as a string.
- If the `__str__()` function is not set, the string representation of the object is returned:
```python
class Person:  
  def __init__(self, name, age):  
    self.name = name  
    self.age = age  
  
p1 = Person("John", 36)  
  
print(p1)#<__main__.Person object at 0x15039e602100>
------------------------------------
class Person:  
  def __init__(self, name, age):  
    self.name = name  
    self.age = age  
  
  def __str__(self):  
    return f"{self.name}({self.age})"  
  
p1 = Person("John", 36)  
  
print(p1)#John(36)
```
##### object can also contain Methods
### The self  Parameter
هي نفس this في جافا بستخدمهم عشان اشاور على object
- The `self` parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
- It does not have to be named `self`, you can call it whatever you like, but it has to be the first parameter of any function in the class
```python
class Person:  
  def __init__(mysillyobject, name, age):  
    mysillyobject.name = name  
    mysillyobject.age = age  
  
  def myfunc(abc):  
    print("Hello my name is " + abc.name)  
  
p1 = Person("John", 36)  
p1.myfunc()#Hello my name is John
```
###### Modify Object Properties
```python
p1.age = 40
```
###### Delete Object Properties
```python
del p1.age
```
###### Delete Object
```python
del p1
```
######  The pass Statement
لما اعمل كلاس مينفعش اسيه فاضي ولو سيبته فاضي هيطلّعلك خطأ (Syntax Error)  فعشان كده بنحط pass لتفادي الايرور.
```python
class Person:  
  pass
```
##  Inheritance
* Inheritance allows us to define a class that inherits all the methods and properties from another class.

- **Parent class** is the class being inherited from, also called base class.

- **Child class** is the class that inherits from another class, also called derived class
### Parent class
Any class can be a parent
```python
class Person:  
  def __init__(self, fname, lname):  
    self.firstname = fname  
    self.lastname = lname  
  
  def printname(self):  
    print(self.firstname, self.lastname)  
  
#Use the Person class to create an object, and then execute the printname method:  
  
x = Person("John", "Doe")  
x.printname()#John Doe
```
### Child class
Create a class named `Student`, which will inherit the properties and methods from the `Person` class:
```python
class Student(Person):  
  pass
```

#### And  the __ init __ () Function
لما عملنا وراثة من غير ما نضيف `()__int__` هو كده بس عنده خاصئص الاب من غير مايكون ليه خصائص خاصة بيه 
عشان كده لازم نضيف  `()__int__` ولكن لو ضفناها كده مباشرة child مش هيورث خصائص الاب تاني لانه هيحصله `overrides` اذا ماهو الحل 
الحل إننا نادي على `()__init__` بتاع الأب صراحةً باستخدام `()__Person.__init`
```python

class Student(Person):  
  def __init__(self, fname, lname):  
    Person.__init__(self, fname, lname)
    -----------------------------------
   class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()# Mike Olsen
```

#### Use the super() Function
`super()`
هنخلي الكلاس الفرعي يورث كل حاجة من الرئيسي من غير ما كل شوية تكتب اسم الرئيسي
هنا الـ `super().__init__(fname, lname)` بتعمل نفس شغل
`Person.__init__(self, fname, lname)

```python

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)  # Calls Person's __init__

student1 = Student("Ahmed", "Mohamed")
student1.printname()  # Outputs: Ahmed Mohamed
```
ولو عايز تضيف حاجة زيادة تقدر تستخدم `()super` وتضيف الخصائص الجديدة

```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, gradyear):
        super().__init__(fname, lname)      # Inherits from the parent
        self.graduationyear = gradyear      # Adds something new

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname}, graduated in {self.graduationyear}")

student1 = Student("Ahmed", "Mohamed", 2023)
student1.welcome()  # Outputs: Welcome Ahmed Mohamed, graduated in 2023
```
سوبر برضو مفيدة في multiple inheritance (more than one parent)
