from currency_converter import Money
import unittest


class CurrencyConverterTestCase(unittest.TestCase):

    def test_Money_class(self):
        money = Money(1, "USD")
        self.assertEqual(money.amount, 1)
        self.assertEqual(money.denomination, "USD")
        self.assertEqual(money.convert_currency(), .9)

        money = Money(5, "EUR")
        self.assertEqual(money.amount, 5)
        self.assertEqual(money.denomination, "EUR")
        self.assertEqual(money.convert_currency(), 5.55)

        money = Money(186.43, "USD")
        self.assertEqual(money.convert_currency(), 167.79)

        money = Money([1, 2, .5, 186.43], "USD")
        self.assertEqual(money.convert_currency(), [.90, 1.80, .45, 167.79])

        money = Money([.90, 1, 10.89], "EUR")
        self.assertEqual(money.convert_currency(), [1.0, 1.11, 12.09])

    def test_can_perform_numerical_operations_on_two_instances_of_money_class(self):
        money1 = Money(100, "USD")
        money2 = Money(50, "USD")
        money3 = Money(25, "EUR")
        money4 = Money(35, "EUR")
        money5 = Money(20, "USD")
        money6 = Money(20, "EUR")

        # add two instances
        self.assertEqual(money1 + money2, 150)
        self.assertEqual(money3 + money4, 60)
        self.assertEqual(money1 + money3, 127.75)
        self.assertEqual(money4 + money2, 80.0)

        # subtract two instances
        self.assertEqual(money1 - money2, 50)
        self.assertEqual(money3 - money4, -10.0)
        self.assertEqual(money1 - money3, 72.25)
        self.assertEqual(money4 - money2, -10.0)

        # compare using >
        self.assertEqual(money1 > money2, True)
        self.assertEqual(money3 > money4, False)
        self.assertEqual(money1 > money3, True)
        self.assertEqual(money4 > money2, False)
        self.assertEqual(money5 > money6, False)

        # compare using <
        self.assertEqual(money1 < money2, False)
        self.assertEqual(money3 < money4, True)
        self.assertEqual(money1 < money3, False)
        self.assertEqual(money4 < money2, True)
        self.assertEqual(money5 < money6, True)

    def test_usd_to_euro_can_convert_usd_to_euro(self):
        money = Money(0, "USD")
        self.assertEqual(money.usd_to_euro(1), .90)
        self.assertEqual(money.usd_to_euro(2), 1.80)
        self.assertEqual(money.usd_to_euro(.5), .45)
        self.assertEqual(money.usd_to_euro(186.43), 167.79)

    def test_euro_to_usd_can_convert_euro_to_usd(self):
        money = Money(0, "EUR")
        self.assertEqual(money.euro_to_usd(.90), 1.0)
        self.assertEqual(money.euro_to_usd(1), 1.11)
        self.assertEqual(money.euro_to_usd(10.89), 12.09)

    def test_usd_to_euro_list_can_convert_all_usd_amounts_in_list_to_euro(self):
        money = Money([0], "USD")
        self.assertEqual(money.usd_to_euro_list([1]), [.90])
        self.assertEqual(money.usd_to_euro_list([1, 2, .5, 186.43]), [.90, 1.80, .45, 167.79])

    def test_euro_to_usd_list_can_convert_all_euro_amounts_in_list_to_usd(self):
        money = Money([0], "EUR")
        self.assertEqual(money.euro_to_usd_list([.90]), [1.0])
        self.assertEqual(money.euro_to_usd_list([.90, 1, 10.89]), [1.0, 1.11, 12.09])