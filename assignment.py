from vector import Vector
from datetime import datetime

class Assignment:
    """Assignment class"""
    
    def __init__(self, title: str, max_score: int, deadline: str):
        self.title = title
        self.max_score = max_score
        self.deadline = deadline
        self.submissions = Vector()  # Vector of submissions
    
    def get_title(self) -> str:
        """Get assignment title"""
        return self.title
    
    def get_max_score(self) -> int:
        """Get maximum score"""
        return self.max_score
    
    def get_deadline(self) -> str:
        """Get deadline"""
        return self.deadline
    
    def __str__(self):
        return f"Assignment: {self.title} (Max: {self.max_score}, Deadline: {self.deadline})"
    
    def __eq__(self, other):
        if isinstance(other, Assignment):
            return self.title == other.title
        return False