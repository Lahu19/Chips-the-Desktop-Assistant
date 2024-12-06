# Chips AI - Virtual Assistant  

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)  
![Pyttsx3](https://img.shields.io/badge/Library-Pyttsx3-orange.svg)  
![SpeechRecognition](https://img.shields.io/badge/Library-SpeechRecognition-brightgreen.svg)  
![OpenCV](https://img.shields.io/badge/Library-OpenCV-red.svg)  
![PyAutoGUI](https://img.shields.io/badge/Library-PyAutoGUI-lightblue.svg)  

## Overview  
Chips AI is a Python-based virtual assistant designed to execute system commands, interact with online services, and provide conversational AI features. Powered by various Python libraries and Google Generative AI, Chips AI serves as a multipurpose assistant for automating tasks and answering user queries.  

---

## Features  
### System Commands  
- **Open Notepad, Chrome, Command Prompt, Camera**  
- **System Operations**: Shutdown, restart, or sleep the system.  
- **Battery Status**: Checks system battery percentage.  

### Web and Social Media  
- **Open Websites**: YouTube, Google, Facebook, and Stack Overflow.  
- **Search on Google**: Perform a quick Google search based on user queries.  
- **Instagram Integration**: Open profiles and download profile pictures using Instaloader.  

### Tools and Utilities  
- **Take Screenshots**: Save screenshots with custom names.  
- **Tell Jokes**: Provides jokes to lighten your mood.  
- **Switch Windows**: Switch active windows via keyboard shortcuts.  

### Advanced AI  
- **Conversational AI**: Powered by Google's Gemini Generative AI, Chips can process natural language queries and generate responses.  

---

## Prerequisites  
Ensure you have the following installed:  
1. Python 3.9 or later.  
2. Required Python libraries:  
   ```bash
   pip install pyttsx3 SpeechRecognition opencv-python requests pyjokes pyautogui instaloader psutil google-generativeai
   ```  

3. **Google Generative AI Key**:  
   - Sign up for access to the Gemini API.  
   - Save the API key as `Gemini_API_KEY` in an `api.py` file.

---

## Installation and Setup  

1. Clone the repository:  
   ```bash
   git clone <repository_url>
   cd ChipsAI
   ```

2. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Run the script:  
   ```bash
   python chips_ai.py
   ```  

---

## Usage  

1. **Start the Assistant**:  
   The assistant welcomes you and listens for commands.  

2. **Command Examples**:  
   - "Open Notepad"  
   - "What's my IP address?"  
   - "Tell me a joke"  
   - "Search Python tutorials on Google"  

3. **Exit the Assistant**:  
   Say "exit" or "stop" to terminate the program.  

---

## Built With  

- **Pyttsx3**: Text-to-speech conversion.  
- **SpeechRecognition**: Audio input recognition.  
- **OpenCV**: Accessing the webcam.  
- **PyAutoGUI**: Automating GUI operations.  
- **Instaloader**: Instagram profile handling.  
- **Google Generative AI**: Conversational AI.  

---

## Contributions  
Feel free to fork the project, create pull requests, or report issues.  

---

## Acknowledgments  
Special thanks to the developers of Python libraries and APIs used in this project.  

Happy coding! 🎉
