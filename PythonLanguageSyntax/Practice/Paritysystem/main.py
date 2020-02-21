from p1.upgrade import stone4g, stone6g
from p1.pricecomparison import comparison
sumcount, fail = stone4g()
gold = stone6g(sumcount, fail)
comparison(gold)

