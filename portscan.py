import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
data_file = 'PortScan_vs_BENIGN.csv'
data = pd.read_csv(data_file, low_memory=False)

# Strip leading/trailing spaces from column names
data.columns = data.columns.str.strip()

# Define features and target variable
X = data.drop(columns='Label')
y = data['Label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Initialize and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Get feature importances
importances = model.feature_importances_

# Create a DataFrame for feature importances
importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importances
})

# Sort the DataFrame by importance
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Save to CSV
importance_df.to_csv('PortScan_importance.csv', index=False)

print("Feature importances saved to 'PortScan_importance.csv'")
