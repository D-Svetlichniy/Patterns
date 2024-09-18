from Lab3.QueryBuilder import QueryBuilder


class MySQLQueryBuilder(QueryBuilder):  # Реалізація для MySQL
    def __init__(self):
        self.query = ""

    def select(self, table: str, columns: list):
        columns_str = ', '.join(columns)
        self.query = f"SELECT {columns_str} FROM {table}"
        return self

    def where(self, condition: str):
        self.query += f" WHERE {condition}"
        return self

    def limit(self, limit: int):
        self.query += f" LIMIT {limit}"
        return self

    def getSQL(self) -> str:
        return self.query + ";"
