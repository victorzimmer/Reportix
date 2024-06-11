# Reportix
## Project Description
AI-powered web application which helps users write reports. The application uses pre-trained models to generate text live as the user types. The texts which the model generates is directional help to the user.

## Prerequisites
LaTeX needs to be installed on the host system.

For macOS [SimpleTex](https://formulae.brew.sh/cask/simpletex#default) or MacTex will do.


## Installation
Clone the repository and navigate to the project directory:
```console
$ git clone https://github.com/victorzimmer/Reportix
```

Install necessary packages using pip and npm:
```console
$ pip install -r requirements.txt
$ npm install
```

## Running Ollama
If Ollama is not already installed it can be found [here](https://ollama.com)
Ollama needs to be running for Reportix to work.

## Pulling models
Models need to be available in Ollama and we reccommend pulling them before using Reportix.
```console
$ ollama pull modelName
```

We reccommend using llama3, but llama2, phi3, phi, and llava have also been found to work well.
Feel free to try more models from the Ollama [list of available models](https://ollama.com/library).


## Usage

### Development
NPM Development Setup (Frontend)
```console
$ npm run watch
```

Run using FastAPI Development Mode
```console
$ fastapi dev main.py
```


### Production
```console
NPM Production Setup (Frontend)
$ npm run build
```

```console
Run using FastAPI Production Mode
$ fastapi run main.py
```
