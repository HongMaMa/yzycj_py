# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import time

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:5555?",])


# script content

sleep(3)
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
