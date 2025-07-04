# Feedback Collector App

A modern, responsive feedback collection web application built with **React** (Frontend) and **Flask** (Backend), designed to collect and display user feedback based on categories like General, Bug, and Feature Request.

The app is fully deployed using:
-  **Frontend**: [Vercel](https://feedback-frontend-henna.vercel.app/)
-  **Backend**: [Railway](https://web-production-df92f.up.railway.app)

---

##  Features

-  Users can submit feedback with a category
-  Validations for empty input or unselected category
-  Notification system for successful or failed submission
-  Dynamically shows list of all submitted feedbacks
-  Minimalistic and elegant UI with custom black + beige theme
-  Fully deployed frontend + backend

---

##  Tech Stack

| Layer      | Technology        |
|------------|-------------------|
| Frontend   | React, Axios, CSS |
| Backend    | Python (Flask)    |
| Database   | SQLite (local file `feedback.db`) |
| Deployment | Vercel (Frontend), Railway (Backend) |

---

## 🛠 Setup Instructions

###  1. Backend (Flask + Railway)

```bash
# Clone the backend repo
git clone https://github.com/Sowndarya19/feedback-backend.git
cd feedback-backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the server
python app.py

# Clone the frontend repo
git clone https://github.com/Sowndarya19/feedback-frontend.git
cd feedback-frontend

# Install node modules
npm install

# Create a .env file and add:
REACT_APP_API_URL=https://your-backend-url.up.railway.app

# Start the development server
npm start

