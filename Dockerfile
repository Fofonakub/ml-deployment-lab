
# Base image ใช้ Python 3.11
FROM python:3.11-slim

# สร้างโฟลเดอร์ทำงาน
WORKDIR /app

# ติดตั้ง dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกไฟล์โปรเจกต์
COPY . .



# เปิด port 5000
EXPOSE 5000

# ใช้ Gunicorn รัน Flask
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
