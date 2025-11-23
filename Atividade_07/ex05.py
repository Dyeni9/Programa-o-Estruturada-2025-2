#  Crie uma função converte_fahrenheit que receba uma temperatura em Celsius e a converta para Fahrenheit. Teste com 25°C

def converte_fahrenheit(celsius):
    """Converte temperatura de Celsius para Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_celsius = 25
temp_fahrenheit = converte_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C é igual a {temp_fahrenheit}°F")