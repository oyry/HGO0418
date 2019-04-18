# @Time    : 19-4-16
# @Author  : 欧阳
# @File    : uitestlog.py
import logging,time,os

def uilog(logger_name=time.strftime('WALLET-'+'%Y%m%d%H%M%S.log', time.localtime(time.time()))):
    # 创建一个logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    #调试用
    # if not os.path.exists('../Logs'):
    #     os.makedirs('../Logs')
    # log_file_path = os.path.join('../Logs', logger_name)
    #打包用
    if not os.path.exists('./Logs'):
        os.makedirs('./Logs')
    log_file_path = os.path.join('./Logs', logger_name)

    # 创建handler
    # 创建一个handler写入所有日志
    fh = logging.FileHandler(log_file_path)
    fh.setLevel(logging.INFO)
    # 创建一个handler写入错误日志
    eh = logging.FileHandler(log_file_path)
    eh.setLevel(logging.ERROR)
    # 创建一个handler输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 定义日志输出格式
    # 以时间-日志器名称-日志级别-日志内容的形式展示
    log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S")
    # 将定义好的输出形式添加到handler
    fh.setFormatter(log_formatter)
    ch.setFormatter(log_formatter)
    eh.setFormatter(log_formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(eh)
    logger.addHandler(ch)
    return logger