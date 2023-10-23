# 使用 Python 3.9 作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录中的代码到容器中的 /app 目录
COPY . .

# 设置容器的执行命令
CMD [ "python", "hello.py" ]
