# AI Assignment 2: Cryotherapy Treatment Classification

## 📋 Assignment Overview

This assignment focuses on **machine learning classification** for predicting the success of cryotherapy treatment for wart removal. The solution implements and evaluates six different classification algorithms on the Cryotherapy dataset.

---

## 📊 Dataset Description

**Cryotherapy.csv** - Contains 90 patient records with the following features:

| Feature | Type | Range | Description |
|---------|------|-------|-------------|
| **sex** | Categorical | 1, 2 | Patient gender (1=Male, 2=Female) |
| **age** | Numeric | 15-67 | Patient age in years |
| **Time** | Numeric | 0.5-12 | Treatment duration in weeks |
| **Number_of_Warts** | Numeric | 1-12 | Number of warts being treated |
| **Type** | Categorical | 1-3 | Type of wart |
| **Area** | Numeric | 4-750 | Total affected area in mm² |
| **Result_of_Treatment** | Target | 0, 1 | Treatment outcome (0=Failed, 1=Successful) |

**Dataset Statistics:**
- Total Samples: 90
- Training Set: 72 (80%)
- Testing Set: 18 (20%)
- Class Distribution: 53.3% Success, 46.7% Failure
- Missing Values: 0
- Imbalance Ratio: ~1.14 (slightly imbalanced)

---

## 🤖 Machine Learning Models Implemented

### 1. **Decision Tree Classifier**
- **Algorithm:** Recursively partitions data using information gain criterion
- **Hyperparameters:** max_depth=10, min_samples_split=5
- **Performance:**
  - Accuracy: 66.67%
  - F1-Score: 0.7273
  - Top Feature: Age (73.6% importance)
- **Observation:** Shows signs of overfitting; poor generalization

### 2. **Random Forest Classifier** ⭐
- **Algorithm:** Ensemble of 100 decision trees with bootstrap aggregating
- **Hyperparameters:** n_estimators=100, max_depth=15
- **Performance:**
  - Accuracy: 83.33%
  - Precision: 88.89%
  - Recall: 80.00%
  - F1-Score: 0.8421
- **Feature Importance:**
  - Age: 36.8%
  - Time: 32.9%
  - Type: 14.8%
  - Area: 8.8%
  - Number_of_Warts: 4.8%
  - Sex: 2.0%
- **Recommendation:** Primary model - excellent balance of performance and interpretability

### 3. **Support Vector Machine (SVM)**
- **Algorithm:** RBF kernel support vector classifier
- **Hyperparameters:** kernel='rbf', C=1.0 (default)
- **Performance:**
  - Accuracy: 77.78%
  - Precision: 80.00%
  - Recall: 80.00%
  - F1-Score: 0.8000
- **Advantage:** Balanced performance across all metrics
- **Disadvantage:** Less interpretable than tree-based models

### 4. **Naive Bayes**
- **Algorithm:** Gaussian Naive Bayes with probabilistic modeling
- **Hyperparameters:** Default (assumes feature independence)
- **Performance:**
  - Accuracy: 61.11%
  - Precision: 61.54%
  - Recall: 80.00%
  - F1-Score: 0.6957
- **Limitation:** Assumes feature independence (violated in this dataset)

### 5. **K-Nearest Neighbors (KNN)** ⭐
- **Algorithm:** Instance-based classification with k=5 neighbors
- **Hyperparameters:** n_neighbors=5, metric='euclidean'
- **Performance:**
  - Accuracy: 83.33%
  - Precision: 88.89%
  - Recall: 80.00%
  - F1-Score: 0.8421
- **Status:** Tied with Random Forest for best performance
- **Limitation:** Less interpretable, computationally expensive for large datasets

### 6. **Neural Network (MLPClassifier)**
- **Architecture:** 6 → 64 → 32 → 16 → 2 (multi-layer perceptron)
- **Hyperparameters:** max_iter=1000, early_stopping=True, learning_rate=0.001
- **Performance:**
  - Accuracy: 83.33%
  - Precision: 100.00%
  - Recall: 70.00%
  - F1-Score: 0.8235
- **Trade-off:** Perfect precision but slightly lower recall

---

## 📈 Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score | Rank |
|-------|----------|-----------|--------|----------|------|
| **Random Forest** | 83.33% | 88.89% | 80.00% | **0.8421** | 🥇 1st |
| **KNN** | 83.33% | 88.89% | 80.00% | **0.8421** | 🥇 1st |
| **Neural Network** | 83.33% | 100.00% | 70.00% | 0.8235 | 3rd |
| **SVM** | 77.78% | 80.00% | 80.00% | 0.8000 | 4th |
| **Decision Tree** | 66.67% | 66.67% | 80.00% | 0.7273 | 5th |
| **Naive Bayes** | 61.11% | 61.54% | 80.00% | 0.6957 | 6th |

---

## 🎯 Key Findings

### 1. Feature Importance Analysis
- **Age** (36.8%) and **Time** (32.9%) are dominant predictors accounting for ~70% of Random Forest's decision-making
- **Type** (14.8%) provides additional predictive power
- **Sex** (2.0%) has minimal impact on treatment outcome prediction
- This suggests patient age and treatment duration are critical factors for successful outcomes

### 2. Model Insights
- **Tree-based ensemble methods** (Random Forest, Decision Tree) outperform distance-based methods in feature importance analysis
- **Scaling benefits** SVM (+14%), KNN (+17%), and Neural Network by improving feature normalization
- **Ensemble approach** (100 trees) significantly improves over single decision tree (+17% accuracy)

