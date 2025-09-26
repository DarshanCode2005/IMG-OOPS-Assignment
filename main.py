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

    def admin_menu(self):
        """Admin menu interface"""
        while True:
            print(f"\n--- Admin Menu ({self.current_user.name}) ---")
            print("1. View My Clubs")
            print("2. Add Student to Club")
            print("3. Remove Student from Club")
            print("4. Create Assignment")
            print("5. View Assignment Submissions")
            print("6. View Club Members")
            print("7. Logout")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.view_admin_clubs()
            elif choice == "2":
                self.add_student_to_club()
            elif choice == "3":
                self.remove_student_from_club()
            elif choice == "4":
                self.create_assignment()
            elif choice == "5":
                self.view_assignment_submissions()
            elif choice == "6":
                self.view_club_members()
            elif choice == "7":
                self.current_user = None
                print("Logged out successfully!")
                break
            else:
                print("Invalid choice! Please try again.")

    def view_student_clubs(self):
        """View clubs student is member of"""
        student = self.current_user
        print(f"\n--- {student.name}'s Clubs ---")
        
        if student.clubs.get_size() == 0:
            print("You are not a member of any club.")
        else:
            for i, club in enumerate(student.clubs, 1):
                print(f"{i}. {club}")

    def join_club(self):
        """Student joins a club"""
        student = self.current_user
        print("\n--- Available Clubs ---")
        
        available_clubs = Vector()
        for club in self.clubs:
            if club.members.search_element(student) == -1:
                available_clubs.add_element(club)
        
        if available_clubs.get_size() == 0:
            print("No clubs available to join.")
            return
        
        for i, club in enumerate(available_clubs, 1):
            print(f"{i}. {club}")
        
        try:
            choice = int(input("Enter club number to join: ")) - 1
            if 0 <= choice < available_clubs.get_size():
                club = available_clubs.get(choice)
                club.add_member(student)
                print(f"Successfully joined {club.name}!")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number!")

    def view_assignments(self):
        """View assignments from student's clubs"""
        student = self.current_user
        print("\n--- Your Assignments ---")
        
        assignment_found = False
        for club in student.clubs:
            if club.assignments.get_size() > 0:
                print(f"\nFrom {club.name}:")
                print("-" * 30)
                for assignment in club.assignments:
                    print(f"  {assignment}")
                    assignment_found = True
        
        if not assignment_found:
            print("No assignments found.")    

    def submit_assignment(self):
        """Submit an assignment"""
        student = self.current_user
        
        # Collect all assignments from student's clubs
        all_assignments = Vector()
        assignment_clubs = Vector()
        
        for club in student.clubs:
            for assignment in club.assignments:
                all_assignments.add_element(assignment)
                assignment_clubs.add_element(club)
        
        if all_assignments.get_size() == 0:
            print("No assignments available to submit.")
            return
        
        print("\n--- Available Assignments ---")
        for i, assignment in enumerate(all_assignments, 1):
            club = assignment_clubs.get(i-1)
            print(f"{i}. {assignment} (From: {club.name})")
        
        try:
            choice = int(input("Enter assignment number: ")) - 1
            if 0 <= choice < all_assignments.get_size():
                assignment = all_assignments.get(choice)
                
                # Check if already submitted
                already_submitted = False
                for submission in assignment.submissions:
                    if submission.student == student:
                        already_submitted = True
                        break
                
                if already_submitted:
                    print("You have already submitted this assignment!")
                    return
                
                # Check if late
                current_date = datetime.now()
                deadline = datetime.strptime(assignment.deadline, "%Y-%m-%d")
                is_late = current_date > deadline
                
                if is_late:
                    print("Warning: This submission will be marked as LATE!")
                    confirm = input("Do you still want to submit? (y/n): ").lower()
                    if confirm != 'y':
                        print("Submission cancelled.")
                        return
                
                # Create submission
                submission = Submission(student, assignment, is_late=is_late)
                assignment.submissions.add_element(submission)
                student.submissions.add_element(submission)
                
                status = "LATE" if is_late else "ON TIME"
                print(f"Assignment submitted successfully! Status: {status}")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number!")

    def view_my_submissions(self):
        """View student's submissions"""
        student = self.current_user
        print(f"\n--- {student.name}'s Submissions ---")
        
        if student.submissions.get_size() == 0:
            print("No submissions found.")
        else:
            for submission in student.submissions:
                print(submission.get_details())

    def view_admin_clubs(self):
        """View clubs managed by admin"""
        admin = self.current_user
        print(f"\n--- {admin.name}'s Managed Clubs ---")
        
        if admin.managed_clubs.get_size() == 0:
            print("No clubs managed.")
        else:
            for i, club in enumerate(admin.managed_clubs, 1):
                print(f"{i}. {club}")
                print(f"   Members: {club.members.get_size()}")
                print(f"   Assignments: {club.assignments.get_size()}")


    def add_student_to_club(self):
        """Add student to club"""
        admin = self.current_user
        
        if admin.managed_clubs.get_size() == 0:
            print("You don't manage any clubs.")
            return
        
        # Select club
        print("\n--- Your Clubs ---")
        for i, club in enumerate(admin.managed_clubs, 1):
            print(f"{i}. {club.name}")
        
        try:
            club_choice = int(input("Select club: ")) - 1
            if 0 <= club_choice < admin.managed_clubs.get_size():
                club = admin.managed_clubs.get(club_choice)
                
                # Select student
                print("\n--- Available Students ---")
                available_students = Vector()
                for student in self.students:
                    if club.members.search_element(student) == -1:
                        available_students.add_element(student)
                
                if available_students.get_size() == 0:
                    print("No students available to add.")
                    return
                
                for i, student in enumerate(available_students, 1):
                    print(f"{i}. {student}")
                
                student_choice = int(input("Select student: ")) - 1
                if 0 <= student_choice < available_students.get_size():
                    student = available_students.get(student_choice)
                    admin.add_member(club, student)
                else:
                    print("Invalid student choice!")
            else:
                print("Invalid club choice!")
        except ValueError:
            print("Please enter a valid number!")

    def remove_student_from_club(self):
        """Remove student from club"""
        admin = self.current_user
        
        if admin.managed_clubs.get_size() == 0:
            print("You don't manage any clubs.")
            return
        
        # Select club
        print("\n--- Your Clubs ---")
        for i, club in enumerate(admin.managed_clubs, 1):
            print(f"{i}. {club.name} ({club.members.get_size()} members)")
        
        try:
            club_choice = int(input("Select club: ")) - 1
            if 0 <= club_choice < admin.managed_clubs.get_size():
                club = admin.managed_clubs.get(club_choice)
                
                if club.members.get_size() == 0:
                    print("No members in this club.")
                    return
                
                # Select member
                print(f"\n--- Members of {club.name} ---")
                for i, member in enumerate(club.members, 1):
                    print(f"{i}. {member}")
                
                member_choice = int(input("Select member to remove: ")) - 1
                if 0 <= member_choice < club.members.get_size():
                    member = club.members.get(member_choice)
                    admin.remove_member(club, member)
                else:
                    print("Invalid member choice!")
            else:
                print("Invalid club choice!")
        except ValueError:
            print("Please enter a valid number!")

    def create_assignment(self):
        """Create assignment for club"""
        admin = self.current_user
        
        if admin.managed_clubs.get_size() == 0:
            print("You don't manage any clubs.")
            return
        
        # Select club
        print("\n--- Your Clubs ---")
        for i, club in enumerate(admin.managed_clubs, 1):
            print(f"{i}. {club.name}")
        
        try:
            club_choice = int(input("Select club: ")) - 1
            if 0 <= club_choice < admin.managed_clubs.get_size():
                club = admin.managed_clubs.get(club_choice)
                
                # Get assignment details
                title = input("Assignment Title: ").strip()
                max_score = int(input("Maximum Score: "))
                deadline = input("Deadline (YYYY-MM-DD): ").strip()
                
                admin.create_assignment(club, title, max_score, deadline)
            else:
                print("Invalid club choice!")
        except ValueError:
            print("Please enter valid values!")

    def view_assignment_submissions(self):
        """View submissions for assignments"""
        admin = self.current_user
        
        # Collect all assignments from admin's clubs
        all_assignments = Vector()
        assignment_clubs = Vector()
        
        for club in admin.managed_clubs:
            for assignment in club.assignments:
                all_assignments.add_element(assignment)
                assignment_clubs.add_element(club)
        
        if all_assignments.get_size() == 0:
            print("No assignments found in your clubs.")
            return
        
        print("\n--- Select Assignment ---")
        for i, assignment in enumerate(all_assignments, 1):
            club = assignment_clubs.get(i-1)
            print(f"{i}. {assignment.title} (From: {club.name})")
        
        try:
            choice = int(input("Enter assignment number: ")) - 1
            if 0 <= choice < all_assignments.get_size():
                assignment = all_assignments.get(choice)
                admin.view_submissions(assignment)
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number!")