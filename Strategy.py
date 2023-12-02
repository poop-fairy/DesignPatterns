"""
Challange:
Implement a payment gateway using the Strategy Pattern.
Use should be able to make Payments using a CreditCard, PayPal, or Bitcoin.
"""

from abc import ABC, abstractmethod


class DummyAccounts(ABC):
    __instance = None

    def __init__(self):
        if DummyAccounts.__instance is not None:
            raise Exception(
                "DummyAccounts instance already exists. Use the existing instance using get_instance method"
            )
        DummyAccounts.set_account_details()
        DummyAccounts.__instance = self

    def get_instance():
        if DummyAccounts.__instance is None:
            DummyAccounts()
        return DummyAccounts.__instance

    def set_account_details():
        DummyAccounts.credit_account_numbers = {
            "9u3j24tris-ee33rt": 400000,
            "rwgehshdg-fdh4fdf": 6070000,
            "s32ty4243t232-a5s": 9000,
            "54ujryfzdrfh-trjsgfx": 42,
            "dsfgf3434t3y-ght535": 823,
            "jsdg3ertedfgd56-465yrdd": 624546,
        }

        DummyAccounts.bitcoin_wallets = {
            "BTC-SatoshiNaka": 10000000,
            "BTC-Brokie": 0.04,
            "BTC-Investor": 3.53,
        }

        DummyAccounts.paypal_wallets = {
            "PY-User34255": 99023,
            "PY-User55323": 500,
        }

    def update_creditcard_account_details(self, account_number, amount):
        DummyAccounts.credit_account_numbers[account_number] = amount

    def update_bitcoin_wallet_details(self, wallet_number, amount):
        DummyAccounts.bitcoin_wallets[wallet_number] = amount

    def update_paypal_wallet_details(self, wallet_number, amount):
        DummyAccounts.paypal_wallets[wallet_number] = amount


class PaymentGateway(ABC):
    @abstractmethod
    def __init__():
        """
        Account number checks to be performed here
        """
        pass

    @abstractmethod
    def make_payment():
        """
        Define Payment business logic here
        """
        pass


class Context:
    @abstractmethod
    def __init__(self, strategy):
        self._strategy = strategy

    @abstractmethod
    def set_strategy(self, strategy):
        self._strategy = strategy

    @abstractmethod
    def execute_strategy(self, account_number, method, amount):
        self._strategy.execute(account_number, method, amount)


class CreditCardPaymentGateway(PaymentGateway):
    def __init__(self, account_number, method, amount):
        self._dummy_account = DummyAccounts.get_instance()
        if account_number not in self._dummy_account.credit_account_numbers:
            raise Exception("The Account Number is invalid")
        self._account_number = account_number
        self._method = method
        self._amount = amount
        print("Credit Card Payment Method Initialized")

    def make_payment(self):
        if self._method == "Credit":  # Extracting money
            if (
                self._dummy_account.credit_account_numbers[self._account_number]
                - self._amount
                < 0
            ):
                raise Exception("You're not as rich as you think :(")

            current_balance = self._dummy_account.credit_account_numbers[
                self._account_number
            ]
            updated_balance = current_balance - self._amount

            self._dummy_account.update_creditcard_account_details(
                self._account_number, updated_balance
            )

            return (
                self._account_number,
                self._dummy_account.credit_account_numbers[self._account_number],
            )

        if self._method == "Debit":  # Depositing money
            current_balance = self._dummy_account.credit_account_numbers[
                self._account_number
            ]
            updated_balance = current_balance + self._amount

            self._dummy_account.update_creditcard_account_details(
                self._account_number, updated_balance
            )

            return (
                self._account_number,
                self._dummy_account.credit_account_numbers[self._account_number],
            )


