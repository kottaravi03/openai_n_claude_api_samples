from dotenv import load_dotenv
import os
import cld


load_dotenv()


def print_api_keys():
    print(
        "Anthropic key loaded:",
        bool(os.getenv("ANTHROPIC_API_KEY"))
    )


if __name__ == "__main__":
    print_api_keys()

    cld.interact_with_model()

    # cld.ask_claude_to_do_something()