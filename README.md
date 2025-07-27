# 🐍 Django For Beginners - Cricket Club Project

This is a beginner-friendly Django web application that manages cricket club activities, including player registration, match scheduling, and score tracking.

---

## 🚀 Features

- 🧾 Player Registration with validations
- 📅 Match Scheduling and History
- 🏏 Scoreboard and Player Stats
- 🔐 User Authentication (Login/Logout)
- 💾 PostgreSQL Database Integration
- 🖼️ Responsive Frontend with HTML & Bootstrap

---

## 🛠️ Tech Stack

| Layer       | Technology            |
|-------------|------------------------|
| Backend     | Django (Python)        |
| Frontend    | HTML5, CSS3, Bootstrap |
| Database    | PostgreSQL             |
| Deployment  | (Add here if deployed) |

---
setup instructions>>>

# 1. Clone the repo
git clone https://github.com/Mahi9390/Django_For_Beginners-Project-.git
cd Django_For_Beginners-Project-

# 2. Create virtual environment & activate it
python -m venv myenv
myenv\Scripts\activate  # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the server
python manage.py runserver

Folder structure>>>

cricket_club/
├── cricket_club/        # Project settings
├── players/             # Main app for cricket logic
├── templates/           # HTML files
├── static/              # CSS, JS, images
├── db.sqlite3           # SQLite DB (if using)
└── manage.py

