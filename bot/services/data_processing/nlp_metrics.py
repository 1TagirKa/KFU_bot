from sklearn.metrics import precision_recall_fscore_support, accuracy_score

def calculate_nlp_metrics(y_true, y_pred):
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average='binary')
    accuracy = accuracy_score(y_true, y_pred)
    return {'precision': precision, 'recall': recall, 'f1_score': f1, 'accuracy': accuracy}
