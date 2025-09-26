from vector import Vector

class Club:
    """Club class"""
    
    def __init__(self, name: str, admin):
        self.name = name
        self.admin = admin  # ClubAdmin object
        self.members = Vector()  # Vector of Student objects
        self.assignments = Vector()  # Vector of Assignment objects
        
        # Add admin to managed clubs
        admin.managed_clubs.add_element(self)
    
    def add_member(self, student) -> None:
        """Add member to club"""
        if self.members.search_element(student) == -1:
            self.members.add_element(student)
            student.clubs.add_element(self)
    
    def remove_member(self, student) -> None:
        """Remove member from club"""
        index = self.members.search_element(student)
        if index != -1:
            self.members.remove_element(index)
            # Remove club from student's clubs
            club_index = student.clubs.search_element(self)
            if club_index != -1:
                student.clubs.remove_element(club_index)
    
    def add_assignment(self, assignment) -> None:
        """Add assignment to club"""
        self.assignments.add_element(assignment)
    
    def list_members(self):
        """List all club members"""
        print(f"\nMembers of {self.name}:")
        print("-" * 30)
        if self.members.get_size() == 0:
            print("No members yet.")
        else:
            for i, member in enumerate(self.members, 1):
                print(f"{i}. {member.name} ({member.id})")
    
    def list_assignments(self):
        """List all club assignments"""
        print(f"\nAssignments in {self.name}:")
        print("-" * 30)
        if self.assignments.get_size() == 0:
            print("No assignments yet.")
        else:
            for i, assignment in enumerate(self.assignments, 1):
                print(f"{i}. {assignment}")
    
    def __str__(self):
        return f"Club: {self.name} (Admin: {self.admin.name})"
    
    def __eq__(self, other):
        if isinstance(other, Club):
            return self.name == other.name
        return False