### 3. Dataset Characteristics
- **Balanced classes** prevent bias toward majority class
- **Clean data** with no missing values
- **Weak feature correlations** with target (max: 0.22) suggest complex non-linear relationships
- **Small dataset** (90 samples) limits deep learning potential

### 4. Clinical Implications
- Older patients may have different treatment response patterns
- Longer treatment durations correlate with better outcomes
- Patient gender shows minimal influence on treatment success
- Wart type is moderately important (14.8%)

---

## 🔍 Implementation Details

### Data Preparation
```python
# Train-test split: 80-20 stratified
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature scaling (for SVM, KNN, Neural Network)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### Model Training
```python
# Random Forest (Best Model)
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    max_depth=15,
    min_samples_split=5
)
rf.fit(X_train, y_train)
```

### Evaluation Metrics
- **Accuracy:** Overall correctness of predictions
- **Precision:** Reliability of positive predictions
- **Recall:** Coverage of actual positive cases
- **F1-Score:** Harmonic mean balancing precision and recall
- **Confusion Matrix:** Detailed breakdown of prediction types

---

## 📁 Deliverables

### 1. **assignment_2_solution.py** (Primary Python Script)
- Complete implementation of all 6 classification models
- Comprehensive dataset analysis
- Performance evaluation and comparison
- Feature importance analysis
- ~250 lines of production-ready code

**Usage:**
```bash
python assignment_2_solution.py
```

### 2. **Cryotherapy_Classification_Analysis.ipynb** (Jupyter Notebook)
- Interactive analysis with step-by-step explanations
- Data visualization and exploration
- Model training and evaluation with detailed output
- Confusion matrices and ROC curves
- Suitable for learning and presentation

**Usage:**
```bash
jupyter notebook Cryotherapy_Classification_Analysis.ipynb
```

### 3. **Assignment_2_Submission.html** (Professional Report)
- Comprehensive assignment submission document
- Formatted HTML with styling
- Complete methodology, results, and recommendations
- Suitable for printing and formal submission

---

## 🏆 Recommendation

### **Primary Model: Random Forest Classifier**

**Rationale:**
1. **Excellent Performance:** F1-Score of 0.8421 with balanced precision (88.89%) and recall (80%)
2. **Interpretability:** Feature importance ranked for clinical insights
3. **Stability:** Ensemble approach reduces overfitting
4. **Robustness:** Handles non-linear relationships without explicit feature engineering
5. **Scalability:** Can efficiently handle increased data volume

**Alternative:** KNN provides identical performance (0.8421 F1) but less interpretable

### **Model Deployment**
```python
# Train on full dataset
rf_final = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=15)
rf_final.fit(X, y)

# Predict for new patient
new_patient = [[1, 45, 10, 3, 2, 150]]  # [sex, age, time, num_warts, type, area]
prediction = rf_final.predict(new_patient)  # 0 or 1
probability = rf_final.predict_proba(new_patient)  # [prob_failure, prob_success]
```

---

## 💡 Recommendations for Improvement

1. **Expand Dataset:** Collect more samples (target: 500+) to improve model reliability
2. **Feature Engineering:** Create interaction terms (age×time) and ratio features
3. **Hyperparameter Tuning:** Use GridSearchCV for systematic optimization
4. **Cross-Validation:** Implement 5-fold or 10-fold cross-validation for robust evaluation
5. **Class Balancing:** If class distribution becomes severely imbalanced, apply SMOTE resampling
6. **Ensemble Stacking:** Combine predictions from RF, KNN, and SVM for potential improvement
7. **Feature Selection:** Use mutual information or permutation importance for variable selection
8. **Regularization:** Implement L1/L2 regularization for neural networks to prevent overfitting

---

## 📚 Learning Outcomes

✅ Successfully implemented 6 different classification algorithms
✅ Performed comprehensive exploratory data analysis
✅ Evaluated models using multiple performance metrics
✅ Analyzed feature importance and model interpretability
✅ Created production-ready code and documentation
✅ Demonstrated understanding of ML model selection and evaluation

---

## 🔗 References

1. **Scikit-learn Documentation:** https://scikit-learn.org/
2. **Random Forest Classifier:** Breiman, L. (2001). "Random Forests"
3. **Support Vector Machines:** Cortes, C., & Vapnik, V. (1995). "Support-vector networks"
4. **Neural Networks:** Goodfellow, I., Bengio, Y., & Courville, A. (2016)
5. **KNN Algorithm:** Fix, E., & Hodges, J. L. (1951). "Discriminatory analysis"
6. **Naive Bayes:** Russell, S. J., & Norvig, P. (2020). Modern Artificial Intelligence

---

## 📞 Notes for Instructor

- All models have been trained and evaluated on stratified train-test split (80-20)
- Hyperparameters tuned based on default recommendations and empirical testing
- No data leakage: scaling/preprocessing only fitted on training data
- Results are reproducible with random_state=42
- Full implementation details available in source code comments

---

**Assignment Status:** ✅ COMPLETED

**Best Model:** Random Forest Classifier (F1-Score: 0.8421)  
**Submission Date:** April 2026  
**Course:** IS ZC444 - Artificial Intelligence, BITS Pilani
