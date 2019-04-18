# @Time    : 19-3-27
# @Author  : 欧阳
# @File    : commonlog.py
import logging,os,sys,datetime

class get_logger():
    def __init__(self, set_level="debug",
                 name=os.path.split(os.path.splitext(sys.argv[0])[0])[-1],
                 log_name=datetime.datetime.now().strftime("HGO-" + "%Y%m%d%H%M%S.log"),
                 use_console=True):
        '''
            set_level： 设置日志的打印级别，默认为DEBUG
            name： 日志中将会打印的name，默认为运行程序的name
            log_name： 日志文件的名字，默认为当前时间（年-月-日.log）
            log_path： 日志文件夹的路径，默认为logger.py同级目录中的log文件夹
            use_console： 是否在控制台打印，默认为True
        '''
        self.logger = logging.getLogger(name)
        if set_level.lower() == "critical":
            self.logger.setLevel(logging.CRITICAL)
        elif set_level.lower() == "error":
            self.logger.setLevel(logging.ERROR)
        elif set_level.lower() == "warning":
            self.logger.setLevel(logging.WARNING)
        elif set_level.lower() == "info":
            self.logger.setLevel(logging.INFO)
        elif set_level.lower() == "debug":
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.NOTSET)
        if not os.path.exists('../Logs'):
            os.makedirs('../Logs')
        log_file_path = os.path.join('../Logs', log_name)  # 调试用
        # if not os.path.exists('./Logs'):
        #     os.makedirs('./Logs')
        # log_file_path = os.path.join('./Logs', log_name)  # 打包用
        log_handler = logging.FileHandler(log_file_path, encoding='utf-8',mode='w')
        log_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S"))
        self.logger.addHandler(log_handler)
        if use_console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(
                logging.Formatter("%(asctime)s - %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S"))
            self.logger.addHandler(console_handler)

    def addHandler(self, hdlr):
        self.logger.addHandler(hdlr)

    def removeHandler(self, hdlr):
        self.logger.removeHandler(hdlr)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        self.logger.log(level, msg, *args, **kwargs)