# 🔢 Prime Number Checker – Flask Web App

A simple web application built using **Python Flask** that allows users to check whether a given number is a **prime number** or not. This beginner-friendly project demonstrates the integration of **HTML forms**, **Python logic**, and **Flask routing**.

---

## 🌟 Features

* 📥 Input number through an interactive HTML form
* ✅ Efficient Python-based prime number checking logic
* 🔁 Clean Flask routing with GET/POST handling
* 🎨 Responsive UI using basic CSS styling
* ⚡ Instant result displayed on the same page

---

## 🛠️ Tech Stack

| Technology | Description                      |
| ---------- | -------------------------------- |
| Python     | Backend programming language     |
| Flask      | Lightweight Python web framework |
| HTML5      | Markup for frontend structure    |
| CSS3       | Styling for user interface       |

---

## 📂 Project Structure

```
prime_checker/
├── app.py                # Flask application logic
├── templates/
│   └── index.html        # Frontend (HTML + CSS)
├── static/
│   └── screenshot.png    # App UI preview image
└── README.md             # Project documentation
```

---

## 🧠 Prime Number Logic (Python)

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

The function checks divisibility only up to the square root of the number, making it more efficient for large inputs.

---

## 💻 Getting Started

### 1. Install Flask

```bash
pip install flask
```

### 2. Run the Application

```bash
python app.py
```

### 3. Open in Browser

```
http://127.0.0.1:5000
```

---

## 📸 Screenshot

![App Screenshot](static/screenshot.png)

---

## 🚀 Future Enhancements

* 🔢 Input validation for non-integer and negative values
* 🕘 Display history/log of checked numbers
* ☁️ Deploy on platforms like **Render**, **Replit**, or **Netlify with Flask wrapper**

---

## 👨‍💻 Author

**Routhu Satya Hemesh**
📧 [Portfolio](https://satyahemesh.netlify.app) • 🧑‍💻 [GitHub](https://github.com/satyahemesh)

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use and modify it.

---
