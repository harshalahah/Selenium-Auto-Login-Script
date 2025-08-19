# College Wi-Fi Auto Login

This project automates the login process for a college Wi-Fi portal using **Python + Selenium**.

## Motivation

My college Wi-Fi network required logging in repeatedly after short intervals, which was inconvenient.
I built this script as my **first real-world application project**, to save time and effort by automatically handling the login process.

## Features

* Automates entering username and password into the login form
* Works with Selenium WebDriver (tested with Chrome)
* Can be customized for similar Wi-Fi portals with minimal changes

## How it works

1. Script launches a browser using Selenium
2. Navigates to the Wi-Fi login portal page
3. Inputs credentials (stored securely in the script or via environment variables)
4. Submits the form automatically

## Requirements

* Python 3.x
* Selenium
* WebDriver for your browser (e.g., ChromeDriver)

## Note

⚠️ This script is for educational purposes only. Credentials and network details should never be shared publicly.
