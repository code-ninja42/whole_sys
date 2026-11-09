import os
import re
import requests
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY"),
)


@tool
def get_furniture_data(query: str) -> str:
    """Search furniture from API by product name, category, or price. Use queries like 'table', 'sofa', '720', or 'cheapest'."""
    
    url = "https://6a0eaa2f1736097c360a40fc.mockapi.io/furnitureapi"
    
    response = requests.get(url)
    data = response.json()

    query = query.strip().lower()
    
    stop_words = {
        "price",
        "cost",
        "the",
        "a",
        "an",
        "of",
        "what",
        "is",
        "how",
        "much",
        "show",
        "find",
        "get"
    }

    tokens = [word for word in query.split() if word not in stop_words]

    if not tokens and query:
        tokens = query.split()

    result = []

    for item in data:

        searchable = " ".join(
            str(item.get(field, ""))
            for field in (
                "productname",
                "producttitle",
                "productdescription",
                "category",
                "productprice",
            )
        ).lower()

        if not tokens or all(
            re.search(rf"\b{re.escape(token)}\b", searchable)
            for token in tokens
        ):
            result.append(item)

    if "cheapest" in query:
        result.sort(
            key=lambda x: float(
                str(x.get("productprice", "0")).replace(",", "") or 0
            )
        )

    summary = []

    for item in result[:5]:

        summary.append(
            {
                "name": item.get("productname"),
                "title": item.get("producttitle"),
                "price": item.get("productprice"),
                "category": item.get("category"),
            }
        )

    if not summary:
        return "No products found for that query."

    return str(summary)


agent = create_agent(
    llm,
    tools=[get_furniture_data],
    system_prompt=(
        "You are a helpful furniture shopping assistant. "
        "Always use get_furniture_data to look up real product info before answering about prices or availability."
    ),
    debug=False,
)

while True:

    user_input = input("You: ")

    if user_input == "exit":
        break

    result = agent.invoke({"messages": [HumanMessage(user_input)]})

    last_message = result["messages"][-1]

    content = last_message.content

    if isinstance(content, list):

        text_parts = [
            block.get("text", "")
            for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        ]

        content = "\n".join(part for part in text_parts if part) or str(content)

    print("Bot:", content)