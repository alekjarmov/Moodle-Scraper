# Recording links scraper

#### Clone the repo and install the dependencies:

    * git clone
    * pip install -r requirements.txt

The newest version of chrome and chromedriver is required. You can download the latest stable version of chrome driver from [here](https://chromedriver.chromium.org/home).
#### Create a config.yaml file in the root directory with the following content:
```yaml
MoodleCookie:
  name: MoodleSession
  value: 'cookie_value'  # Your MoodleSession value
  domain: 'courses.finki.ukim.mk'

Login:
    username: 'courses_username'  # Your username for courses (index)
    password: 'courses_password' # Your password for courses

chromedriver: 'your_path_here'  # Enter your path to chromedriver here or chromedriver.exe if it is in path

# change to 'auto' if you want to automatically login and have put username and password above
# change to 'cookie' if you want to use your MoodleSession cookie and have put it above
# If the value is left as 'manual' you will have to log in manually and only the chromedriver: needs to be changed 
# the Login and MoodleCookie can be left as is
login_method: 'manual'  # 'auto' or 'cookie' or 'manual'
```
#### Run the script:
    python main.py
