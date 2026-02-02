# Gemma 3 Text Generation App (Streamlit)

## Summary

This project is a Streamlit web application that uses the Gemma 3 (270M IT) large language model from Hugging Face to generate text from user prompts.

The app demonstrates how to:

* Load a transformer-based language model

* Generate text with controllable parameters (temperature, top-k, top-p)

* Build an interactive UI using Streamlit

It’s designed as a simple playground for experimenting with prompt-based text generation.

## Project Files

The repository contains:

1. `main.py` – A Streamlit application that loads the Gemma 3 model and generates text from predefined prompts using sampling-based generation.

2. `GPT AI ESSAY.pdf` - 

3. `gpt_text_generation.ipynb`


## Features

* Uses google/gemma-3-270m-it from Hugging Face

* Generates creative text responses from prompts

* Adjustable generation behavior using:

* Temperature

* Top-k sampling

* Top-p (nucleus) sampling

* Interactive UI built with Streamlit

* Session state used to cache generated results


## Tools Used
* Python 3.x

* Streamlit

* Transformers (Hugging Face)

* PyTorch


## How to Run the App

### 1. Clone the repository
> Download the project folder and open a terminal in the root directory.

### 2. Create and activate virtual environment
```
     # On Windows
    python -m venv venv
    venv\Scripts\activate
    
     # On Mac/Linux
    python3 -m venv .venv
    source .venv/bin/activate
```

### 3. Install required libraries
```
    pip install streamlit transformers torch
```

### 4. Run the Streamlit app
```
    streamlit run main.py
```

## How It Works

1. Model Loading

    * Loads `google/gemma-3-270m-it` using `AutoTokenizer` and `AutoModelForCausalLM`

2. Text Generation

    * Tokenizes the input prompt

    * Uses sampling (temperature, top_k, top_p) for creative generation

    * Decodes the model output into readable text

3. User Interface

    * Displays preset prompts

    * Generates and shows model responses in text areas

    * Uses Streamlit session state to persist results