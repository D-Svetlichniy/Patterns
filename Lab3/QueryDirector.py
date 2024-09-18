from Lab3.QueryBuilder import QueryBuilder


class QueryDirector:  # Директор для управління процесом будівництва запиту
    def __init__(self, builder: QueryBuilder):
        self.builder = builder

    def constructSimpleQuery(self, table: str, columns: list, condition: str, limit: int):
        return (self.builder
                .select(table, columns)
                .where(condition)
                .limit(limit)
                .getSQL())
