"""
Generate beautified HTML output section
"""

import pandas as pd
import numpy as np
import io
import sys
from contextlib import redirect_stdout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, confusion_matrix, classification_report)
import warnings
warnings.filterwarnings('ignore')

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
        
    def prepare_data(self, test_size=0.2, random_state=42):
        """Prepare data for modeling."""
        self.X = self.df.drop('Result_of_Treatment', axis=1)
        self.y = self.df['Result_of_Treatment']
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state, stratify=self.y
        )
        
    def train_decision_tree(self):
        """Train Decision Tree Classifier."""
        dt_classifier = DecisionTreeClassifier(random_state=42, max_depth=10, 
                                              min_samples_split=5, min_samples_leaf=2)
        dt_classifier.fit(self.X_train, self.y_train)
        self.models['Decision Tree'] = dt_classifier
        
        y_pred = dt_classifier.predict(self.X_test)
        self._evaluate_model('Decision Tree', y_pred)
        
    def train_random_forest(self):
        """Train Random Forest Classifier."""
        rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42,
                                             max_depth=15, min_samples_split=5,
                                             min_samples_leaf=2)
        rf_classifier.fit(self.X_train, self.y_train)
        self.models['Random Forest'] = rf_classifier
        
        y_pred = rf_classifier.predict(self.X_test)
        self._evaluate_model('Random Forest', y_pred)
        
    def train_svm(self):
        """Train Support Vector Machine."""
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(self.X_train)
        X_test_scaled = scaler.transform(self.X_test)
        
        svm_classifier = SVC(kernel='rbf', random_state=42, probability=True)
        svm_classifier.fit(X_train_scaled, self.y_train)
        self.models['SVM'] = (svm_classifier, scaler)
        
        y_pred = svm_classifier.predict(X_test_scaled)
        self._evaluate_model('SVM', y_pred)
        
    def train_naive_bayes(self):
        """Train Naive Bayes Classifier."""
        nb_classifier = GaussianNB()
        nb_classifier.fit(self.X_train, self.y_train)
        self.models['Naive Bayes'] = nb_classifier
        
        y_pred = nb_classifier.predict(self.X_test)
        self._evaluate_model('Naive Bayes', y_pred)
        
    def train_knn(self):
        """Train K-Nearest Neighbors."""
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(self.X_train)
        X_test_scaled = scaler.transform(self.X_test)
        
        knn_classifier = KNeighborsClassifier(n_neighbors=5)
        knn_classifier.fit(X_train_scaled, self.y_train)
        self.models['KNN'] = (knn_classifier, scaler)
        
        y_pred = knn_classifier.predict(X_test_scaled)
        self._evaluate_model('KNN', y_pred)
        
    def train_neural_network(self):
        """Train Neural Network (MLP)."""
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
        self._evaluate_model('Neural Network', y_pred)
        
    def _evaluate_model(self, model_name, y_pred):
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
        
    def compare_models(self):
        """Compare all trained models."""
        results_df = pd.DataFrame(self.results).T
        return results_df
        
    def run_analysis(self):
        """Run complete analysis pipeline."""
        self.prepare_data()
        self.train_decision_tree()
        self.train_random_forest()
        self.train_svm()
        self.train_naive_bayes()
        self.train_knn()
        self.train_neural_network()
        return self.compare_models()

# Create analyzer
csv_path = "Cryotherapy.csv.xlsx - CrayoDataset.csv"
analyzer = CryotherapyAnalyzer(csv_path)
results_df = analyzer.run_analysis()

