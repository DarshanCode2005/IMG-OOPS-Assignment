from vector import Vector
from person import Person

class ClubAdmin(Person):
    """Club Admin class"""
    
    def __init__(self, id_str: str, name: str, password: str):
        super().__init__(id_str, name, password)
        self.managed_clubs = Vector()  # Clubs this admin manages
    
    def add_member(self, club, student) -> None:
        """Add student to club"""
        if hasattr(club, 'members'):
            if club.members.search_element(student) == -1:
                club.members.add_element(student)
                student.clubs.add_element(club)
                print(f"Added {student.name} to {club.name}")
            else:
                print(f"{student.name} is already a member of {club.name}")
    
    def remove_member(self, club, student) -> None:
        """Remove student from club"""
        if hasattr(club, 'members'):
            index = club.members.search_element(student)
            if index != -1:
                club.members.remove_element(index)
                # Also remove club from student's clubs
                club_index = student.clubs.search_element(club)
                if club_index != -1:
                    student.clubs.remove_element(club_index)
                print(f"Removed {student.name} from {club.name}")
            else:
                print(f"{student.name} is not a member of {club.name}")
    
    def create_assignment(self, club, title: str, max_score: int, deadline: str) -> None:
        """Create assignment for club"""
        from assignment import Assignment
        assignment = Assignment(title, max_score, deadline)
        club.assignments.add_element(assignment)
        print(f"Assignment '{title}' created for {club.name}")
    
    def view_submissions(self, assignment):
        """View all submissions for an assignment"""
        print(f"\nSubmissions for: {assignment.title}")
        print("-" * 40)
        if assignment.submissions.get_size() == 0:
            print("No submissions yet.")
        else:
            for submission in assignment.submissions:
                status = "Late" if submission.is_late else "On Time"
                print(f"Student: {submission.student.name}")
                print(f"Score: {submission.score}")
                print(f"Status: {status}")
                print(f"Date: {submission.submission_date}")
                print("-" * 20)