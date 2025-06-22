from my_project.calculator import Calculator

def test_addiction():
    calculation : Calculator = Calculator(10,5)
    assert calculation.addiction() == 13, "the sum is wrong"

def test_subtration():
    calculation : Calculator = Calculator(10,5)
    assert calculation.subcraction() == 5, "the subcrtation is wrong"

def test_multiplication():
    calculation: Calculator = Calculator(10,5)
    assert calculation.multiplcation() == 50, "the multiplication is wrong"

def test_division():
    calculation : Calculator = Calculator(10,5)
    assert calculation.division() == 2.00, "the quotient is wrong"