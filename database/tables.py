from database.connection import databaseConnection


def create_tables():
    try:
        database_config = databaseConnection()
        cursor = database_config.cursor()
        customers_table = """  CREATE TABLE IF NOT EXISTS customers (
                        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(100) NOT NULL,
                        email VARCHAR(150) UNIQUE NOT NULL,
                        phone VARCHAR(15),
                        address TEXT,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                    );
                    """
        fruits_table = """
                        CREATE TABLE IF NOT EXISTS fruits (
                            fruit_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(100) NOT NULL,
                            season VARCHAR(50),
                            sweetness INTEGER CHECK (sweetness BETWEEN 1 AND 10),
                            price DECIMAL(6,2) NOT NULL,
                            color VARCHAR(50),
                            stock INTEGER DEFAULT 0,
                            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                        );
                        """
        orders_table = """CREATE TABLE IF NOT EXISTS orders (
                    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    fruit_id INTEGER,
                    quantity INTEGER NOT NULL,
                    total_price DECIMAL(8,2),
                    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,

                    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                    FOREIGN KEY (fruit_id) REFERENCES fruits(fruit_id)
                );
                """
        cursor.execute(customers_table)
        customers_table(fruits_table)
        cursor.execute(orders_table)
        database_config.commit()

        cursor.close()
        database_config.close()
        

    except Exception as e:
        return f"Something wrong in database/tables.py:{e}"