#基于的基础镜像
FROM python:3.9-slim
#代码添加到code文件夹
ADD . /code
# 设置code文件夹是工作目录
WORKDIR /code
# 安装支持
RUN pip install flask -i https://pypi.douban.com/simple/
CMD ["python", "main.py"]
