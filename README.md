# python-oop-journey
A step-by-step log of my journey learning Python Object-Oriented Programming concepts and building mini-projects.

## 📁 Repository Structure
`01-oop-basics/` — Core concepts mastered: `class`, `object`, `__init__`, and `self`.

---

## 📈 Concept 1: Featured Programs

## i) 📱 'social_media.py'
**What it does:** Simulates an interactive social media post tracker. 
**OOP Concept:** Demonstrates how methods use `self` to dynamically update internal states, such as incrementing live like counts and appending user comments to an array.

## ii) 🛒 'digital_cart.py'
**What it does:** Simulates an e-commerce digital shopping cart checkout workflow.
**OOP Concept:** Uses an initialized constructor to map string keys to numerical values inside a dictionary (`self.items = {}`). It utilizes built-in math aggregation to loop through stored attributes and generate an itemized invoice calculation upon checkout.

## 📈 Concept 2: Encapsulation

Advanced concepts mastered: **Private Variables (`__`)**, **Class Variables**, and **Data Validation**.
## i) secure_atm.py
A simulated secure banking application. It highlights data privacy by locking down crucial information (`__pin` and `__balance`) from external tampering. It implements structural logic checks to securely validate user credentials before allowing account inquiries, deposits, or withdrawals.

Feat: Completed SecureATM with PIN validation, secure deposits, and withdrawal logic!

Advanced concepts mastered: **Private Variables (`__`)** and **Class Variables**.
## ii) smart_flight.py
An airline ticket booking simulation. It sets up private attributes (`__passport_no` and `__ticket_price`) to secure sensitive travel metrics from unauthorized direct access.

Feat: Completed SmartFlight with passport validation and business class upgrade logic!

## 📈 Concept 3: Inheritance

Advanced concepts mastered: **Base Class (Parent)**, **Derived Class (Child)**, `super().__init__()`, **Method Overriding**, **Multi-level Hierarchy**, and **Hierarchical Branching**.

## i) 🚗 'vehicle_showroom.py'
**What it does:** Simulates a digital product catalog for a premium vehicle dealership tracking different stock configurations.
**OOP Concept:** Illustrates basic Parent-to-Child inheritance mapping. Child models reuse baseline attributes while implementing specialized features like electric vehicle battery metrics or superbike velocity limits via method overriding.

## ii) 🏢 'employee_hierarchy.py'
**What it does:** Simulates an enterprise corporate organizational payroll system.
**OOP Concept:** Demonstrates **Multi-level Inheritance** (`Employee` ➡️ `Manager` ➡️ `Executive`). It shows how data configurations and calculation engines scale down a vertical chain while maintaining formatted output alignment columns using space formatting.

## 📱 iii) 'smart_home_device.py'
**What it does:** Simulates an automated smart home central dashboard managing real-time IoT utility operations.
**OOP Concept:** Demonstrates **Hierarchical Inheritance** where multiple entirely distinct specialized appliances (`SmartThermostat` and `SmartSecurityCamera`) branch off a single parent core. It integrates standard `datetime` modules to track state mutations automatically.

-> Feat: Completed all Day 3 inheritance tasks with custom overriding and multi-tier classes!




