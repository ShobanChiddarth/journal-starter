
# TODO: Import your chosen LLM SDK
from datetime import datetime, UTC

from openai import OpenAI
# import anthropic
# import boto3
# from google.cloud import aiplatform
async def get_response(string) -> str:
    client = OpenAI()
    response = client.responses.create(
        model="openai.gpt-oss-120b",
        input=string
    )
    return response.output[0].content[0].text

async def analyze_journal_entry(entry_id: str, entry_text: str) -> dict:
    """
    Analyze a journal entry using your chosen LLM API.

    Args:
        entry_id: The ID of the journal entry being analyzed
        entry_text: The combined text of the journal entry (work + struggle + intention)

    Returns:
        dict with keys:
            - entry_id: ID of the analyzed entry
            - sentiment: "positive" | "negative" | "neutral"
            - summary: 2 sentence summary of the entry
            - topics: list of 2-4 key topics mentioned
            - created_at: timestamp when the analysis was created

    TODO: Implement this function using your chosen LLM provider.
    See the Learn to Cloud curriculum for guidance on:
    - Setting up your LLM API client
    - Crafting effective prompts
    - Handling structured JSON output
    """

    result_d = {}
    result_d["entry_id"]=entry_id
    result_d["sentiment"] = await get_response("Answer in one word without explanation. Give me the sentiment (positive/negative/neutral) of this entry in journal: "+entry_text)
    result_d["summary"] = await get_response("Give me summary without explanation. Give me 2 sentence summary of this entry: "+entry_text)
    result_d["topics"] = await get_response("Give me topics without explanation. List 2-4 key topics mentioned in this entry: "+entry_text)
    result_d["created_at"] = datetime.now(UTC).strftime("%Y-%m-%d.%H:%M:%S")

    return result_d