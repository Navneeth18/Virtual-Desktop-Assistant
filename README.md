# Virtual Desktop Assistant

This Python-based Virtual Desktop Assistant is designed to automate routine desktop tasks, enable efficient web interactions, and enhance productivity through voice commands. The assistant can handle application control, web searches, messaging automation, and more.

---

## Features

### 1. Voice Recognition
- Converts voice commands into actions using speech recognition.

### 2. Personalized Greetings
- Greets the user based on the time of day with a friendly message.

### 3. Web Automation
- **Google Search**: Searches queries and provides summarized results.
- **YouTube Search and Play**: Opens YouTube, searches for content, and plays videos.
- **Website Access**: Opens any website specified by the user.

### 4. Desktop Control
- **Application Launch**: Opens specified desktop applications.
- **Application Closure**: Closes applications or tabs.
- **Screenshot Capture**: Captures screenshots and saves them in the project directory.
- **Video Controls**: Controls media playback like play, pause, mute, and full screen.

### 5. Messaging Automation
- Sends instant WhatsApp messages using voice commands and automates the process via pywhatkit.

### 6. Temperature Information
- Provides the current temperature for a specified city.

### 7. System Commands
- Commands to open file explorer, calculator, task manager, etc.

### 8. Custom Commands
- Interacts with user-specified websites or portals, such as a college student portal.

---

## Modules and Files

### 1. **main.py**
- Handles the primary logic for voice recognition and response.
- Key Functions:
  - `speak(text)`: Outputs text as speech.
  - `takeCommand()`: Captures voice commands.
  - `playInitializeSound()`: Plays an audio file on activation.
  - Command handling for tasks like searching, opening/closing apps, and more.

### 2. **DictApp.py**
- Contains logic for application and website control.
- Key Functions:
  - `openAppWeb(query)`: Launches applications or websites based on user commands.
  - `closeappweb(query)`: Closes applications or tabs.

### 3. **GreetMe.py**
- Provides personalized greetings.
- Key Function:
  - `greetMe()`: Greets the user based on the current time.

### 4. **SearchNow.py**
- Manages search functionality for Google and YouTube.
- Key Functions:
  - `searchGoogle(query)`: Searches on Google and provides a summary.
  - `searchYoutube(query)`: Opens YouTube and plays videos.

### 5. **WhatsApp.py**
- Automates sending WhatsApp messages.
- Key Function:
  - `send_whatsapp_message()`: Sends WhatsApp messages using pywhatkit.

---

## Installation and Setup
Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
Run the assistant:
  ```bash
  python main.py
  ```


### Prerequisites
- Python 3.7 or above installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Navneeth18/Virtual-Desktop-Assistant.git
   ```
2. Install dependencies:
   ```bash
    pip install -r requirements.txt
    ```
3. Run the assistant:
   ```bash
  python main.py
  ```

