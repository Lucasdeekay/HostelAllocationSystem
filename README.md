# HostelAllocationSystem

# Overview
The Hostel Allocation System is a web application developed using Django, designed to streamline the process of assigning hostels to students automatically upon registration. The system simplifies the allocation process and enhances efficiency by eliminating the need for manual intervention.

# Features

## Automatic Hostel Assignment
Upon successful registration, students are automatically assigned to a hostel based on predefined criteria. This feature ensures a fair and efficient allocation process, saving time and resources.

## Hostel Information
The system provides detailed information about each hostel. Students can access this information to familiarize themselves with their assigned hostel.

## Printable Allocation Slip
Students can generate and print a hostel allocation slip directly from the system. The slip contains essential details such as hostel name, room number, and any additional instructions. This feature enables students to have a physical record of their hostel allocation.

# Getting Started

## Prerequisites
Python 3.x
Django (install using pip install django)

## Installation

### Clone the repository:
```git clone https://github.com/Lucasdeekay/HostelAllocationSystem.git```

### Navigate to the project directory:
```cd HostelAllocationSystem```

### Create a virtual environment:
```python -m venv venv```

### Activate the virtual environment:
On Windows:
```venv\Scripts\activate```

On Unix or MacOS:
```source venv/bin/activate```

### Install dependencies:
```pip install -r requirements.txt```

### Apply database migrations:
```python manage.py migrate```

### Run the development server:
```python manage.py runserver```

Access the application in your web browser at http://localhost:8000/.

# Usage
Register as a new student on the system.
Upon successful registration, the system will automatically assign a hostel based on predefined criteria.
Login to learn more about the assigned hostel.
Generate and print the hostel allocation slip for your records.


# License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as needed.

# Acknowledgments
Special thanks to the Django community for their excellent documentation and support.

For any issues or inquiries, please contact lucasdeekay98@gmail.com.
