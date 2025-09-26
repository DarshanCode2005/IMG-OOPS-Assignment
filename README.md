# Club Management System

A lightweight **CLI-based club management system** for students and administrators.
This project is built entirely in Python and demonstrates concepts like **inheritance, custom data structures, and modular design**, while offering a practical use case: managing student clubs, assignments, and submissions.

---

## 📂 Project Structure

```
club_management_system/
├── vector.py        # Custom Vector implementation (dynamic resizing)
├── person.py        # Base Person class
├── student.py       # Student class
├── club_admin.py    # ClubAdmin class
├── assignment.py    # Assignment class
├── submission.py    # Submission class
├── club.py          # Club class
└── main.py          # CLI entry point
```

---

## 🚀 How to Run

1. Clone or download this repository.
2. Navigate to the `club_management_system` directory in your terminal.
3. Run the system with:

```bash
python main.py
```

---

## Sample Login Credentials

### Students

* **Rahul Sharma** → ID: `21114001`, Password: `pass123`
* **Priya Singh** → ID: `21114002`, Password: `pass456`
* **Amit Kumar** → ID: `21114003`, Password: `pass789`

### Admins

* **Dr. Rajesh Verma (IMG)** → ID: `admin001`, Password: `admin123`
* **Prof. Sunita Gupta (SDS)** → ID: `admin002`, Password: `admin456`
* **Dr. Vikram Singh (DebSoc)** → ID: `admin003`, Password: `admin789`

---

## Features

* ✅ **Custom Vector** class (dynamic resizing, memory-efficient)
* ✅ **Inheritance hierarchy** → `Person → Student / ClubAdmin`
* ✅ **Club management** with admin privileges
* ✅ **Assignment creation and submission** system
* ✅ **Late submission tracking**
* ✅ **Multi-club membership** for students
* ✅ **Complete CLI interface** with sample data
* ✅ **Login system** for students & admins

---

## 🔧 Extra Functionality

*   System statistics overview
*   New student registration
*   Real-time submission status
*   Submission history for students
*   Admins can view all submissions with scores
*   Clubs can have multiple assignments
*   Error handling & clean separation of concerns

---