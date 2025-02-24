
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
  عبارة عن if , else , elif  معندناش  else if زي جافا  ولكن اسمها elif
  
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

### 🛠 **أمثلة على `range()`**
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
# Lambda Expressions

هي عبارة عن فانكشن مجهولة من غير اسم بتتكتب في سطر واحد وبتاخد أي عدد من arguments ولكن جواها one expression

syntax:
```python
square = lambda x: x ** 2
print(square(5))  # Output: 25

```
تعتبر اختصار لكود عكس def ، مفيدة في أي فانكشن بسيطة و تستخدم في الاغلب مع map() و filter() و sorted()`
مثال:
```python
add = lambda x, y: x + y
print(add(3, 5))  # الناتج: 8

```


# list 

Lists are used to store multiple items in a single variable
يعني بتخزن كذا datatype في list واحدة عادي و طبعا ده غير ال array لأنها لازم يكونوا كلهم نفس النوع

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
عندي فانكشن اسمها append() ودي بنضيف عنصر في نهاية الليست 

```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ['apple', 'banana', 'cherry', 'orange']
```

عندي فانكشن اسمها remove() ودي بتحذف عنصر معين

```python
List2 = ["apple", "banana", "cherry"] 
List2.remove("banana") 
print(List2) # ['apple', 'cherry']
```

عندي فانكشن اسمها Clear() ودي بتمسح محتويات الليست 

```python
List2 = ["apple", "banana", "cherry"] 
List2.clear() 
print(List2) # []
```

في طريقتين لعرض list لاما for x in List3 وده اسمه تكرار مباشر وده مش بيعدل او ان اعرضها بالانديكس 
for i in range(len(List3))  وده اقدر اعدل القيم 

```python
List3 = ["apple", "banana", "cherry"]
for x in List3: 
    print(x) # apple # banana # cherry 
List3 = ["apple", "banana", "cherry"] 
for i in range(len(List3)):
    print(List3[i]) # apple # banana # cherry


```


# Dictionaries
  بيستخدم عشان اخزن الداتا على شكل ازواج يعني الحاجة والقيمة بتاعتها وهو بيتكةن من حاجتين key  وvalue بتاعتها 
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
print(person)
```
--output
```python
{
    "name": "Ahmed",
    "age": 30,
    "city": "Cairo",
    "country": "Egypt"
}

```
## Looping through dictionary
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

# Array
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

# Set

هي مجموعة لا تحتوي على تكرار ودي من اهم مميزاتها
- الـ `Set` في بايثون  زي الكيس البلونات، بتحط فيه حاجات بس من غير ترتيب وماينفعش تحط نفس الحاجة مرتين! 
- بتتكتب `{}` أو بـ `set()`. 
- **ملهاش Index** يعني مش هتعرف تجيب عنصر بمكانه زي الـ List. 
- **بتتعدل** بس مش بتقبل تكرار. 
-  زاي تعمل Set؟ 
```python 
my_set = {1, 2, 3, 4, 5}
print(my_set)
# {1, 2, 3, 4, 5}
```
-لو كررت رقم، بايثون هيمسح التكرار لوحده
```python
my_set = {1, 2, 2, 3, 4, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}

```

## operations on set
 ```python
 #add
my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}

#مسح عنصر معين بـ remove() أو discard()

my_set.remove(3)  # لو العنصر مش موجود هيعمل Error
print(my_set)

my_set.remove(3)  # لو العنصر مش موجود هيعمل Error
print(my_set)

#مسح عنصر عشوائي بـ pop()

popped_item = my_set.pop()
print(popped_item)  # هيشيل أي عنصر عشوائي

```

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
        
- `symmetric_difference()`
    
    - بستخدمها عشان الاقي العناصر الموجودة في واحدة من اتنين set ولكن مش مشتركة بينهم وبترجع اللي مش مشترك بينهم
        
    - بتساوي XOR (^)
        
    - `set1.symmetric_difference(set2)= set1 ^ set2`
        
    - الفرق بينها وبين difference() :
        
        - `s.symmetric_difference(ss)` أو `s ^ ss` يُرجع القيم غير المشتركة فقط بين المجموعتين.
            
        - `difference()` يُرجع القيم الخاصة بمجوعة واحدة فقط دون الأخرى.
            

# Tuble
  هو شبه الليست ولكن مش بيقبل التعديل 
  ```python 
  fruits = ("apple", "banana", "cherry")
  print(fruits)
  #output
  ('apple', 'banana', 'cherry')

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
عشان اقدر اعدل على tuble لازم الاول احوله ل list اعدل عليه وبعدين ارجعه تاتي :
 ```python
fruits_list = list(fruits)  # تحويل tuble to list
fruits_list.append("orange")  # إضافة عنصر جديد
fruits = tuple(fruits_list)  # تحويل list to tuble
print(fruits)
#output:
('apple', 'banana', 'cherry', 'orange')

```
 لو هحذفه تماما :
 ```python
 del fruits

```




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
