#!/usr/bin/env python3.7

import logging.config
from .log_filter import LogFilter
from .log_parser import LogParser
from .database_connector import DatabaseConnector


class LogAnalyser:

    def __init__(self, file_name):

        self.file_name = file_name

        self.logger = logging.getLogger(__name__)

        self.logger.info("Setting up Log Analyser")

        self.logger.info("Creating Database connector")
        self.db_connector = DatabaseConnector()
        self.logger.info("Database connector created")

        self.logger.info("Creating Log Filter")
        self.log_filter = LogFilter(self.db_connector)
        self.logger.info("Log Filter created")

        self.logger.info("Log Analyser set up")

    def run(self):

        self.logger.info("Starting Log Analyser")

        self.logger.info("Starting Log Parser")
        LogParser(self.file_name, self.log_filter)  # blocks for parsing
        self.logger.info("Log Parser stopped")

        self.logger.info("Exiting Log Analyser")
