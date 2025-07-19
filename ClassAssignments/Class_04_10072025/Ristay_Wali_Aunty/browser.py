from browser_use.llm import ChatGoogle
from browser_use import Agent, BrowserSession
from dotenv import load_dotenv
import asyncio
from agents import function_tool

load_dotenv()

# Connect to your browser (optional)
# If no executable_path provided, uses Playwright/Patchright's built-in Chromium
browser_session = BrowserSession(
    # Path to a specific Chromium-based executable (optional)
    executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',  # Window
    # For Windows: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    # For Linux: '/usr/bin/google-chrome'
    # For Mac: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

    # Use a specific data directory on disk (optional, set to None for incognito)
    user_data_dir='~/.config/browseruse/profiles/default',   # this is the default
    # ... any other BrowserProfile or playwright launch_persistnet_context config...
    # headless=False,
)



# Initialize the LLM
llm = ChatGoogle(model="gemini-2.0-flash")

@function_tool
async def search_browser_for_linkedin_profile():
    """
    Performs a safe public web search to find LinkedIn profile URLs
    based on user-defined criteria (e.g., age, religion, region).
    
    The agent uses a browser-powered language model (LLM) to search
    for publicly visible LinkedIn profile links using web search
    (not scraping LinkedIn directly).

    Parameters:
    - prompt (str): A description of the kind of people to search for 
      (e.g., "Muslim girls minimum age 22 from South Asia").

    Returns:
    - A list of dictionaries with profile name (if found) and profile link:
        [
            {"name": "Name (if inferred)", "link": "https://linkedin.com/in/xyz"},
            ...
        ]

    Notes:
    - This function does **not** access LinkedIn directly or scrape any
      personal data.
    - It relies only on public web search and returns links only.
    - It is intended for use in matchmaking or networking contexts where
      consent and respect for privacy are honored.
    """

    initial_action = [
        {
            'open_tab': {'url': 'https://www.google.com/'}
        }
    ]
    agent = Agent(
        task="Search LinkedIn profile links using browser search based on user prompt. Do NOT scrape LinkedIn directly.",
        llm=llm,
        browser_session=browser_session,
        initial_action=initial_action,
    )
    result = await agent.run()
    return result
    await browser_session.close()


# For direct testing
if __name__ == "__main__":
    asyncio.run(search_browser_for_linkedin_profile())
