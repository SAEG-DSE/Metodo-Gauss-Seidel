import unittest
from should_dsl import should
from gauss import Gauss

class TestGauss(unittest.TestCase):

    def setUp(self):
        self.gauss = Gauss([[10,2,1],[1,5,1],[2,3,10]])

    def test_convergencia_d1_igual_a_0_3(self):
        self.gauss.convergencia_d1() |should| equal_to(0.3)

    def test_convergencia_d2_igual_a_0_26(self):
        self.gauss.convergencia_d2() |should| equal_to(0.26)

    def test_convergencia_d3_igual_a_0_138(self):
        self.gauss.convergencia_d3() |should| equal_to(0.138)

    def test_validar_convergencia(self):
        self.gauss.convergencia_d1() |should| be_less_than(1)
        self.gauss.convergencia_d2() |should| be_less_than(1)
        self.gauss.convergencia_d3() |should| be_less_than(1)
