# Flights_Django ✈️

A Django-based web application for managing flight information, including airports, flights, and passengers. This project also features an AI-powered assistant for flight-related queries.

## 🌟 Project Overview

This project is a demonstration of building a flight management system using the Django framework. It allows users to view flight details, manage passenger bookings, and interact with an AI assistant for flight information. The application leverages Django's ORM for data management and integrates with an external AI service for conversational capabilities.

## 🚀 Features

*   **Flight Management:** View and manage flight details (origin, destination, duration).
*   **Airport Management:** Define and associate airports with flights.
*   **Passenger Management:** Assign passengers to flights and manage bookings.
*   **AI Flight Assistant:** Interact with an AI chatbot powered by OpenRouter to get information about flights based on manifest data.
*   **User Authentication:** Basic user login/logout functionality.
*   **Responsive Design:** Utilizes Bootstrap for a consistent user interface.

## 📚 Table of Contents

*   [Project Title & Badges](#project-title--badges)
*   [Description](#description)
*   [Features](#features)
*   [Tech Stack](#tech-stack)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Project Structure](#project-structure)
*   [Contributing](#contributing)
*   [License](#license)
*   [Important Links](#important-links)
*   [Footer](#footer)

## 🛠️ Tech Stack

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS, Bootstrap
*   **Database:** SQLite (default Django setup)
*   **AI Integration:** OpenAI API via OpenRouter
*   **Other:** `python-dotenv`

## ⚙️ Installation

This project uses Django and Python. To set up and run the project locally, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Odeh182003/Flights_Django.git
    cd Flights_Django
    ```

2.  **Set up a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    # source venv/bin/activate
    ```

3.  **Install Dependencies:**
    The project relies on Django and `python-dotenv`. You can install them using pip:
    ```bash
    pip install django python-dotenv openai
    ```

4.  **Configure Environment Variables:**
    This project uses environment variables for sensitive information like API keys. Create a `.env` file in the root directory of the project and add the following:
    ```
    OPENROUTER_API_KEY=your_openrouter_api_key
    LLM_MODEL=your_llm_model_name
    ```
    Replace `your_openrouter_api_key` and `your_llm_model_name` with your actual credentials.

5.  **Apply Migrations:**
    Apply the database migrations to set up the necessary tables.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

## 🚀 Usage

Once the server is running, you can interact with the application through your web browser:

1.  **Dashboard:** Navigate to `/flights_app/dashboard` to see a summary of airports and passengers.
2.  **Flight List:** Access `/flights_app/` to view a list of all available flights. Clicking on a flight will take you to its details page.
3.  **Flight Details:** On the flight details page (e.g., `/flights_app/1`), you can see flight information, view assigned passengers, cancel their bookings, or book new passengers.
4.  **AI Assistant:** Go to `/flights_app/chat` to interact with the AI flight assistant. You can ask questions about flight manifests, and the AI will provide answers based on the available data.
5.  **User Authentication:** Access `/users/login` to log in. The system uses basic username and password authentication. After logging in, you will be redirected to the user profile page.

### Example Scenario:

*   **Viewing Flights:** Visit the flight list page to see all flights.
*   **Booking a Passenger:** On a flight's detail page, select a passenger from the dropdown and click 'Book' to assign them to that flight.
*   **Querying AI:** In the chat interface, ask something like, "What are the notes for flight ID 5?" or "Which flight goes from New York to London?".

## 📂 Project Structure

```
Flights_Django/
├── .env              # Environment variables (API keys, etc.)
├── db.sqlite3        # Database file
├── manage.py         # Django management script
├── flights_app/      # Main flight application
│   ├── __init__.py
│   ├── admin.py      # Django admin configurations
│   ├── apps.py       # App configuration
│   ├── agent.py      # AI agent logic
│   ├── migrations/   # Database migration files
│   ├── models.py     # Database models (Airport, Flight, Passenger, FlightManifest)
│   ├── static/       # Static files (CSS, JS, images)
│   │   └── flights_app/
│   │       └── styles.css
│   ├── templates/    # HTML templates
│   │   └── flights/
│   │       ├── base.html     # Base template
│   │       ├── chat.html     # AI chat interface
│   │       ├── dashboard.html # Dashboard view
│   │       ├── flight.html   # Flight detail view
│   │       ├── index.html    # Flight list view
│   │       └── layout.html   # General layout template
│   ├── tests.py      # Unit tests
│   └── urls.py       # App-specific URLs
├── flightsproject/   # Project configuration
│   ├── __init__.py
│   ├── asgi.py       # ASGI configuration
│   ├── settings.py   # Django settings
│   └── urls.py       # Project-level URLs
└── users/            # User management app
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── templates/
    │   └── users/
    │       ├── layout.html
    │       ├── login.html
    │       └── user.html
    ├── tests.py
    └── views.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to:

*   Fork the repository.
*   Create a new branch for your feature or bug fix (`git checkout -b feature/your-feature`).
*   Make your changes and commit them (`git commit -m 'Add some feature'`).
*   Push to the branch (`git push origin feature/your-feature`).
*   Open a Pull Request.

Please ensure you follow the coding style and add tests where appropriate.

## 📄 License

No license information was detected for this project. Please refer to the repository for any specific usage terms.

## 🔗 Important Links

*   **Repository:** [https://github.com/Odeh182003/Flights_Django](https://github.com/Odeh182003/Flights_Django)

## 📝 Footer

© 2023 Flights_Django | Repository available at [Odeh182003/Flights_Django](https://github.com/Odeh182003/Flights_Django)

**Author:** Odeh182003


---
**<p align="center">Generated by [ReadmeCodeGen](https://www.readmecodegen.com/)</p>**
