class Employee:
    def __init__(self,emp_id,name,salary,role="Staff"):
        """The Base Parent Class for all staff members."""
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
        self.role=role

    def calculatePayout(self):
        """Returns the basic salary footprint."""
        return self.salary
    
    def displayDetails(self):
        print(f"Role: {self.role:<11} | Id: {self.emp_id} | Name: {self.name} | Total Payout: {self.calculatePayout():,}")

class Manager(Employee):
    """Child Class inheriting from Employee (Adds management team bonuses)."""
    def __init__(self, emp_id, name, salary, team_size):
        super().__init__(emp_id, name, salary, role="Manager")
        self.team_size=team_size

    """Method Overriding: Base Salary + Team Management Bonus."""
    def calculatePayout(self):
        manager_bonus=2000*self.team_size
        return self.salary+manager_bonus

class Executive(Manager):
    """Grandchild Class inheriting from Manager (Multi-level Inheritance)."""
    def __init__(self, emp_id, name, salary, team_size,stock_options):
        # Passes arguments up to the Manager constructor
        super().__init__(emp_id, name, salary, team_size)
        self.stock_options=stock_options
        self.role="Executive"

    def calculatePayout(self):
        """Method Overriding: Uses Manager's payout calculation and adds stock incentives."""
        executive_bonus=5000
        return super().calculatePayout()+executive_bonus

#----Testing the corporate Hierarchy---
print("======== CORPORATE PAYROLL SYSTEM ========")

#1.Standard Employee Profile
staff=Employee("E101","Amit",40000)
staff.displayDetails()

print("-" * 50)

# 2. Manager Profile (Manages 5 people)
mgr=Employee("M101","Sneha",80000,5)
mgr.displayDetails()

print("-" * 50)

#3. Executive Profile (Manages a team of 20)
exe=Executive("EX101","Dr. Riya",90000,20,500)
exe.displayDetails()

exe1=Executive("EX102","Krish",80000,10,500)
exe1.displayDetails()

print("-" * 50)