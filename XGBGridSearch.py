def XGBGridSearch():
    """
    This function directly takes in the train, test data
    Returns a fitted grid search object
    """
    
    # to ensure those packages are imported
    import xgboost as xgb
    from sklearn.model_selection import GridSearchCV
    import numpy as np
    
    mdl = xgb.XGBClassifier(use_label_encoder=False)
    hyperparameters = {
        'eta':np.linspace(0, 0.2, 4),
        'min_child_weight': [0.5, 1, 1.5],
        'max_depth ': np.linspace(3, 10, 3),
        'subsample': [0.5, 0.75, 1],
        'eval_metric': ['rmse', 'logloss']
    }
    
    grid = GridSearchCV(mdl, hyperparameters, return_train_score = True)
    return grid