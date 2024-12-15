# Sử dụng Python 3.10 làm base image
FROM python:3.10-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép các tệp yêu cầu vào container
COPY requirements.txt /app/

# Cài đặt các thư viện cần thiết
RUN pip install -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . /app

# Thiết lập biến môi trường
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Mở cổng 8000
EXPOSE 8000

# # Lệnh để chạy server Django
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
