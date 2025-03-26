# 使用Python官方镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 添加 Python 路径
ENV PYTHONPATH=/app

# 暴露端口
EXPOSE 8000

# 修改启动命令指向正确的模块
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 