# -*- encoding=utf8 -*-
__author__ = "76921"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import os
import time
# #########################个人配置########################
#要刷的图
AUTO_MAP = 18
########################系统配置#########################
ST.FIND_TIMEOUT_TMP=0.5     #识别速度
#using("conf.py")
if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["android://127.0.0.1:5037/127.0.0.1:5555?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",], project_root="C:/Users/76921/Desktop/air/mdk_v2.1")


class game_md:
    query_mapper={
        1:Template(r"tpl1698165495371.png", record_pos=(0.004, -0.151), resolution=(720, 1280)),
        2:Template(r"tpl1698165485739.png", record_pos=(0.001, 0.101), resolution=(720, 1280)),
        3:Template(r"tpl1698165480270.png", record_pos=(-0.032, -0.004), resolution=(720, 1280)),
        4:Template(r"tpl1698165473857.png", record_pos=(0.0, 0.158), resolution=(720, 1280)),
        5:Template(r"tpl1698165466805.png", record_pos=(0.004, 0.001), resolution=(720, 1280)),
        6:Template(r"tpl1698165461131.png", record_pos=(-0.025, -0.2), resolution=(720, 1280)),
        7:Template(r"tpl1698165454246.png", record_pos=(-0.001, 0.115), resolution=(720, 1280)),
        8:Template(r"tpl1698165447172.png", record_pos=(0.033, 0.086), resolution=(720, 1280)),
        9:Template(r"tpl1698165441630.png", record_pos=(0.103, 0.089), resolution=(720, 1280)),
        10:Template(r"tpl1698165430729.png", record_pos=(0.033, -0.228), resolution=(720, 1280)),
        11:Template(r"tpl1698165420006.png", record_pos=(0.117, -0.181), resolution=(720, 1280)),
        12:Template(r"tpl1698165383269.png", record_pos=(0.074, 0.06), resolution=(720, 1280)),
        13:Template(r"tpl1698165355728.png", record_pos=(0.014, 0.106), resolution=(720, 1280)),
        14:Template(r"tpl1698165343196.png", record_pos=(-0.072, 0.008), resolution=(720, 1280)),
        15:Template(r"tpl1698165313013.png", record_pos=(0.093, -0.09), resolution=(720, 1280)),
        16:Template(r"tpl1698165293535.png", record_pos=(-0.007, -0.042), resolution=(720, 1280)),
        17:Template(r"tpl1698165284249.png", record_pos=(0.024, -0.081), resolution=(720, 1280)),
        18:Template(r"tpl1698165274546.png", record_pos=(0.003, -0.074), resolution=(720, 1280)),
        19:Template(r"tpl1698165267667.png", record_pos=(-0.015, -0.035), resolution=(720, 1280)),
        20:Template(r"tpl1698165256771.png", record_pos=(0.013, -0.078), resolution=(720, 1280)),
        21:Template(r"tpl1698165248364.png", record_pos=(-0.036, -0.072), resolution=(720, 1280)),
        22:Template(r"tpl1698165240282.png", record_pos=(-0.004, -0.056), resolution=(720, 1280)),
        23:Template(r"tpl1698165207089.png", record_pos=(-0.033, -0.049), resolution=(720, 1280)),
        24:Template(r"tpl1711383852513.png", record_pos=(-0.04, -0.062), resolution=(720, 1280)),
        25:Template(r"tpl1711383865567.png", record_pos=(-0.036, -0.01), resolution=(720, 1280)),
        26:Template(r"tpl1711383875536.png", record_pos=(0.001, -0.025), resolution=(720, 1280))}
    def __init__(self,lock_map):
        self.auto_map=lock_map
        self.start_time=0
        self.end_time=0
        self.huanshen=(91, 961)
        self.zhaohuan=(639, 960)
        self.heidong=(95, 1128)
        self.wudi=(631, 1136)
        self.kongbai=(426, 1254)
        pass
    #登录
    def login(self):
        if exists(Template(r"tpl1698161964828.png", record_pos=(-0.343, 0.404), resolution=(720, 1280))):
            touch(Template(r"tpl1698162005692.png", record_pos=(-0.343, 0.404), resolution=(720, 1280)))
        sleep(10)
        try:
            wait(Template(r"tpl1698162054176.png", record_pos=(0.0, 0.449), resolution=(720, 1280)))
        except Exception as login_exception:
            print("login ERROR!!!",str(login_exception))
            return False
        sleep(1)
        touch(Template(r"tpl1698162072632.png", record_pos=(-0.003, 0.451), resolution=(720, 1280)))

        if exists(Template(r"tpl1698162123963.png", record_pos=(0.001, 0.604), resolution=(720, 1280))):
            touch(Template(r"tpl1698162133953.png", record_pos=(-0.019, 0.607), resolution=(720, 1280)))
        sleep(6)
        return True
    #意外情况
    def circumstances(self):
        if exists(Template(r"tpl1698164980116.png", record_pos=(0.388, -0.75), resolution=(720, 1280))):
            touch(Template(r"tpl1698164989196.png", record_pos=(0.021, 0.754), resolution=(720, 1280)))
            return True
        if exists(Template(r"tpl1698162921239.png", record_pos=(-0.003, -0.133), resolution=(720, 1280))):
            touch(Template(r"tpl1698162929618.png", record_pos=(0.206, 0.085), resolution=(720, 1280)))
            return True
        if exists(Template(r"tpl1698162734245.png", record_pos=(0.004, -0.036), resolution=(720, 1280))):
            touch(Template(r"tpl1698162756731.png", record_pos=(0.147, 0.199), resolution=(720, 1280)))
            return True
        return False
    def is_map(self):
        if exists(Template(r"tpl1711391167151.png", record_pos=(0.007, -0.581), resolution=(720, 1280))):
            touch(self.kongbai)

        if exists(Template(r"tpl1698043459932.png", record_pos=(-0.008, -0.537), resolution=(720, 1280))):
            touch((128, 973))
            sleep(0.5)
        if exists(self.query_mapper[self.auto_map]):
            return True
        return False
        
    #查找地图
    def find_all_map(self):
        for key in range(len(self.query_mapper),0,-1):
            if exists(self.query_mapper[key]):
                return key
    def next_d(self,count):
        for i in range(0,count):
            sleep(0.2)
            swipe((642, 395), vector=[-0.6869, 0.0233])
    def d_next(self,count):
        for i in range(0,count):
            sleep(0.2)
            swipe((88, 393), vector=[0.6773, 0.0043])
    def select_map(self):
        if exists(Template(r"tpl1698172923668.png", record_pos=(0.107, 0.222), resolution=(720, 1280))):
            if exists(self.query_mapper[self.auto_map]):
                return True
        if exists(Template(r"tpl1698173051046.png", record_pos=(0.342, -0.354), resolution=(720, 1280))):
            touch((614, 392))
            touch(Template(r"tpl1698173290525.png", record_pos=(0.386, -0.753), resolution=(720, 1280)))
            
            rel = self.find_all_map()
            if(rel>self.auto_map):
                self.d_next(abs(rel-self.auto_map))
            else:
                self.next_d(abs(rel-self.auto_map))
            try:
                touch(Template(r"tpl1698173564615.png", record_pos=(0.01, 0.754), resolution=(720, 1280)))
            except Exception as login_exception:
                print("select map fail!!!",str(login_exception))
             
        return True

    def auto_query(self):
    
        if exists(Template(r"tpl1698171714981.png", record_pos=(-0.343, 0.411), resolution=(720, 1280))):
            self.login()
            sleep(10)
        if exists(Template(r"tpl1698171617700.png", record_pos=(-0.397, -0.824), resolution=(720, 1280))):
            touch(Template(r"tpl1698171636964.png", record_pos=(-0.404, -0.824), resolution=(720, 1280)))
        if exists(Template(r"tpl1698044056929.png", record_pos=(0.003, -0.45), resolution=(720, 1280))):
            touch((346, 287))
        if exists(Template(r"tpl1698062935273.png", record_pos=(0.082, 0.854), resolution=(720, 1280))):
            print("INFO: 游戏已登录，准备执行刷图程序")
            touch(Template(r"tpl1698062935273.png", record_pos=(0.082, 0.854), resolution=(720, 1280)))   
            sleep(1)
            if self.is_map():
                return 
            else:
                self.select_map()
                
        if self.circumstances():
            sleep(3)
            return 
    def select_rouge_a(self) :
        sleep(0.8)
        if exists(Template(r"tpl1698043471445.png", record_pos=(-0.319, 0.211), resolution=(720, 1280))):
            touch(Template(r"tpl1698043471445.png", record_pos=(-0.319, 0.211), resolution=(720, 1280)))
            return
        if exists(Template(r"tpl1698044687677.png", rgb=False, record_pos=(-0.319, 0.211), resolution=(720, 1280))):
            touch(Template(r"tpl1698044687677.png", record_pos=(-0.319, 0.211), resolution=(720, 1280)))
            return
        touch((428, 973))
        sleep(0.5)
    def select_touge_b(self):
        touch((129, 979))
    def copy_swipe(self,ms):
        touch((428, 973))
        sleep(0.1)
        swipe((362, 1034), vector=[-0.0069, -0.225],duration=ms)
        sleep(0.2)
        touch((428, 973))
    def run(self):
        self.start_time=0
        self.end_time=0
        self.start_time=time.time()
        while True :
            self.end_time=time.time()
            if exists(Template(r"tpl1698043785636.png", record_pos=(0.007, -0.518), resolution=(720, 1280))):
                self.select_touge_b()
                sleep(0.5)
                self.copy_swipe(1)
                continue
            if exists(Template(r"tpl1698139534302.png", record_pos=(-0.253, -0.719), resolution=(720, 1280))):
                sleep(2.2)
                if exists(Template(r"tpl1698139519196.png", record_pos=(-0.25, -0.719), resolution=(720, 1280))):
                    self.copy_swipe(3)
            if exists(Template(r"tpl1698043459932.png", record_pos=(-0.008, -0.537), resolution=(720, 1280))):
                self.select_rouge_a()
                sleep(0.5)
                if exists(Template(r"tpl1698043459932.png", record_pos=(-0.008, -0.537), resolution=(720, 1280))):
                    self.select_rouge_a()
                self.copy_swipe(3)
                continue
            
            if exists(Template(r"tpl1698139227577.png", record_pos=(0.0, 0.546), resolution=(720, 1280))):
                touch(self.zhaohuan) #召唤
                touch(self.heidong) 
                if (self.end_time-self.start_time)>80:
                    #幻神
                    touch(self.huanshen)
                    continue
            if exists(Template(r"tpl1698044056929.png", record_pos=(0.003, -0.45), resolution=(720, 1280))):
                touch((346, 287))
                return       
            if exists(self.query_mapper[self.auto_map]):
                return
            sleep(0.2)
            if exists(Template(r"tpl1698162734245.png", record_pos=(0.004, -0.036), resolution=(720, 1280))):
                touch(Template(r"tpl1698162756731.png", record_pos=(0.147, 0.199), resolution=(720, 1280)))
        
        
    def auto_run(self):
        while True:
            if self.is_map() or exists(Template(r"tpl1698139534302.png", record_pos=(-0.253, -0.719), resolution=(720, 1280))):
                sleep(1)
            if exists(Template(r"tpl1698043407732.png", record_pos=(0.115, 0.218), resolution=(720, 1280))) or exists(Template(r"tpl1698139534302.png", record_pos=(-0.253, -0.719), resolution=(720, 1280))):
                sleep(1)
                if exists(Template(r"tpl1698113360661.png", record_pos=(0.003, -0.458), resolution=(720, 1280))):
                    sleep(1)
                    touch(Template(r"tpl1698113370469.png", record_pos=(0.003, -0.444), resolution=(720, 1280)))
                    sleep(1)
                    continue

                if exists(Template(r"tpl1698043432153.png", record_pos=(0.001, 0.483), resolution=(720, 1280))):
                    touch(Template(r"tpl1698043432153.png", record_pos=(0.001, 0.483), resolution=(720, 1280)))
                if exists(Template(r"tpl1698049190675.png", record_pos=(-0.015, -0.397), resolution=(720, 1280))):
                    touch(Template(r"tpl1698049208670.png", record_pos=(0.401, -0.408), resolution=(720, 1280)))
                    print("体力执行完成,程序退出")
                    break
                sleep(2)
                if exists(Template(r"tpl1711391167151.png", record_pos=(0.007, -0.581), resolution=(720, 1280))):
                    touch(self.kongbai)
                self.run()
    def start(self):
        self.auto_query();
        self.auto_run()
        
        
        
     
if __name__ == "__main__":
    game = game_md(AUTO_MAP)
    game.start();


