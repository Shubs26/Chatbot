#!/usr/bin/env python3
"""Ecogrm GG personal chatbot (CLI).

A lightweight, dependency-free chatbot that answers common questions about
Ecogrm GG and can be extended by editing `ecogrm_gg_profile.json`.
"""

from __future__ import annotations

import json
from difflib import SequenceMatcher
from pathlib import Path

PROFILE_PATH = Path(__file__).with_name("ecogrm_gg_profile.json")
EXIT_WORDS = {"exit", "quit", "bye"}


DEFAULT_PROFILE = {
    "name": "Ecogrm GG Assistant",
    "tone": "friendly, concise, and product-focused",
    "fallback": (
        "I can help with Ecogrm GG product details, features, pricing, and setup. "
        "Could you share a bit more context so I can give a precise answer?"
    ),
    "faq": [
        {
            "q": "what is ecogrm gg",
            "a": "Ecogrm GG is your product assistant and support channel for customers.",
        },
        {
            "q": "who is this chatbot for",
            "a": "This chatbot is designed for Ecogrm GG users, prospects, and support needs.",
        },
        {
            "q": "how do i contact support",
            "a": "Add your real support email/URL in ecogrm_gg_profile.json so I can share it here.",
        },
        {
            "q": "what are your key features",
            "a": "Add your product feature list in ecogrm_gg_profile.json for accurate answers.",
        },
    ],
}


def load_profile() -> dict:
    if not PROFILE_PATH.exists():
        PROFILE_PATH.write_text(json.dumps(DEFAULT_PROFILE, indent=2), encoding="utf-8")
        return DEFAULT_PROFILE

    with PROFILE_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if "faq" not in data or not isinstance(data["faq"], list):
        data["faq"] = DEFAULT_PROFILE["faq"]
    if "fallback" not in data:
        data["fallback"] = DEFAULT_PROFILE["fallback"]
    if "name" not in data:
        data["name"] = DEFAULT_PROFILE["name"]
    return data


def normalize(text: str) -> str:
    return " ".join(text.lower().strip().split())


def best_answer(user_message: str, faq: list[dict], threshold: float = 0.60) -> str | None:
    message = normalize(user_message)
    best_score = 0.0
    answer = None

    for item in faq:
        q = normalize(item.get("q", ""))
        if not q:
            continue
        score = SequenceMatcher(None, message, q).ratio()
        if q in message:
            score = max(score, 0.90)
        if score > best_score:
            best_score = score
            answer = item.get("a")

    if best_score >= threshold:
        return answer
    return None


def run_chat() -> None:
    profile = load_profile()
    bot_name = profile.get("name", "Ecogrm GG Assistant")

    print(f"{bot_name}: Hi! I'm your personal chatbot for Ecogrm GG.")
    print("Type your question, or 'exit' to stop.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        if normalize(user_input) in EXIT_WORDS:
            print(f"{bot_name}: Thanks for chatting. See you soon!")
            break

        answer = best_answer(user_input, profile.get("faq", []))
        if answer:
            print(f"{bot_name}: {answer}")
        else:
            print(f"{bot_name}: {profile.get('fallback', DEFAULT_PROFILE['fallback'])}")


if __name__ == "__main__":
    run_chat()
