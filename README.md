
# 🐦 Tweet — A Simple Django Tweeting App

**Tweet** is a minimal Django-based web application that allows users to create, edit, delete, and browse tweet-like posts.
It also includes user registration, login/logout, and a search feature for filtering tweets by title.

This project is ideal for beginners looking to understand **Django CRUD**, **authentication**, **forms**, and **templating**.

---

## 🚀 Features

### 📌 Public

* View all tweets (latest first)
* Search tweets by title (case-insensitive)

### 🔐 Authenticated Users

* Create a new tweet
* Edit your own tweets
* Delete your own tweets
* Upload images with tweets
* Register a new account
* Auto-login after registration

---

## 📸 Core Functionality (From views.py)

### **1. Tweet List**

* Shows all tweets ordered by `created_at`
* Supports searching by title:

```python
tweets = Tweets.objects.filter(title__icontains=stx)
```

### **2. Create Tweet** (Login required)

* Handles text + image uploads
* Auto-assigns logged-in user to the tweet

### **3. Edit Tweet** (User owns tweet)

* Ensures only the tweet owner can edit

### **4. Delete Tweet** (User owns tweet)

* Confirms deletion before removing

### **5. User Register**

* Custom registration form
* Automatically logs user in after successful registration

---

## 🔧 Installation & Setup

Follow these steps to run **Tweet** on your local machine.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/tweet.git
cd tweet
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser (optional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Start Development Server

```bash
python manage.py runserver
```

Your app is now live at:

👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧪 Screenshots (Optional Section)

You can add screenshots here.

```
![Home Page](path/to/screenshot.png)
![Tweet List](path/to/screenshot2.png)
```

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Django**
* **SQLite (default)**
* HTML / CSS (Django Templates)

---

## 🤝 Contributing

Pull requests and suggestions are welcome!
Feel free to open an issue for feature ideas or bug reports.

---

## 📄 License

This project is open-source and available under the **MIT License**.