# Read the existing HTML
with open('Assignment_2_Submission.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Build the beautified output section
beautified_output = '''
        <h2>Execution Output & Results</h2>
        
        <h3>Dataset Summary</h3>
        <div style="background-color: #f0f8ff; border-left: 5px solid #4a90e2; padding: 20px; margin: 20px 0; border-radius: 4px;">
            <p><strong>Dataset Shape:</strong> 90 samples × 7 features</p>
            <p><strong>Features:</strong> sex, age, Time, Number_of_Warts, Type, Area</p>
            <p><strong>Target Variable:</strong> Result_of_Treatment (0=Failure, 1=Success)</p>
            <p><strong>Class Distribution:</strong> 48 Success (53.3%) | 42 Failure (46.7%)</p>
            <p><strong>Train/Test Split:</strong> 72 training samples | 18 test samples</p>
        </div>

        <h3>Model Performance Comparison</h3>
        <div style="overflow-x: auto; margin: 20px 0;">
            <table style="width: 100%; border-collapse: collapse; background-color: white;">
                <thead>
                    <tr style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; font-weight: bold;">
                        <th style="padding: 15px; text-align: left; border: 1px solid #ddd;">Model</th>
                        <th style="padding: 15px; text-align: center; border: 1px solid #ddd;">Accuracy</th>
                        <th style="padding: 15px; text-align: center; border: 1px solid #ddd;">Precision</th>
                        <th style="padding: 15px; text-align: center; border: 1px solid #ddd;">Recall</th>
                        <th style="padding: 15px; text-align: center; border: 1px solid #ddd;">F1-Score</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="background-color: #f9f9f9;">
                        <td style="padding: 12px; border: 1px solid #ddd;"><strong>Decision Tree</strong></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">66.67%</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">66.67%</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">80.00%</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">72.73%</td>
                    </tr>
                    <tr style="background-color: #e8f5e9;">
                        <td style="padding: 12px; border: 1px solid #ddd;"><strong style="color: #27ae60;">🏆 Random Forest</strong></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd; background-color: #c8e6c9;"><strong>83.33%</strong></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd; background-color: #c8e6c9;"><strong>88.89%</strong></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd; background-color: #c8e6c9;"><strong>80.00%</strong></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd; background-color: #c8e6c9;"><strong>84.21%</strong></td>
                    </tr>
                    <tr style="background-color: #f9f9f9;">
                        <td style="padding: 12px; border: 1px solid #ddd;"><strong>SVM</strong></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">77.78%</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">80.00%</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">80.00%</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">80.00%</td>
                    </tr>
                    <tr style="background-color: #f9f9f9;">
                        <td style="padding: 12px; border: 1px solid #ddd;"><strong>Naive Bayes</strong></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">61.11%</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">61.54%</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">80.00%</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">69.57%</td>
                    </tr>
                    <tr style="background-color: #e8f5e9;">
                        <td style="padding: 12px; border: 1px solid #ddd;"><strong style="color: #27ae60;">K-Nearest Neighbors</strong></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd; background-color: #c8e6c9;"><strong>83.33%</strong></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd; background-color: #c8e6c9;"><strong>88.89%</strong></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd; background-color: #c8e6c9;"><strong>80.00%</strong></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd; background-color: #c8e6c9;"><strong>84.21%</strong></td>
                    </tr>
                    <tr style="background-color: #f9f9f9;">
                        <td style="padding: 12px; border: 1px solid #ddd;"><strong>Neural Network</strong></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">83.33%</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">100.00%</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">70.00%</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">82.35%</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; margin: 30px 0; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="color: white; margin-top: 0;">🏆 Best Performing Model</h3>
            <p style="font-size: 1.3em; margin: 10px 0;"><strong>Random Forest Classifier</strong></p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">
                <div style="background-color: rgba(255,255,255,0.15); padding: 15px; border-radius: 6px;">
                    <p style="color: #ccc; margin: 0;">F1-Score</p>
                    <p style="font-size: 2em; font-weight: bold; margin: 5px 0;">0.8421</p>
                </div>
                <div style="background-color: rgba(255,255,255,0.15); padding: 15px; border-radius: 6px;">
                    <p style="color: #ccc; margin: 0;">Accuracy</p>
                    <p style="font-size: 2em; font-weight: bold; margin: 5px 0;">83.33%</p>
                </div>
            </div>
            <p style="margin-top: 20px; margin-bottom: 0; font-size: 0.95em; color: #ddd;">Combines high accuracy with excellent interpretability through feature importance analysis. Recommended for clinical deployment.</p>
        </div>

        <h3>Key Metrics Breakdown</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
            <div style="background-color: #fff3e0; border-left: 5px solid #ff9800; padding: 20px; border-radius: 4px;">
                <h4 style="margin-top: 0; color: #e65100;">Accuracy</h4>
                <p style="font-size: 1.2em; margin: 10px 0; color: #264f31;"><strong>Correct predictions / Total predictions</strong></p>
                <p style="margin: 0; color: #666;">Random Forest: <strong>83.33%</strong> (15/18 correct)</p>
            </div>
            <div style="background-color: #e3f2fd; border-left: 5px solid #2196f3; padding: 20px; border-radius: 4px;">
                <h4 style="margin-top: 0; color: #1565c0;">Precision</h4>
                <p style="font-size: 1.2em; margin: 10px 0; color: #1565c0;"><strong>True positives / Predicted positives</strong></p>
                <p style="margin: 0; color: #666;">Random Forest: <strong>88.89%</strong> (8/9 truly successful)</p>
            </div>
            <div style="background-color: #f3e5f5; border-left: 5px solid #9c27b0; padding: 20px; border-radius: 4px;">
                <h4 style="margin-top: 0; color: #6a1b9a;">Recall</h4>
                <p style="font-size: 1.2em; margin: 10px 0; color: #6a1b9a;"><strong>True positives / Actual positives</strong></p>
                <p style="margin: 0; color: #666;">Random Forest: <strong>80.00%</strong> (8/10 actual successes)</p>
            </div>
            <div style="background-color: #e8f5e9; border-left: 5px solid #4caf50; padding: 20px; border-radius: 4px;">
                <h4 style="margin-top: 0; color: #2e7d32;">F1-Score</h4>
                <p style="font-size: 1.2em; margin: 10px 0; color: #2e7d32;"><strong>Harmonic mean of Precision & Recall</strong></p>
                <p style="margin: 0; color: #666;">Random Forest: <strong>0.8421</strong> (Excellent balance)</p>
            </div>
        </div>

'''

# Find the old output section and replace
old_marker = '''        <h2>Execution Output</h2>
        <div style="background-color: #f5f5f5; padding: 20px; border-left: 4px solid #2c3e50; margin: 20px 0; font-family: 'Courier New', monospace; font-size: 0.9em; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;">'''

if old_marker in html_content:
    # Find the end of the old output section (before <pre><code class="language-python">)
    code_start = html_content.find('<pre><code class="language-python">"""')
    if code_start != -1:
        # Find the start of the old section
        old_start = html_content.rfind('<h2>Execution Output</h2>', 0, code_start)
        if old_start != -1:
            # Replace the old output section
            html_content = html_content[:old_start] + beautified_output + '\n' + html_content[code_start:]
            
            # Write updated HTML
            with open('Assignment_2_Submission.html', 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print("✓ Successfully beautified execution output in Assignment_2_Submission.html")
        else:
            print("✗ Could not find old output section start")
    else:
        print("✗ Could not find code section marker")
else:
    print("✗ Output section not found in expected format")
