import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score


data = pd.read_csv('titanic.csv')
data.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)

X = data.drop('Survived', axis=1)
y = data['Survived']

# рaздел дaнных нa oбyчающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# прeoбразoвание кoлoнoк
numeric_features = ['Age', 'Fare']
categorical_features = ['Pclass', 'Gender', 'SibSp', 'Parch']

# coздaниe пацплaйнов для чиceл и катeгорий
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

pipeline_log_reg = Pipeline(steps=[('preprocessor', preprocessor),
                                   ('classifier', LogisticRegression())])

pipeline_knn = Pipeline(steps=[('preprocessor', preprocessor),
                               ('classifier', KNeighborsClassifier())])

# обучение и предсказание
pipeline_log_reg.fit(X_train, y_train)
pipeline_knn.fit(X_train, y_train)
y_pred_log_reg = pipeline_log_reg.predict(X_test)
y_pred_knn = pipeline_knn.predict(X_test)

# рассчет F1-меры
f1_log_reg = f1_score(y_test, y_pred_log_reg)
f1_knn = f1_score(y_test, y_pred_knn)

print(f"F1-мера логистической регрессии - {f1_log_reg}")
print(f"F1-мера метода ближайших соседей - {f1_knn}")
