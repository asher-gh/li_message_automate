# LinkedIn message script (:warning: WIP)

Small script using [selenium] to automate sending messages for product feedback.

## Setup

1. You can use system's python installation, however this repo uses [poetry] to
   manage dependencies and manage virtual env. If using poetry, use the
   following to initialise the project

   ```sh
   poetry install
   ```

2. Make sure [chrome] is installed on the system. If getting a driver error,
   also install [chrome-webdriver] on your system.

   On MacOS, if you have [homebrew], you can install [chrome-webdriver] with

   ```sh
   brew install chromedriver
   ```

3. Make sure that your LinkedIn username and password are in the `.env` as

   ```env
   USERNAME=john@gmail.com
   PASSWORD=yourpassword
   ```

4. The profiles have to be in `profiles.csv` with the following schema:
   ```
   ProfileURL
   ```

## Running

To launch the script

```sh
poetry run app
```

[selenium]: https://pypi.org/project/selenium/ "Slenium-PiPy"
[poetry]: "https://python-poetry.org/docs/" "Poetry home"
[chrome]: "https://www.google.com/intl/en_uk/chrome/"
[chrome-webdriver]: "https://sites.google.com/a/chromium.org/chromedriver/"
[homebrew]: "https://brew.sh/"
