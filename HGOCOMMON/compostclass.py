# @Time    : 19-4-8
# @Author  : 欧阳
# @File    : compostclass.py
import requests, json
from HGOCOMMON import commonlog

logging = commonlog.get_logger()
res = None

class MainTest(object):
    """POST入口"""
    def HgoPost(self, host, port, url, querystring, payload, header):
        global response
        if header != None:
            try:
                res = requests.request("Post", url='http://' + host + ':' + port + url, params=querystring,
                                           data=json.dumps(payload), headers=header, timeout=8, verify=False)
                response = res.content.decode('utf-8')
            except Exception as e:
                logging.error("请求异常" + "-" * 20 + ">" * 2 + " %s", e)
        else:
            try:
                res = requests.request("Post", url='http://' + host + ':' + port + url, params=querystring,
                                           data=json.dumps(payload), timeout=8, verify=False)
                response = res.content.decode('utf-8')
            except Exception as e:
                logging.error("请求异常" + "-" * 20 + ">" * 2 + " %s", e)
        logging.info("接口请求url" + "-" * 20 + ">" * 2 + " %s", res.url)
        logging.info("接口请求data" + "-" * 20 + ">" * 2 + " %s", payload)
        if res.status_code == 200:
            returncode = json.loads(response)
            code = returncode['returncode']
            if code == 0 or code == '0':
                logging.info("Success" + "-" * 20 + ">" * 2 + " %s", response)
            else:
                logging.debug("Failure" + "-" * 20 + ">" * 2 + " %s", response)
                exit()
        else:
            logging.error("Error" + "-" * 20 + ">" * 2 + " %s", response)
    """GET入口"""
    def HgoGet(self, host, port, url, querystring, payload, header):
        if header != None:
            try:
                res = requests.request("Get", url='http://' + host + ':' + port + url, params=querystring,
                                       data=json.dumps(payload), headers=header, timeout=8, verify=False)
                response = res.content.decode('utf-8')
            except Exception as e:
                logging.error("请求异常" + "-" * 20 + ">" * 2 + " %s", e)
        else:
            try:
                res = requests.request("Get", url='http://' + host + ':' + port + url, params=querystring,
                                       data=json.dumps(payload), timeout=8, verify=False)
                response = res.content.decode('utf-8')
            except Exception as e:
                logging.error("请求异常" + "-" * 20 + ">" * 2 + " %s", e)
        logging.info("接口请求url" + "-" * 20 + ">" * 2 + " %s", res.url)
        logging.info("接口请求data" + "-" * 20 + ">" * 2 + " %s", payload)
        if res.status_code == 200:
            returncode = json.loads(response)
            code = returncode['returncode']
            if code == 0 or code == '0':
                logging.info("Success" + "-" * 20 + ">" * 2 + " %s", response)
            else:
                logging.debug("Failure" + "-" * 20 + ">" * 2 + " %s", response)
                exit()
        else:
            logging.error("Error"+ "-" * 20 + ">" * 2 + " %s",response)
    """主入口"""
    def HgoMain(self, host, port, url, querystring, payload, header=None, method='post'):
        if method in ('post', 'Post', 'POst', 'POSt', 'POST', 'get', 'Get', 'GEt', 'GET'):
            if method == 'post' or 'Post' or 'POst' or 'POSt' or 'POST':
                try:
                    response = self.HgoPost(host, port, url, querystring, payload, header)
                except ValueError as e:
                    return e
            else:
                try:
                    response = self.HgoGet(host, port, url, querystring, payload, header)
                except ValueError as e:
                    return e
        else:
            raise Exception('暂不支持该请求类型！')
        return response

    def UserInfo(self):
        info = json.loads(response)
        cid = info['data']['cid']
        ctype = info['data']['cust_type']
        mobile = info['data']['mobile']
        name = info['data']['name']
        return cid, ctype, mobile, name  # 会员认证信息

    def CzkKey(self):
        info = json.loads(response)
        ph_key = info['data'][0]['ph_key']
        return ph_key

    def CzkBillno(self):
        info = json.loads(response)
        billno = info['data']['czk_rebate_hd']['billno']
        return billno

    def Award_Bill(self):
        info = json.loads(response)
        award_bill = info['data']['awardset'][0]['award_bill']
        return award_bill

    def Czkgkbillno(self):
        info = json.loads(response)
        billno = info['data']['billno']
        return billno
