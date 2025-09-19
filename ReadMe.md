# Auto Reply Assistant 🤖

This is a simple Streamlit app that generates polite, professional auto-replies for any incoming message.  
It uses OpenAI's GPT model to analyze the input text and suggest 3 short replies you can directly use.  

### Features
- Automatically generates 3 professional replies ✉️  
- Runs on Streamlit Cloud 🌐  
- Uses OpenAI GPT for smart text generation  

### How to run locally
1. Clone the repo
    
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   
3.Set your OpenAI API key:

    setx OPENAI_API_KEY "your_api_key_here"

4.Run the app:

      streamlit run app.py