# Fruit-Market Web Application

## Project Description

Fruit-Market is a full-stack Flask web application designed to demonstrate dynamic web functionality and database integration. Users can view a list of fruits, search for specific fruits, and explore a responsive interface.

This project showcases practical skills in building Python Flask applications, connecting to a database, handling form submissions, and rendering dynamic content with templates. It reflects an intermediate to advanced understanding of full-stack development.

## Tech Stack

* **Backend:** Python, Flask
* **Database:** MySQL (via `database.utility`)
* **Frontend:** HTML, CSS, Jinja2 Templates
* **Tools:** Git, VS Code, Flask Debug Server

## Features

* Search for fruits by name using a form
* View all fruits stored in the database
* Dynamic rendering of fruit data using Flask and Jinja2 templates
* Modular Python code with separation of database utility functions
* Easy to extend for additional functionality like login, registration, or admin panel

## Key Skills / Concepts Learned

* Flask routing and template rendering
* Database integration and queries
* Form handling and POST/GET methods
* Modular project structure
* Dynamic content rendering and search functionality

## Project Structure

```
/Fruit-Market-App
│
├── app.py                # Main Flask application
├── templates/            # HTML templates
│   ├── index.html        # Home / Search page
│   └── fruits.html       # Fruits listing page
├── database/
│   └── utility.py        # Database helper functions
└── static/               # (Optional) CSS/JS/images
```

## How to Run

1. Clone the repository:

```bash
git clone <your-repo-link>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
python app.py
```

4. Open a browser and visit:

```
http://127.0.0.1:5005/
```

## Sample Data

Example entries for testing the app:

| Fruit Name | Price |
| ---------- | ----- |
| Apple      | 100   |
| Banana     | 40    |
| Mango      | 120   |
| Orange     | 60    |

## Future Enhancements

* Add login and registration functionality for users
* Enable admin panel to add/update fruits
* Implement shopping cart functionality
* Improve UI using Bootstrap or Tailwind CSS

## Screenshots

*(Add screenshots of your app here to showcase search and fruit list p
