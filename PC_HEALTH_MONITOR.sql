CREATE DATABASE PC;
USE PC;

CREATE TABLE health (
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cpu_usage FLOAT,
    ram_usage FLOAT,
    battery INT,
    
    pc_status VARCHAR(20) AS (
        CASE 
            WHEN cpu_usage > 70 THEN 'HIGH'
            WHEN cpu_usage > 40 THEN 'MEDIUM'
            ELSE 'LOW'
        END
    )
);