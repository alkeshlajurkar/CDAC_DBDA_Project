import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up your WebDriver
driver = webdriver.Chrome()  # or any other WebDriver you prefer
driver.get("https://www.mpcb.gov.in/air-quality/Nanded/0000000244")

# Wait for the dropdown to load
wait = WebDriverWait(driver, 10)

# Function to select option from dropdown
def select_option(option_value):
    dropdown = wait.until(EC.presence_of_element_located((By.ID, "cities-listing")))
    driver.execute_script("arguments[0].value = arguments[1];", dropdown, option_value)

# Function to select date
def select_date(date_str):
    from_date_input = wait.until(EC.presence_of_element_located((By.ID, "datepicker")))
    from_date_input.clear()
    from_date_input.send_keys(date_str)

def end_date(date_end):
    todate_date_input = wait.until(EC.presence_of_element_located((By.ID, "todate")))
    todate_date_input.clear()
    todate_date_input.send_keys(date_end)

# Function to click on the show button
def click_show_button():
    show_button = wait.until(EC.element_to_be_clickable((By.ID, "airQualityShow")))
    driver.execute_script("arguments[0].click();", show_button)

# Function to scrape table data and append to CSV
def scrape_table_data(csv_writer, city_name):
    try:
        # Select date range and click show button
        date_str ='01-01-2001'
        to_date='31-04-2024'
        select_date(date_str)
        time.sleep(2)
        end_date(to_date)
        click_show_button()

        # Wait for the table to load
        parent_div = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "air-quality-details")))
        child_div1 = WebDriverWait(parent_div, 30).until(EC.presence_of_element_located((By.ID, "demostReading")))
        child_div2 = WebDriverWait(child_div1, 30).until(EC.presence_of_element_located((By.ID, "divToPrint0")))
        table_data = WebDriverWait(child_div2, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.readtab.table.table-responsive.check_table.wq-monitor-box")))
        rows_data = WebDriverWait(table_data, 30).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))

        # Find all table rows except the header
        rows = rows_data.find_elements(By.TAG_NAME, "tr")[1:]

        # Iterate through each row and extract the data
        for row in rows:
            # Extract data from each column in the row
            columns = row.find_elements(By.TAG_NAME, "td")
            data = [city_name] + [column.text for column in columns]  # Adding city name to data

            # Write the data to the CSV file
            csv_writer.writerow(data)
    except Exception as e:
        print(f"Error occurred while processing {city_name}: {e}")

# Open CSV file in append mode
with open("2001_2024_MPCB.csv", "a", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    header = ["City","Sr.No.","Date","SO2 µg/m3","RSPM µg/m3","SPM µg/m3","AQI"]
    csv_writer.writerow(header)

    # Get the list of city options
    city_list = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "city_list")))
    options = city_list.find_elements(By.TAG_NAME, "option")

    for option in options:
        # Get the city name and value
        city_name = option.text.strip()
        city_value = option.get_attribute("value")

        # Select the current city
        select_option(city_value)

        # Scrape table data for the current city
        scrape_table_data(csv_writer, city_name)

# Close the WebDriver
driver.quit()