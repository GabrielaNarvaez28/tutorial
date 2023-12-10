import locale
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
#driver = webdriver.Chrome("/usr/lib/chromum-browser/chromedriver")

# Initialize the browser driver
driver = webdriver.Chrome()

products=[] #List to store name of the product
prices=[] #List to store price of the product
score=[] #List to store rating of the product

driver.get("https://www.flipkart.com/laptops/%3C/a%3E~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")
contenido = driver.page_source
soup = BeautifulSoup(contenido,'html.parser')
productos = soup.find_all('div', attrs={'class': '_4rR01T'})
precios = soup.find_all('div',attrs ={'class':'_30jeq3 _1_WHN1'})
estrellas = soup.find_all('div',attrs={'class':'_3LWZlK'})
for producto in productos:
    print(producto.text)
    products.append(producto.text)
for precio in precios:
    precio_sin_coma = precio.text.replace(",", "")
    precio_sin_simbolo = precio_sin_coma.replace("₹", "")
    print(precio_sin_simbolo)
    en_dolares =0.012 * float(precio_sin_simbolo)
    prices.append(en_dolares)


for i, s in enumerate(estrellas):
    if i < 24:#limita a 24 iteraciones
      score.append(s.text)
      print(s.text)
    else:
        break #sale del bucle despues de 24 iteraciones

df = pd.DataFrame({'Producto':products,'Precio':prices,'Rating':score})
df.to_csv('products.csv', index=False,encoding='utf-8')
