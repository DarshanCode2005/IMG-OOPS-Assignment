from vector import Vector
from student import Student
from club_admin import ClubAdmin
from person import Person
from club import Club
from assignment import Assignment
from submission import Submission
from datetime import datetime, timedelta
import sys

class ClubManagementSystem:
    """Main Club Management System"""
    
    def __init__(self):
        self.students = Vector()
        self.clubs = Vector()
        self.admins = Vector()
        self.current_user = None
        self.initialize_system()
    
    def initialize_system(self):
        """Initialize system with sample data"""
        print("Initializing Club Management System...")
        
        # Create sample students
        student1 = Student("21114001", "Rahul Sharma", "pass123")
        student2 = Student("21114002", "Priya Singh", "pass456")
        student3 = Student("21114003", "Amit Kumar", "pass789")
        
        self.students.add_element(student1)
        self.students.add_element(student2)
        self.students.add_element(student3)
        
        # Create sample admins
        admin1 = ClubAdmin("admin001", "Dr. Rajesh Verma", "admin123")
        admin2 = ClubAdmin("admin002", "Prof. Sunita Gupta", "admin456")
        admin3 = ClubAdmin("admin003", "Dr. Vikram Singh", "admin789")
        
        self.admins.add_element(admin1)
        self.admins.add_element(admin2)
        self.admins.add_element(admin3)
        
        # Create sample clubs
        img_club = Club("Information Management Group (IMG)", admin1)
        sds_club = Club("Software Development Section (SDS)", admin2)
        debsoc_club = Club("Debate Society (DebSoc)", admin3)
        
        self.clubs.add_element(img_club)
        self.clubs.add_element(sds_club)
        self.clubs.add_element(debsoc_club)
        
        # Add some members to clubs
        img_club.add_member(student1)
        img_club.add_member(student2)
        sds_club.add_member(student1)
        sds_club.add_member(student3)
        debsoc_club.add_member(student2)
        
        # Create sample assignments
        assignment1 = Assignment("Web Development Project", 100, "2024-12-31")
        assignment2 = Assignment("Database Design", 80, "2024-11-30")
        assignment3 = Assignment("Debate Preparation", 50, "2024-10-15")
        
        img_club.add_assignment(assignment1)
        sds_club.add_assignment(assignment2)
        debsoc_club.add_assignment(assignment3)
        
        # Create sample submissions
        submission1 = Submission(student1, assignment1, "2024-12-25 10:00:00", False, 85)
        submission2 = Submission(student2, assignment1, "2025-01-02 14:30:00", True, 75)
        
        assignment1.submissions.add_element(submission1)
        assignment1.submissions.add_element(submission2)
        
        print("System initialized with sample data!")
        print(f"Students: {self.students.get_size()}")
        print(f"Clubs: {self.clubs.get_size()}")
        print(f"Admins: {self.admins.get_size()}")

    def start(self):
        """Start the club management system"""
        print("\n" + "="*50)
        print("   CLUB MANAGEMENT SYSTEM - IIT ROORKEE")
        print("="*50)
        
        while True:
            self.display_main_menu()
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.student_login()
            elif choice == "2":
                self.admin_login()
            elif choice == "3":
                self.register_new_student()
            elif choice == "4":
                self.display_all_clubs()
            elif choice == "5":
                self.display_system_stats()
            elif choice == "6":
                print("Thank you for using Club Management System!")
                sys.exit(0)
            else:
                print("Invalid choice! Please try again.")
    
        def display_main_menu(self):
            """Display main menu"""
            print("\n--- MAIN MENU ---")
            print("1. Student Login")
            print("2. Admin Login")
            print("3. Register New Student")
            print("4. View All Clubs")
            print("5. System Statistics")
            print("6. Exit")
    
    def student_login(self):
        """Handle student login"""
        print("\n--- Student Login ---")
        student_id = input("Enter Student ID: ").strip()
        password = input("Enter Password: ").strip()
        
        for student in self.students:
            if student.login(student_id, password):
                self.current_user = student
                print(f"Welcome, {student.name}!")
                self.student_menu()
                return
        
        print("Invalid credentials! Please try again.")
    
    def admin_login(self):
        """Handle admin login"""
        print("\n--- Admin Login ---")
        admin_id = input("Enter Admin ID: ").strip()
        password = input("Enter Password: ").strip()
        
        for admin in self.admins:
            if admin.login(admin_id, password):
                self.current_user = admin
                print(f"Welcome, {admin.name}!")
                self.admin_menu()
                return
        
        print("Invalid credentials! Please try again.")

    def student_menu(self):
        """Student menu interface"""
        while True:
            print(f"\n--- Student Menu ({self.current_user.name}) ---")
            print("1. View My Clubs")
            print("2. Join Club")
            print("3. View Assignments")
            print("4. Submit Assignment")
            print("5. View My Submissions")
            print("6. Logout")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.view_student_clubs()
            elif choice == "2":
                self.join_club()
            elif choice == "3":
                self.view_assignments()
            elif choice == "4":
                self.submit_assignment()
            elif choice == "5":
                self.view_my_submissions()
            elif choice == "6":
                self.current_user = None
                print("Logged out successfully!")
                break
            else:
                print("Invalid choice! Please try again.")
    