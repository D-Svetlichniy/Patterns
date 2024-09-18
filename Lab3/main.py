from Lab3.MySQLQueryBuilder import MySQLQueryBuilder
from Lab3.PostgreSQLQueryBuilder import PostgreSQLQueryBuilder


def client_code():
    # Будуємо запит для PostgreSQL
    postgres_builder = PostgreSQLQueryBuilder()
    query = (postgres_builder
                .select("users", ["id", "name", "email"])
                .where("age > 18")
                .limit(10)
                .getSQL())
    print("PostgreSQL Query:", query)

    # Будуємо запит для MySQL
    mysql_builder = MySQLQueryBuilder()
    query = (mysql_builder
                .select("users", ["id", "name", "email"])
                .where("age > 18")
                .limit(10)
                .getSQL())
    print("MySQL Query:", query)

client_code()
