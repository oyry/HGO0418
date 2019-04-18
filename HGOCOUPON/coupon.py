# @Time    : 19-3-28
# @Author  : 欧阳
# @File    : coupon.py
from HGOCOMMON import commonpost, commonvariable
import random

ent_id = 1582944742277124566
_id = _uid = random.randint(1,999)
"""引用函数变量"""
validity_sdate = sdate = commonvariable.Sdate()
validity_edate = edate = commonvariable.Edate()
inputdate = commonvariable.Inputdate()

if __name__ == '__main__':
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.billaccnttype.save', 'ent_id': ent_id},
                       payload={"pid": "0201", "name": "面值券" + commonvariable.time(), "billmoduleid": "6006002",
                                "usertype": "02",
                                "billstatus": "N", "face_mode": "2", "face_val": "25", "mje": "0", "useamtimit": "0",
                                "usenumlimit": "1", "canpayback": "Y", "validity_mode": "3", "validity_days": "0",
                                "edate": edate, "return_day": "0", "return_rate": "1", "custtype": "ALL",
                                "custtype_name": "[ALL]所有人", "paycode": "0505", "paycodename": "[0505]自助惠Go券",
                                "ruleexcettype": "1", "usescope": "0", "chid": "%", "chid_name": "[%]全部", "mktid": "%",
                                "mktid_name": "[%]全部", "tenantcope": "2", "tenantsetmode": "0", "tenantrate": "0",
                                "tenantcode": "%", "tenantcode_name": "[%]全部", "setmode": "ALL", "is_pop": "N",
                                "is_jf": "N", "is_czz": "N", "qtname": "面值券" + sdate, "description": "面值券" + edate,
                                "fdresult": "1",
                                "fdmode": "3", "popzkfd": "1", "corpid": "0", "group_id": "02",
                                "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate,
                                "billcustdetail": [
                                    {"flag": "I", "cancelflag": "N", "custgroup": "00", "custtype": "ALL",
                                     "billmoduleid": "6006002", "custtype_name": "[ALL]所有人", "tags": "T", "_id": _id,
                                     "_uid": _uid, "_state": "added"}], "billmktdetail": [], "billchanneldetail": [],
                                "billtenantdetail": [], "flag": "I", "baccnttypegoodsdet": [],
                                "baccnttypedatedet": []})  # 面值券定义新增
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.billaccnttype.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 面值券定义查询
    mzhd = commonpost.mztid()
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.billaccnttype.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.jbillno()})  # 面值券定义审核
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.save', 'ent_id': ent_id},
                       payload={"billmoduleid": "6006103", "billstatus": "N",
                                "activity_name": "买券" + commonvariable.time(),
                                "tpid": "1901001",
                                "tpid_name": "[1901001]19年档期", "tid": mzhd[0], "name": "[" + mzhd[0] + "]" + mzhd[1],
                                "face_val": mzhd[2], "usertype": mzhd[3], "validity_mode": mzhd[4],
                                "validity_days": mzhd[5],
                                "sdate": sdate, "edate": edate, "stime": "00:00", "etime": "23:59",
                                "weeks": "1,2,3,4,5,6,7", "cash": "0.01", "points": "0", "totnum": "0",
                                "totnum_day": "0", "custlimit": "0", "custlimit_day": "0", "jftype": "1",
                                "custtype": "HALL", "custtype_name": "[HALL]所有会员", "mktid": "207",
                                "mktid_name": "[207]水晶城", "corpid": "002", "group_id": "02", "billcustdetail": [],
                                "flag": "I"})  # 买券活动定义
    ph_key = commonpost.ph_key()
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.get', 'ent_id': ent_id},
                       payload=ph_key)  # 买券活动查询
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.hdbillno()})  # 买券活动审核
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.get', 'ent_id': ent_id},
                       payload=ph_key)  # 获取买券活动ID
    commonpost.HgoMain('/omp-activity-webin/rest', {'method': 'efuture.omp.activity.show', 'ent_id': ent_id},
                       payload={"category": [
                           {"category_code": "001", "category_name": "热点关注", "channel_id": "WECHAT", "group_id": "00"}],
                           "channel": [{"channel_id": "WECHAT"}], "detail_usage_desc": "买券活动" + sdate,
                           "detail_usage_rule": "买券活动" + edate,
                           "displaypos": [{"channel_id": "WECHAT", "display_code": "01", "display_name": "首页推荐"}],
                           "event_id": commonpost.event_id(), "event_pic_url": "", "coupon_pic_url": "",
                           "order_seq": 10000, "show_in_list": "Y"})  # 买券活动发布

    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.billaccnttype.save', 'ent_id': ent_id},
                       payload={"pid": "0201", "name": "礼品券" + commonvariable.time(), "billmoduleid": "6006003",
                                "usertype": "03", "billstatus": "N",
                                "face_mode": "2", "face_val": "25", "mje": "0", "useamtimit": "0", "usenumlimit": "1",
                                "canpayback": "Y", "validity_mode": "3", "validity_days": "0", "edate": edate,
                                "return_day": "0", "return_rate": "0", "custtype": "ALL", "custtype_name": "[ALL]所有人",
                                "ruleexcettype": "1", "usescope": "0", "chid": "%", "chid_name": "[%]全部", "mktid": "%",
                                "mktid_name": "[%]全部", "tenantcope": "2", "tenantsetmode": "0", "tenantrate": "0",
                                "tenantcode": "%", "tenantcode_name": "[%]全部", "setmode": "ALL", "is_pop": "N",
                                "is_jf": "N",
                                "is_czz": "N", "qtname": "礼品券" + sdate, "description": "礼品券" + edate, "fdresult": "1",
                                "fdmode": "3",
                                "popzkfd": "1", "corpid": "0", "group_id": "02", "inputer_name": "[admin]惠Go MSS 管理员",
                                "inputdate": inputdate, "billmktdetail": [], "billchanneldetail": [],
                                "billtenantdetail": [], "billcustdetail": [
                               {"flag": "I", "cancelflag": "N", "custgroup": "00", "custtype": "ALL",
                                "billmoduleid": "6006003", "custtype_name": "[ALL]所有人", "tags": "T", "_id": _id,
                                "_uid": _uid, "_state": "added"}], "flag": "I", "baccnttypegoodsdet": [],
                                "baccnttypedatedet": []})  # 礼品券定义新增
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.billaccnttype.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 礼品券定义查询
    mzhd = commonpost.mztid()
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.billaccnttype.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.jbillno()})  # 礼品券定义审核
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.save', 'ent_id': ent_id},
                       payload={"billmoduleid": "6006104", "billstatus": "N",
                                "activity_name": "兑券" + commonvariable.time(),
                                "tpid": "1901001",
                                "tpid_name": "[1901001]19年档期", "tid": mzhd[0], "name": "[" + mzhd[0] + "]" + mzhd[1],
                                "face_val": mzhd[2], "usertype": mzhd[3], "validity_mode": mzhd[4],
                                "validity_sdate": validity_sdate, "validity_edate": validity_edate,
                                "validity_days": mzhd[5],
                                "sdate": sdate, "edate": edate, "stime": "00:00", "etime": "23:59",
                                "weeks": "1,2,3,4,5,6,7", "cash": "0", "points": "10", "totnum": "0", "totnum_day": "0",
                                "custlimit": "0", "custlimit_day": "0", "jftype": "1", "custtype": "HALL",
                                "custtype_name": "[HALL]所有会员", "mktid": "207", "mktid_name": "[207]水晶城",
                                "corpid": "002", "group_id": "02", "billcustdetail": [], "flag": "I"})  # 兑券活动定义
    ph_key = commonpost.ph_key()
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.get', 'ent_id': ent_id},
                       payload=ph_key)  # 兑券活动查询
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.hdbillno()})  # 兑券活动审核
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.get', 'ent_id': ent_id},
                       payload=ph_key)  # 获取兑券活动ID
    commonpost.HgoMain('/omp-activity-webin/rest', {'method': 'efuture.omp.activity.show', 'ent_id': ent_id},
                       payload={"category": [
                           {"category_code": "001", "category_name": "热点关注", "channel_id": "WECHAT", "group_id": "00"}],
                           "channel": [{"channel_id": "WECHAT"}], "detail_usage_desc": "兑券活动" + sdate,
                           "detail_usage_rule": "兑券活动" + edate,
                           "displaypos": [{"channel_id": "WECHAT", "display_code": "01", "display_name": "首页推荐"}],
                           "event_id": commonpost.event_id(), "event_pic_url": "", "coupon_pic_url": "",
                           "order_seq": 10000, "show_in_list": "Y"})  # 兑券活动发布

    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.billaccnttype.save', 'ent_id': ent_id},
                       payload={"pid": "0201", "name": "折扣券" + commonvariable.time(), "billmoduleid": "6006004",
                                "usertype": "04",
                                "billstatus": "N", "face_mode": "2", "face_val": "0.25", "mje": "0", "useamtimit": "0",
                                "usenumlimit": "1", "canpayback": "Y", "validity_mode": "3", "validity_days": "0",
                                "edate": edate, "return_day": "0", "return_rate": "0", "custtype": "ALL",
                                "custtype_name": "[ALL]所有人", "ruleexcettype": "1", "usescope": "0", "chid": "%",
                                "chid_name": "[%]全部", "mktid": "%", "mktid_name": "[%]全部", "tenantcope": "2",
                                "tenantsetmode": "1", "tenantrate": "0", "tenantcode": "%", "tenantcode_name": "[%]全部",
                                "setmode": "ALL", "is_pop": "N", "is_jf": "N", "is_czz": "N", "qtname": "折扣券" + sdate,
                                "description": "折扣券" + edate, "fdresult": "1", "fdmode": "3", "popzkfd": "1",
                                "corpid": "0",
                                "group_id": "05", "inputer_name": "[admin]惠Go MSS 管理员",
                                "inputdate": inputdate, "billcustdetail": [
                               {"flag": "I", "cancelflag": "N", "custgroup": "00", "custtype": "ALL",
                                "billmoduleid": "6006004", "custtype_name": "[ALL]所有人", "tags": "T", "_id": _id,
                                "_uid": _uid, "_state": "added"}], "billmktdetail": [], "billchanneldetail": [],
                                "billtenantdetail": [], "flag": "I", "baccnttypegoodsdet": [],
                                "baccnttypedatedet": []})  # 折扣券定义新增
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.billaccnttype.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 折扣券定义查询
    mzhd = commonpost.mztid()
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.billaccnttype.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.jbillno()})  # 折扣券定义审核
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.save', 'ent_id': ent_id},
                       payload={"billmoduleid": "6006101", "billstatus": "N",
                                "activity_name": "领券" + commonvariable.time(), "tpid": "1901001",
                                "tpid_name": "[1901001]19年档期", "tid": mzhd[0], "name": "[" + mzhd[0] + "]" + mzhd[1],
                                "face_val": mzhd[2], "usertype": mzhd[3], "validity_mode": mzhd[4],
                                "validity_days": mzhd[5],
                                "sdate": sdate, "edate": edate, "stime": "00:00", "etime": "23:59",
                                "weeks": "1,2,3,4,5,6,7", "cash": "0", "points": "0", "totnum": "0", "totnum_day": "0",
                                "custlimit": "0", "custlimit_day": "0", "jftype": "1", "custtype": "HALL",
                                "custtype_name": "[HALL]所有会员", "mktid": "207", "mktid_name": "[207]水晶城",
                                "corpid": "002", "group_id": "05", "billcustdetail": [], "flag": "I"})  # 领券活动定义
    ph_key = commonpost.ph_key()
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.get', 'ent_id': ent_id},
                       payload=ph_key)  # 领券活动查询
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.hdbillno()})  # 领券活动审核
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.get', 'ent_id': ent_id},
                       payload=ph_key)  # 获取领券活动ID
    commonpost.HgoMain('/omp-activity-webin/rest', {'method': 'efuture.omp.activity.show', 'ent_id': ent_id},
                       payload={"category": [
                           {"category_code": "001", "category_name": "热点关注", "channel_id": "WECHAT", "group_id": "00"}],
                           "channel": [{"channel_id": "WECHAT"}], "detail_usage_desc": "领券活动" + sdate,
                           "detail_usage_rule": "领券活动" + edate,
                           "displaypos": [{"channel_id": "WECHAT", "display_code": "01", "display_name": "首页推荐"}],
                           "event_id": commonpost.event_id(), "event_pic_url": "", "coupon_pic_url": "",
                           "order_seq": 10000, "show_in_list": "Y"})  # 领券活动发布

    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.billaccnttype.save', 'ent_id': ent_id},
                       payload={"pid": "0201", "name": "满减券" + commonvariable.time(), "billmoduleid": "6006005",
                                "usertype": "05", "billstatus": "N", "face_mode": "2",
                                "face_val": "25", "mje": "0", "useamtimit": "0", "usenumlimit": "1", "canpayback": "Y",
                                "validity_mode": "3",
                                "validity_days": "0", "edate": edate, "return_day": "0", "return_rate": "0",
                                "custtype": "ALL",
                                "custtype_name": "[ALL]所有人", "ruleexcettype": "1", "usescope": "0", "chid": "%",
                                "chid_name": "[%]全部",
                                "mktid": "%", "mktid_name": "[%]全部", "tenantcope": "2", "tenantsetmode": "1",
                                "tenantrate": "0", "tenantcode": "%",
                                "tenantcode_name": "[%]全部", "setmode": "ALL", "is_pop": "N", "is_jf": "N",
                                "is_czz": "N", "qtname": "满减券" + sdate,
                                "description": "满减券" + edate, "fdresult": "1", "fdmode": "3", "popzkfd": "1",
                                "corpid": "0",
                                "group_id": "05",
                                "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate, "billcustdetail": [
                               {"flag": "I", "cancelflag": "N", "custgroup": "00", "custtype": "ALL",
                                "billmoduleid": "6006005",
                                "custtype_name": "[ALL]所有人", "tags": "T", "_id": _id, "_uid": _uid, "_state": "added"}],
                                "billmktdetail": [],
                                "billchanneldetail": [], "billtenantdetail": [], "flag": "I", "baccnttypegoodsdet": [],
                                "baccnttypedatedet": []})  # 满减券定义新增
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.billaccnttype.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 满减券定义查询
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.billaccnttype.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.jbillno()})  # 满减券定义审核
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.save', 'ent_id': ent_id},
                       payload={"billmoduleid": "6006104", "billstatus": "N",
                                "activity_name": "兑券" + commonvariable.time(),
                                "tpid": "1901001",
                                "tpid_name": "[1901001]19年档期", "tid": mzhd[0], "name": "[" + mzhd[0] + "]" + mzhd[1],
                                "face_val": mzhd[2], "usertype": mzhd[3], "validity_mode": mzhd[4],
                                "validity_sdate": validity_sdate, "validity_edate": validity_edate,
                                "validity_days": mzhd[5],
                                "sdate": sdate, "edate": edate, "stime": "00:00", "etime": "23:59",
                                "weeks": "1,2,3,4,5,6,7", "cash": "0", "points": "10", "totnum": "0", "totnum_day": "0",
                                "custlimit": "0", "custlimit_day": "0", "jftype": "1", "custtype": "HALL",
                                "custtype_name": "[HALL]所有会员", "mktid": "207", "mktid_name": "[207]水晶城",
                                "corpid": "002", "group_id": "02", "billcustdetail": [], "flag": "I"})  # 抢券活动定义
    ph_key = commonpost.ph_key()
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.get', 'ent_id': ent_id},
                       payload=ph_key)  # 抢券活动查询
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.hdbillno()})  # 抢券活动审核
    commonpost.HgoMain('/omp-work-webin/rest', {'method': 'omp.work.couponactivity.get', 'ent_id': ent_id},
                       payload=ph_key)  # 获取抢券活动ID
    commonpost.HgoMain('/omp-activity-webin/rest', {'method': 'efuture.omp.activity.show', 'ent_id': ent_id},
                       payload={"category": [
                           {"category_code": "001", "category_name": "热点关注", "channel_id": "WECHAT", "group_id": "00"}],
                           "channel": [{"channel_id": "WECHAT"}], "detail_usage_desc": "抢券活动" + sdate,
                           "detail_usage_rule": "抢券活动" + sdate,
                           "displaypos": [{"channel_id": "WECHAT", "display_code": "01", "display_name": "首页推荐"}],
                           "event_id": commonpost.event_id(), "event_pic_url": "", "coupon_pic_url": "",
                           "order_seq": 10000, "show_in_list": "Y"})  # 抢券活动发布
