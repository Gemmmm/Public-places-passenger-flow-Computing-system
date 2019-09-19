from flask import Flask, render_template, Response
from flask import jsonify
import cv2
import datetime
import time
import json
import os
os.environ["CUDA_VISIBLE_DEVICES"] = '1'

app = Flask(__name__)

json_data={}

class VideoCamera(object):
    def __init__(self):
        # 通过opencv获取实时视频流
        self.video = cv2.VideoCapture("D:/zz/3.mp4")
        self.lasttime = 0
        self.lastcounter=0
        json_data['sum']=0
        json_data['max'] = 0

    def __del__(self):
        self.video.release()

    def get_frame(self):
        face_cascade = cv2.CascadeClassifier("data/haarcascade_fullbody.xml")
        success, frame = self.video.read()
        if success == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            bodys = face_cascade.detectMultiScale(gray, 1.3, 5)
            nowTimehms = datetime.datetime.now().strftime('%H:%M:%S')  # 现在
            ticks = time.time()
            self.counter=0
            for (x, y, w, h) in bodys:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (55, 255, 155), 5)
                cv2.putText(frame, '', (int(w / 2 + x), int(y - h / 5)), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 155), 2)
                self.counter+=1
            if self.counter>self.lastcounter:
                json_data['sum'] = json_data['sum']+self.counter-self.lastcounter
            if self.counter> json_data['max']:
                json_data['max']=self.counter
            if int(ticks * 10) % 10 == 0 and self.lasttime != int(ticks):
                print("时间戳为:", int(ticks), "时间", nowTimehms, "数量", self.counter)
                json_data['time'] = nowTimehms
                json_data['data'] = self.counter
                #print(json.dumps(json_data))
            self.lasttime = int(ticks)
            self.lastcounter = self.counter
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()




@app.route('/index/')  # 主页
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('index.html')


@app.route('/t1/')
def t1():
    return render_template('t1.html')

@app.route('/')
def begin():
    return render_template('begin.html')

@app.route('/infor/')
def information():
    return render_template('information.html')

@app.route('/list/')
def list():
    return render_template('listpic.html')




def gen(camera):
    while True:
        frame = camera.get_frame()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


class VideoCamera2(object):
    def __init__(self):
        # 通过opencv获取实时视频流
        self.i=0
        self.video = cv2.VideoCapture("D:/zz/3.avi")
        self.lasttime = 0
        self.lastcounter = 0
        json_data['sum2'] = 0
        json_data['max2'] = 0

    def __del__(self):
        self.video.release()

    def get_frame(self):
        face_cascade = cv2.CascadeClassifier("data/haarcascade_fullbody.xml")
        success, frame = self.video.read()
        if success == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            bodys = face_cascade.detectMultiScale(gray, 1.3, 5)
            nowTimehms = datetime.datetime.now().strftime('%H:%M:%S')  # 现在
            ticks = time.time()
            self.counter = 0
            for (x, y, w, h) in bodys:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (55, 255, 155), 5)
                cv2.putText(frame, '', (int(w / 2 + x), int(y - h / 5)), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 155), 2)
                self.counter += 1
            if self.counter>self.lastcounter:
                json_data['sum2'] = json_data['sum2']+self.counter-self.lastcounter
            if self.counter> json_data['max2']:
                json_data['max2']=self.counter
            if int(ticks * 10) % 10 == 0 and self.lasttime != int(ticks):
                #print("时间戳为:", int(ticks), "时间", nowTimehms, "数量", self.counter)
                json_data['time2'] = nowTimehms
                json_data['data2'] = self.counter
                    #print(json.dumps(json_data))
            self.lasttime = int(ticks)
            self.lastcounter = self.counter

        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()


def gen2(camera):
    while True:
        frame = camera.get_frame()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed2')  # 这个地址返回视频流响应
def video_feed2():
    return Response(gen2(VideoCamera2()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


class VideoCamera3(object):
    def __init__(self):
        # 通过opencv获取实时视频流
        self.i=0
        self.video = cv2.VideoCapture("D:/zz/3.avi")
        self.lasttime = 0
        self.lastcounter = 0
        json_data['sum3'] = 0
        json_data['max3'] = 0

    def __del__(self):
        self.video.release()

    def get_frame(self):
        face_cascade = cv2.CascadeClassifier("data/haarcascade_fullbody.xml")
        success, frame = self.video.read()
        if success == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            bodys = face_cascade.detectMultiScale(gray, 1.3, 5)
            nowTimehms = datetime.datetime.now().strftime('%H:%M:%S')  # 现在
            ticks = time.time()
            self.counter = 0
            for (x, y, w, h) in bodys:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (55, 255, 155), 5)
                cv2.putText(frame, '', (int(w / 2 + x), int(y - h / 5)), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 155), 2)
                self.counter += 1
            if self.counter>self.lastcounter:
                json_data['sum3'] = json_data['sum3']+self.counter-self.lastcounter
            if self.counter> json_data['max3']:
                json_data['max3']=self.counter
            if int(ticks * 10) % 10 == 0 and self.lasttime != int(ticks):
                print("3时间戳为:", int(ticks), "时间", nowTimehms, "数量", self.counter)
                json_data['time3'] = nowTimehms
                json_data['data3'] = self.counter
                    #print(json.dumps(json_data))
            self.lasttime = int(ticks)
            self.lastcounter = self.counter

        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()


def gen3(camera):
    while True:
        frame = camera.get_frame()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed3')  # 这个地址返回视频流响应
def video_feed3():
    return Response(gen3(VideoCamera3()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')






@app.route('/setData/')  # 路由
def setData():
    data = {'time':  json_data['time'], 'data':json_data['data'], 'max':json_data['max'], 'sum':json_data['sum']
           ,'time2':  json_data['time2'], 'data2':json_data['data2'], 'max2':json_data['max2'], 'sum2':json_data['sum2']
           ,'time3':  json_data['time3'], 'data3':json_data['data3'], 'max3':json_data['max3'], 'sum3':json_data['sum3']}
    print(data)
    return jsonify(data)  # 将数据以字典的形式传回


if __name__ == '__main__':
    app.run(host='127.0.0.1',threaded=True, port = 5000)

