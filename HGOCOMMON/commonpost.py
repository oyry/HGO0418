# @Time    : 19-3-27
# @Author  : 欧阳
# @File    : commonpost.py
import requests, json, traceback
from HGOCOMMON import commonlog

logging = commonlog.get_logger()
res = None

"""定义Post"""
def HgoPost(host, port, url, querystring, payload, header=None):
    global response
    if header != None:
        try:
            res = requests.request("Post", url=host + port + url, params=querystring, data=json.dumps(payload),
                                   headers=header, timeout=8, verify=False)
            response = res.content.decode('utf-8')
        except:
            logging.error("接口异常" + "-" * 20 + ">" * 2 + " %s", res.raise_for_status())
    else:
        try:
            res = requests.request("Post", url=host + port + url, params=querystring, data=json.dumps(payload),
                                   timeout=8, verify=False)
            response = res.content.decode('utf-8')
        except:
            logging.error("接口异常" + "-" * 20 + ">" * 2 + " %s", res.raise_for_status())
    logging.info("接口请求url" + "-" * 20 + ">" * 2 + " %s", res.url)
    logging.info("接口请求data" + "-" * 20 + ">" * 2 + " %s", payload)
    returncode=json.loads(response)
    code=returncode['returncode']
    if code == 0 or code == '0':
        logging.info("Success" + "-" * 20 + ">" * 2 + " %s", response)
    else:
        logging.debug("Failure" + "-" * 20 + ">" * 2 + " %s", response)
        exit()

"""定义Get"""
def HgoGet(host, port, url, querystring, payload, header=None):
    if header != None:
        try:
            res = requests.request("Get", url=host + port + url, params=querystring, data=json.dumps(payload),
                                   headers=header, timeout=8, verify=False)
            response = res.content.decode('utf-8')
        except:
            logging.error("接口异常" + "-" * 20 + ">" * 2 + " %s", res.raise_for_status())
    else:
        try:
            res = requests.request("Get", url=host + port + url, params=querystring, data=json.dumps(payload),
                                   timeout=8, verify=False)
            response = res.content.decode('utf-8')
        except:
            logging.error("接口异常" + "-" * 20 + ">" * 2 + " %s", res.raise_for_status())
    logging.info("接口请求url" + "-" * 20 + ">" * 2 + " %s", res.url)
    logging.info("接口请求data" + "-" * 20 + ">" * 2 + " %s", payload)
    returncode=json.loads(response)
    code=returncode['returncode']
    if code == 0 or code == '0':
        logging.info("Success" + "-" * 20 + ">" * 2 + " %s", response)
    else:
        logging.debug("Failure" + "-" * 20 + ">" * 2 + " %s", response)
        exit()

"""定义主体"""
def HgoMain(url, querystring, method='post', payload=None, header=None, host='http://172.17.13.74', port=':91'):
    if method == 'Post' or 'post':
        try:
            response = HgoPost(host, port, url, querystring, payload, header)
        except:
            traceback.print_exc()
    else:
        try:
            response = HgoGet(host, port, url, querystring, payload, header)
        except:
            traceback.print_exc()
    return response


"""管理平台字段"""
def ph_key():
    info = json.loads(response)
    key = info['data'][0]
    return key  # ph_key字段

def czbillno():
    info = json.loads(response)
    billno = info['data']['czk_rebate_hd']['billno']
    return billno  # 储值卡通用billno

def rzinfo():
    info = json.loads(response)
    cid = info['data']['cid']
    ctype = info['data']['cust_type']
    mobile = info['data']['mobile']
    name = info['data']['name']
    return cid, ctype, mobile, name  # 会员信息认证

def mztid():
    info = json.loads(response)
    tid = info['data']['baccnttypehead']['tid']
    name = info['data']['baccnttypehead']['name']
    face_val = info['data']['baccnttypehead']['face_val']
    usertype = info['data']['baccnttypehead']['usertype']
    validity_mode = info['data']['baccnttypehead']['validity_mode']
    validity_days = info['data']['baccnttypehead']['validity_days']
    return tid, name, face_val, usertype, validity_mode, validity_days  # 券平台

def jbillno():
    info = json.loads(response)
    billno = info['data']['baccnttypehead']['billcustdetail'][0]['billno']
    return billno  # 券平台billno

def hdbillno():
    info = json.loads(response)
    billno = info['data']['bactivityshead']['billno']
    return billno  # 券平台活动billno

def event_id():
    info = json.loads(response)
    event_id = info['data']['bactivityshead']['event_id']
    return event_id  # 券平台活动ID

def lpda():
    info = json.loads(response)
    tid_name = info["data"]["giftsupplierbase"]["tid_name"]
    tid = info["data"]["giftsupplierbase"]["tid"]
    return tid, tid_name  # 积分商城礼品档案

def lpkc():
    info = json.loads(response)
    gbid = info["data"]["report"][0]["gbid"]
    gbname = info["data"]["report"][0]["gbname"]
    gsdrate = info["data"]["report"][0]["gsdrate"]
    gsdjj = info["data"]["report"][0]["gsdjj"]
    gsdbhsjj = info["data"]["report"][0]["gsdbhsjj"]
    gsdsj = info["data"]["report"][0]["gsdsj"]
    return gbid, gbname, gsdrate, gsdjj, gsdbhsjj, gsdsj  # 积分商城礼品库存

def lpbillno():
    info = json.loads(response)
    billno = info["data"]["giftstockhead"]["billno"]
    return billno  # 积分商城

def jftlbillno():
    info = json.loads(response)
    billno = info["data"]["jfsc_exchange_gift_hd"]["billno"]
    return billno  # 积分商城礼品活动

def cmda():
    info = json.loads(response)
    gbid = info["data"]["giftbase"][0]["gbid"]
    cityid = info["data"]["giftbase"][0]["cityid"]
    city_name = info["data"]["giftbase"][0]["city_name"]
    gbname = info["data"]["giftbase"][0]["gbname"]
    return gbid, cityid, city_name, gbname  # 积分商城串码档案

def lpinfo():
    info = json.loads(response)
    gift_id = info["data"]["giftbase"][0]["gbid"]
    gift_name = info["data"]["giftbase"][0]["gbname"]
    purchasing_price = info["data"]["giftbase"][0]["gbjj"]
    selling_price = info["data"]["giftbase"][0]["gbsj"]
    return gift_id, gift_name, purchasing_price, selling_price  # 串码录入

def cmbillno():
    info = json.loads(response)
    billno = info["data"]["difgiftinput"]["billno"]
    return billno  # 积分商城串码活动
"""微信端字段"""
def jfevent_id():
    info = json.loads(response)
    event_id = info["data"]["datalist"][0]["event_id"]
    points = info['data']['datalist'][0]['points']
    cash = info['data']['datalist'][0]['cash']
    return event_id, points, cash  # 积分商城
def order_no():
    info = json.loads(response)
    orderno = info['data']['order_no']
    return orderno  # 积分商城订单号
def award_bill():
    info = json.loads(response)
    awardbill=info['data']['awardset'][0]['award_bill']
    return awardbill
def gkbillno():
    info = json.loads(response)
    billno = info['data']['billno']
    return billno
def card_no():
    info = json.loads(response)
    cardno=info['data']['datalist'][0]['cardno']
    return cardno