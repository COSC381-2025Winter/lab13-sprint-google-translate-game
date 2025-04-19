# Google Translate Quiz Game
The Google Translate Quiz Game was created for Lab 13: Agile Project with GitHub Flow. You can quiz basic terms corresponding to a language you select.


# Installation
1. Set up a virtual environment
```bash
    python3 -m venv .venv
	source .venv/bin/activate
```
2. Create a .json file called **galvanic-circle-456503-r4-87f89aed0c2a.json** we emailed you this file.


3. Set the **`GOOGLE_APPLICATION_CREDENTIALS`** environment variable

#### On macOS:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="Absolute_Path_to_File"
```

#### On Windows:
```bash
set GOOGLE_APPLICATION_CREDENTIALS="C:\Users\your-username\lab13-sprint-google-translate-game\galvanic-circle-456503-r4-87f89aed0c2a.json"
```


4. install package from TestPyPi:
```bash
pip install --index-url https://test.pypi.org/simple/ \
            --extra-index-url https://pypi.org/simple \
            COSC381-WINTER25-TRANSLATION-GAME --upgrade
```
5. run the file by running:
...bash
python -m translate_game.main
...

# Team
#### Patrick Martus
Created the menu for the user, automated testing, combined the UML diagrams, project management, leader

#### Adam Snowgold
Created the main, hooked up the Google Cloud Translation API, and tests corresponding to both

#### Sanghyeon Jun
Created the grading system, and tests corresponding to the grading system

#### Hunter Martin
Created the quiz, translating each answer choice, list of questions using dictonaries, tests 
