# Durand Cup Scraping 
![alt text](https://github.com/Stat-Peekers/scrape-durand-cup/blob/main/logo.png "Durand Cup")

This repo is to scrape **Durand Cup** match data from official sources

Pre-requisites:
1. **Clone repository**
    1. Clone this repo in your local system -> [How to?](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
2. **Work in a conda / python environment**\
   (Proceed to Step 3 if you don't want to work in an environment)
    1. _Preferred_ -> Create a new python environment
    2. Docs for creating and activating environment in conda -> [How to?](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)
    3. Activate the environment -> [How to?](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment)
3. **Installing required libraries**
    1. Using Anaconda prompt / terminal
        1. Open Anaconda prompt / terminal
        2. Go to local folder where cloned/downloaded repository
        4. Run this code `pip install -r requirements.txt`\
4. **Driver for chrome**
    1. Check browser version
        1. Open Chrome
            1. In the chrome address bar enter -> chrome://settings/help
            2. OR Open Chrome Click `⋮` -> Help -> About Google Chrome
        2. Download driver
            1. [Download from here](https://chromedriver.chromium.org/downloads)
            2. Choose the one that matches your current version as obtained in step `i`
            3. A zip file will be downloaded. Extract the file inside it into the cloned local folder.\

       NOTE: If you use any other browser than chrome, kindly go through [this](https://selenium-python.readthedocs.io/installation.html#drivers) and you will also have to change the code accordingly. I will be doing this in future updates

To get the data:
1. Data for one match:
    1. Find specific match ID from `config/fixture_info.json`
       (for info on tournament `id` check `config/tour_info.json`)
    2. Run file: `main.py`
    3. Select option `1` and desired tournament and season.
    4. Enter the match ID required for data from the desired match as obtained in Step `i`
2. Data for a tournament in a particular season:
   1. Run file: `main.py`
   2. Select option `2` Select desired tournament and season
   3. Sit back and let the code do the work for you :smiley:
    ```
    NOTE: All data files will be stored under a local folder in this format
    data/<tour name>/match_json_files/<match_id>.json
    ```

Reach me [here](https://twitter.com/StatPeekers) for any kind of help :)
