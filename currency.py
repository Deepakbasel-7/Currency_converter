from forex_python.converter import CurrencyRates

def currency_converter():
    #Instantiate the converter
    converter= CurrencyRates()
    #Enter the amount to convert
    amount= int(input("Please enter the amount to convert:"))
    #currency code of the amount to convert
    from_currency= input("Enter the currency code of "
                        "amount you are converting: ").upper()
    #currency code of the amount to convert to
    to_currency= input("Enter the currency code you"
                    "are converting to: ").upper()
    #convert the amount
    converted_amount= converter.convert(from_currency,to_currency,amount)
    return f'The {amount}{from_currency} is {converted_amount:.2f} in {to_currency}s'
print(currency_converter())