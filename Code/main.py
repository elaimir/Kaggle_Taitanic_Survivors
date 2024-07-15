import pandas as pd
from src.data_cleaning import clean_data
from src.feature_engineering import prepare_features
from src.model_training import train_model, find_best_max_depth
from src.model_evaluation import evaluate_model
from src.visualizations import plot_histograms, plot_count, plot_correlation_heatmap, plot_additional
from src.additional_statistics import calculate_statistics

# Load data
train_data = pd.read_csv('data/train.csv')
test_data = pd.read_csv('data/test.csv')

# Clean data
train_cleaned = clean_data(train_data)
test_cleaned = clean_data(test_data)

# Prepare features for model training and testing
X_train, X_test = prepare_features(train_cleaned, test_cleaned)
y_train = train_cleaned['Survived']

# Find the best value for max_depth in the RandomForest model
candidate_max_leaf_nodes = [5, 25, 50, 100, 220, 250, 400, 500]
best_max_depth = find_best_max_depth(X_train, y_train, candidate_max_leaf_nodes)
print("Best max_depth:", best_max_depth)

# Train the model with the best max_depth
model = train_model(X_train, y_train, best_max_depth)

# Evaluate the trained model
evaluate_model(model, X_train, y_train)

# Visualize data distributions and relationships
plot_histograms(train_cleaned, ['Age', 'Fare'])
plot_count(train_cleaned, 'Pclass')
plot_count(train_cleaned, 'Survived', hue='Sex')
plot_correlation_heatmap(train_cleaned, ['Age', 'Fare', 'Pclass'])
plot_additional(train_cleaned)

# Calculate additional statistical metrics
calculate_statistics(train_cleaned)
