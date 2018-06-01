import unittest


from openprocurement.auctions.core.tests.plugins.transferring.transfer import (
    TestTransfer,
    TestTransferResource
)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTransfer))
    suite.addTest(unittest.makeSuite(TestTransferResource))
    unittest.main()
