import json
import joblib
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data_path = Path("data") / "data.csv"
params_path = Path("params.yaml")
metrics_path = Path("metrics.json")


def load_train_params(path: Path) -> dict[str, float | int]:
    params: dict[str, float | int] = {}
    inside_train_block = False

    with path.open("r", encoding="utf-8") as params_file:
        for raw_line in params_file:
            line = raw_line.rstrip()

            if not line or line.lstrip().startswith("#"):
                continue

            if line == "train:":
                inside_train_block = True
                continue

            if not inside_train_block or not line.startswith("  "):
                continue

            key, value = [part.strip() for part in line.split(":", maxsplit=1)]
            params[key] = float(value) if "." in value else int(value)

    return params


params = load_train_params(params_path)

df = pd.read_csv(data_path)

X = df.drop(columns=["target"])
y = df["target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=params["test_size"],
    random_state=params["random_state"],
)

# Train model
model = RandomForestClassifier(
    n_estimators=params["n_estimators"],
    random_state=params["random_state"],
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Save model
joblib.dump(model, "model.pkl")

with metrics_path.open("w", encoding="utf-8") as metrics_file:
    json.dump({"accuracy": accuracy}, metrics_file, indent=2)

print(f"Model trained from {data_path} and saved as model.pkl")
print(f"Accuracy: {accuracy:.4f}")
