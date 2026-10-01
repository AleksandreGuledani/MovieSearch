# MovieSearch

A Django web application for searching movies and viewing basic movie information using the OMDb API.

## Features

* 🔎 Search for movies by name
* 🎬 View movie information, including:

  * Movie poster
  * Short description
  * Director
* 🔐 User registration and login
* 👤 User profile with previous searches and search dates
* 📧 Contact form for sending messages directly to the site owner
* 📄 About page
* 🚪 User logout
* 💾 Persistent search history using SQLite

## How It Works

1. Visitors can enter a movie name from the home page.
2. Users who are not logged in are redirected to the login page.
3. New users can create an account and then log in.
4. Authenticated users can search for movies using the search form.
5. Movie information is retrieved from the OMDb API and displayed on the page.
6. Successful searches are saved to the user's profile.
7. Users can view their previous searches and the dates they were made.

## Technologies

* **Python**
* **Django**
* **JavaScript**
* **HTML / CSS**
* **SQLite**
* **OMDb API**
* **python-dotenv**
* **Requests**

## Project Structure

```text
MovieSearch/
├── Contact/
├── movie_search/
├── static/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AleksandreGuledani/MovieSearch.git
cd MovieSearch
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the same directory as `manage.py`:

```text
DJANGO_SECRET_KEY=your_django_secret_key
OMDB_API_KEY=your_omdb_api_key
DEBUG=True
```

The `.env` file is excluded from version control and should never be committed to the repository.

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

## Environment Variables

| Variable            | Purpose                                    |
| ------------------- | ------------------------------------------ |
| `DJANGO_SECRET_KEY` | Django's cryptographic secret key          |
| `OMDB_API_KEY`      | API key used to retrieve movie information |
| `DEBUG`             | Enables or disables Django debug mode      |

## Project Purpose

MovieSearch was developed as a personal project to practice building a complete Django web application. The project combines user authentication, database operations, API integration, form handling, and frontend development into one application.
