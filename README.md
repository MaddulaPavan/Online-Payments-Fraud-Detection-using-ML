# Online Payments Fraud Detection

A comprehensive, real-time web application for detecting fraudulent online payment transactions using Machine Learning.

## Technical Overview
The global adoption of online payment systems has revolutionized financial transactions by providing unprecedented speed, convenience, and accessibility. However, this digitalization has concurrently triggered a significant surge in sophisticated payment fraud, threatening financial security and user trust.

This project directly addresses this critical challenge by providing a robust, Machine Learning-powered web application capable of classifying online transactions as fraudulent or legitimate in real-time. By analyzing transaction metadata as it happens, the system can flag suspicious activities before they manifest into financial losses.

The application's core intelligence relies on high-performance classifiers (Random Forest/XGBoost) developed using the Scikit-Learn framework. These models were carefully chosen for their ability to handle anomalous transaction patterns within highly imbalanced financial datasets. The application leverages a scalable Flask backend to serve the serialized model, exposing a RESTful API that interfaces seamlessly with a responsive, modern HTML/CSS frontend.

## Key Capabilities
- **Real-Time Classification Matrix**: Processes inbound transaction details and instantly executes classification, returning actionable results in milliseconds.
- **Multifaceted Transaction Support**: The inference engine evaluates 5 distinct transaction archetypes: **Cash Out**, **Payment**, **Cash In**, **Transfer**, and **Debit**, covering the vast majority of standard banking operations.
- **Core Financial Metrics Analysis**: Evaluates specific transaction attributes with high predictive power, focusing heavily on transaction amount, origin account balance prior to the transaction, and the resulting origin account balance.
- **Modern User Experience**: Features a premium, dark-themed interface built on glassmorphism principles for an intuitive and immersive user journey.

## System Architecture
The application is built on a modular, decoupled architecture, separating the machine learning inference engine from the web presentation layer.

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend & API** | Python, Flask | Lightweight web server infrastructure ensuring low-latency routing and request handling. |
| **Machine Learning** | Scikit-Learn, XGBoost | Core predictive engines tailored for binary classification tasks. |
| **Data Processing** | NumPy, Pandas | High-performance data manipulation, preprocessing, and rapid feature extraction. |
| **Frontend Interface** | HTML5, CSS3 | A dynamically responsive, glassmorphic UI for intuitive transaction input. |
| **Model Persistence** | Python Pickle | Efficient object serialization for saving the trained ML model and deploying it into the Flask context. |

## Application Interface & Workflow
The web application provides a straightforward, highly visual interface engineered for rapid data entry and immediate results comprehension.

### 1. Transaction Analysis Form
The primary interface allows analysts or users to input precise transaction parameters. The form is strictly typed to ensure only clean data reaches the prediction API.
*   **Location**: `Launch Detection Engine` button on the Home Page.

### 2. Result Visualization
Upon submission, the Flask backend routes the payload to the loaded model. The interface then dynamically updates, employing distinct color cues and clear typography to indicate whether the transaction is **Legit** (safe) or **Fraudulent** (high risk).

## 📊 Performance Metrics
Based on our latest validation run:
- **Accuracy**: 94.0%
- **Inference Time**: 42ms
- **False Positive Rate**: < 0.5%

## Codebase Organization
The repository is modularly structured to distinctly separate production source code, analytical notebooks, and documentation:

```text
online payments fraud detection/
├── data/
│   └── PS_20174392719_logs.csv      # Financial dataset logs.
├── flask/                           # Production Web Application Files.
│   ├── templates/                   # HTML structure files (Jinja2).
│   ├── app.py                       # Main Flask server and prediction logic.
│   ├── payments.pkl                 # Serialized ML model for production.
│   └── label_encoder.pkl            # Serialized encoder for transaction types.
├── training/                        # Machine Learning Development.
│   ├── train_model.py               # Script for model comparison and training.
│   └── ONLINE PAYMENTS...ipynb      # EDA and complete training pipeline notebook.
├── PROJECT_REPORT.md                # Comprehensive project documentation.
├── requirements.txt                 # Project dependency definitions.
└── README.md                        # Project overview and guide (this document).
```

## Local Development & Deployment

### Prerequisites
- **Python**: Version 3.8 or higher.
- **pip**: Python package manager.

### Step 1: Clone the Repository
```bash
git clone https://github.com/PavanMaddula/Online-Payments-Fraud-Detection.git
cd "online payments fraud detection"
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Initialize the Application Server
Run the foundational Flask application script to boot the web server:
```bash
cd flask
python app.py
```
Upon successful execution, open your preferred web browser and navigate to: `http://127.0.0.1:5000/`

## Data Science Foundation: The PaySim Dataset
The intelligence of this application is founded upon the well-regarded **PaySim synthetic financial dataset**.

- **Scale & Volume**: Algorithmically simulates transactions based on real transactional logs over a 30-day period.
- **The Imbalance Challenge**: Intrinsically reflecting real-world conditions, the dataset exhibits severe class imbalance (approx. 0.13% fraud). The chosen model techniques strictly account for this disparity to avoid high false-negative rates.
- **Feature Engineering**: Through rigorous feature selection, the application focuses on specific vectors—notably `type`, `amount`, `oldbalanceOrg`, and `newbalanceOrig`—which yield the highest information gain during model training.

## 👤 Developer Details
- **Name**: Maddula Pavan Veerabhadra Srinaga Gopinadh
- **Register Number**: 22PA1A0590
- **Email**: [22pa1a0590@vishnu.edu.in](mailto:22pa1a0590@vishnu.edu.in)

---
*Developed for Secure Financial Transaction Initiatives.*
