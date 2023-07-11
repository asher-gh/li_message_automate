import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from decouple import config

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TODO: Dynamic messages


def from_csv(csv_file="profiles.csv"):
    try:
        li_username = str(config("USERNAME"))
        li_password = str(config("PASSWORD"))
    except Exception as e:
        print(e)
        exit(1)

    # Initialize the Selenium web driver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 600)
    # Open LinkedIn and log in (adjust the URL if necessary)
    driver.get("https://www.linkedin.com/login")

    # Fill in your login credentials
    email = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    email.send_keys(li_username)
    password.send_keys(li_password)
    password.send_keys(Keys.RETURN)

    # Wait for the user to manually complete the CAPTCHA if prompted
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body[dir]")))

    # Read the CSV file
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if it exists
        for row in reader:
            profile_url = row[0]
            print(f"Messaging {profile_url}")

            # Open the LinkedIn profile URL
            driver.get(profile_url)

            msg_btn_path = "//*[contains(@class, \
            'pvs-profile-actions__action')]/button[contains(@aria-label, 'Message')]"
            msg_btn = wait.until(
                EC.visibility_of_element_located((By.XPATH, msg_btn_path))
            )

            name = driver.find_element(
                By.XPATH,
                "//h1[@class='text-heading-xlarge inline t-24 v-align-middle break-words']",
            ).text.split(" ")[0]

            # Click on the "Message" button
            msg_btn = driver.find_element(
                By.XPATH,
                "//*[contains(@class, \
                'pvs-profile-actions__action')]/button[contains(@aria-label, 'Message')]",
            )
            msg_btn.click()

            # Find the message input field and send the predefined message
            msg_input_path = "//div[@aria-label='Write a message…']/p"
            msg_input = wait.until(
                EC.visibility_of_element_located((By.XPATH, msg_input_path))
            )

            message = f"Hi {name}! Hope you are doing well."

            msg_input.send_keys(message)

            # send the message
            send_btn_path = '//button[contains(@type, "submit") and \
            contains(@class, msg-form__send-button)]'
            send_btn = wait.until(EC.element_to_be_clickable((By.XPATH, send_btn_path)))
            send_btn.click()

            # wait until the message is sent
            wait.until(
                EC.none_of(EC.element_to_be_clickable((By.XPATH, send_btn_path)))
            )

    # Close the web driver
    driver.quit()


if __name__ == "__main__":
    from_csv()
