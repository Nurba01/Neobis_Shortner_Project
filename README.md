
#  URL Shortner

This project implements a URL shortener service using Django and PostgreSQL. It allows users to input a URL and receive a shortened version of it, which redirects to the original URL when accessed.

##  Features

- **URL Shortening**: Users can submit a URL to be shortened. The application generates a unique identifier, saves it along with the original URL, and provides a shortened URL to the user.
- **URL Redirection**: When a user accesses a shortened URL, the application redirects them to the original, longer URL.
- **Database**: PostgreSQL is used to store the original and shortened URLs, ensuring fast retrieval and management of data.

## 🛠 Technologies and Libraries
![Alt text for Logo1](https://camo.githubusercontent.com/0562f16a4ae7e35dae6087bf8b7805fb7e664a9e7e20ae6d163d94e56b94f32d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534)
![Alt text for Logo2](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) 
![Alt text for Logo3](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) 
![Alt text for Logo3](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

## 🏁 Getting Started

These instructions will guide you through setting up the project on your local machine.

### Prerequisites

- Python 3.x
- pip
- Virtualenv (optional but recommended)
- PostgreSQL

### Setting Up a Virtual Environment
1. **Clone the repository:**

2. **Set up and activate a virtual environment:**

  - Install virtualenv if you haven't installed it yet:

      ```bash
      pip install virtualenv
      ```

  - Create a virtual environment in the project directory:

      ```bash
      virtualenv venv
      ```

  - Activate the virtual environment:

      - On Windows:

          ```bash
          venv\Scripts\activate
          ```

      - On Unix or MacOS:

          ```bash
          source venv/bin/activate
          ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the PostgreSQL database:**

    Ensure you have PostgreSQL installed and running. Create a database for this project and configure the database settings in your project's `settings.py` file.

5. **Perform database migrations:**

    ```bash
    cd url-shortener
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser


7. **Run the project:**

    ```bash
    python manage.py runserver


##  Usage

To shorten a URL, navigate to the home page and enter the URL in the form provided. Submitting the form will generate a shortened URL which redirects to the original URL when accessed.

For administrative tasks, such as viewing or deleting shortened URLs, access Django's admin panel at `http://127.0.0.1:8000/admin` using the superuser credentials you created.


##  Contributing
Contributions to improve the project are welcome. Please feel free to fork the repository and submit pull requests.
