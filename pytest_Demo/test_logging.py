# logging is show all the testcase logs with detailed information
import logging

def test_logging():

    logger = logging.getLogger(__name__) # get logger will get logs from executed TCs, __name__ is capture the testcase/file name in runtime

    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")  # Printing the error message with the format
    fileHandler = logging.FileHandler('logfile.log')  #passing file name

    fileHandler.setFormatter(formatter) # Formatted the log messages line 6

    logger.addHandler(fileHandler)    # Filehandler object (file path) and formatter for log message

    logger.setLevel(logging.INFO)   # It will print the info to critical level messages (Debug will skip from the hyrachy)
    logger.debug("Debug statement is executed")  # It will print the statement
    logger.info("Information statement")
    logger.warning("Something is in warning mode")  # It'll alert as warning without failing TC
    logger.error("A major error happened")
    logger.critical("Critical issue")


