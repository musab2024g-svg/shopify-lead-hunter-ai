from gemini_test import ask_gemini


def find_store(niche="shopify"):

    prompt = f"""
You are an ecommerce lead finder.

Niche: {niche}

Generate ONE ecommerce store opportunity.

Return exactly in this format:

Store:
https://example.com

Reason:
Short reason

Issues:
- issue 1
- issue 2
- issue 3
"""

    result = ask_gemini(prompt)

    return result
