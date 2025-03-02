from oscar.apps.shipping import methods
from decimal import Decimal as D
from oscar.core import prices


class Standard(methods.FixedPrice):
    code = 'standard'
    name = 'frais de livraison'
    
    def calculate(self, basket):
        charge = 0
        for line in basket.all_lines():
            charge += line.quantity
        if charge < 5:
            return prices.Price(
                currency=basket.currency, 
                excl_tax=D('6.67'), incl_tax=D('8.00')
            )
        if charge > 4 and charge < 9:
            return prices.Price(
                currency=basket.currency, 
                excl_tax=D('7.50'), incl_tax=D('9.00')
            )
        if charge > 8:
            return prices.Price(
                currency=basket.currency, 
                excl_tax=D('8.33'), incl_tax=D('10.00')
            )