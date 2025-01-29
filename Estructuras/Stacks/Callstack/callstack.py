"""
Usando el debugging para entender un callstack.
"""

text = 'hola!'

def make_upper(text: str) -> str: #Hinting to define data type and memory usage
    text = text + '!!!'
    return text.upper()


print(len(make_upper(text)))