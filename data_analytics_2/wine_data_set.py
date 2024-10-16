# %%
"""

# **Analytics 2 : <font color=#DF4807> Python for Data Science**

"""

# %%
"""
Objectives:
1. Practice basic functions / operations in Python for Data science
2. Explore the Wine Quality Dataset (Cortez, Cerdeira, Almeida, Matos, & Reis, 2009)
3. Model wine quality using the best predictors.
"""

# %%
"""
## **Python Libraries for Data Science**
"""

# %%
#import libs
import pandas as pd # importing, analyzing, cleaning, exploring & manipulating data

# %%
"""
## **Loading the Data from url:**

"""

# %%
#Read in data from url
url='https://drive.google.com/file/d/1q_ss-nbcRfZ8QFpSMHaCWqCBEl8yGElX/view?usp=share_link'
file_id=url.split('/')[-2]
dwn_url='https://drive.google.com/uc?id=' + file_id
df = pd.read_csv(dwn_url, encoding='latin-1')
df.head()

# %%
"""
## **Data Exploration: Missing Values and Dependant Variable**

⭐: **Task 1: (15 min)**

A few things we have to check for:
<br> a) Check for null or missing values in data. Decide on the appropriate way to deal with them.
<br> b) Plot the dependant variable "Quality". What do the plots show us?
<br> c) Create a correlation chart so we can see the correlation of features against eachother. What intuitions can be drawn?
<br> d) Check for any outliers
<br> e) Take note of any interesting characteristics of the data.
"""

# %%
#your code here
df.describe()

# %%
df.info()

# %%
df.isnull()

# %%
len(df)

# %%
df.isna().sum()

# %%
import matplotlib.pyplot as plt
import seaborn as sns

numerical_columns = df.select_dtypes(include='number').columns.tolist()
plt.figure(figsize=(12, 8))
sns.heatmap(df[numerical_columns].isnull(), cmap='viridis', cbar=True)
plt.title('Heatmap Before Null Value Removal')
plt.show()


# %%
df.dropna(inplace=True)

# %%


plt.figure(figsize=(12, 8))
sns.heatmap(df.isnull(), cmap='viridis', cbar=True)
plt.title('Heatmap After Null Value Removal')
plt.show()


# %%
categorical_columns = df.select_dtypes(object).columns
print(categorical_columns)


# %%
from sklearn.preprocessing import OrdinalEncoder

# %%
oe=OrdinalEncoder()

# %%
df[categorical_columns]=oe.fit_transform(df[categorical_columns])

# %%
df.head()

# %%
for col in df.columns:
  Q1 = df[col].quantile(0.25)
  Q3 = df[col].quantile(0.75)
  IQR = Q3 - Q1  # Interquartile range

  # Define the lower and upper bounds for outliers
  lower_bound = Q1 - 1.5 * IQR
  upper_bound = Q3 + 1.5 * IQR

  outliers = df[(df[col] < lower_bound) | (df[col]> upper_bound)]
  print("Number of outliers:", outliers)



# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew
from sklearn.preprocessing import PowerTransformer

for col in df.columns:
  skewness =df[col].skew()
  sns.histplot(data=df, x=col,kde=True)
  print(f"{col}: {skewness}")
  plt.show()

# %%
import pandas as pd
from sklearn.preprocessing import PowerTransformer


numerical_features = df.select_dtypes(include='number').columns.tolist()

numerical_features.remove('quality')
numerical_features.remove('type')

pt = PowerTransformer(method='yeo-johnson')

df_transformed = df.copy()

for col in numerical_features:
    df_transformed[col] = pt.fit_transform(df[[col]])

print(df_transformed.head())

# %%
len(df)

# %%
for col in df_transformed.columns:
  Q1 = df_transformed[col].quantile(0.25)
  Q3 = df_transformed[col].quantile(0.75)
  IQR = Q3 - Q1

  lower_bound = Q1 - 1.5 * IQR
  upper_bound = Q3 + 1.5 * IQR

  outliers = df[(df[col] < lower_bound) | (df[col]> upper_bound)]
  print("Number of outliers:", outliers)

# %%
for col in df_transformed.columns:
  skewness =df_transformed[col].skew()
  sns.histplot(data=df_transformed, x=col,kde=True)
  print(f"{col}: {skewness}")
  plt.show()

# %%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.figure(figsize=(8, 6))
sns.histplot(df_transformed['quality'], bins=10, kde=False, discrete=True, color='gray')
plt.title('Distribution of Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Frequency')
plt.xticks(range(0, 11))
plt.show()


# %%
import matplotlib.pyplot as plt
import seaborn as sns

numerical_features = df_transformed.select_dtypes(include=['number'])

correlation_matrix = numerical_features.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Wine Quality Features')
plt.show()

# %%
"""
## **Data Preparation: Sorting and Aggregating**

⭐: **Task 2: (15 min)**
<br> a) Randomly select 70% of your data. This will be your training data.
<br> b) Transfer the "Quality" column from your training data to your yTrain.
<br> c) Using the remaining 30%, do the same for your test data.

<br> Replace "None" with your own code.
"""

