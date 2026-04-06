import sys
import anthropic

SYSTEM_PROMPT = (
    "You are a financial analyst assistant. Analyze earnings call transcripts and extract "
    "key information. If any metric is not explicitly stated in the transcript, write "
    "Not Disclosed rather than estimating."
)

USER_PROMPT_TEMPLATE = """Analyze the following earnings call transcript and return a structured report with exactly these five sections:

1. KEY FINANCIAL METRICS
   - Revenue (with YoY comparison if available)
   - EPS (with YoY comparison if available)
   - Gross Margin (with YoY comparison if available)

2. FORWARD GUIDANCE
   Summarize any forward-looking targets or outlook provided by management.

3. MANAGEMENT SENTIMENT
   Assess the overall tone of management commentary (e.g., bullish, cautious, defensive, mixed) and briefly explain why.

4. KEY RISKS
   List the key risks and concerns raised during the call, as bullet points.

5. EXECUTIVE SUMMARY
   Write exactly 3 sentences summarizing the most important takeaways from this earnings call.

---

TRANSCRIPT:
{transcript}
"""

SECTION_DIVIDER = "-" * 60


def main():
    if len(sys.argv) != 2:
        print("Usage: python app.py <transcript.txt>")
        sys.exit(1)

    transcript_path = sys.argv[1]

    try:
        with open(transcript_path, "r", encoding="utf-8") as f:
            transcript = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {transcript_path}")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

    print(f"Analyzing transcript: {transcript_path}")
    print(SECTION_DIVIDER)

    with client.messages.stream(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": USER_PROMPT_TEMPLATE.format(transcript=transcript),
            }
        ],
    ) as stream:
        output = stream.get_final_message()

    result_text = next(
        block.text for block in output.content if block.type == "text"
    )

    print(result_text)
    print(SECTION_DIVIDER)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(f"Source: {transcript_path}\n")
        f.write(SECTION_DIVIDER + "\n")
        f.write(result_text)
        f.write("\n")

    print(f"Output saved to output.txt")


if __name__ == "__main__":
    main()
