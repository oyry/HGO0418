# @Time    : 19-4-8
# @Author  : 欧阳
# @File    : commtest.py
from HGOCOMMON import compostclass,commvarclass
import random

testing = compostclass.MainTest()
variable = commvarclass.Variable()

_id = _uid = random.randint(1, 999)
host = '172.17.13.74'
port = ['80','91']
url = ['/ocm-info-webin/rest', '/ocm-wallet-webin/rest']
querystring = [{'method': 'efuture.ocm.info.main.auth', 'ent_id': 1582944742277124566},
               {'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124566},
               {'method': 'efuture.ocm.wallet.rebate.get', 'ent_id': 1582944742277124566},
               {'method': 'efuture.ocm.wallet.rebate.billaudit', 'ent_id': 1582944742277124566},
               {'method': 'efuture.ocm.wallet.card.salelist', 'ent_id': 1582944742277124566},
               {'method': 'efuture.ocm.wallet.card.award', 'ent_id': 1582944742277124566},
               {'method': 'efuture.ocm.wallet.card.sale', 'ent_id': 1582944742277124566},
               {'method': 'efuture.ocm.wallet.card.orderfinish', 'ent_id': 1582944742277124566},
               {'method': 'efuture.ocm.wallet.card.ordersearch', 'ent_id': 1582944742277124566}]
date = [variable.Sdate(), variable.Edate(), variable.Inputdate()]
if __name__ == '__main__':
    """优惠信息流程"""
    testing.HgoMain(host, port[1], url[1], querystring[1], [
        {"billmoduleid": "9006666", "billstatus": "N", "summary": "C", "rebate_target": "1", "rebate_type": "1",
         "totallimit": "0", "singlelimit": "0", "sdate": str(date[0]), "edate": str(date[1]), "inputer": "admin",
         "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": str(date[2]), "pagesize": "100", "czk_rebate_det": [
            {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "rebate_condition": "38",
             "rebate_discount_money": "2.5"}], "flag": "I"}])  # 新增购卡优惠-折扣金额
    testing.HgoMain(host, port[1], url[1], querystring[2], {"ph_key": testing.CzkKey()})  # 查询购卡优惠-折扣金额
    testing.HgoMain(host, port[1], url[1], querystring[3], {"billno": testing.CzkBillno()})  # 审核购卡优惠-折扣金额
    """购卡接口流程"""
    testing.HgoMain(host, port[1], url[0], querystring[0],
                    {'corp_id': '002', 'channel_id': 'WECHAT', 'mkt_id': '207', 'id_password': '',
                     'id_keyword': '9800021122746', 'id_type': 'C', 'fields': '*,consumers_data'})  # 会员认证
    hyxx = testing.UserInfo()
    testing.HgoMain(host, port[1], url[1], querystring[4],
                    {"page_no": 1, "page_size": 100, "status": "%", "channel_id": "WECHAT", "cid": hyxx[0],
                     "ctype": hyxx[1], "cflag": "04", "wxid": "limin", "receiver_mobile": hyxx[2]})  # 可售卖清单查询
    testing.HgoMain(host, port[1], url[1], querystring[5],
                    {"channel_id": "WECHAT", "cid": hyxx[0], "ctype": hyxx[1], "summary": "C"})  # 购卡优惠信息
    testing.HgoMain(host, port[1], url[1], querystring[6],
                    {"UserAgreement": "免责声明", "market": "6206", "channel_id": "WECHAT", "cid": hyxx[0],
                     "ctype": hyxx[1], "cflag": "04", "wxid": "limin", "mobile": hyxx[2], "corp_id": "0",
                     "summary": "C", "card_num": 1, "memo": "购买100元面值储值卡1张", "amount": 38, "discount": 2.5, "award": 0,
                     "award_bill": testing.Award_Bill(), "sale_price": 100, "face_value": 100, "cardtype": "468",
                     "cardtype_name": "HGO电子卡"})  # 购卡订单提交
    billno = testing.Czkgkbillno()
    testing.HgoMain(host, port[1], url[1], querystring[7],
                    {"channel_id": "WECHAT", "billno": billno, "summary": "C", "eventtype": "01", "merchantid": "",
                     "transaction_id": "", "out_trade_no": "PURH" + billno, "total_fee": 8900, "paycode": "debugpay",
                     "payname": "模拟支付", "payref1": "", "payref2": "", "payref3": ""})  # 购卡订单完成
    testing.HgoMain(host, port[1], url[1], querystring[8],
                    {"page_no": 1, "page_size": 100, "billno": billno, "channel_id": "WECHAT",
                     "cid": hyxx[0]})  # 购卡订单查询

    """异常测试"""
    testing.HgoMain(host, port[0],'/ampOpenapiService', {'method': 'usercenter.authentication.signInNoEnt'},
                    {"userCode": "admin", "password": "111", "tag": "mss", "locale": "CN"})
    testing.HgoMain(host, port[0],'/amp-auth-service/rest', {'method': 'amp.auth.authentication.signInNoEnt'},
                    {"code": "1582944742277124566", "password": "j8ptrt", "tag": "mss"})
    testing.HgoMain(host, port[1], '/amp-auth-service/rest', {'method': 'amp.auth.authentication.signInNoEnt'},
                    {"code": "1582944742277124566", "password": "j8ptrt", "tag": "mss"})
