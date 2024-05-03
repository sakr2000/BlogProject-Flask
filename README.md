# Professional Blog Website

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Video Demonstration](#video-demonstration)
- [Installation and Usage](#installation-and-usage)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [Future Plans](#future-plans)

## Overview

This project is a professional blog website created using Python Flask, HTML, CSS, and Bootstrap. It features a modern and responsive design, allowing users to create, manage, and share blog posts easily. The blog includes user authentication, form validation, profile picture upload, password reset via email, and database integration with SQLAlchemy. It provides a sleek and user-friendly platform for bloggers and readers.

## Key Features

- **Responsive Design:** Ensures a seamless user experience across devices.
- **Form Validation:** Implemented using Flask-WTF for data integrity.
- **User Authentication:** Secure login and registration with password hashing and Flask-Login Manager.
- **User Profile Picture:** Supports upload with file type validation and large image compression.
- **Post Management:** CRUD operations for creating, updating, and deleting blog posts.
- **Pagination:** Allows for easier navigation of long lists of posts.
- **Database Integration:** Uses SQLAlchemy models to interact with the SQLite database.
- **Password Reset:** Secure password reset functionality via email with timed token for added security.
- **Component-based Structure:** Organized using Flask blueprints for scalability.
- **Custom Error Pages:** Personalized 404, 500, and other error pages for a polished user experience.
- **Access Control:** Restrictions implemented for certain routes to manage user access.
- **Configuration Class:** Custom configuration class for easy application setup.

## Technologies Used

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Sqlite](https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)

- Python
- Flask
- HTML
- CSS
- Jinja
- Bootstrap
- SQLite DB
- PyCharm

## Video Demonstration

<div align="center">

[![Watch the video](https://img.youtube.com/vi/nN33B2KiL40/0.jpg)](https://www.youtube.com/watch?v=nN33B2KiL40)

</div>
## Installation and Usage

1. **Clone the Repository:**

```bash
git clone https://github.com/sakr2000/BlogProject-Flask.git
```

2. **Create and Activate a Virtual Environment:**

- Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

- MacOs/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set Up the Environment Variables:**

- For Windows (Command Prompt):

```bash
setx EMAIL_USER "your-email@gmail.com"
setx EMAIL_PASS "your-email-password"
setx SECRET_KEY "your-secret-key"
setx SQLALCHEMY_DATABASE_URI "sqlite:///site.db"
```

- For macOS/Linux (Terminal):

```bash
export EMAIL_USER="your-email@gmail.com"
export EMAIL_PASS="your-email-password"
export SECRET_KEY="your-secret-key"
export SQLALCHEMY_DATABASE_URI="sqlite:///site.db"
```

5. **Set Up the Database:** Run the following command to create the SQLite database:

```bash
python db_create.py
```

6. **Run the Application:**

```bash
python run.py
```

7. **Access the Website:** Open `http://localhost:5000` in your web browser.

## Contributing

We welcome contributions to improve the project. To contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature`)
3. Make changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature`)
5. Create a pull request

## Acknowledgements

Special thanks to [Corey Schafer](https://www.youtube.com/user/schafer5) for his helpful tutorial videos on Flask and web development, which were instrumental in the creation of this project.

## Future Plans

- Implement search and filtration functionality for posts.
- Enhance the UI with more modern design elements.
- Improve security measures further, such as implementing CSRF protection.
