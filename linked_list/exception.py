import logging

__author__ = "akhtar"

logger = logging.getLogger(__name__)


class RangeError(Exception):
    pass


class EmptyListError(Exception):
    pass
