# Personal AI Assistant (Gemini API + OOP + Streamlit)
# video link: https://drive.google.com/file/d/1gJeYeUS5ViFFRr1NG8AlySOyTyqOKlth/view?usp=sharing
## 🎯 Objective

The objective of this project is to design and develop a **Personal AI Assistant** that:

- Answers general user questions  
- Helps with learning and productivity  
- Acts as a tutor, coding assistant, and career mentor  
- Maintains conversation memory  
- Follows clean and modular **OOP architecture**  

---

## 🛠 Tech Stack

- **Python** 3.10+  
- **Streamlit**  
- **Google Gemini API**  
- **python-dotenv**  
- **Object-Oriented Programming (OOP)**  

---

## 🧠 OOP Concepts Used

- ✅ Classes & Objects  
- ✅ Encapsulation  
- ✅ Inheritance  
- ✅ Modular Coding  

---

## 🤖 JARVIS Core Capabilities

- Greet the user like a personal assistant  
- Answer general questions using Gemini AI  
- Act as:
  - 📘 Tutor  
  - 💻 Coding Assistant  
  - 🎓 Career Mentor  
- Maintain conversation history using a **JSON file**  
- Follow system-level instructions  
- Handle errors gracefully  

---

## 📁 Project Structure

```bash
jarvis_assistant/
│
├── app.py                     # Streamlit UI
│
├── jarvis/
│   ├── assistant.py           # JARVIS main controller
│   ├── gemini_engine.py       # Gemini API handler
│   ├── prompt_controller.py   # Prompt & system behavior
│   └── memory.py              # Conversation memory (JSON)
│
├── config/
│   └── settings.py            # Environment & configuration
│
├── .env                       # API key (ignored in GitHub)
├── requirements.txt
└── README.md




```

## Clone the repository
```bash


# Clone the repository
git clone https://github.com/mkador/Assignment-05.git

# Navigate to the project directory
cd Persomal-AI-Assistant

# Install required dependencies
pip install -r requirements.txt

# Add your Gemini API key in .env file
GEMINI_API_KEY=your_api_key_here

# Run the Streamlit app
streamlit run app.py




