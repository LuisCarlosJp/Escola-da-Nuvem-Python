from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
# Carregamento do Dataset
data = load_breast_cancer()

# Divide os dados em 75% para treino e 25% para teste
X_train, X_test, y_train, y_test = train_test_split(
                                    data.data, data.target, test_size=0.25, random_state=42)

# Cria e configura o classificador Random Forest
model = RandomForestClassifier(
    n_estimators = 100,
    criterion = 'entropy',
    max_depth= None,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features='sqrt',
    random_state=42,
    n_jobs=-1
)

# Treina o modelo com os dados de treinamento
model.fit(X_train, y_train)

# Realiza a predição com os dados de teste
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Calcular métricas
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_proba)

# Exibir resultados
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1-Score: {f1:.2f}')
print(f'AUC-ROC: {auc:.2f}')