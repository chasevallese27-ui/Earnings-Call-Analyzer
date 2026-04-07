# Prompt Revisions

## Initial Prompt

**System prompt:**
```
You are a financial analyst assistant. Analyze earnings call transcripts and extract key information. If any metric is not explicitly stated in the transcript, write Not Disclosed rather than estimating.
```

**User prompt:**
```
Analyze the following earnings call transcript and return a structured report with exactly these five sections:

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
```

---

## Revision 1 — Dynamic Output Filename

**Change:** Updated `app.py` to name the output file based on the input transcript filename instead of always saving to `output.txt`.

**Behavior:** The output filename is derived by stripping the `.txt` extension from the input filename and appending `_summary.txt`.

**Example:**
- Input: `nvda_transcript.txt` → Output: `nvda_summary.txt`
- Input: `aapl_transcript.txt` → Output: `aapl_summary.txt`
- Input: `rdi_transcript.txt` → Output: `rdi_summary.txt`

---

## Revision 2 — Interactive Terminal Input

**Change:** Replaced file argument (`python3 app.py transcript.txt`) with interactive terminal prompts. The app no longer accepts a command-line argument.

**New flow:**
1. Prompts `Enter the company name:` — used to name the output file
2. Prompts `Paste your transcript below (press Enter twice when done):` — reads lines until two consecutive blank lines

**Output file:** Named after the company entered (e.g., `NVDA` → `NVDA_summary.txt`)

---

## Revision 3 — Streamlined Full Workflow

**Change:** Consolidated the end-to-end workflow into two terminal commands and one file edit, removing all manual file handling from the command line.

**Workflow:**
1. `touch COMPANYNAME_transcript.txt` — create the transcript file
2. Open the file, paste the transcript, save it
3. `python3 app.py` — prompts for the company name, automatically finds `COMPANYNAME_transcript.txt`, runs the analysis, and saves `COMPANYNAME_summary.txt`

**Why:** The app now owns the file naming convention entirely. The user only needs to know the company ticker — no file paths, no arguments, no manual renaming. The same three steps work repeatably for every new company.

Changes Explanation

Originally the user would use Claude Code to create the blank text file and then copy/paste the earnings report into that and name it. To streamline the process the user would just use the touch command and the company name to create the blank text file and then paste the earnings report text into that file. Then run the python app command to generate the summary (which is already named based on the company. 
