from flask import Flask, render_template

app = Flask(__name__)  # 绑定app


# 函数一：关联页面
@app.route('/')  # 路由
def image():
    return render_template('image.html')


# 函数二：生成数据
from flask import jsonify  # 数据转为json，并以字典的形式传回前端

import datetime, random  # 导入时间和随机数模块


@app.route('/setData/')  # 路由
def setData():
    now = datetime.datetime.now().strftime('%H:%M:%S')
    data = {'time': now, 'data': random.randint(1, 10)}
    print(data)
    return jsonify(data)  # 将数据以字典的形式传回


if __name__ == '__main__':
    app.run(host="127.0.0.1",debug=True,port=5000)