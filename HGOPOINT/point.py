# @Time    : 19-3-28
# @Author  : 欧阳
# @File    : point.py
from HGOCOMMON import commonpost, commonvariable
import random

ent_id = 1582944742277124566
_id = _uid = random.randint(1,999)
"""引用函数变量"""
inputdate = commonvariable.Inputdate()
serialno = commonvariable.Number_BJZ()
serialno1 = commonvariable.Number_BJZ()
serialno2 = commonvariable.Number_BJZ()
serialno3 = commonvariable.Number_BJZ()

if __name__ == '__main__':
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.giftsupplierbase.save", "ent_id": ent_id},
                       payload={"tid_name": "供应商" + commonvariable.Chinese(), "mktid": "207", "mktid_name": "[207]水晶城",
                                "status": "Y",
                                "giftsupmktdetail": [
                                    {"flag": "I", "mktid": "207", "mktid_name": "[207]水晶城", "mktgroup": "0",
                                     "mktgroup_name": "0", "billmoduleid": 900901, "_id": _id, "_uid": _uid,
                                     "_state": "added"}],
                                "flag": "I"})  # 供应商档案新增
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.giftsupplierbase.get", "ent_id": ent_id},
                       payload=commonpost.ph_key())  # 供应商档案查询
    lpda = commonpost.lpda()
    """礼品+积分兑礼部分"""
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.giftbase.save", "ent_id": ent_id},
                       payload={"formData": {"formData": [
                           {"ph_key": "", "gbid": "", "gbname": "LP档案" + commonvariable.Chinese(), "gbjj": 25,
                            "gbtype": 1, "mktid": "207",
                            "mktid_name": "[207]水晶城", "gbsj": 38, "gbchr2": lpda[0],
                            "tid_name": "[" + lpda[0] + "]" + lpda[1],
                            "chflag": "N",
                            "gbchr1": "1", "gbnum1": 0.02, "gbintro": "", "gbmemo": "",
                            "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate,
                            "inputer": "admin", "picture1": "", "picture2": "", "picture3": "", "picture4": "",
                            "picture5": "", "gbchr3": "[" + lpda[0] + "]" + lpda[1], "gbkcsl": 0, "flag": "I"}]},
                           "giftmktdetail": {
                               "mktarray": [{"mktid": "207", "mktid_name": "水晶城", "flag": "I"}]}})  # 礼品档案新增
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.report.query", "ent_id": ent_id},
                       payload={"page_size": 100, "giftsupid": lpda[0], "mktid": "207", "status2": "Y",
                                "queryid": "select_supgift",
                                "fields": "gbid,gbname,gsdrate,gsdjj,gsdbhsjj,gsdsj,gbmemo,midjj",
                                "order_field": "gbid", "order_direction": "desc"})  # 礼品档案查询
    lpck = commonpost.lpkc()
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.giftstock.save", "ent_id": ent_id},
                       payload={"billstatus": "N", "billmoduleid": "900902", "mktid": "207", "mktid_name": "[207]水晶城",
                                "giftsupname": "[" + lpda[0] + "]" + lpda[1], "stocktype": "1", "giftsupid": lpda[0],
                                "inputer_name": "[admin]惠Go MSS 管理员", "inputer": "admin", "giftstockdetail": [
                               {"flag": "I", "gsdsl": "10", "_id": _id, "_uid": _uid, "_state": "added",
                                "gbid": lpck[0],
                                "gbname": lpck[1], "gsdrate": lpck[2], "gsdjj": lpck[3], "gsdbhsjj": lpck[4],
                                "gsdsj": lpck[5], "gsdhsjjze": "", "gsdbhsjjze": "", "gsdsjze": "380"}],
                                "flag": "I"})  # 礼品库存管理新增
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.giftstock.get", "ent_id": ent_id},
                       payload=commonpost.ph_key())  # 礼品库存管理查询
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.giftstock.billaudit", "ent_id": ent_id},
                       payload={"billno": commonpost.lpbillno()})  # 礼品库存管理审核
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.exchangeGift.save", "ent_id": ent_id},
                       payload=[{"billmoduleid": "800803", "activity_name": "礼品兑换" + commonvariable.Chinese(),
                                 "billstatus": "N", "mktid": "207",
                                 "exchange_mode": "1,2", "jftype": "1", "jfaccnt_type_name": "当期积分", "custtype": "HALL",
                                 "custtype_name": "[HALL]所有会员", "start_date": commonvariable.Start_Date(),
                                 "end_date": commonvariable.Start_Date(),
                                 "mktid_name": "[207]水晶城", "inputer_name": "[admin]惠Go MSS 管理员",
                                 "inputdate": inputdate, "inputer": "admin", "giftDetail": [
                               {"flag": "I", "undefined": " ", "gift_id": lpck[0], "gift_name": lpck[1],
                                "purchasing_price": lpck[3], "selling_price": lpck[5], "gbmemo": "", "gbtype": "1",
                                "dhjf": "38", "maxsl": "0", "yjjf": "0", "add_amount": "0", "chflag": "N",
                                "gbintro": "", "picture1": "", "picture2": "", "picture3": "", "picture4": "",
                                "picture5": "", "hdzsl": "0", "_id": _id, "_uid": _uid, "_state": "added",
                                "change_edate": commonvariable.End_Date(), "rowno": 1}], "mktDetail": [
                               {"mktid": "207", "mktid_name": "[207]水晶城", "corpid": "002", "flag": "I", "_id": _id,
                                "_uid": _uid, "_state": "added"}], "custtypeDetail": [
                               {"custtype": "HALL", "custtype_name": "[HALL]所有会员", "tags": "T", "flag": "I",
                                "billmoduleid": "800803", "_id": _id, "_uid": _uid, "_state": "added"}],
                                 "flag": "I"}])  # 礼品兑换活动新增
    ph_key = commonpost.ph_key()
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.exchangeGift.get", "ent_id": ent_id},
                       payload=ph_key)  # 礼品兑换活动查询
    billno = commonpost.jftlbillno()
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.exchangeGift.billaudit", "ent_id": ent_id},
                       payload={"billno": billno})  # 礼品兑换活动审核
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.exchangeGift.publish", "ent_id": ent_id},
                       payload={"billno": billno, "ph_key": ph_key["ph_key"], "chid": "WECHAT",
                                "chid_name": "微信", "ppid": "01", "ppid_name": "[01]首页推荐", "displaypos": [
                               {"channel_id": "WECHAT", "display_code": "01", "display_name": "首页推荐"}]})  # 积分兑礼活动发布
    commonpost.HgoMain('/ocm-info-webin/rest', {'method': 'efuture.ocm.info.main.auth', 'ent_id': ent_id},
                       payload={'corp_id': '002', 'channel_id': 'WECHAT', 'mkt_id': '207', 'id_password': '',
                                'id_keyword': "19989198319", 'id_type': '5', 'fields': '*,consumers_data'})  # 会员认证
    hyxx=commonpost.rzinfo()
    commonpost.HgoMain("/omp-activity-webin/rest", {"method": "efuture.omp.activities.getlist", "ent_id": ent_id},
                       payload={"channel_id": "WECHAT", "page_no": 1, "page_size": 100, "cid": hyxx[0],
                                "ctype": hyxx[1], "event_type_code": "6,8", "market": "207"})  # 积分兑礼活动列表
    lpdh=commonpost.jfevent_id()
    commonpost.HgoMain("/omp-activity-webin/rest", {"method": "efuture.omp.activities.getinfo", "ent_id": ent_id},
                       payload={"event_id": lpdh[0], "channel_id": "WECHAT", "cid": hyxx[0],
                                "ctype": hyxx[1]})  # 积分兑礼活动详情
    commonpost.HgoMain("/omp-activity-webin/rest", {"method": "efuture.omp.activities.buycoupon.submitorder", "ent_id": ent_id},
                       payload={"channel_id": "WECHAT", "event_id": lpdh[0], "cid": hyxx[0],
                                "ctype": hyxx[1], "cflag": "04", "wxid": "limin", "name": hyxx[3],
                                "mobile": hyxx[2], "isfl": "Y", "exchage_mode": "1", "city": "00000", "num": 1,
                                "gh_state": "gh_f79e23f74622", "points":lpdh[1]})  # 礼品兑换订单提交-门店自提
    commonpost.HgoMain("/omp-activity-webin/rest", {"method": "efuture.omp.activities.buycoupon.submitorder", "ent_id": ent_id},
                       payload={"channel_id": "WECHAT", "event_id": lpdh[0], "cid": hyxx[0],
                                "ctype": hyxx[1], "cflag": "04", "wxid": "limin", "name": hyxx[3],
                                "mobile": hyxx[2], "isfl": "Y", "exchage_mode": "2", "city": "00000",
                                "post_mobile": hyxx[2], "receiver": hyxx[3], "post_address": "湖北省武汉市武昌区测试模拟地址",
                                "num": 1,
                                "gh_state": "gh_f79e23f74622", "points": lpdh[1]})  # 礼品兑换订单提交-自费邮寄
    """串码+积分兑礼部分"""
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.giftbase.save", "ent_id": ent_id},
                       payload={"formData": {"formData": [
                           {"ph_key": "", "gbid": "", "gbname": "CM档案" + commonvariable.Chinese(), "useScope": "1",
                            "cityid": "00000",
                            "city_name": "[00000]所有城市", "gbjj": "25.00", "gbsj": "38.00",
                            "gbnum1": 0.02, "gbintro": "", "gbmemo": "",
                            "inputer_name": "[admin]惠Go MSS 管理员", "inputer": "admin",
                            "inputdate": inputdate, "picture1": "", "picture2": "", "picture3": "",
                            "picture4": "", "picture5": "", "gbtype": 3, "chflag": "Y", "gbkcsl": 0, "gbstatus": "Y",
                            "flag": "I"}]}, "giftmktdetail": {"mktarray": []}})  # 串码档案新增
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.giftbase.search", "ent_id": ent_id},
                       payload=commonpost.ph_key())  # 串码档案查询
    cmda = commonpost.cmda()
    cmxx=commonpost.lpinfo()
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.difgiftinput.checkData", "ent_id": ent_id},
                       payload={"checkData": [
                           {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added",
                            "serialno": serialno},
                           {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added",
                            "serialno": serialno1},
                           {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added",
                            "serialno": serialno2},
                           {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added",
                            "serialno": serialno3}],
                           "billno": "", "zpid": cmda[0], "cityid": cmda[1]})  # 异业礼品串码录入
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.difgiftinput.save", "ent_id": ent_id},
                       payload=[{"billmoduleid": "7003302", "billstatus": "N", "corpid": "002", "zpid": cmda[0],
                                 "zpname": "[" + cmda[0] + "]" + cmda[3], "cityid": cmda[1], "cityname": cmda[2],
                                 "supplier": lpda[0], "supplier_name": "[" + lpda[0] + "]" + lpda[1], "mktid": "207",
                                 "mktid_name": "[207]水晶城", "gbjj": "25.00", "tax": "0", "hsjj": "0", "bhsjj": "0",
                                 "inputer": "admin", "inputer_name": "[admin]惠Go MSS 管理员",
                                 "inputdate": inputdate, "difgiftinputdetail": [
                               {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "serialno": serialno},
                               {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "serialno": serialno1},
                               {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "serialno": serialno2},
                               {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "serialno": serialno3}],
                                 "flag": "I"}])  # 异业礼品串码保存
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.difgiftinput.get", "ent_id": ent_id},
                       payload=commonpost.ph_key())  # 异业礼品串码查询
    billno = commonpost.cmbillno()
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.difgiftinput.billaudit", "ent_id": ent_id},
                       payload={"billno": billno})  # 异业礼品串码审核
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.exchangeGift.save", "ent_id": ent_id},
                       payload=[{"billmoduleid": "800803", "activity_name": "串码兑换" + commonvariable.Chinese(),
                                 "billstatus": "N", "mktid": "207",
                                 "exchange_mode": "1,2", "jftype": "1", "jfaccnt_type_name": "当期积分", "custtype": "HALL",
                                 "custtype_name": "[HALL]所有会员", "start_date": commonvariable.Start_Date(),
                                 "end_date": commonvariable.Start_Date(),
                                 "mktid_name": "[207]水晶城", "inputer_name": "[admin]惠Go MSS 管理员",
                                 "inputdate": inputdate, "inputer": "admin", "pagesize": "100",
                                 "giftDetail": [
                                     {"flag": "I", "undefined": " ", "gift_id": cmxx[0], "gift_name": cmxx[1],
                                      "purchasing_price": cmxx[2], "selling_price": cmxx[3], "gbmemo": "",
                                      "gbtype": "3", "dhjf": "38", "maxsl": "0", "yjjf": "0",
                                      "add_amount": "0", "chflag": "Y", "usescope": "1", "gbintro": "",
                                      "picture1": "", "picture2": "", "picture3": "", "picture4": "",
                                      "picture5": "", "hdzsl": "0", "_id": _id, "_uid": _uid,
                                      "_state": "added", "smktid": "207", "smktid_name": "[207]水晶城",
                                      "rowno": 1}], "mktDetail": [
                               {"mktid": "207", "mktid_name": "[207]水晶城", "corpid": "002", "flag": "I", "_id": _id,
                                "_uid": _uid, "_state": "added"}], "custtypeDetail": [
                               {"custtype": "HALL", "custtype_name": "[HALL]所有会员", "tags": "T", "flag": "I",
                                "billmoduleid": "800803", "_id": _id, "_uid": _uid, "_state": "added"}],
                                 "flag": "I"}])  # 串码兑换活动新增
    ph_key = commonpost.ph_key()
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.exchangeGift.get", "ent_id": ent_id},
                       payload=ph_key)  # 串码兑换活动查询
    billno = commonpost.jftlbillno()
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.exchangeGift.billaudit", "ent_id": ent_id},
                       payload={"billno": billno})  # 串码兑换活动审核
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "pshop.work.exchangeGift.publish", "ent_id": ent_id},
                       payload={"billno": billno, "ph_key": ph_key["ph_key"], "chid": "WECHAT",
                                "chid_name": "微信", "ppid": "01", "ppid_name": "[01]首页推荐", "displaypos": [
                               {"channel_id": "WECHAT", "display_code": "01", "display_name": "首页推荐"}]})  # 积分兑礼活动发布
    commonpost.HgoMain("/omp-activity-webin/rest", {"method": "efuture.omp.activities.getlist", "ent_id": ent_id},
                       payload={"channel_id": "WECHAT", "page_no": 1, "page_size": 100, "cid": hyxx[0],
                                "ctype": hyxx[1], "event_type_code": "6,8", "market": "207"})  # 积分兑礼活动列表
    cmdh=commonpost.jfevent_id()
    commonpost.HgoMain("/omp-activity-webin/rest", {"method": "efuture.omp.activities.getinfo", "ent_id": ent_id},
                       payload={"event_id": cmdh[0], "channel_id": "WECHAT", "cid": hyxx[0],
                                "ctype": hyxx[1]})  # 积分兑礼活动详情
    commonpost.HgoMain("/omp-activity-webin/rest", {"method": "efuture.omp.activities.buycoupon.submitorder", "ent_id": ent_id},
                       payload={"channel_id": "WECHAT", "event_id": cmdh[0], "cid": hyxx[0],
                                "ctype": hyxx[1], "cflag": "04", "wxid": "limin", "name": hyxx[3],
                                "mobile": hyxx[2], "isfl": "Y", "exchage_mode": "3", "city": "00000", "num": 1,
                                "gh_state": "gh_f79e23f74622", "points":cmdh[1]})  # 串码兑换订单提交
    order_no=commonpost.order_no()
    commonpost.HgoMain("/omp-pshop-webin/rest", {"method": "efuture.omp.activities.buycoupon.done", "ent_id": ent_id},
                       payload={"channel_id": "WECHAT", "order_no": order_no, "merchantid": "",
                                "transaction_id": "", "out_trade_no": "BGIF" + order_no, "total_fee": 10,
                                "paycode": "debugpay", "payname": "模拟支付", "payref1": "", "payref2": "",
                                "payref3": ""})  # 积分兑礼订单支付
