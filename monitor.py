import psutil
import mysql.connector
import time

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jaanbira#91",
        database="PC"
    )
    cursor = connection.cursor()
    print("✅ Connected. Monitoring...")

    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        batt = psutil.sensors_battery().percent

        query = "INSERT INTO health (cpu_usage, ram_usage, battery) VALUES (%s, %s, %s)"
        data = (cpu, ram, batt)

        cursor.execute(query, data)
        connection.commit()

        print(f"Logged -> CPU: {cpu}% | RAM: {ram}% | Battery: {batt}%")
        
        time.sleep(10)

except mysql.connector.Error as err:
    print(f"❌ SQL Error: {err}")
except KeyboardInterrupt:
    print("\n🛑 Stopped.")
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()