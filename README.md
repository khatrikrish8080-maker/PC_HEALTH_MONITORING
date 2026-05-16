# PC_HEALTH_MONITORING

# Real-Time PC Health Monitoring & Diagnostic Pipeline

An end-to-end Machine Learning and Data Engineering pipeline that monitors local system hardware metrics (CPU, RAM) in real-time, stores diagnostic data in a MySQL database, and uses a Support Vector Machine (SVM) classifier to instantly predict system health status via an interactive Streamlit dashboard.

---

## 🚀 Features
* **Real-Time Telemetry:** Continuous hardware tracking using `psutil`.
* **Predictive Diagnostics:** Multi-class SVM classification identifying system states (`Healthy`, `Warning`, `Critical`).
* **Persistent Storage:** Seamless local logging into a structured MySQL database instance.
* **Interactive Dashboard:** Dynamic Streamlit frontend rendering live diagnostic banners and performance metrics.

---

## 🛠️ Tech Stack & Libraries
* **Frontend:** Streamlit
* **Machine Learning:** Core Python, Scikit-learn (SVM), NumPy, Pandas
* **Database:** MySQL (via `mysql-connector-python`)
* **System Utilities:** `psutil`

---

## 📁 Repository Structure
```text
PC_HEALTH_MONITORING/
│
├── app.py                  # Live Streamlit dashboard application
├── ML_model.py             # Model training script, evaluation, & database extraction
├── monitor.py              # Background system metric collection loop
├── PC_HEALTH_MONITOR_.sql  # MySQL database schema definition script
└── README.md               # Project documentation
