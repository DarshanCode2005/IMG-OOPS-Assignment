class Person:
    """Base class for all persons in the system"""
    
    def __init__(self, id_str: str, name: str, password: str):
        self.id = id_str
        self.name = name
        self.password = password
    
    def login(self, id_str: str, password: str) -> bool:
        """Login method"""
        return self.id == id_str and self.password == password
    
    def get_name(self) -> str:
        """Get person's name"""
        return self.name
    
    def __str__(self):
        return f"{self.name} ({self.id})"
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.id == other.id
        return False