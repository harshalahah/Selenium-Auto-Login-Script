# Selenium-Auto-Login-Script
A simple Selenium script to automate website login -- my first hands-on project.

## 📌 Overview

This was my **first real application project**.
I built a simple Python script using **Selenium** to automate the login process on a website.
The main goal was to understand how browser automation works and how Selenium can interact with web elements like forms, buttons, and cookies.
Even though it’s small, this project gave me confidence to move on to bigger things (like building an MCP server 🚀).

---

## ⚡ Features

* Automates opening a browser and navigating to a login page
* Inputs username and password automatically
* Submits the login form
* (Optional) Handles wait times and errors gracefully

---

## 🛠️ Tech Stack

* **Python**
* **Selenium WebDriver**
* **ChromeDriver / GeckoDriver** (depending on browser)

---

## ▶️ How to Run

1. Install requirements:

   pip install selenium
   
3. Download a matching browser driver (e.g., ChromeDriver) and place it in your PATH.

4. Update the script with your test login details (⚠️ **Never hardcode real credentials if pushing code publicly**).

5. Run the script:

   python auto_login.py

## 🚀 Learnings

* Interacting with web elements using XPath, CSS selectors, and IDs
* Handling delays with **explicit and implicit waits**
* Debugging automation scripts when websites change their structure
* Understanding the importance of safe credential handling

---

## 🌱 Next Steps

* Automate filling out forms beyond login
* Add support for multiple websites
* Integrate with a password manager API for safe credential handling
