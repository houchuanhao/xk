﻿# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import httplib2
import re
base_url = 'http://jwxt.imu.edu.cn/'
#供外部调用的方法
def xk(zjh,mm,kcs):
    flag, cookie = login(zjh=zjh,mm=mm)
    if flag:
        if get_xk_status(cookie=cookie):
            http = httplib2.Http()
            headers = {'Cookie': cookie}
            fajhh = get_fajhh(cookie=cookie)
            url = base_url + 'xkAction.do?actionType=-1&fajhh=' + str(fajhh)
            http.request(url,method='GET',headers=headers)
            url = base_url + 'xkAction.do?actionType=2&pageNumber=-1&oper1=ori'
            http.request(url,method='GET',headers=headers)
            sum = 0
            for kc in kcs:
                # 开始执行搜索请求的发送操作
                kch = kc.get('kch')
                kxh = kc.get('kxh')
                url = base_url + 'xkAction.do?jhxn=&kcsxdm=&kch=<kch>&cxkxh=<cxkxh>&actionType=2&oper2=gl&pageNumber=-1'
                url = url.replace('<kch>',str(kch)).replace('<cxkxh>',str(kxh))
                response, content = http.request(uri=url, method='GET', headers=headers)
                url = base_url + 'xkAction.do?kcId=<kcId>&preActionType=2&actionType=9'
                url = url.replace('<kcId>',str(kch) + '_' + str(kxh))
                response, content = http.request(uri=url, method='GET', headers=headers)
                if '成功' in content.decode('gbk'):
                    sum = sum + 1
            if sum == len(kcs):
                return True,'get calss success'
            else:
                return False,'get calss success ' + str(sum) + 'men faild to get class:' + str(len(kcs)-sum) + 'men'
        else:
            return False, '非选课阶段不允许选课'
    else:
        return False,'password error'

def tk(zjh, mm, kcs):
    flag, cookie = login(zjh=zjh, mm=mm)
    if flag:
        if get_xk_status(cookie=cookie):
            http = httplib2.Http()
            for kc in kcs:
                kch = kc.get('kch')
                headers = {'Cookie': cookie}
                url = base_url + 'xkAction.do?actionType=7'
                request, content = http.request(url, method='GET', headers=headers)
                if kch not in content.decode('GBK'):
                    return False, 'gkcwbx'
                url = base_url + 'xkAction.do?actionType=10&kcId=' + str(kch)
                request, content = http.request(url, method='GET', headers=headers)
                content = content.decode('GBK')
                if kch in content:
                    return False, 'error to lost class'
                return True, 'success to lost class'
        else:
            return False, '非选课阶段不允许选课'
    else:
        return False, 'erro password for lost class'

def tk2xk(src_zjh, src_mm, obj_zjh, obj_mm, kcs):
    flag = False
    tflag, tmsg =  tk(src_zjh, src_mm, kcs)
    print(tmsg)
    while not(flag):
        flag, msg = xk(obj_zjh, obj_mm, kcs)
        print(msg)


"""
以下方法供内部调用
"""
def get_xk_status(cookie):
    url = base_url + 'xkAction.do'
    http = httplib2.Http()
    headers = {'Cookie': cookie}
    response, content = http.request(uri=url, method='GET', headers=headers)
    content = content.decode('gbk')
    if '不允许选课' in content:
        return False
    else:
        return True

def get_fajhh(cookie):
    url = base_url + 'xkAction.do'
    http = httplib2.Http()
    headers = {'Cookie':cookie}
    response, content = http.request(uri=url, method='GET',headers=headers)
    content = content.decode('gbk')
    results = re.findall(r'<td colspan="2"><input type="radio" name="fajhh" value=\'[0-9]{4,6}\'>',content)
    return results[0].replace('<td colspan="2"><input type="radio" name="fajhh" value=\'','').replace('\'>','')


def login(zjh,mm):
    http = httplib2.Http()
    url = base_url + 'loginAction.do'
    body = '?zjh=' + zjh + '&mm=' + mm

    response , content = http.request(url+body, method='GET')
    cookie = response['set-cookie'].replace('; path=/','')
    content = content.decode('gbk')

    if '登录' in content:
        return False, cookie
    else:
        return True, cookie
