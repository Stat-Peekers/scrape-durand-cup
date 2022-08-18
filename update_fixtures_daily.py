"""
@title: Get info on fixtures in the tournament
@author: Sushant Rao
@twitter: StatPeekers
"""
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from utils.common_functions import select_tournament_name, get_data_from_file_json, put_data_to_file_json


def get_fixture_info(tour_id: int, base_url: str, event_no: int, month=0, year=2022):

    s_driver = webdriver.Chrome('chromedriver.exe')
    scrape_url = base_url + "event=" + str(event_no) + "&month=" + str(month) + "&year=" + str(year)
    s_driver.get(scrape_url)
    from time import sleep
    sleep(5)
    # Read the existing json file:
    fixture_data = get_data_from_file_json("config/fixture_info.json")
    """
    Obtain table headers
    """
    t_rows = s_driver.find_elements(By.XPATH, '//*[@id="calendar"]/div[3]/div[1]/table/tbody/tr')
    for row in t_rows:
        # Get match_id
        try:
            match_url = row.find_element(By.XPATH, ".//td/a").get_attribute("href")
            match_id = re.findall('[0-9]+', match_url)[0]
            _ = {
                fix.update({"link": match_url})
                for tour_fix in fixture_data if tour_fix["id"] == tour_id
                for fix in tour_fix["events"] if fix["id"] == int(match_id)
            }
            print("URL updated for matchID:", match_id)
        except NoSuchElementException:
            pass
    s_driver.close()
    # Write to the existing json file:
    put_data_to_file_json("config/fixture_info.json", fixture_data)
    print("Fixture update completed")


if __name__ == "__main__":
    t_id, t_name = select_tournament_name()
    mapping_dict = {
        237: {
            "event_no": 19,
            "month": 0,
            "year": 2020
        },
        366: {
            "event_no": 19,
            "month": 0,
            "year": 2022
        }
    }
    b_url = "https://www.the-aiff.com/calendar?"
    e_no = mapping_dict[t_id]["event_no"]  # for Durand Cup
    mnth = mapping_dict[t_id]["month"]  # 0 for all months in a calender year else specify the month number
    yr = mapping_dict[t_id]["year"]  # Year of the tournament
    get_fixture_info(t_id, b_url, e_no, mnth, yr)
