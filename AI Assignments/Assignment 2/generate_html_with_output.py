"""
Generate HTML submission file with actual script output
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, confusion_matrix, classification_report,
                             roc_curve, auc, roc_auc_score)
import warnings
warnings.filterwarnings('ignore')
import io
import sys
from contextlib import redirect_stdout

class CryotherapyAnalyzer:
    """Comprehensive analysis and classification of cryotherapy dataset."""
    
    def __init__(self, csv_path):
        """Initialize the analyzer with dataset."""
        self.df = pd.read_csv(csv_path)
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.models = {}
        self.results = {}
        
    def explore_dataset(self):
        """Perform exploratory data analysis."""
        print("=" * 80)
        print("DATASET EXPLORATION")
        print("=" * 80)
        
        print(f"\nDataset Shape: {self.df.shape}")
        print(f"\nFirst 5 rows:\n{self.df.head()}")
        print(f"\nDataset Info:")
        print(self.df.info())
        print(f"\nStatistical Summary:\n{self.df.describe()}")
        print(f"\nMissing Values:\n{self.df.isnull().sum()}")
        print(f"\nTarget Variable Distribution:")
        print(self.df['Result_of_Treatment'].value_counts())
        print(f"\nTarget Variable Percentages:")
        print((self.df['Result_of_Treatment'].value_counts(normalize=True) * 100))
        
    def prepare_data(self, test_size=0.2, random_state=42):
        """Prepare data for modeling."""
        print("\n" + "=" * 80)
        print("DATA PREPARATION")
        print("=" * 80)
        
        # Separate features and target
        self.X = self.df.drop('Result_of_Treatment', axis=1)
        self.y = self.df['Result_of_Treatment']
        
        print(f"\nFeatures (X): {self.X.shape}")
        print(f"Target (y): {self.y.shape}")
        print(f"\nFeature columns: {self.X.columns.tolist()}")
        
        # Split data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state, stratify=self.y
        )
        
        print(f"\nTraining set size: {self.X_train.shape[0]}")
        print(f"Testing set size: {self.X_test.shape[0]}")
        print(f"\nTraining set class distribution:")
        print(self.y_train.value_counts())
        
    def train_decision_tree(self):
        """Train Decision Tree Classifier."""
        print("\n" + "=" * 80)
        print("DECISION TREE CLASSIFIER")
        print("=" * 80)
        
        dt_classifier = DecisionTreeClassifier(random_state=42, max_depth=10, 
                                              min_samples_split=5, min_samples_leaf=2)
        dt_classifier.fit(self.X_train, self.y_train)
        self.models['Decision Tree'] = dt_classifier
        
        y_pred = dt_classifier.predict(self.X_test)
        self._evaluate_model('Decision Tree', y_pred, dt_classifier)
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'Feature': self.X.columns,
            'Importance': dt_classifier.feature_importances_
        }).sort_values('Importance', ascending=False)
        
        print(f"\nFeature Importance:\n{feature_importance}")
        
    def train_random_forest(self):
        """Train Random Forest Classifier."""
        print("\n" + "=" * 80)
        print("RANDOM FOREST CLASSIFIER")
        print("=" * 80)
        
        rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42,
                                             max_depth=15, min_samples_split=5,
                                             min_samples_leaf=2)
        rf_classifier.fit(self.X_train, self.y_train)
        self.models['Random Forest'] = rf_classifier
        
        y_pred = rf_classifier.predict(self.X_test)
        self._evaluate_model('Random Forest', y_pred, rf_classifier)
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'Feature': self.X.columns,
            'Importance': rf_classifier.feature_importances_
        }).sort_values('Importance', ascending=False)
        
        print(f"\nFeature Importance:\n{feature_importance}")
        
    def train_svm(self):
        """Train Support Vector Machine."""
        print("\n" + "=" * 80)
        print("SUPPORT VECTOR MACHINE (SVM)")
        print("=" * 80)
        
        # Scale features for SVM
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(self.X_train)
        X_test_scaled = scaler.transform(self.X_test)
        
        svm_classifier = SVC(kernel='rbf', random_state=42, probability=True)
        svm_classifier.fit(X_train_scaled, self.y_train)
        self.models['SVM'] = (svm_classifier, scaler)
        
        y_pred = svm_classifier.predict(X_test_scaled)
        self._evaluate_model('SVM', y_pred, svm_classifier, X_test_scaled)
        
    def train_naive_bayes(self):
        """Train Naive Bayes Classifier."""
        print("\n" + "=" * 80)
        print("NAIVE BAYES CLASSIFIER")
        print("=" * 80)
        
        nb_classifier = GaussianNB()
        nb_classifier.fit(self.X_train, self.y_train)
        self.models['Naive Bayes'] = nb_classifier
        
        y_pred = nb_classifier.predict(self.X_test)
        self._evaluate_model('Naive Bayes', y_pred, nb_classifier)
        
    def train_knn(self):
        """Train K-Nearest Neighbors."""
        print("\n" + "=" * 80)
        print("K-NEAREST NEIGHBORS (KNN)")
        print("=" * 80)
        
        # Scale features for KNN
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(self.X_train)
        X_test_scaled = scaler.transform(self.X_test)
        
        knn_classifier = KNeighborsClassifier(n_neighbors=5)
        knn_classifier.fit(X_train_scaled, self.y_train)
        self.models['KNN'] = (knn_classifier, scaler)
        
        y_pred = knn_classifier.predict(X_test_scaled)
        self._evaluate_model('KNN', y_pred, knn_classifier, X_test_scaled)
        
    def train_neural_network(self):
        """Train Neural Network (MLP)."""
        print("\n" + "=" * 80)
        print("NEURAL NETWORK (MULTI-LAYER PERCEPTRON)")
        print("=" * 80)
        
        # Scale features for Neural Network
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(self.X_train)
        X_test_scaled = scaler.transform(self.X_test)
        
        nn_classifier = MLPClassifier(hidden_layer_sizes=(64, 32, 16), 
                                     max_iter=1000, random_state=42,
                                     learning_rate_init=0.001, early_stopping=True,
                                     validation_fraction=0.1)
        nn_classifier.fit(X_train_scaled, self.y_train)
        self.models['Neural Network'] = (nn_classifier, scaler)
        
        y_pred = nn_classifier.predict(X_test_scaled)
        self._evaluate_model('Neural Network', y_pred, nn_classifier, X_test_scaled)
        
    def _evaluate_model(self, model_name, y_pred, model, X_test_scaled=None):
        """Evaluate model performance."""
        accuracy = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred)
        recall = recall_score(self.y_test, y_pred)
        f1 = f1_score(self.y_test, y_pred)
        
        self.results[model_name] = {
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1-Score': f1
        }
        
        print(f"\nAccuracy: {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1-Score: {f1:.4f}")
        
        print(f"\nConfusion Matrix:")
        cm = confusion_matrix(self.y_test, y_pred)
        print(cm)
        
        print(f"\nClassification Report:")
        print(classification_report(self.y_test, y_pred, 
                                   target_names=['Failure', 'Success']))
        
    def compare_models(self):
        """Compare all trained models."""
        print("\n" + "=" * 80)
        print("MODEL COMPARISON")
        print("=" * 80)
        
        results_df = pd.DataFrame(self.results).T
        print(f"\n{results_df}")
        
        # Best model
        best_model = results_df['F1-Score'].idxmax()
        best_score = results_df.loc[best_model, 'F1-Score']
        print(f"\nBest Model: {best_model} (F1-Score: {best_score:.4f})")
        
    def run_analysis(self):
        """Run complete analysis pipeline."""
        self.explore_dataset()
        self.prepare_data()
        
        self.train_decision_tree()
        self.train_random_forest()
        self.train_svm()
        self.train_naive_bayes()
        self.train_knn()
        self.train_neural_network()
        
        self.compare_models()


def escape_html(text):
    """Escape HTML special characters."""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')


if __name__ == "__main__":
    # Path to dataset
    csv_path = "Cryotherapy.csv.xlsx - CrayoDataset.csv"
    
    # Capture output
    output_buffer = io.StringIO()
    
    with redirect_stdout(output_buffer):
        # Create analyzer
        analyzer = CryotherapyAnalyzer(csv_path)
        
        # Run full analysis
        analyzer.run_analysis()
    
    # Get the captured output
    captured_output = output_buffer.getvalue()
    
    # Read the existing HTML file
    with open('Assignment_2_Submission.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Create the output section HTML
    output_section = f'''
        <h2>Execution Output</h2>
        <div style="background-color: #f5f5f5; padding: 20px; border-left: 4px solid #2c3e50; margin: 20px 0; font-family: 'Courier New', monospace; font-size: 0.9em; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;">
{escape_html(captured_output)}
        </div>
'''
    
    # Find the insertion point (before the code section)
    insertion_marker = '<pre><code class="language-python">"""'
    
    if insertion_marker in html_content:
        # Insert the output section before the code section
        html_content = html_content.replace(insertion_marker, output_section + '\n' + insertion_marker)
        
        # Write the updated HTML
        with open('Assignment_2_Submission.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("✓ Successfully added execution output to Assignment_2_Submission.html")
    else:
        print("✗ Could not find insertion point in HTML file")
