
from decimal import Decimal as D
from oscar.apps.partner import strategy


class Selector(object):
    """
    Custom selector to return a UK-specific strategy that charges VAT
    """

    def strategy(self, request=None, user=None, **kwargs):
        return UKStrategy()


class IncludingVAT(strategy.FixedRateTax):
    """
    Price policy to charge VAT on the base price
    """
    # We can simply override the tax rate on the core FixedRateTax.  Note
    # this is a simplification: in reality, you might want to store tax
    # rates and the date ranges they apply in a database table.  Your
    # pricing policy could simply look up the appropriate rate.
    rate = D('0.20')


class UKStrategy(strategy.UseFirstStockRecord, IncludingVAT,
                 strategy.StockRequired, strategy.Structured):
    """
    Typical UK strategy for physical goods.

    - There's only one warehouse/partner so we use the first and only
      stockrecord
    - Enforce stock level.  Don't allow purchases when we don't have stock.
    - Charge UK VAT on prices.  Assume everything is standard-rated.
    """