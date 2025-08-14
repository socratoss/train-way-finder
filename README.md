# train-way-finder

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-~3.x-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/License-Unspecified-lightgrey?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/last-commit/socratoss/train-way-finder?style=for-the-badge&label=Last%20Commit" alt="Last Commit">
  <img src="https://img.shields.io/github/languages/code-size/socratoss/train-way-finder?style=for-the-badge" alt="Code Size">
</p>

## Project Overview

`train-way-finder` is a Django-based web application designed to help users find optimal train routes between cities. It provides a robust platform for managing cities and trains, and utilizes a depth-first search algorithm to find the best routes based on criteria like travel time and intermediate cities. User authentication is a core feature, ensuring secure access to data management functionalities.

## Features & Functionality ✨

-   **City Management**: A comprehensive CRUD system for cities, powered by Django's generic class-based views.
-   **Train Management**: Full CRUD capabilities for train information, accessible through the Django admin interface.
-   **Route Finding**: An efficient route search engine that finds optimal paths and allows users to save them for later use.
-   **User Authentication**: Secure user registration and login, with authentication required for all data modification actions.

## Technology Stack 🚀

-   **Backend**: Python, Django (Models, Forms, Templates, Generic Views, Authentication)
-   **Frontend**: HTML5, CSS3, Bootstrap (for responsive design), JavaScript (with Select2 for enhanced select boxes)
-   **Database**: SQLite (default for development)

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

---

## Getting Started 🛠️

### Prerequisites

-   **Python** 3.6 or higher
-   **pip** (Python package installer)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/socratoss/train-way-finder.git](https://github.com/socratoss/train-way-finder.git)
    cd train-way-finder
    ```

2.  **Create and activate a virtual environment**:
    * On **Windows**:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    * On **macOS** and **Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies**:
    * Install the necessary packages:
        ```bash
        pip install django django-crispy-forms django-select2
        ```
    * **(Optional)** Generate a `requirements.txt` file for future use:
        ```bash
        pip freeze > requirements.txt
        ```

4.  **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an admin user.

---

## Usage Guide 🧭

1.  **Run the development server**:
    ```bash
    python manage.py runserver
    ```
    Access the application at `http://127.0.0.1:8000/`.

2.  **Explore features**:
    * Use the navigation bar to manage **Cities** and **Trains**.
    * On the homepage, use the search form to find **routes** between cities.
    * Log in or register via the **Authentication** links to gain full access.

---

## Contributing 🤝

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

1.  **Fork** the repository.
2.  **Create a feature branch**:
    `git checkout -b feature/your-feature-name`
3.  **Commit your changes**:
    `git commit -m "feat: Add a new feature"`
4.  **Push to the branch**:
    `git push origin feature/your-feature-name`
5.  **Create a Pull Request**.

---

## License 📜

This project does not have a specified license. All rights belong to the repository owner.

---

## Support

For any questions or support, please open an issue on the GitHub repository.
