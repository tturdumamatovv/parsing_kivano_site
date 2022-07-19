import csv

def write_to_csv(data):
    with open('data.csv', 'w') as file:
        columns = ["Название", "Описание", "Цена", "Картинка"]
        writer = csv.DictWriter(file, columns)
        writer.writeheader()
        for product in data:
            writer.writerow({
                "Название": product['title'],
                "Описание": product['description'],
                "Цена": product['price'],
                "Картинка": product['image']
            })