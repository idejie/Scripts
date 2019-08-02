import hashlib
from bs4 import BeautifulSoup
from http import cookiejar
from urllib import request, parse


URL_TEACHING = 'http://bkjws.sdu.edu.cn/'
URL_LOGIN = 'b/ajaxLogin'
URL_GRADE = 'f/jxjh/xs/wcqk'
HEADER = {
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/63.0.3239.132 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
RENZHENG = ['IBM Websphere', 'UML认证', 'CCF计算机职业资格认证']   # 认证课


def login(username, password, url):
    password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
    post_data = {
        "j_username": username,
        "j_password": password_md5
    }
    cookie = cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    req = request.Request(url=URL_TEACHING + url,
                          data=parse.urlencode(post_data).encode('utf-8'),
                          headers=HEADER)
    res = opener.open(req)
    print('login', res.read().decode())
    return opener


def get_grade(opener, url):
    ret = opener.open(URL_TEACHING + url).read().decode()
    ret = BeautifulSoup(ret, "html5lib")
    return ret


def get_grade_from_tab1(tab):

    ths = tab.find_all('th')
    grades = list()

    for tr in tab.find_all('tr'):
        if tr.find_all('td'):
            tds = tr.find_all('td')
            grade = dict()
            for i in range(1,len(tds)):
                grade[ths[i].string] = tds[i].string

            grades.append(grade)
    return grades


def get_grade_from_tab2(tab):
    ths = tab.find_all('th')
    grades = list()

    for tr in tab.find_all('tr'):
        if tr.find_all('td'):
            tds = tr.find_all('td')
            grade = dict()
            if tds[5].string:
                for i in range(1,len(tds)):
                    grade[ths[i].string] = tds[i].string
                grades.append(grade)
    return grades


def get_sum_grade_by_attr_class(grades, attr_class):
    score = 0
    ret = list()
    for grade in grades:
        if grade['课程属性'] == attr_class:
            score = score + float(grade['学分'])
            ret.append(grade)
    return score, ret


def get_sum_grade(grades):
    score = 0
    ret = list()
    for grade in grades:
        score = score + float(grade['学分'])
        ret.append(grade)
    return score, ret


def get_sum_grade_by_list(grades, list_class):
    score = 0
    ret = list()
    for grade in grades:
        if grade['课程名称'] in list_class:
            score = score + float(grade['学分'])
            ret.append(grade)
    return score, ret


def get_sum_grade_by_name(grades, name_class):
    score = 0
    ret = list()
    for grade in grades:
        if name_class in grade['课程名']:
            score = score + float(grade['学分'])
            ret.append(grade)
    return score, ret


if __name__ == '__main__':
    username = input('username:')
    password = input('password：')
    opener = login(username, password, URL_LOGIN)
    response = get_grade(opener, URL_GRADE)

    tabs = response.find_all('table')
    grade1 = get_grade_from_tab1(tabs[1])
    grade2 = get_grade_from_tab2(tabs[2])
    grade3 = get_grade_from_tab1(tabs[3])
    # 获取所有课程以及总分：
    score_all, ret_all = get_sum_grade(grade1 + grade2 + grade3)
    print("==========================================================================")
    print('总学分：', score_all)
    print("==========================================================================")
    score_bi, ret_bi = get_sum_grade_by_attr_class(grade1 + grade2, '必修')
    print('必修学分：', score_bi)
    print(ret_bi)
    print("==========================================================================")
    score_xian, ret_xian = get_sum_grade_by_attr_class(grade1 + grade2, '限选')
    print('限选课学分：',score_xian)
    print(ret_xian)
    print("==========================================================================")
    # 获取所有认证课
    score_rz, ret_rz = get_sum_grade_by_list(grade2, RENZHENG)
    print('认证课数：',len(ret_rz),'学分：',score_rz)
    print(ret_rz)
    print("==========================================================================")
    score_tx, ret_tx = get_sum_grade_by_name(grade3, '通选')
    print('通选：',score_tx, ret_tx)
    print("==========================================================================")
    score_rw, ret_rw = get_sum_grade_by_name(grade3, '人文')
    print('人文：',score_rw, ret_rw)
    print("==========================================================================")
    score_sk, ret_sk = get_sum_grade_by_name(grade3, '社科')
    print('社科：',score_sk, ret_sk)
    print("==========================================================================")
    score_ys, ret_ys = get_sum_grade_by_name(grade3, '艺术')
    print('艺术：',score_ys, ret_ys)
    print("==========================================================================")
    score_cx, ret_cx = get_sum_grade_by_name(grade3, '创新')
    print('创新：', score_cx, ret_cx)
    print("==========================================================================")
    # print by yourself
