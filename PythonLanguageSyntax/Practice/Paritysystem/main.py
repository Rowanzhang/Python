from p1.upgrade import StoneUpgrade
from p1.pricecomparison import Comparison
stoneupgrade = StoneUpgrade()
sumcount, fail = stoneupgrade.stone4g()
gold = stoneupgrade.stone6g(sumcount, fail)
comp = Comparison()
comp.comparison_price(gold)

