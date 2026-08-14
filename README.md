# 🤖 HeyDeep – Voice Assistant

HeyDeep is a simple **Python-based Voice Assistant** that can listen to voice commands and perform basic tasks such as opening Google, opening YouTube, telling the current time, and greeting the user.

## ✨ Features

* 🎤 Voice command recognition
* 🔊 Text-to-speech response
* 👋 Greeting based on time
* 🕐 Current time
* 🌐 Open Google
* ▶️ Open YouTube
* 👋 Exit using "exit" or "bye"

## 🛠️ Technologies Used

* Python
* `pyttsx3`
* `SpeechRecognition`
* `datetime`
* `webbrowser`

## 📦 Installation

Install the required Python libraries:

```bash
pip install pyttsx3 SpeechRecognition
```

For microphone support, install PyAudio if required:

```bash
pip install PyAudio
```

## 🚀 How to Run

1. Clone this repository:

```bash
git clone https://github.com/pardeep7070/jarvis-.git
```

2. Open the project folder:

```bash
cd heydeep-voice-assistant
```

3. Run the Python file:

```bash
python heydeep.py
```

4. Speak commands after seeing:

```text
Listening...
```

## 🎙️ Available Commands

| Command   | Action                 |
| --------- | ---------------------- |
| `Hello`   | Gives a greeting       |
| `Time`    | Tells the current time |
| `Google`  | Opens Google           |
| `YouTube` | Opens YouTube          |
| `Exit`    | Stops the assistant    |
| `Bye`     | Stops the assistant    |

## 📁 Project Structure

```text
HeyDeep/
│
├── heydeep.py
└── README.md
```

## 💻 Example

```text
Listening...
Recognizing...
You: hello

heydeep: Hello, how are you?
```

Another example:

```text
You: time

heydeep: Current time is 02:15 PM
```

## 🔮 Future Improvements

* Add Hindi voice commands
* Open applications using voice
* Search Google by voice
* Play music
* Weather information
* Send messages
* Set alarms and reminders
* AI chatbot integration
* Wake-word support such as "Hey Deep"

## 👨‍💻 Author

**Pardeep Kumar**

B.Tech CSE (AI & ML)

---

⭐ If you like this project, consider giving the repository a **Star**!
