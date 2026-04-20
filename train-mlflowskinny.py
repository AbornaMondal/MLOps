# import mlflow
# import mlflow.sklearn
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import load_iris

# # Load data
# X, y = load_iris(return_X_y=True)

# # Split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# # Start MLflow run
# with mlflow.start_run():
#     model = RandomForestClassifier()
#     model.fit(X_train, y_train)

#     accuracy = model.score(X_test, y_test)

#     # Log metrics
#     mlflow.log_metric("accuracy", accuracy)

#     # Log model
#     mlflow.sklearn.log_model(model, "model")

#     print("Accuracy:", accuracy)