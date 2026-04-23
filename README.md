# PC_HEALTH_MONITORING
🖥️ PC Health Monitor: Real-Time System Intelligence
A robust system monitoring tool built with Python and MySQL that tracks hardware performance, logs metrics to a relational database, and utilizes Generated Columns for automated health status classification.

🚀 Project Overview
This project provides a "Smart Dashboard" for your PC. By leveraging the psutil library, it captures real-time data on CPU, RAM, and Battery life. Unlike standard trackers, this system uses Database-Level Logic to automatically categorize system health without needing extra Python code for classification.

✨ Key Features
Real-time Telemetry: Captures precise CPU usage, Memory (RAM) consumption, and Battery percentages.

Automated Triage: Uses a MySQL Generated Column with CASE logic to instantly label system load as HIGH, MEDIUM, or LOW.

Persistence: All logs are timestamped and stored in a local MySQL instance for historical analysis.

Clean Schema: Optimized SQL structure designed for fast queries and professional data management.

🛠️ Tech Stack
Language: Python 3.x

Database: MySQL 8.0

Key Libraries: * psutil (System metrics)

mysql-connector-python (Database connectivity)

time (Polling intervals)

Environment: VS Code, MySQL Workbench


GUI Dashboard: Building a Tkinter or Flask interface to visualize metrics.
