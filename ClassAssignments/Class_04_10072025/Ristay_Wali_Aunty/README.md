# Rishta Wali Aunty - AI Matchmaking Assistant

An AI-powered matchmaking assistant that helps users find potential marriage matches through public LinkedIn profiles while maintaining privacy and respect.

## 🌟 Features

- Interactive chat-based interface using Chainlit
- Natural conversational flow with a friendly "Aunty" persona
- Safe and privacy-respecting LinkedIn profile search
- WhatsApp integration for sending match recommendations
- Powered by Google's Gemini AI model

## 🛠️ Technical Components

### Main Components:
1. **Chainlit Chat Interface** (`main.py`)
   - Handles user interactions
   - Manages chat history
   - Integrates with the AI agent system

2. **WhatsApp Integration** (`whatsapp.py`)
   - Uses Ultramsg API for WhatsApp messaging
   - Sends match recommendations to users

3. **Browser Search** (`browser.py`)
   - Implements safe LinkedIn profile search
   - Uses browser automation with Playwright
   - Respects privacy by only accessing public information

## 🔧 Prerequisites

- Python 3.x
- Google Chrome browser installed
- Ultramsg API account
- Google API key (for Gemini AI)

## ⚙️ Environment Variables

Create a `.env` file with the following variables:

```env
GOOGLE_API_KEY=your_gemini_api_key
Ultramsg_InstanceID=your_ultramsg_instance_id
Ultramsg_Token=your_ultramsg_token
```

## 📦 Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Application

1. Start the Chainlit application:
   ```bash
   chainlit run main.py
   ```
2. Open the provided URL in your browser
3. Start interacting with the Rishta Wali Aunty!

## 💬 How It Works

1. **Initial Interaction**
   - The aunty greets users in a friendly manner
   - Collects preferences for potential matches

2. **Profile Search**
   - Uses browser automation to search for matching LinkedIn profiles
   - Only accesses publicly available information
   - Returns relevant profile links

3. **Match Delivery**
   - Collects user's WhatsApp number
   - Sends curated matches via WhatsApp

## 🔒 Privacy & Ethics

- Only uses publicly available information
- Does not scrape or store personal data
- Respects user privacy and consent
- Maintains professional and respectful communication

## ⚠️ Important Notes

- The application requires a stable internet connection
- Chrome browser must be installed for profile searches
- WhatsApp functionality requires valid Ultramsg credentials
- Always use the tool responsibly and ethically

## 📝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
