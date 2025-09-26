from vector import Vector
from person import Person

class Student(Person):
    """Student class inheriting from Person"""
    
    def __init__(self, id_str: str, name: str, password: str):
        super().__init__(id_str, name, password)
        self.clubs = Vector()  # Vector of clubs student is member of
        self.submissions = Vector()  # Vector of submissions
        self.logged_in_user = None
    
    def start(self) -> None:
        """Start student session - placeholder for CLI interaction"""
        print(f"Student {self.name} session started")
    
    def display_system_menu(self) -> None:
        """Display student menu options"""
        print("\n--- Student Menu ---")
        print("1. View My Clubs")
        print("2. Join Club") 
        print("3. View Assignments")
        print("4. Submit Assignment")
        print("5. View My Submissions")
        print("6. Logout")
    
    def handle_student_menu(self) -> None:
        """Handle student menu interactions"""
        pass  # Implementation will be in main
    
    def handle_student_menu(self) -> None:
        """Handle student menu interactions"""
        pass
    
    def login_user(self) -> None:
        """Set logged in user"""
        self.logged_in_user = self
    
    def create_club(self) -> None:
        """Students cannot create clubs directly"""
        print("Students cannot create clubs. Contact admin.")
    
    def register_student(self) -> None:
        """Register new student - handled by system"""
        pass