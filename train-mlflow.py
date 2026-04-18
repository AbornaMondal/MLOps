from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import mlflow
import mlflow.sklearn

# Start MLflow run
with mlflow.start_run():

    # Load dataset
    data = load_iris()
    X = data.data
    y = data.target

    # Parameters
    test_size = 0.2
    random_state = 42

    # Log parameters
    mlflow.log_param("test_size", test_size)
    mlflow.log_param("random_state", random_state)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Log metric
    mlflow.log_metric("accuracy", accuracy)

    # Save model locally
    joblib.dump(model, "model.pkl")

    # Log model in MLflow
    mlflow.sklearn.log_model(model, "model")

    print(f"Model saved. Accuracy: {accuracy}")