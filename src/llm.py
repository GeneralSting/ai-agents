"""Shared LLM client for all lessons.

Every lesson gets its client and model from here, so the provider (Gemini,
Groq, Ollama, Claude) is switched only in the .env file, without touching code.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

# Loads variables from .env into os.environ (like the dotenv package in Node).
# Runs once, on the first import of this module.
load_dotenv()


def _require_env(name: str) -> str:
    """Return a variable from .env, or fail with a clear error if it is missing."""
    value = os.getenv(name)
    if not value:
        # Better to fail early with a clear message than later with a vague SDK error.
        raise RuntimeError(f"{name} is missing from .env. See .env.example.")
    return value


def get_client() -> OpenAI:
    """Create an OpenAI client pointed at the provider configured in .env."""
    # base_url is the trick: the same SDK talks to any OpenAI-compatible API.
    return OpenAI(
        base_url=_require_env("LLM_BASE_URL"),
        api_key=_require_env("LLM_API_KEY"),
    )


def get_model() -> str:
    """Model name from .env (every provider has its own model names)."""
    return _require_env("LLM_MODEL")


def get_provider() -> str:
    """Provider name from .env, only for printing so we know who we are talking to."""
    return _require_env("LLM_PROVIDER")
