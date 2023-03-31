from selenium import webdriver
import files


def load_driver():
    driver_path = files.get_driver_path()
    Driver = webdriver.Chrome(executable_path=driver_path)
    return Driver
