import os
from dotenv import load_dotenv
import openai
from .models import FlightManifest
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
model_name = os.getenv("LLM_MODEL")
client = openai.OpenAI(base_url="https://openrouter.ai/api/v1",api_key=api_key)

def run_ai_agent(user_prompt):
    manifests = FlightManifest.objects.all()
    print(manifests)
    manifest_context = "\n".join(
        f"Flight ID {manifest.pk}: {manifest.flight.origin} to "
        f"{manifest.flight.destination}; duration {manifest.flight.duration} minutes; "
        f"manifest notes: {manifest.notes}"
        for manifest in manifests
    ) or "No flight manifests are currently stored."

    response=client.chat.completions.create(
        model = model_name,
        messages=[
        {
                "role": "system",
                "content": (
                    "You are a flight assistant. Answer using only the flight manifest data below. "
                    "Match the flight by its ID, route, or details. If there is no matching manifest, "
                    "say you could not find one; do not invent notes.\n\n"
                    f"{manifest_context}"
                )
            },
        {"role":"user", "content":user_prompt}
],
    )
    return response.choices[0].message.content