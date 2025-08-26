# Restaurant Kitchen Management

Django project for managing a restaurant kitchen.

## Overview

RestoManage is a Django-based web application designed to help restaurants efficiently manage dishes, ingredients, cooks, and related data. The system provides an intuitive interface for CRUD operations, search, and pagination, along with a modern, responsive design powered by Bootstrap 5.  

## Features

- **Dish Management**
  - Add, update, and delete dishes.
  - Assign multiple cooks, ingredients, and dish types.
  - Upload dish photos with preview.
  - View detailed dish information with all associated data.

- **Ingredient Management**
  - Create, update, delete, and search ingredients.
  - Pagination support for large ingredient lists.
  - Clean, table-based UI with action buttons.

- **Cook Management**
  - Display all cooks with profile details, experience, and avatars.
  - Search functionality.
  - Responsive card-based layout for easy browsing.

- **Dish Types / Categories**
  - Manage dish types with CRUD operations.
  - Small and responsive action buttons for edit/delete.

- **User Experience Enhancements**
  - Search boxes for dishes, ingredients, and cooks.
  - Pagination with lightweight, minimal styling.
  - Responsive design using Bootstrap 5.
  - Alert messages for actions (create, update, delete).

- **Authentication & Profile**
  - Secure login, signup, and logout.
  - Cook profiles with avatar upload.
  - Profile update form with intuitive layout.

## Technologies Used

- Django 5.2.x  
- Python 3.12  
- Bootstrap 5  
- Crispy Forms  
- Bootstrap Icons & Font Awesome  
- SQLite (default, can be replaced with other databases)

## Project Structure

    restaurant_kitchen/
    ├── accounts/ # User authentication and profiles
    ├── cook/ # Cook management
    ├── dish/ # Dish, dish types, ingredients management
    ├── ingredient/ # Ingredient management
    ├── static/ # CSS, JS, images
    ├── templates/ # HTML templates
    └── manage.py


## Getting Started

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd restaurant_kitchen

2. Create and activate a virtual environment:
   ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/Mac
    .venv\Scripts\activate     # Windows

3. Install dependencies:
    ```bash   
    pip install -r requirements.txt
   
4. Run migrations:
    ```bash   
    python manage.py migrate
   
5. Start the development server:
   ```bash
   python manage.py runserver