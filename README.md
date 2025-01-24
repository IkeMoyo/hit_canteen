# hit_canteen
Canteen Ordering System. Final year Capstone Project (2022)

## Table of Contents

- [Hit Canteen](#hit-canteen)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies](#technologies)
  - [Installation](#installation)
  - [Contributing](#contributing)
  - [Contact](#contact)

## Features

- User authentication (Admin, Teachers, Students, Staff)
- CRUD operations for students, teachers, and products
- Wallet management system
- Order recommendation system
- Online ordering
- Customer segmentation
- Sales forcasting
- Feedback communication module
- Order tracking
- Responsive design

## Technologies

- Django 5.x
- Python 3.x
- HTML5, CSS3, JavaScript (Bootstrap 5)
- PostgreSQL
- Data Science technologies: Pandas, Mathplotlib, Seaborn, Numpy

## Installation

### Prerequisites

- Python 3.x
- pip
- virtualenv (optional)
- PostgreSQL

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/school-management-system.git
   cd school-management-system

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   
4. **Configure the database:**

  Update the DATABASES settings in settings.py with your PostgreSQL credentials.
   
5. **Run migrations:**

   ```bash
   python manage.py migrate

6. **Create a superuser (for admin access):**

   ```bash
   python manage.py createsuperuser

6. **Start the development server:**

   ```bash
   python manage.py runserver

## Usage
Access the application at http://localhost:8000/.
Use the admin interface at http://localhost:8000/admin/ with the superuser credentials.

## Contact
Ike Moyo - ikemoyobeta@gmail.com



