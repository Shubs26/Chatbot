# Ecogrm GG Personal Chatbot

A lightweight personal chatbot for your product **Ecogrm GG**.

## What this project includes

- `chatbot.py`: CLI chatbot engine (no external dependencies).
- `ecogrm_gg_profile.json`: your editable product profile + FAQ knowledge base.

## Run the chatbot

```bash
python3 chatbot.py
```

Type `exit` to stop.

## Customize it for Ecogrm GG

Edit `ecogrm_gg_profile.json`:

- `name`: bot display name.
- `fallback`: response when no FAQ match is found.
- `faq`: list of `q`/`a` pairs used to answer user questions.

## Example conversation

```text
Ecogrm GG Assistant: Hi! I'm your personal chatbot for Ecogrm GG.
You: what is ecogrm gg
Ecogrm GG Assistant: Ecogrm GG is your product assistant and support channel for customers.
```
