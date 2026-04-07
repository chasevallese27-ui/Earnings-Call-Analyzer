# Earnings Call Analyzer - Project Report

## Business Use Case

Earnings call transcripts are often 10,000+ words long. Analysts and investors manually read these to extract key metrics, guidance, and sentiment. This tool automates that process using Claude as the LLM, reducing analysis time from 30+ minutes to seconds.

## Model Chosen

Anthropic Claude (`claude-sonnet-4-20250514`) was chosen because of its strong performance on structured text extraction tasks, its ability to follow detailed system prompts, and existing familiarity with the API from prior projects.

## Baseline vs Final Design

- **Baseline:** Single command line argument, output always saved to `output.txt`, basic prompt with no hallucination guardrails
- **Final:** User enters company name at prompt, app finds transcript automatically, output saved to `COMPANYNAME_summary.txt`, system prompt includes explicit instruction to write "Not Disclosed" rather than estimating missing metrics

## Where the Prototype Still Fails

- Very long transcripts may cause the model to miss details in early sections
- Multi-speaker transcripts risk incorrect quote attribution between CEO, CFO, and analyst questions
- The model may still produce vague summaries when transcript language is intentionally ambiguous
- The system requires a human to source and paste the transcript; automated fetching risks hallucination

## Deployment Recommendation

This tool is useful as a personal research assistant for quickly scanning earnings calls. It should not be deployed without human review of outputs before any investment decision is made. A production version would need a verified transcript source, output validation, and clear disclaimers that outputs are AI-generated summaries only.
