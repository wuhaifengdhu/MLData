from mldata.lib.processor import Processor
from unittest import TestCase


class TestProcessor(TestCase):
    def tet_normalize(self):
        processor = Processor("resource/example.csv", "APPROVE/NOT", [])

