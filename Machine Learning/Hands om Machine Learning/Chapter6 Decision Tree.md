# 🌳 Chapter 6: Decision Trees

##  Overview
**Decision Tree** is a supervised learning algorithm that splits data based on feature values to make predictions.

هي ببساطة عبارة عن سلسلة من **`if-else rules`** تبدأ من الـ **Root Node** وتنتهي عند الـ **Leaf Node** عشان توصل للتنبؤ النهائي (Prediction).

---

##  Node Types (مكونات الشجرة)
الشجرة بتتكون من 3 أنواع رئيسية من الـ Nodes:

1.  **Root Node (Top):**
    * هي "الجذر" بتاعنا، أول نقطة في الشجرة من فوق.
2.  **Split Node (Internal Node):**
    * هي النقطة اللي بتسأل سؤال (Ask Question) عشان تقسم البيانات وتوديها يمين أو شمال.
3.  **Leaf Node (Terminal Node):**
    * دي النهاية، الـ Node اللي بتدينا **التنبؤ النهائي (Gives Prediction)** ومبتتقسمش تاني.

---

## Impurity Metrics (قياس النقاء)
عشان الشجرة تقرر هتقسم الداتا إزاي، بتستخدم مقاييس (Metrics) عشان تشوف الـ Node دي "نقية" ولا "مختلطة".

### 1. Gini Impurity (Default in Sklearn)
* **Gini measures how mixed the classes are in a node.**
* بيقيس مدى اختلاط الـ Classes داخل الـ Node.
* **القاعدة:**
    * If **Gini = 0** $\rightarrow$ **Pure Node** (نقية تماماً، يعني كل الداتا اللي فيها من نوع واحد).
    * كل ما الرقم **يزيد** عن الصفر $\rightarrow$ الاختلاط (Impurity) بيزيد.
    * *ملحوظة:* الـ Gini حسابه أسرع شوية من الـ Entropy.

### 2. Entropy
* **Measures the disorder or uncertainty.**
* بيقيس العشوائية أو عدم التأكد في البيانات، وبرضه هدفنا نوصله لـ **Zero**.

---

##  The CART Algorithm
**CART** (Classification and Regression Tree) is the algorithm used to build the tree.
* بيشتغل بإننا نقسم البيانات باستخدام **Feature** معينة و **Threshold** معين.
* الهدف: اختيار التقسيمة اللي **تقلل الـ Impurity (Minimize Impurity)** لأقصى درجة.

---

##  Regularization (علاج الـ Overfitting)
**Mushkila:** Decision Trees easily **overfit** if not regularized.
(الشجرة ممكن تحفظ الداتا زيادة عن اللزوم لو سبناها براحتها).

**Solutions (Hyperparameters):**
بنتحكم في حجم الشجرة باستخدام باراميترز زي:
* `max_depth`: أقصى عمق للشجرة.
* `min_samples_split`: أقل عدد عينات عشان نقسم الـ Node.
* `min_samples_leaf`: أقل عدد عينات مسموح بيه في الـ Leaf الأخيرة.
* `max_leaf_nodes`: أقصى عدد للـ Leaves.

---

##  Regression Trees
الـ Decision Tree مش بس للتصنيف (Classification)، بتنفع كمان للـ Regression.
* **Prediction:** الشجرة بتتوقع قيمة رقمية (Numerical Value).
* **How?** القيمة دي بتكون عبارة عن **متوسط (Average)** القيم الموجودة في الـ Target للبيانات اللي وقعت في الـ Leaf دي.
* **Cost Function:** بنستخدم الـ **MSE (Mean Squared Error)** بدل الـ Gini.

---

##  Limitations & Solutions
رغم قوتها، الـ Decision Trees فيها عيبين كبار:

| Limitation (العيب) | Explanation (الشرح) | Solution (الحل) |
| :--- | :--- | :--- |
| **1. High Variance** | حساسة جداً للداتا؛ أي تغيير بسيط في البيانات بيغير شكل الشجرة تماماً. | **Random Forest** (نستخدم كذا شجرة مع بعض). |
| **2. Sensitive to Data Orientation** | بتحب الخطوط المستقيمة (Orthogonal boundaries)، فلو الداتا مايلة بيبقى صعب عليها تفصلها. | **PCA** (نلف الداتا الأول عشان نسهلها على الشجرة). |


## 🌲 vs. 🌲🌲 Decision Tree vs. Random Forest

مقارنة سريعة توضح الفرق بين استخدام شجرة واحدة ومجموعة أشجار (Ensemble):

| Feature (الميزة) | Decision Tree (شجرة واحدة) | Random Forest (مجموعة أشجار) |
| :--- | :--- | :--- |
| **Type** | Single Learner (خوارزمية فردية). | Ensemble Learner (تجميع لعدة خوارزميات). |
| **Overfitting** | **High Risk** <br> (عرضة جداً للحفظ لو مش معمولة Regularization). | **Low Risk** <br> (بتقلل الـ Variance عن طريق أخذ متوسط توقعات الأشجار). |
| **Interpretability** | **High (White Box)** <br> (سهل جداً نرسمها ونفهم قواعد الـ If-Else بتاعتها). | **Low (Black Box)** <br> (صعب نتخيل أو نفسر قرار طالع من 100 شجرة مع بعض). |
| **Speed** | **Fast** to train & predict. | **Slower** to train (بتحتاج وقت وموارد أكتر). |
| **Performance** | Good for simple datasets. | Better accuracy for complex/non-linear data. |