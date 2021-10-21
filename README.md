# ShanghaiTech
一个有关上科大的库(等待被封装成真正的库)
懒人助手
+ 自动登录egate (done)
+ 查询考试信息 (done)
+ 查询成绩 (todo)
+ 自动登录bb下载新上传课件 (todo)
+ 各种奇怪的操作 (todo)

## 已有功能
+ 自动登录egate:

+ 查询考试信息：
终端复制过来pandas格式有点乱掉
```
                          _          _                 
                         | |        | |                
  _____  ____ _ _ __ ___ | |__   ___| |_ __   ___ _ __ 
 / _ \ \/ / _` | '_ ` _ \| '_ \ / _ \ | '_ \ / _ \ '__|
|  __/>  < (_| | | | | | | | | |  __/ | |_) |  __/ |   
 \___/_/\_\__,_|_| |_| |_|_| |_|\___|_| .__/ \___|_|   
                                      | |              
                                      |_|       
[+] Start to login...
[+] Login successfully!
Python 3.8.10 (default, Jun  2 2021, 10:49:15) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: Checker.getEnglishScore()                                                                                                                                                                                                                                      
[+] Gather English score done!
           id  name              semester subject score status
0  2019533238  刘通  2019-2020学年第2学期    英语   319   通过
Out[1]: 
{'id': '2019533238',
 'name': '刘通',
 'semester': '2019-2020学年第2学期',
 'subject': '英语',
 'score': '319',
 'status': '通过'}

In [2]: Checker.getExamInfo('2020', '1', "期末考试", 'CS152.01', 4696)                                                                                                                                                                                                 
[+] Searching...
 44%|███████████████████████████████████████████████████████████████████████████████████████████████████▍                                                                                                                              | 22/50 [00:12<00:15,  1.80it/s]
[+] Done! Find exam informations:
            id            subject      type        date         time        place status                              others
0     CS101.02      算法与数据结构   期末考试  2020-12-30  09:00~11:00   教学中心201   正常                    闭卷，不带任何资料
1     CS152.01          应用密码学  期末考试   2020-12-30  13:00~15:00   教学中心102   正常    闭卷，一张A4cheatsheet，可带计算器
2  ECON1001.04          经济学导论  期末考试   2021-01-06  13:00~15:00   教学中心202   正常        闭卷，但可以带一张A4cheatsheet
3  MATH1212.03   概率论与数理统计I   期末考试   2021-01-08  09:00~11:30  教学中心301   正常                                NaN
4  PHYS1111.02       普通物理I实验   期末考试  2020-12-29  13:00~13:30   教学中心101   正常                          闭卷，笔试
5  PHYS1181.03          普通物理I   期末考试  2 020-12-28  08:15~09:55  教学中心301   正常                                闭卷
Out[2]: 
[{'id': 'CS101.02',
  'subject': '算法与数据结构',
  'type': '期末考试',
  'date': '2020-12-30',
  'time': '09:00~11:00',
  'place': '教学中心201',
  'status': '正常',
  'others': '闭卷，不带任何资料'},
 {'id': 'CS152.01',
  'subject': '应用密码学',
  'type': '期末考试',
  'date': '2020-12-30',
  'time': '13:00~15:00',
  'place': '教学中心102',
  'status': '正常',
  'others': '闭卷，一张A4cheatsheet，可带计算器'},
 {'id': 'ECON1001.04',
  'subject': '经济学导论',
  'type': '期末考试',
  'date': '2021-01-06',
  'time': '13:00~15:00',
  'place': '教学中心202',
  'status': '正常',
  'others': '闭卷，但可以带一张A4cheatsheet'},
 {'id': 'MATH1212.03',
  'subject': '概率论与数理统计I',
  'type': '期末考试',
  'date': '2021-01-08',
  'time': '09:00~11:30',
  'place': '教学中心301',
  'status': '正常'},
 {'id': 'PHYS1111.02',
  'subject': '普通物理I实验',
  'type': '期末考试',
  'date': '2020-12-29',
  'time': '13:00~13:30',
  'place': '教学中心101',
  'status': '正常',
  'others': '闭卷，笔试'},
 {'id': 'PHYS1181.03',
  'subject': '普通物理I',
  'type': '期末考试',
  'date': '2020-12-28',
  'time': '08:15~09:55',
  'place': '教学中心301',
  'status': '正常',
  'others': '闭卷'}]

In [3]:                                                                                                                                                                                                                                                                
```
