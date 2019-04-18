# @Time    : 19-3-27
# @Author  : 欧阳
# @File    : wallet.py
from HGOCOMMON import commonpost, commonvariable
import random

ent_id = 1582944742277124566
_id = _uid = random.randint(1,999)
"""引用函数变量"""
sdate = edate = commonvariable.Sdate()
inputdate = commonvariable.Inputdate()
name = commonvariable.Chinese()
reg_keyword = commonvariable.Hfmobile()

if __name__ == '__main__':
    """新增购卡优惠"""
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': ent_id},
                       payload=[
                           {"billmoduleid": "9006666", "billstatus": "N", "summary": "C", "rebate_target": "1",
                            "rebate_type": "1",
                            "totallimit": "0", "singlelimit": "0", "sdate": sdate, "edate": edate, "inputer": "admin",
                            "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate, "pagesize": "100",
                            "czk_rebate_det": [
                                {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "rebate_condition": "38",
                                 "rebate_discount_money": "2.5"}], "flag": "I"}])  # 新增购卡优惠-折扣金额
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 查询购卡优惠-折扣金额
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.czbillno()})  # 审核购卡优惠-折扣金额
    commonpost.HgoMain('/ocm-info-webin/rest', {'method': 'efuture.ocm.info.main.auth', 'ent_id': ent_id},
                       payload={'corp_id': '002', 'channel_id': 'WECHAT', 'mkt_id': '207', 'id_password': '',
                                'id_keyword': reg_keyword, 'id_type': '5', 'fields': '*,consumers_data'})  # 会员认证
    hyxx = commonpost.rzinfo()
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.card.salelist', 'ent_id': ent_id},
                       payload={"page_no": 1, "page_size": 100, "status": "%", "channel_id": "WECHAT", "cid": hyxx[0],
                                "ctype": hyxx[1], "cflag": "04", "wxid": "limin",
                                "receiver_mobile": hyxx[2]})  # 可售卖清单查询
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.card.award', 'ent_id': ent_id},
                       payload={"channel_id": "WECHAT", "cid": hyxx[0], "ctype": hyxx[1], "summary": "C"})  # 购卡优惠信息
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.card.sale', 'ent_id': ent_id},
                       payload={"UserAgreement": "免责声明", "market": "6206", "channel_id": "WECHAT", "cid": hyxx[0],
                                "ctype": hyxx[1], "cflag": "04", "wxid": "limin", "mobile": hyxx[2], "corp_id": "0",
                                "summary": "C", "card_num": 1, "memo": "购买100元面值储值卡1张", "amount": 38, "discount": 2.5,
                                "award": 0,
                                "award_bill": commonpost.award_bill(), "sale_price": 100, "face_value": 100,
                                "cardtype": "468",
                                "cardtype_name": "HGO电子卡"})  # 购卡订单提交
    billno = commonpost.gkbillno()
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.card.orderfinish', 'ent_id': ent_id},
                       payload={"channel_id": "WECHAT", "billno": billno, "summary": "C", "eventtype": "01",
                                "merchantid": "",
                                "transaction_id": "", "out_trade_no": "PURH" + billno, "total_fee": 8900,
                                "paycode": "debugpay", "payname": "模拟支付", "payref1": "", "payref2": "",
                                "payref3": ""})  # 购卡订单完成
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.card.ordersearch', 'ent_id': ent_id},
                       payload={"page_no": 1, "page_size": 1, "billno": billno, "channel_id": "WECHAT",
                                "cid": hyxx[0]})  # 购卡订单查询

    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': ent_id},
                       payload=[
                           {"billmoduleid": "9006666", "billstatus": "N", "summary": "C", "rebate_target": "1",
                            "rebate_type": "2",
                            "totallimit": "0", "singlelimit": "0", "sdate": sdate, "edate": edate, "inputer": "admin",
                            "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate, "pagesize": "100",
                            "czk_rebate_det": [
                                {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "rebate_condition": "38",
                                 "rebate_discount_rate": "0.25"}], "flag": "I"}])  # 新增购卡优惠-折扣率
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 查询购卡优惠-折扣率
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.czbillno()})  # 审核购卡优惠-折扣率

    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': ent_id},
                       payload=[
                           {"billmoduleid": "9006666", "billstatus": "N", "summary": "C", "rebate_target": "1",
                            "rebate_type": "3",
                            "totallimit": "0", "singlelimit": "0", "sdate": sdate, "edate": edate, "inputer": "admin",
                            "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate, "pagesize": "100",
                            "czk_rebate_det": [
                                {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "rebate_condition": "38",
                                 "rebate_coupon_id": "MSSMZQ001", "rebate_coupon_name": "[MSSMZQ001]面值券10元",
                                 "rebate_coupon_faceval": "10.00", "rebate_group_id": "02", "rebate_coupon_num": "1",
                                 "totalnum_limit": 0,
                                 "singlenum_limit": 0, "rebate_coupon_amount": 10}], "flag": "I"}])  # 新增购卡优惠-优惠券
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 查询购卡优惠-优惠券
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.czbillno()})  # 审核购卡优惠-优惠券

    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': ent_id},
                       payload=[
                           {"billmoduleid": "9006666", "billstatus": "N", "summary": "C", "rebate_target": "1",
                            "rebate_type": "4",
                            "totallimit": "0", "singlelimit": "0", "sdate": sdate, "edate": edate, "inputer": "admin",
                            "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate, "pagesize": "100",
                            "czk_rebate_det": [
                                {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "rebate_condition": "38",
                                 "rebate_discount_money": "2.5"}], "flag": "I"}])  # 新增购卡优惠-奖励金额
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 查询购卡优惠-奖励金额
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.czbillno()})  # 审核购卡优惠-奖励金额

    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': ent_id},
                       payload=[
                           {"billmoduleid": "9006666", "billstatus": "N", "summary": "C", "rebate_target": "1",
                            "rebate_type": "5",
                            "totallimit": "0", "singlelimit": "0", "sdate": sdate, "edate": edate, "inputer": "admin",
                            "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate, "czk_rebate_det": [
                               {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "rebate_condition": "38",
                                "rebate_discount_rate": "0.25"}], "flag": "I"}])  # 新增购卡优惠-奖励比例
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 查询购卡优惠-奖励比例
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.czbillno()})  # 审核购卡优惠-奖励比例
    """新增充值优惠"""
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': ent_id},
                       payload=[
                           {"billmoduleid": "9006666", "billstatus": "N", "summary": "E", "rebate_target": "1",
                            "rebate_type": "1",
                            "totallimit": "0", "singlelimit": "0", "sdate": sdate, "edate": edate, "inputer": "admin",
                            "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate, "czk_rebate_det": [
                               {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "rebate_condition": "38",
                                "rebate_discount_money": "2.5"}], "flag": "I"}])  # 新增充值优惠-折扣金额
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 查询充值优惠-折扣金额
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.czbillno()})  # 审核充值优惠-折扣金额
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.card.award', 'ent_id': ent_id},
                       payload={"channel_id": "WECHAT", "cid": hyxx[0], "ctype": hyxx[1], "summary": "E"})  # 充值优惠信息
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.card.getlist', 'ent_id': ent_id},
                       payload={"page_no": 1, "page_size": 100, "can_deposit": "Y", "channel_id": "WECHAT",
                                "status": "Y",
                                "cid": hyxx[0]})  # 获取卡列表
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.card.deposit', 'ent_id': ent_id},
                       payload={"UserAgreement": "免责声明", "market": "6206", "channel_id": "WECHAT", "cid": hyxx[0],
                                "ctype": hyxx[1],
                                "cflag": "04", "wxid": "", "mobile": "", "corp_id": "0", "cardno": "", "face_value": 1,
                                "amount": 38, "discount": 0, "award": 0, "summary": "E",
                                "memo": "储值卡[" + commonpost.card_no() + "]充值38.00元"})  # 充值订单提交
    billno = commonpost.gkbillno()
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.card.orderfinish', 'ent_id': ent_id},
                       payload={"channel_id": "WECHAT", "billno": billno, "summary": "E", "eventtype": "02",
                                "merchantid": "",
                                "transaction_id": "", "out_trade_no": "CHAG" + billno, "total_fee": 100,
                                "paycode": "debugpay", "payname": "模拟支付", "payref1": "", "payref2": "",
                                "payref3": ""})  # 充值订单完成
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.card.ordersearch', 'ent_id': ent_id},
                       payload={"page_no": 1, "page_size": 100, "billno": billno, "channel_id": "WECHAT",
                                "cid": hyxx[0]})  # 充值订单查询

    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': ent_id},
                       payload=[
                           {"billmoduleid": "9006666", "billstatus": "N", "summary": "E", "rebate_target": "1",
                            "rebate_type": "2",
                            "totallimit": "0", "singlelimit": "0", "sdate": sdate, "edate": edate, "inputer": "admin",
                            "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate, "pagesize": "100",
                            "czk_rebate_det": [
                                {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "rebate_condition": "38",
                                 "rebate_discount_rate": "0.25"}], "flag": "I"}])  # 新增充值优惠-折扣率
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 查询充值优惠-折扣率
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.czbillno()})  # 审核充值优惠-折扣率

    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': ent_id},
                       payload=[
                           {"billmoduleid": "9006666", "billstatus": "N", "summary": "E", "rebate_target": "1",
                            "rebate_type": "3",
                            "totallimit": "0", "singlelimit": "0", "sdate": sdate, "edate": edate, "inputer": "admin",
                            "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate, "pagesize": "100",
                            "czk_rebate_det": [
                                {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "rebate_condition": "38",
                                 "rebate_coupon_id": "MSSMZQ001", "rebate_coupon_name": "[MSSMZQ001]面值券10元",
                                 "rebate_coupon_faceval": "10.00", "rebate_group_id": "02", "rebate_coupon_num": "1",
                                 "totalnum_limit": 0,
                                 "singlenum_limit": 0, "rebate_coupon_amount": 10}], "flag": "I"}])  # 新增充值优惠-优惠券
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 查询充值优惠-优惠券
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.czbillno()})  # 审核充值优惠-优惠券

    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': ent_id},
                       payload=[
                           {"billmoduleid": "9006666", "billstatus": "N", "summary": "E", "rebate_target": "1",
                            "rebate_type": "4",
                            "totallimit": "0", "singlelimit": "0", "sdate": sdate, "edate": edate, "inputer": "admin",
                            "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate, "czk_rebate_det": [
                               {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "rebate_condition": "38",
                                "rebate_discount_money": "2.5"}], "flag": "I"}])  # 新增充值优惠-奖励金额
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 查询充值优惠-奖励金额
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.czbillno()})  # 审核充值优惠-奖励金额

    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': ent_id},
                       payload=[
                           {"billmoduleid": "9006666", "billstatus": "N", "summary": "E", "rebate_target": "1",
                            "rebate_type": "5",
                            "totallimit": "0", "singlelimit": "0", "sdate": sdate, "edate": edate, "inputer": "admin",
                            "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate, "pagesize": "100",
                            "czk_rebate_det": [
                                {"flag": "I", "_id": _id, "_uid": _uid, "_state": "added", "rebate_condition": "38",
                                 "rebate_discount_rate": "0.25"}], "flag": "I"}])  # 新增充值优惠-奖励比例
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.get', 'ent_id': ent_id},
                       payload=commonpost.ph_key())  # 查询充值优惠-奖励比例
    commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.rebate.billaudit', 'ent_id': ent_id},
                       payload={"billno": commonpost.czbillno()})  # 审核充值优惠-奖励比例

    # commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.report.query', 'ent_id': ent_id},
    #                    payload={"page_size": page_size, "sdate": sdate, "edate": edate,
    #                             "queryid": "select_walletorders"})  # 购卡充值订单查询
    # commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.report.query', 'ent_id': ent_id},
    #                    payload={"page_size": page_size, "sdate": sdate, "edate": edate,
    #                             "queryid": "select_yhmx"})  # 购卡充值优惠明细查询
    # commonpost.HgoMain('/ocm-wallet-webin/rest', {'method': 'efuture.ocm.wallet.report.query', 'ent_id': ent_id},
    #                    payload={"page_size": page_size, "sdate": sdate, "edate": edate,
    #                             "queryid": "select_gkczmx"})  # 购卡充值赠券明细查询