class BitcoinPaymentGateway(PaymentGateway):
    def __init__(self, wallet_number, method, amount):
        self._dummy_account = DummyAccounts.get_instance()
        if wallet_number not in self._dummy_account.bitcoin_wallets:
            raise Exception("The Wallet ID is invalid")
        self._wallet_number = wallet_number
        self._method = method
        self._amount = amount
        print("Bitcoin Payment Method Initialized")

    def make_payment(self):
        if self._method == "Credit":  # Extracting money
            if (
                self._dummy_account.bitcoin_wallets[self._wallet_number] - self._amount
                < 0
            ):
                raise Exception("You're not as rich as you think :(")

            current_balance = self._dummy_account.bitcoin_wallets[self._wallet_number]
            updated_balance = current_balance - self._amount

            self._dummy_account.update_bitcoin_wallet_details(
                self._wallet_number, updated_balance
            )

            return (
                self._wallet_number,
                self._dummy_account.bitcoin_wallets[self._wallet_number],
            )

        if self._method == "Debit":  # Depositing money
            current_balance = self._dummy_account.bitcoin_wallets[self._wallet_number]
            updated_balance = current_balance + self._amount

            self._dummy_account.update_bitcoin_wallet_details(
                self._wallet_number, updated_balance
            )

            return (
                self._wallet_number,
                self._dummy_account.bitcoin_wallets[self._wallet_number],
            )


class PaypalPaymentGateway(PaymentGateway):
    def __init__(self, wallet_number, method, amount):
        self._dummy_account = DummyAccounts.get_instance()
        if wallet_number not in self._dummy_account.paypal_wallets:
            raise Exception("The Wallet ID is invalid")
        self._wallet_number = wallet_number
        self._method = method
        self._amount = amount
        print("Paypal Payment Method Initialized")

    def make_payment(self):
        if self._method == "Credit":  # Extracting money
            if (
                self._dummy_account.paypal_wallets[self._wallet_number] - self._amount
                < 0
            ):
                raise Exception("You're not as rich as you think :(")

            current_balance = self._dummy_account.paypal_wallets[self._wallet_number]
            updated_balance = current_balance - self._amount

            self._dummy_account.update_paypal_wallet_details(
                self._wallet_number, updated_balance
            )

            return (
                self._wallet_number,
                self._dummy_account.paypal_wallets[self._wallet_number],
            )

        if self._method == "Debit":  # Depositing money
            current_balance = self._dummy_account.paypal_wallets[self._wallet_number]
            updated_balance = current_balance + self._amount

            self._dummy_account.update_paypal_wallet_details(
                self._wallet_number, updated_balance
            )

            return (
                self._wallet_number,
                self._dummy_account.paypal_wallets[self._wallet_number],
            )


class MakePayment(Context):
    def __init__(self, payment_method):
        self._payment_method = payment_method

    def set_strategy(self, payment_method):
        self._payment_method = payment_method

    def make_payment(self):
        return self._payment_method.make_payment()


"""Test Cases Start Here"""

credit_transaction1 = MakePayment(
    CreditCardPaymentGateway("54ujryfzdrfh-trjsgfx", method="Debit", amount=10)
)
credit_transaction1.make_payment()

credit_transaction2 = MakePayment(
    CreditCardPaymentGateway("54ujryfzdrfh-trjsgfx", method="Debit", amount=30)
)
credit_transaction2.make_payment()

credit_transaction3 = MakePayment(
    CreditCardPaymentGateway("54ujryfzdrfh-trjsgfx", method="Credit", amount=20)
)
account, final_balance = credit_transaction3.make_payment()
print(" Account Number: ", account, "\n", "Balance: ", final_balance)

btc_transaction1 = MakePayment(
    BitcoinPaymentGateway("BTC-Brokie", method="Debit", amount=0.01)
)
btc_transaction1.make_payment()

btc_transaction2 = MakePayment(
    BitcoinPaymentGateway("BTC-Brokie", method="Debit", amount=0.03)
)
btc_transaction2.make_payment()

btc_transaction3 = MakePayment(
    BitcoinPaymentGateway("BTC-Brokie", method="Credit", amount=0.02)
)
account, final_balance = btc_transaction3.make_payment()
print(" Account Number: ", account, "\n", "Balance: ", final_balance)

paypal_transaction1 = MakePayment(
    PaypalPaymentGateway("PY-User55323", method="Debit", amount=500)
)
paypal_transaction1.make_payment()

paypal_transaction2 = MakePayment(
    PaypalPaymentGateway("PY-User55323", method="Debit", amount=1500)
)
paypal_transaction2.make_payment()

paypal_transaction3 = MakePayment(
    PaypalPaymentGateway("PY-User55323", method="Credit", amount=750)
)
account, final_balance = paypal_transaction3.make_payment()
print(" Account Number: ", account, "\n", "Balance: ", final_balance)
