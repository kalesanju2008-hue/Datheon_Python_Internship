
"""
Rule-Based Interactive Terminal Assistant / Chatbot

Features:
- Keyword and regular-expression intent matching
- Multiple intents in one message
- FAQ loading from a JSON file, with built-in defaults
- Business-hours and product FAQ responses
- Conversational state and graceful fallback
- Clean exit commands: bye, exit, quit

Run:
    python chatbot.py

Optional FAQ file:
    Keep sample_faq.json in the same folder as this script.
"""

import json
import re
from pathlib import Path
from datetime import datetime

FAQ_FILE = Path(__file__).with_name("sample_faq.json")

DEFAULT_FAQS = [
    {
        "intent": "business_hours",
        "patterns": [
            r"\b(hours?|opening hours?|working hours?|timings?|when.*open|when.*close)\b"
        ],
        "response": (
            "Our business hours are Monday to Friday, 9:00 AM to 6:00 PM. "
            "We are closed on weekends."
        ),
    },
    {
        "intent": "returns",
        "patterns": [
            r"\b(return|returns|refund|refunded|exchange|replace|replacement)\b"
        ],
        "response": (
            "You can request a return or exchange within 7 days of delivery, "
            "provided the item is unused and in its original packaging."
        ),
    },
    {
        "intent": "shipping",
        "patterns": [
            r"\b(ship|shipping|delivery|deliver|dispatch|tracking|track order)\b"
        ],
        "response": (
            "Standard delivery usually takes 3–5 business days. "
            "You can use your order ID on the tracking page to check its status."
        ),
    },
    {
        "intent": "payment",
        "patterns": [
            r"\b(payment|pay|paid|credit card|debit card|upi|cash on delivery|cod)\b"
        ],
        "response": (
            "We accept major credit/debit cards, UPI, and cash on delivery "
            "where available."
        ),
    },
    {
        "intent": "products",
        "patterns": [
            r"\b(product|products|catalog|items|available|availability|features?)\b"
        ],
        "response": (
            "You can browse our product catalogue to see available items, "
            "features, and prices. Tell me the product name if you need details."
        ),
    },
    {
        "intent": "contact",
        "patterns": [
            r"\b(contact|support|customer care|phone number|email|speak to|human|agent)\b"
        ],
        "response": (
            "You can contact customer support at support@example.com "
            "or call 1800-000-000."
        ),
    },
    {
        "intent": "order_status",
        "patterns": [
            r"\b(order status|where is my order|my order|order number|order id)\b"
        ],
        "response": (
            "I can help with order status. Please check the tracking page using "
            "your order ID. This demo chatbot does not access live order records."
        ),
    },
]


def load_faqs():
    """Load FAQ intents from JSON, or use built-in examples if unavailable."""
    if not FAQ_FILE.exists():
        return DEFAULT_FAQS

    try:
        with FAQ_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        # Accept either a list of FAQ objects or {"faqs": [...]}
        faqs = data.get("faqs", []) if isinstance(data, dict) else data
        if not isinstance(faqs, list) or not faqs:
            raise ValueError("FAQ JSON must contain a non-empty list.")

        valid_faqs = []
        for item in faqs:
            if not isinstance(item, dict):
                continue
            patterns = item.get("patterns", [])
            response = item.get("response")
            if isinstance(patterns, list) and patterns and isinstance(response, str):
                valid_faqs.append({
                    "intent": str(item.get("intent", "faq")),
                    "patterns": patterns,
                    "response": response,
                })

        if not valid_faqs:
            raise ValueError("No valid FAQ entries were found.")
        return valid_faqs

    except (json.JSONDecodeError, OSError, ValueError) as error:
        print(f"[Notice] Could not load FAQ file: {error}")
        print("[Notice] Using built-in FAQ responses instead.\n")
        return DEFAULT_FAQS


def normalize_text(message):
    """Normalize input for consistent matching."""
    return re.sub(r"\s+", " ", message.lower().strip())


def find_intents(message, faqs):
    """Return every FAQ intent whose regular expression matches the message."""
    matches = []
    for faq in faqs:
        for pattern in faq["patterns"]:
            try:
                if re.search(pattern, message, flags=re.IGNORECASE):
                    matches.append(faq)
                    break
            except re.error:
                # Ignore a malformed pattern rather than crashing the chatbot.
                continue
    return matches


def is_greeting(message):
    return bool(re.search(r"\b(hi|hello|hey|good morning|good afternoon|good evening)\b", message))


def is_thanks(message):
    return bool(re.search(r"\b(thanks|thank you|thx)\b", message))


def respond(message, faqs):
    """Generate a response; one message may match more than one intent."""
    normalized = normalize_text(message)

    if not normalized:
        return "Please type a question so I can help."

    responses = []

    if is_greeting(normalized):
        responses.append("Hello! Welcome to our support assistant. How can I help you today?")

    matched_faqs = find_intents(normalized, faqs)
    for faq in matched_faqs:
        if faq["response"] not in responses:
            responses.append(faq["response"])

    if is_thanks(normalized):
        responses.append("You're welcome! Is there anything else I can help you with?")

    if responses:
        return "\n".join(responses)

    return (
        "Sorry, I didn't understand that. You can ask about business hours, "
        "products, shipping, returns, payments, orders, or customer support."
    )


def main():
    faqs = load_faqs()

    print("=" * 58)
    print("          RULE-BASED CUSTOMER SUPPORT CHATBOT")
    print("=" * 58)
    print("Bot: Hello! I'm your virtual assistant.")
    print("Bot: Ask me about products, orders, delivery, returns, or hours.")
    print("Bot: Type 'bye', 'exit', or 'quit' to end the chat.")

    while True:
        try:
            user_message = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Have a great day.")
            break

        normalized = normalize_text(user_message)

        if re.fullmatch(r"(bye|goodbye|exit|quit|stop)", normalized):
            print("Bot: Goodbye! Thank you for chatting with us.")
            break

        print("Bot:", respond(user_message, faqs))


if __name__ == "__main__":
    main()
