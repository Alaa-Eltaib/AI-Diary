# Learn-Python-
Welcome to Learn-Python, a beginner-friendly repository for understanding the basics of Python! 🐍✨

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





-الجداول دي كلها من هنا [[Python Operators](https://www.w3schools.com/python/python_operators.asp)]


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


# Loops
 عندنا جملتين وهم continue  , break ودول نفس شغلانتهم في أي لوب 
 - break , With the break statement we can stop the loop even if the while condition is true.
 - continue, With the continue statement we can stop the current iteration, and continue with the next
## While
 زي أي while اخدناها قبل كده فرق طريقة الكتابة بس 
```python
i = 1 
while i < 6:
    print(i) i += 1
```
## For Loop

لما باجي اعمل for بكتبه كده -> `for i in range(n)` لو عايزة ازود الاندكس اللي هو i او ابدا الانديكس بواحد مثلا لانه تلقائي يبدأ بزيرو اكتب كده `range(1,n+1)` انا كده خليت i=1 وخليت n ينتهي عند نفسه كأني قولت =n في c++.
```python
for x in range(6): 
    if x == 3: 
        break  
 print(x)
```




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



# Set

هي مجموعة لا تحتوي على تكرار ودي من اهم مميزاتها ولو عندي list وعايز اشيل التكرار احولها ل set عن طريق ->`set(nameOfList)` مع set اقدر استخدم كذا حاجة :

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
            

---
