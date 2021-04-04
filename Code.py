#!/usr/bin/python
# -*- coding: utf-8 -*-
#author:阿狸
import requests
import time,os
from datetime import datetime

class Course:
    def __init__(self):
        self.load_config()
        self.session = requests.Session()
        self.headers = {
            'Host': 'aic.hbswkj.com:8080',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'}
        self.session.get("http://aic.hbswkj.com:8080/jedu/",headers=self.headers)
        self.isLogin = False
        localtime = time.localtime(time.time())
        now_time = time.strftime("%Y-%m-%d %H:%M:%S",localtime)
        print('当前时间：'+now_time)

    def trylogin(self):

            res= self.session.post("http://aic.hbswkj.com:8080/jedu/login.do",{
                "username":self.username,
                "password":self.password
            },headers=self.headers).json()
            self.isLogin = res["success"]
            if res["success"]:
                self.session.cookies.set('username',self.username)
                time.sleep(0.2)
                self.session.get("http://aic.hbswkj.com:8080/jedu/index.do",headers=self.headers).content
            return self.isLogin

    # weeks是每个学期的第几周,程序可以判断当前时间为一年的第几周，所以要减去一个固定的数字
    def get_course_info(self,weeks = int(time.strftime("%W")) -8):
        res = self.session.get('http://aic.hbswkj.com:8080/jedu/edu/core/eduScheduleInfo/getStudentWeekSchedule.do?week=%s&semId='%(weeks),headers = self.headers)
        length = len(res.json()['data']['schedule'])
        info = {};name1 = [];name2 = [];name3 = [];name4 = [];name5 = [];name6 = [];name7 = [];
        for i in range(length):
            name = res.json()['data']['schedule'][i]['courseName']
            placeName = res.json()['data']['schedule'][i]['placeName'] + ''
            week = res.json()['data']['schedule'][i]['weekOfDay']
            start = str(res.json()['data']['schedule'][i]['eduTimeSchedule']['eduLesson']['startLesson'])
            end = str(res.json()['data']['schedule'][i]['eduTimeSchedule']['eduLesson']['endLesson'])

            if week=='mon':
                name1.append('第'+start+'~'+end+'节:' + name+placeName)
            if week=='tue':
                name2.append('第'+start+'~'+end+'节:' + name+placeName)
            if week=='wed':
                name3.append('第'+start+'~'+end+'节:' + name+placeName)
            if week=='thu':
                name4.append('第'+start+'~'+end+'节:' + name+placeName)
            if week=='fri':
                name5.append('第'+start+'~'+end+'节:' + name+placeName)
            if week=='sat':
                name6.append('第'+start+'~'+end+'节:' + name+placeName)
            if week=='sun':
                name7.append('第'+start+'~'+end+'节:' + name+placeName)

        name1.sort(),name2.sort(),name3.sort(),name4.sort(),name5.sort(),name6.sort(),name7.sort();
        info['1'] = name1;info['2'] = name2;info['3'] = name3;info['4'] = name4;info['5'] = name5;info['6'] = name6;info['7'] = name7;

        return info

    def print_course(self,weekofday = str(datetime.today().isoweekday())):
        '''

        此函数接收一个0~7的参数(str类型),用于查询一个星期的某一天课表，默认参数为当天。

        '''

        info = self.get_course_info()
        print(f"Today:{time.strftime('%a')}")
        if info[weekofday]:
            print('='*30)
            for i in info[weekofday]:
                print(i)
            print('='*30)
        else:
            print('='*30)
            print('查询无课。')
            print('='*30)

    def main(self):
        '''

        初始化的时候接受两个参数，分别为账号和密码

        '''
        self.trylogin()
        self.get_course_info()
        self.print_course()

    def load_config(self):
        try:
            #file_name = [i for i in os.listdir(os.path.dirname(__file__)) if '.txt' in i][0]
            
            file_name = os.path.dirname(__file__) + "\config.txt"
            file = open(file_name, 'r', encoding='utf-8')
            data = [i for i in file.read().split(',')]
            username = data[0]
            password = data[1]
            self.username = username;self.password = password
            file.close()

        except BaseException as error:
            print(error)
            

if __name__ =='__main__':
    Course().main()
