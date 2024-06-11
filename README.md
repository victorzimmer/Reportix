# Reportix
## Project Description
AI-powered web application which helps users write reports. The application uses pre-trained models to generate text live as the user types. The texts which the model generates is directional help to the user.

## Prerequisites
LaTeX needs to be installed on the host system.

For macOS SimpleTex[https://formulae.brew.sh/cask/simpletex#default] or MacTex will do.


## Installation
Clone the repository and navigate to the project directory:
'''console
$ git clone https://github.com/victorzimmer/Reportix
'''

Install necessary packages using pip and npm:
'''console
$ pip install -r requirements.txt
$ npm install
'''

## Usage

### Development
NPM Development Setup (Frontend)
'''console
$ npm run watch
'''

Run using FastAPI Development Mode
'''console
$ fastapi dev main.py
'''


### Production
'''console
NPM Production Setup (Frontend)
$ npm run build
'''

'''console
Run using FastAPI Production Mode
$ fastapi run main.py
'''
