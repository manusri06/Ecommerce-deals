# 🛒 E-Commerce Deals Display App

A Django-based web application that displays e-commerce deals from **pre-scraped data files** (CSV/JSON).  
The data is collected beforehand (not live scraping) and shown in a clean, responsive interface, with direct links to the original product pages.

---

## ✨ Features
- 📂 Reads deals from **local CSV/JSON files** (scraped beforehand).
- 🖥️ Displays deals in a **user-friendly and responsive** layout.
- 🔗 Redirects users to the **original product page**.
- ⚡ Fast performance as data is loaded from local files.

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Data Source:** Local CSV/JSON files (pre-scraped)

---

## 📂 Project Structure
```
├── app/         → where your Django app files are (views, urls, models, etc.)
├── templates/   → HTML templates for your pages
├── static/      → CSS, JS, and images
├── data/        → a folder to keep your sample CSV/JSON data files
├── manage.py    → Django’s main management script
└── README.md    → your project’s description file
```
