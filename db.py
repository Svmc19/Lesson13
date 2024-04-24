import psycopg2

data_base = psycopg2.connect(
    host='rain.db.elephantsql.com',
    user='aexavlwh',
    database='aexavlwh',
    password='6FjAxDSAAyTTzOgklLmqrxP_5PTPdw4c'
)

cursor = data_base.cursor()

def insert_data(laptop_name, laptop_image, laptop_price, credit_price):
    cursor.execute(f"""
        INSERT INTO laptops(laptop_name, laptop_image, laptop_price, credit_price)
        VALUES
        ('{laptop_name}', '{laptop_image}', '{laptop_price}', '{credit_price}')
    """)

    data_base.commit()


cursor.execute("""
    SELECT laptop_name, laptop_image, laptop_price, credit_price
    FROM laptops
""")


data_base = cursor.fetchall()
for x in data_base:
    print([x])

laptop_name = data_base[0]
laptop_image = data_base[1]
laptop_price = data_base[2]
credit_price = data_base[3]

print(laptop_name,laptop_image,laptop_price,credit_price)












