from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options
options = Options()
options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=ChromeService(), options=options)

# Navigate to the SonicWall login page
driver.get("https://192.168.192.200/sonicui/7/login/#/")

try:
    # Wait for and fill in the username field
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys("YOUR_USN")  # Replace with your actual username

    # Wait for and fill in the password field
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.send_keys("YOUR_PASSWORD")  # Replace with your actual password

    # Wait for the login button and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[4]/div[2]/div"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
    driver.execute_script("arguments[0].click();", login_button)

    # Wait for the Continue button to appear
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[3]/div/div/button"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", continue_button)
    driver.execute_script("arguments[0].click();", continue_button)

    print("Login Successful!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()  # Close the browser after completion

