import csv
from selenium import webdriver
from bs4 import BeautifulSoup

# Инициализация веб-драйвера
driver = webdriver.Chrome()
driver.get("https://svetilnik-online.ru/lampi/nastolnie")

# Ждем, пока страница загрузится
driver.implicitly_wait(20)

# Получаем HTML-код страницы
html = driver.page_source

# Закрываем веб-драйвер
driver.quit()

# Парсим HTML с помощью BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Находим все товары на странице (используем метод select вместо find)
products = soup.select('p.product-name > a')

# Открываем файл для записи в формате txt
with open("products_data.txt", "w", encoding="utf-8") as txt_file:
    # Открываем файл для записи в формате csv
    with open("products_data.csv", "w", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        # Записываем заголовки столбцов в CSV-файл
        writer.writerow(["Lamp Name", "Price", "Link"])

        for product in products:
            lamp_name = product.get('title')  # Извлекаем название лампы
            link = product.get('href')  # Извлекаем ссылку на товар
            price = product.find_next('span', class_='pprice').text  # Извлекаем цену

            # Записываем данные в txt файл
            txt_file.write(f"Lamp Name: {lamp_name}\n")
            txt_file.write(f"Price: {price}\n")
            txt_file.write(f"Link: {link}\n")
            txt_file.write("\n")

            # Записываем данные в CSV файл
            writer.writerow([lamp_name, price, link])

            # Печатаем данные
            print(f"Lamp Name: {lamp_name}")
            print(f"Price: {price}")
            print(f"Link: {link}")
            print("\n")

    print("Данные успешно записаны в файлы 'products_data.txt' и 'products_data.csv'.")

