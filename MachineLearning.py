import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

attack_types = ["Bot", "DDoS", "DoS GoldenEye", "DoS Hulk", "DoS Slowhttptest", "DoS slowloris", "FTP-Patator",
                "PortScan", "SSH-Patator"]
benign_type = "BENIGN"
results = []

for attack_type in attack_types:
    importance_file = f"{attack_type}_importance.csv"
    data_file = f"{attack_type}_vs_{benign_type}.csv"

    # Handle missing importance file
    try:
        importance_data = pd.read_csv(importance_file, low_memory=False)
    except FileNotFoundError:
        print(f"Importance file not found: {importance_file}")
        continue

    # Handle missing data file
    try:
        data = pd.read_csv(data_file, low_memory=False)
    except FileNotFoundError:
        print(f"Data file not found: {data_file}")
        continue

    # Strip leading/trailing spaces from column names
    importance_data.columns = importance_data.columns.str.strip()
    data.columns = data.columns.str.strip()

    # Print cleaned column names for debugging
    print(f"Cleaned Data file columns for {attack_type}: {data.columns}")

    # Select top features
    selected_features = importance_data['Feature'][:3].tolist()

    # Check the existence of required columns
    required_columns = selected_features + ['Label']
    for col in required_columns:
        if col not in data.columns:
            print(f"Missing column in {data_file}: {col}")
            continue

    try:
        selected_data = data[selected_features + ['Label']]
    except KeyError as e:
        missing_cols = list(set(required_columns) - set(data.columns))
        print(f"Missing columns in {data_file}: {missing_cols}")
        print("Available columns:", data.columns)
        continue

    # Prepare data for training
    X = selected_data[selected_features]
    y = selected_data['Label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

    # Train and evaluate models
    nb_model = GaussianNB()
    nb_model.fit(X_train, y_train)

    qda_model = QuadraticDiscriminantAnalysis()
    qda_model.fit(X_train, y_train)

    mlp_model = MLPClassifier(random_state=42, max_iter=1000, learning_rate_init=0.001)
    mlp_model.fit(X_train, y_train)

    nb_preds = nb_model.predict(X_test)
    qda_preds = qda_model.predict(X_test)
    mlp_preds = mlp_model.predict(X_test)

    nb_accuracy = accuracy_score(y_test, nb_preds)
    qda_accuracy = accuracy_score(y_test, qda_preds)
    mlp_accuracy = accuracy_score(y_test, mlp_preds)

    result_dict = {
        'Attack Type': attack_type,
        'Naive Bayes Accuracy': nb_accuracy,
        'QDA Accuracy': qda_accuracy,
        'MLP Accuracy': mlp_accuracy
    }
    results.append(result_dict)

results_df = pd.DataFrame(results)
print(results_df)


