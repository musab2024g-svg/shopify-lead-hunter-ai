from gemini_test import ask_gemini


def find_store(niche="shopify"):

    prompt = f"""
Find ONE REAL Shopify store in the niche: {niche}

Rules:

- Return a REAL store URL
- Do NOT use example.com
- Do NOT invent stores
- Do NOT explain anything outside the format

Format:

Store:
https://store-url.com

Reason:
Short reason

Issues:
- issue 1
- issue 2
- issue 3
"""

    try:
        result = ask_gemini(prompt)

        if not result:
            return "❌ Gemini returned empty response"

        return result

    except Exception as e:
        return f"❌ Gemini Error:\n{str(e)}"
