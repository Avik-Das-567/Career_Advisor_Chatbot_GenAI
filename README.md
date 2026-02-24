# Career Advisor Chatbot
### Project Structure:

```

career-advisor-genai/
│
├── app.py                     # Streamlit UI entrypoint
├── requirements.txt
│
├── config/
│   └── settings.py            # App-level configuration
│
├── core/
│   ├── gemini_client.py       # Gemini API integration
│   ├── prompt_manager.py      # Prompt engineering layer
│   ├── memory_manager.py      # Multi-turn conversation memory
│   └── response_handler.py    # Post-processing & safety
│
├── utils/
│   ├── logger.py              # Centralized logging
│   └── exceptions.py          # Custom exception handling
│
└── assets/
    └── ui_styles.py           # Streamlit UI styling

```
