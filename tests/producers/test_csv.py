from .test_core import GenericProducerTest
from apf.producers import CSVProducer
import unittest
import tempfile

import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
EXAMPLES_PATH = os.path.abspath(os.path.join(FILE_PATH, "../examples"))


class CSVProducerTest(GenericProducerTest):

    component = CSVProducer
    file_path = os.path.join(EXAMPLES_PATH, "test_csv_producer.csv")
    params = {"FILE_PATH": file_path}

    def tearDown(self):
        self.assertTrue(os.path.exists(self.file_path))
        os.remove(self.file_path)
