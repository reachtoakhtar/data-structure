import logging

__author__ = "akhtar"

logger = logging.getLogger(__name__)


class NodeSingle:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next
