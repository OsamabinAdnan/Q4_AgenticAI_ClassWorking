from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, set_tracing_disabled


load_dotenv()

set_tracing_disabled=True,

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not set in .env file")

external_provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_provider,
)

config= RunConfig(
    model=model,
    model_provider=external_provider,
    tracing_disabled=True
)

webDevelopment_agent = Agent(
    name="Web Development Agent",
    instructions="""You are responsible for building responsive, accessible, and high-performance websites using modern frameworks like Next.js, Vue 3, or SvelteKit. Use Tailwind CSS or CSS Modules for styling with mobile-first, flex/grid-based layouts. Optimize performance via lazy loading, code splitting, and minimal dependencies. Ensure semantic HTML, accessibility (WCAG), and test with Lighthouse and Playwright. Output clean, modular code with proper project structure and documentation.""",
    model= model,
    handoff_description="handoff to web development agent if the task is related to web development",
)

mobileAppDev_agent = Agent(
    name="Mobile App Development Agent",
    instructions="""You are responsible for building high-performance, responsive, and user-friendly mobile apps using modern frameworks like React Native or Flutter. Ensure cross-platform compatibility, smooth UI/UX, and accessibility. Optimize app performance, use modular architecture, and follow platform-specific guidelines.    Test thoroughly on Android and iOS, and output clean, maintainable code with clear documentation.""",
    model=model,
    handoff_description="handoff to mobile app development agent if the task is related to mobile app development",
)

marketing_Agent = Agent(
    name="Marketing Agent",
    instructions="""You are a Marketing Agent responsible for creating and optimizing digital marketing strategies.Your tasks include generating persuasive ad copy, email campaigns, social media posts, and SEO-optimized content.Focus on engaging the target audience, increasing conversions, and maintaining brand consistency. Use data-driven insights and A/B testing to refine messaging and maximize ROI. Deliver clear, compelling, and action-oriented marketing content suitable for various platforms.""",
    model=model,
    handoff_description="handoff to marketing agent if the task is related to marketing",
)

async def myAgent(user_input):
    manager = Agent(
        name="Manager Agent",
        instructions= """ You are the Manager Agent responsible for coordinating and delegating tasks to specialized agents, including Web Development, Mobile App Development, and Marketing agents. Analyze the task or request,identify which agent is best suited for the job, and assign it accordingly. Ensure smooth communication      between agents, handle task dependencies, and maintain high-level oversight of progress and quality. Your goal is to ensure efficient workflow, clear task ownership, and successful project execution.
        """,
        model=model,
        handoffs=[webDevelopment_agent, mobileAppDev_agent, marketing_Agent],
    )

    response = await Runner.run(
        manager,
        user_input,
        run_config=config,
    )

    return response.final_output
