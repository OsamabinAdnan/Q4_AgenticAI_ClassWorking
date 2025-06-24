# Weather Assistant Agent

A conversational AI chatbot built with Chainlit and Gemini AI that provides weather information for cities.

## Features

- Interactive chat interface using Chainlit
- Weather information retrieval for any city
- Conversational memory to maintain context
- Powered by Google's Gemini AI model

## Prerequisites

- Python 3.x
- Google Gemini API key
- Required Python packages (see Installation section)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd chainlit_agent
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install chainlit python-dotenv
```

4. Create a `.env` file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

1. Start the chatbot:
```bash
chainlit run main.py
```

2. Open your web browser and navigate to `http://localhost:8000`

3. Start chatting with the Weather Assistant! You can ask questions like:
   - "What's the weather like in London?"
   - "Tell me the weather in Tokyo"
   - "How's the weather in New York?"

## Project Structure

- `main.py`: Main application file containing the chatbot logic
- `.env`: Environment variables file (create this with your API key)
- `README.md`: Project documentation
- `chainlit.md`: Chainlit configuration file

## Current Implementation Notes

- The weather information is currently implemented as a placeholder that returns dummy data
- To get real weather data, you would need to integrate with a weather API service

## Future Improvements

1. Integrate with a real weather API service
2. Add support for temperature unit conversion
3. Include more weather details like humidity, wind speed, etc.
4. Add error handling for invalid city names
5. Implement weather forecasts

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgments

- Built with [Chainlit](https://github.com/Chainlit/chainlit)
- Powered by Google's Gemini AI
