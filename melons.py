"""Classes for melon orders."""
class AbstractMelonOrder:
    """An abstract base Melon class"""
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.tax = 0
        self.order_type = ""


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == 'christmas melon':
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price
        if (self.order_type == 'international' and 
            self.qty <10):
            total +=3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
    

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
        """sets the passed_inspection attribute to the value of passed"""
        self.passed_inspection = passed

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
