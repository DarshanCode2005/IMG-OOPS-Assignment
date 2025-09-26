from datetime import datetime

class Submission:
    """Submission class for assignment submissions"""
    
    def __init__(self, student, assignment, submission_date: str = None, is_late: bool = False, score: int = 0):
        self.student = student
        self.assignment = assignment
        self.submission_date = submission_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_late = is_late
        self.score = score
    
    def mark_late(self) -> None:
        """Mark submission as late"""
        self.is_late = True
    
    def set_score(self, score: int) -> None:
        """Set submission score"""
        self.score = score
    
    def get_details(self) -> str:
        """Get submission details"""
        status = "Late" if self.is_late else "On Time"
        return f"Assignment: {self.assignment.title}, Score: {self.score}, Status: {status}, Date: {self.submission_date}"