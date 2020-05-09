from random import randint
import datetime


"""Classes for melon orders."""

class TooManyMelonsError(ValueError):
    """raises an error if qty > 100"""
    def __init__(self):
        super().__init__("No more than 100 melons")


class AbstractMelonOrder:
    """An abstract base Melon class"""
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.tax = 0
        self.order_type =""

        if qty > 100:
            raise TooManyMelonsError

    def get_total(self):
        """Calculate price, including tax."""        

        #if christmas melon base_price *1.5
        base_price = self.get_base_price()        
        if self.species == 'christmas melon':
            base_price *= 1.5

        #add $4 to base if during rush hour
        order_time = datetime.datetime.now()
        if (order_time.hour >=8 and order_time.hour < 11) and \
            order_time.weekday() < 5:
            base_price += 4

        total = (1 + self.tax) * self.qty * base_price

        return total

    def get_base_price(self):
        """return base price as random integer between 5 and 9"""

        return randint(5,9)

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
    country_code = 'USA'

    def __init__(self, species, qty):
        super().__init__(species, qty, 'USA')
        """Initialize melon order attributes."""

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order within the USA for the govermnent."""
    order_type = "domestic"
    tax = 0
    country_code = 'USA'

    def __init__(self, species, qty):
        super().__init__(species, qty, 'USA')
        """Initialize melon order attributes."""
        
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """return the value of passed"""

        return passed

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total():
        #add $3 to the order total if < 10 melons ordered
        total = super.get_total()
        if self.qty < 10:
            total +=3
