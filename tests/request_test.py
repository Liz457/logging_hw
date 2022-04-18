import os

from app import create_log_folder
from tests.click_test import runner

""" This checks if the request log file is created"""
def test_create_request_log():
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root,'../app/logs')
    response = os.path.exists(logdir)
    assert response == True
