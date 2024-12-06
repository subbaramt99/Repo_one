import logging

class Baseclass:
    def getLogger(self):

        logger = logging.getLogger(__name__) # get logger will get logs from executed TCs, __name__ is capture the testcase/file name in runtime
        fileHandler = logging.FileHandler('logfile.log')  # passing file name
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")  # Printing the error message with the format


        fileHandler.setFormatter(formatter) # Formatted the log messages line 6

        logger.addHandler(fileHandler)    # Filehandler object (file path) and formatter for log message

        logger.setLevel(logging.DEBUG)   # It will print the info to critical level messages (Debug will skip from the hyrachy)

        return logger