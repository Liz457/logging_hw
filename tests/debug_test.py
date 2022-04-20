import os

""" This checks if the debug log file is created"""

root = os.path.dirname(os.path.abspath(__file__))
logdir = os.path.join(root, '../app/logs')
def test_before_request_logging():
    assert os.path.exists(logdir) == True
    logfile = os.path.join(root,'../app/logs/lizDebugApp.log')
    assert os.path.exists(logfile) == True
    
