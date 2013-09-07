import math

def factorial_divide(n, i):
  result = 1
  while n > i:
    result *= n
    n-=1
  return result

class Rules:
  def __init__(self, rule_string):
    self.parse_rule_string(rule_string)
    self._odds = None

  def parse_rule_string(self, rule_string):
    self.name, options = rule_string.split(":")
    choices, blanks, _sorted, unique = options.split(" ")[1:]
    self.choices = int(choices)
    self.blanks = int(blanks)
    self._sorted = True if _sorted == "T" else False
    self.unique = True if unique == "T" else False

  @property
  def odds(self):
    if self._odds:
      return self._odds
    if not self.unique and not self._sorted:
      self._odds = pow(self.choices, self.blanks)
    elif self.unique and not self._sorted:
      self._odds = factorial_divide(self.choices, self.choices - self.blanks)
    elif self._sorted and not self.unique:
      self._odds = factorial_divide(
        self.choices + self.blanks - 1, self.choices - 1)/math.factorial(self.blanks)
    else:
      self._odds = factorial_divide(
        self.choices, self.choices - self.blanks)/math.factorial(self.blanks)
    return self._odds

class Lottery:

  def sortByOdds(self, rule_tuple):
    self.rules = dict([(rules.name, rules)
      for rules in [Rules(rule_string) for rule_string in rule_tuple]])
    sorted_rules = []
    while len(sorted_rules) < len(self.rules):
      min_odds = 0
      best_rules = None
      for name, rules in self.rules.items():
        if rules.name not in sorted_rules:
          if rules.odds > min_odds or rules.odds == min_odds and rules.name > best_rules.name:
            best_rules = rules
            min_odds = best_rules.odds
      sorted_rules.append(best_rules.name)
    return tuple(reversed(sorted_rules))
