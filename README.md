# Google Translate Quiz Game
The Google Translate Quiz Game was created for Lab 13: Agile Project with GitHub Flow. You can quiz basic terms corresponding to a language you select.


# Installation
1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install our requirements.txt

```bash
pip install -r requirements.txt
```
2. Create a .json file called **galvanic-circle-456503-r4-87f89aed0c2a.json** we emailed you this file.


3. Set the **`GOOGLE_APPLICATION_CREDENTIALS`** environment variable

#### On macOS:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/Users/your-username/lab13-sprint-google-translate-game/galvanic-circle-456503-r4-87f89aed0c2a.json"
```

#### On Windows:
```bash
set GOOGLE_APPLICATION_CREDENTIALS="C:\Users\your-username\lab13-sprint-google-translate-game\galvanic-circle-456503-r4-87f89aed0c2a.json"
```


4. Run the following python command:
```python
python3 main.py
```

# Team
#### Patrick Martus
Created the menu for the user, automated testing, combined the UML diagrams, project management, leader

#### Adam Snowgold
Created the main, hooked up the Google Cloud Translation API, and tests corresponding to both

#### Sanghyeon Jun
Created the grading system, and tests corresponding to the grading system

#### Hunter Martin
Created the quiz, translating each answer choice, list of questions using dictonaries, tests 
