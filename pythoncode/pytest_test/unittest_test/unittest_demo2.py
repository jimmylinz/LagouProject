import unittest
class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardowm")

    def test_case01(self):
        print("testcases")
        self.assertEqual(2,2,"判断相等")
        self.assertIn('h','this')

    def test_case02(self):
        print("testcases")
        self.assertEqual(1,1,"判断相等")
        self.assertIn('h','this')

    @unittest.skipIf(1+1==2,"跳过")
    def test_case03(self):
        print("testcases")
        self.assertEqual(3,3,"判断相等")
        self.assertIn('h','this')

class demo1(unittest.TestCase):

    def test_demo1_case1(self):
        print("test_demo1_case1")

    def test_demo1_case2(self):
        print("test_demo1_case2")

class demo2(unittest.TestCase):

    def test_demo2_case1(self):
        print("test_demo2_case1")

    def test_demo2_case2(self):
        print("test_demo2_case2")

if __name__ == '__main__':
    # unittest.main()
    # suit = unittest.TestSuite()
    # suit.addTest(demo("test_case01"))
    # suit.addTest(demo1("test_demo1_case2"))
    # unittest.TextTestRunner().run(suit)
    suite = unittest.TestLoader().loadTestsFromTestCase(demo)
    suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    suites = unittest.TestSuite([suite,suite1])
    unittest.TextTestRunner().run(suites)