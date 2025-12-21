class BaseModel:
    table: str  # subclasses must define in subclasses

    @classmethod
    def get_table(cls) -> str:
        return cls.table