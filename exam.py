# -*- coding: UTF-8 -*-

import json
import time
import string
import IPython
import pandas as pd
from login import *
from tqdm import trange
from bs4 import BeautifulSoup

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# data = {
#     'callCount':'1',
#     'page':"/webapps/bb-mygrades-BBLEARN/myGrades?course_id=_2441_1&stream_name=mygrades",
#     'httpSessionId':'E0B6208F4C1E181451879D30E653738B',
#     'scriptSessionId':'126D9C65B9150D511B06AA72F6F9B7C2319',
#     'c0-scriptName':'UserDataDWRFacade',
#     'c0-methodName':'getStringPermScope',
#     'c0-id':'0',
#     'c0-param0':'string:mygrades.filterBy',
#     'batchId':'1'
# }
# response = session.post(url, data=data)

class checker:
    def __init__(self, studentid, password, session = None):
        self.trash = ["\r", "\t", "\n", " "]
        with open('scorebanner', 'r') as f:
            self.banner = ''.join(f.readlines())
        print(self.banner)
        if not session:
            print('[+] Start to login...')
            self.session = login(studentid, password)

    def getEnglishScore(self):
        url = r"https://eams.shanghaitech.edu.cn/eams/myOtherEngGrade!search.action?semester.id=142"
        response = self.session.get(url)
        soup = BeautifulSoup(self.htmlfilter(response.text), "html.parser")
        data = soup.find_all('td')
        id_idx = 0
        for i in range(len(data)):
            if str(data[i].contents[0]).isnumeric():
                id_idx = i
                break
        ret_data = {
            'id': data[id_idx].contents[0],
            'name': data[id_idx+1].contents[0],
            'semester': data[id_idx+2].contents[0],
            'subject': data[id_idx+3].contents[0],
            'score': data[id_idx+4].contents[0],
            'status': data[id_idx+5].contents[0],
        }
        print('[+] Gather English score done!')
        print(pd.DataFrame([ret_data]))
        return ret_data
    
    def getExamInfo(self, year, semester, target_exam, tag, redirectid, which=1):

        def gatherData(data):
            id_idx = 0
            for i in range(len(data)):
                if self.idchecker(str(data)):
                    id_idx = i
                    break
            place = str(data[id_idx+5].contents[0])
            place = place[place.find('>')+1:]
            place = place[:place.find('<')]
            ret_data = {
                'id': data[id_idx].contents[0],
                'subject': data[id_idx+1].contents[0],
                'type': data[id_idx+2].contents[0],
                'date': data[id_idx+3].contents[0],
                'time': data[id_idx+4].contents[0],
                'place': place,
                'status': data[id_idx+6].contents[0],
            }
            last_other = data[id_idx+7]
            if last_other.contents:
                ret_data['others'] = data[id_idx+7].contents[0]
            return ret_data, id_idx

        print('[+] Searching...')
        cnt = 0
        ampli = int(year) - 2020
        lb = 500 + 100 * ampli + (int(semester) - 1) * 50
        ub = lb + 50 * int(semester)
        for queryid in trange(lb, ub):
            url = f"https://eams.shanghaitech.edu.cn/eams/stdExamTable!examTable.action?examBatch.id={queryid}&tutorRedirectstudentId={redirectid}"
            response = self.session.get(url)
            if tag in response.text and target_exam in response.text:
                cnt += 1
                if cnt == which:
                    break
            time.sleep(0.5)
        soup = BeautifulSoup(self.htmlfilter(response.text), "html.parser")
        data = soup.find_all('td')
        ret_data = []
        while data:
            tmp_ret_data, id_idx = gatherData(data)
            data = data[id_idx+8:]
            ret_data.append(tmp_ret_data)
        print('[+] Done! Find exam informations:')
        print(pd.DataFrame(ret_data))
        return ret_data

    def htmlfilter(self, data):
        for t in self.trash:
            data = data.replace(t, '')
        return data
    
    def idchecker(self, data):
        tabel = string.digits + string.ascii_letters
        for x in data:
            if x not in tabel:
                return False
        return True

if __name__ == '__main__':
    Checker = checker('*******', '******')
    IPython.embed()
    # Checker.getEnglishScore()
    # Checker.getExamInfo('2020', '1', "期末考试", 'CS152.01', 4696)
