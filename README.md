

# Eactive_assignment_from_yash_lalwani

# Flask Users API

## Setup

1. Clone the repository:
   git clone https://github.com/codewithlalwani/Eactive_assignment_from_yash_lalwani.git

2. Install dependencies:
   pip install flask flask-mysqldb

3. Configure database settings in app.py:
   - MYSQL_HOST: localhost
   - MYSQL_USER: your_mysql_user
   - MYSQL_PASSWORD: your_mysql_password
   - MYSQL_DB: users

4. Initialize database:
   - Create database and table with the provided SQL commands.
   - Insert sample data.

5. Run the Flask app:
   python app.py

6. Access routes:
   - `/hello`
   - `/users`
   - `/new_user`
   - `/users/<id>`

Database Schema

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100),
  role VARCHAR(50)
);

Sample Data

INSERT INTO users (name, email, role) VALUES
('Alice', 'alice@example.com', 'Admin'),

Task 2, Point c: SQL Queries Used
Retrieve all users:

text
SELECT * FROM users;

Retrieve a specific user by ID:

text
SELECT * FROM users WHERE id

Dependencies
Python 3.x

Flask

flask-mysqldb

MySQL

Git Workflow & Contribution
text
- All new features or fixes should be developed in a branch (e.g., "assignment").
- After making changes, push your branch to the remote repo.
- Open a pull request to merge into "main".
- Review and approve changes before merging.

