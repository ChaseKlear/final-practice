from testing_utils import run_a_test
from question_5 import fraud_cards

def test_q5_fraud_cards_1():
    run_a_test(fraud_cards, ['Jon Snow', 'Lord Volde... nvm', 'Jinx from Arcane'], 'data/credit_cards.csv')


def test_q5_fraud_cards_2():
    run_a_test(fraud_cards, None, 'data/invalid.csv')
