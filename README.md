# Earnings Call Analyzer

A Python tool that uses an LLM to automatically summarize earnings call transcripts into structured, analyst-ready reports.

## Overview

Earnings call transcripts are dense, 10,000+ word documents packed with financial metrics, forward guidance, and executive commentary. Reading and extracting key information manually takes hours. This tool processes a raw transcript and produces a structured summary in seconds — covering everything from financial metrics to risk factors and management sentiment.

## Who It's For

- **Finance students** learning to analyze public company performance
- **Analysts and investors** who need to quickly extract signal from earnings calls

## Workflow

```
Raw transcript (.txt)
        |
        v
  Earnings Call Analyzer (LLM)
        |
        v
  Structured Summary Report
```

1. Provide a raw earnings call transcript as a `.txt` file
2. The tool sends the transcript to an LLM with structured extraction prompts
3. A formatted summary is returned, ready for review or further analysis

## Output

The structured summary includes:

- **Executive Summary** — 3–5 sentence overview of the call's key takeaways
- **Financial Metrics** — Revenue, EPS, margins, and YoY comparisons
- **Forward Guidance** — Management's outlook and targets for upcoming quarters
- **Sentiment Analysis** — Tone assessment of management commentary (bullish, cautious, defensive, etc.)
- **Risk Factors** — Key risks and concerns raised during the call

## Why It's Valuable

Earnings call transcripts are long, repetitive, and filled with boilerplate language. Manually extracting the information that matters — guidance, metrics, risks — takes significant time and expertise. This tool automates that extraction in seconds, letting analysts focus on interpretation rather than information retrieval.

## Requirements

- Python 3.9+
- Anthropic API key

## Usage

```bash
python app.py --transcript path/to/transcript.txt
```
