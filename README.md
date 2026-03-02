# Audio Grammar Checker

## Overview
Ever wondered how to check the grammar of spoken English? This project lets you do just that! The **Audio Grammar Checker** takes in a `.wav` audio file, transcribes it into text using **OpenAI Whisper**, and evaluates the grammar using **LanguageTool**. It then gives a **grammar score** (0–10) and highlights the first few grammar issues, helping you quickly see where improvements can be made.

We’ve also added a **Gradio interface**, so you can easily upload audio files and see results instantly—no coding required.

---

## Features
- **Speech-to-Text Transcription:** Converts spoken English into text using Whisper.  
- **Grammar Scoring:** Detects grammatical mistakes and provides a score out of 10.  
- **Sample Issues:** Shows the first 5 important grammar issues detected in the text.  
- **Interactive Interface:** Gradio makes it easy to test without installing anything.

---

## Technologies Used
- **Python 3.8+**  
- **OpenAI Whisper** – Speech-to-text transcription  
- **LanguageTool** – Grammar checking engine  
- **Gradio** – Simple web interface for testing  

---

## How to Run Locally
1. Clone this repository:

```bash
git clone https://github.com/rahiankita18/Audio-Grammar-Checker.git
cd Audio-Grammar-Checker