# %%
# Your code here:
import pandas as pd
from sklearn.model_selection import train_test_split

X = df_transformed.drop('quality',axis=1)  # Features
y = df_transformed['quality']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(f"Training data shape: {X_train.shape}, yTrain shape: {y_train.shape}")
print(f"Test data shape: {X_test.shape}, yTest shape: {y_test.shape}")

# %%
"""

⭐: **Task 3: (5 min)**
<br> a) create new data frame called meanData by aggregating df to mean.
<br> Replace "None" with your own code.
"""

# %%
meanData = None

meanData = df_transformed.mean(numeric_only=True)

meanData = pd.DataFrame(meanData, columns=['Mean'])

print(meanData)


# %%
"""
⭐: **Task 4: (15 min)**
Model Fitting:

Given your data, what model do you think makes sense? Select a model and fit your data. Also evaluate your model with an appropriate metric.




"""

# %%
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

rf_classifier = RandomForestClassifier(n_estimators=100)

rf_classifier.fit(X_train, y_train)

y_pred = rf_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(confusion)
print("Classification Report:")
print(report)


# %%
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

linear_model = LinearRegression()

linear_model.fit(X_train, y_train)

yPred_linear = linear_model.predict(X_test)

mse = mean_squared_error(y_test, yPred_linear)
r2 = r2_score(y_test, yPred_linear)
print(f"Linear Regression Mean Squared Error: {mse:.2f}")
print(f"Linear Regression R-squared: {r2:.2f}")


# %%
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

logistic_model = LogisticRegression(max_iter=1000, random_state=42)

logistic_model.fit(X_train, y_train)

yPred_logistic = logistic_model.predict(X_test)

accuracy_logistic = accuracy_score(y_test, yPred_logistic)
print(f"Logistic Regression Accuracy: {accuracy_logistic * 100:.2f}%")

print("Logistic Regression Classification Report:")
print(classification_report(y_test, yPred_logistic))

conf_matrix_logistic = confusion_matrix(y_test, yPred_logistic)
print("Logistic Regression Confusion Matrix:")
print(conf_matrix_logistic)


# %%
"""
## **Visualizing your fit:**
⭐: **Task 5: (15 min)**
Data Visualitzaions:

Visualize your model as compared to the data. What intuitions can you draw from the visual?

"""

# %%
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay

def plot_confusion_matrix(y_true, y_pred, model_name):
    plt.figure(figsize=(8, 6))
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=sorted(y.unique()), yticklabels=sorted(y.unique()))
    plt.title(f'Confusion Matrix for {model_name}')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()

plot_confusion_matrix(y_test, y_pred, 'Random Forest')

plot_confusion_matrix(y_test, yPred_logistic, 'Logistic Regression')

plt.figure(figsize=(8, 6))
plt.scatter(y_test, yPred_linear, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)

plt.title('Predicted vs Actual Values (Linear Regression)')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(yPred_logistic, bins=10, kde=True)
plt.title('Distribution of Predictions (Logistic Regression)')
plt.xlabel('Predicted Quality')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
sns.histplot(y_pred, bins=10, kde=True)
plt.title('Distribution of Predictions (Random Forest)')
plt.xlabel('Predicted Quality')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


importances = rf_classifier.feature_importances_
feature_names = X.columns
plt.figure(figsize=(10, 6))
sns.barplot(x=importances, y=feature_names)
plt.title('Feature Importance')
plt.xlabel('Importance Score')
plt.ylabel('Features')
plt.show()


# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 1. Count of Wine Types by Quality - Proportion
count_data = df_transformed.groupby(['quality', 'type']).size().unstack(fill_value=0)
count_data = count_data.divide(count_data.sum(axis=1), axis=0)  # Normalize to proportions

plt.figure(figsize=(10, 6))
count_data.plot(kind='bar', stacked=True)
plt.title('Proportion of Types by Quality Rating', fontsize=16)
plt.xlabel('Quality Rating', fontsize=14)
plt.ylabel('Proportion', fontsize=14)
plt.legend(title='Wine Type')
plt.tight_layout()
plt.show()

# 2. Boxplot of Volatile Acidity by Quality Rating
plt.figure(figsize=(10, 6))
sns.boxplot(x='quality', y='volatile acidity', data=df_transformed, palette='viridis')
plt.title('Volatile Acidity by Quality Rating', fontsize=16)
plt.xlabel('Quality Rating', fontsize=14)
plt.ylabel('Volatile Acidity', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()

# 3. Average Fixed Acidity, Volatile Acidity, and Citric Acid by Quality
avg_attributes = df_transformed.groupby('quality')[['fixed acidity', 'volatile acidity', 'citric acid']].mean().reset_index()

plt.figure(figsize=(10, 6))
avg_attributes.plot(x='quality', kind='bar', color=['lightblue', 'lightgreen', 'salmon'])
plt.title('Average Fixed Acidity, Volatile Acidity, and Citric Acid by Quality Rating', fontsize=16)
plt.xlabel('Quality Rating', fontsize=14)
plt.ylabel('Average Value', fontsize=14)
plt.xticks(rotation=0)
plt.legend(title='Attribute')
plt.tight_layout()
plt.show()

