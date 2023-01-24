############################# TO DO #####################################

# write import statement for psycopg2
import matplotlib.pyplot as plt
import psycopg2
from psycopg2 import Error
from database import get_connected

# write import statement to import Error from psycopg2

# import the get_connected function from your database.py file

# import matplotlib.pyplot as plt


try:
    # connection to database
    connection = get_connected()

    # creates cursor
    cursor = connection.cursor()



############################# TO DO #####################################

##### create product_revenue_query with the query from parts 3 and 4 which get the total revenue from each product category
    product_revenue_query = """SELECT invoices.product_category,
                            SUM(invoices.Unit_price*invoices.Quantity) FROM invoices
                            GROUP BY invoices.Product_category
                            ORDER BY SUM DESC"""
#### follow the project directions to create a function called get_revenue which fetches the results from the product_revenue_query
    def get_revenue():
        with connection:
            with cursor:
                cursor.execute(product_revenue_query)
                return cursor.fetchall()




#### create a variable called product_revenue and set it equal to the get_revenue function invoked##
    product_revenue = get_revenue()   

#### print the product_revenue variable to look at the structure of the variable to help you write the next function
    print(product_revenue)
#### write a function which loops through the product_revenue variable and creates two lists - one with product categories and one with total revenue values
    product_categories = []
    revenue = []
    count = 0
    index = 0

    while count < (len(product_revenue)):
        product_categories.append(product_revenue[index][0])
        revenue.append(product_revenue[index][1])

        count += 1
        index += 1
#### follow the project directions to create a function which makes a bar chart in matplotlib using the total revenue from each product category
    def create_bar_chart():
        figure = plt.figure()
        data = revenue
        labels = product_categories
        plt.xticks(range(len(labels)), [label[0] for label in labels], rotation=60)
        plt.xlabel('Product Category')
        plt.ylabel('Revenue(USD)')
        plt.title('Product Revenue by Category')
        plt.bar(labels, data)
        return figure

#### invoke the create_bar_chart function
    create_bar_chart()
#### use plt.show() to show a pop-up of the bar chart you created
    plt.show()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL DB", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("DB connection is closed.")
