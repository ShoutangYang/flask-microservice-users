FROM python:3.6.4

# 设置工作路径
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# 添加依赖
ADD ./requirements.txt /usr/src/app/requirements.txt


# 安装依赖

RUN pip install -r requirements.txt

# 添加应用
ADD . /usr/src/app

# run app server
CMD python manage.py runserver -h 0.0.0.0
