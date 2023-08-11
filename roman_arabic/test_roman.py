import roman_numeral_converter as rnc

def test_to_arabic_number_1_rta(): 
    """simple rnc.to_arabic_number (I) == 1""" 
    assert rnc.to_arabic_number("I") == 1 
 
 
def test_to_arabic_number_2008_rta(): 
    """multi rnc.to_arabic_number (MMVIII) == 2008""" 
    assert rnc.to_arabic_number("MMVIII") == 2008 
 
 
def test_to_arabic_number_4_rta(): 
    """simple subtraction rnc.to_arabic_number (IV) == 4""" 
    assert rnc.to_arabic_number("IV") == 4 
 
 
def test_to_arabic_number_90_rta(): 
    """subtraction rnc.to_arabic_number (XC) == 90""" 
    assert rnc.to_arabic_number("XC") == 90 
 
 
def test_to_arabic_number_3999_rta(): 
    """big rnc.to_arabic_number (MMMCMXCIX) == 3999""" 
    assert rnc.to_arabic_number("MMMCMXCIX") == 3999 

def test_to_roman_numeral_1_atn(): 
    """simple rnc.to_roman_numeral (1) == I""" 
    assert rnc.to_roman_numeral(1) == "I" 
 
 
def test_to_roman_numeral_2008_atn(): 
    """multi rnc.to_roman_numeral (2008) == MMVIII""" 
    assert rnc.to_roman_numeral(2008) == "MMVIII" 
 
 
def test_to_roman_numeral_4_atn(): 
    """simple subtraction rnc.to_roman_numeral (4) == IV""" 
    assert rnc.to_roman_numeral(4) == "IV" 
 
 
def test_to_roman_numeral_90_atn(): 
    """subtraction rnc.to_roman_numeral (90) == XC""" 
    assert rnc.to_roman_numeral(90) == "XC" 
 
 
def test_to_roman_numeral_3999_atn(): 
    """big rnc.to_roman_numeral (3999) == MMMCMXCIX""" 
    assert rnc.to_roman_numeral(3999) == "MMMCMXCIX" 
 