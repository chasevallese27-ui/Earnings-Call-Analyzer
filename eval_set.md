# Eval Set — Earnings Call Analyzer

Five test cases covering normal operation, edge cases, and hallucination risk.

---

## Test Case 1 — Normal Case: NVDA Strong Quarter

**Scenario**
A strong beat-and-raise quarter from NVIDIA. Management is confident, numbers are explicitly stated, and forward guidance is clearly given. This is the ideal, clean input the model should handle easily.

**Input Description**
Transcript includes:
- CEO opens with explicit revenue figure (e.g., "$26.0 billion, up 122% YoY")
- CFO provides EPS, gross margin, and segment breakdowns
- Management raises full-year guidance with specific numbers
- Tone throughout is confident and forward-looking
- No ambiguity in figures or attribution

**What a Good Output Should Do**
- Extract all financial metrics accurately with no invented numbers
- Reflect strongly positive sentiment in the sentiment section
- Capture raised guidance with the exact figures provided
- Produce a concise executive summary that leads with the beat and raise narrative
- List minimal or no material risks (consistent with the transcript's tone)

---

## Test Case 2 — Normal Case: AAPL Steady Quarter

**Scenario**
A predictable, in-line quarter from Apple. Well-structured transcript with standard financial disclosures. No major surprises. Tests whether the model produces a clean, complete summary when there is no dramatic narrative.

**Input Description**
Transcript includes:
- Revenue, EPS, and segment revenue (iPhone, Mac, Services, etc.) stated explicitly
- CFO provides YoY comparisons for each segment
- Guidance given as a revenue range for next quarter
- Measured, professional tone — no hyperbole or hedging
- Clean speaker turns: CEO intro, CFO financials, Q&A with analysts

**What a Good Output Should Do**
- Populate all output sections fully and accurately
- Reflect neutral-to-positive sentiment — not overstating enthusiasm
- Report guidance as a range (not a single number) matching the transcript
- Correctly break out segment metrics rather than lumping them together
- Executive summary should convey "steady, in-line quarter" — not a beat or miss narrative

---

## Test Case 3 — Edge Case: Guidance Withheld

**Scenario**
Management explicitly declines to provide forward guidance, citing macroeconomic uncertainty. Tests whether the model fabricates numbers to fill the guidance section or correctly reports that guidance was not given.

**Input Description**
Transcript includes:
- Normal financial results for the current quarter (revenue, EPS stated clearly)
- CFO explicitly states: "Given the uncertain macro environment, we will not be providing guidance for the coming quarter at this time"
- Analysts ask follow-up questions about guidance; management deflects each time
- No forward-looking revenue or EPS figures are given anywhere in the transcript

**What a Good Output Should Do**
- Write "Not disclosed" (or equivalent) in the Forward Guidance section
- Must NOT invent a guidance range or extrapolate from past quarters
- Note in the executive summary that management withheld guidance and the stated reason
- Sentiment section should reflect the cautious or uncertain tone
- This is a hallucination red line: any fabricated guidance figure is a failure

---

## Test Case 4 — Edge Case: Multiple Speakers

**Scenario**
A long, realistic transcript with CEO, CFO, and several sell-side analysts asking questions in the Q&A section. Tests whether the model correctly attributes statements and does not mix up who said what.

**Input Description**
Transcript includes:
- CEO delivers opening remarks with strategic commentary
- CFO delivers financial results and guidance
- 6–8 analyst Q&A exchanges, each analyst identified by name and firm
- CEO and CFO both respond to different questions throughout the Q&A
- Some questions span multiple topics; some answers are split between CEO and CFO

**What a Good Output Should Do**
- Attribute financial metrics to the CFO, not the CEO
- Attribute strategic commentary and vision statements to the CEO
- If quotes are used in the summary, correctly label the speaker
- Not conflate an analyst's question with management's answer
- Executive summary should reflect management's voice, not analyst skepticism
- Risk factors section should distinguish between risks management acknowledged vs. risks raised by analysts

---

## Test Case 5 — Hallucination Risk Case: Vague Transcript

**Scenario**
A transcript with no explicit financial figures — only qualitative language. Management uses phrases like "continued growth," "strong momentum," and "we are pleased with results" without disclosing any numbers. This may occur when a company provides a limited public transcript or when a partial/corrupted transcript is passed as input.

**Input Description**
Transcript includes:
- No revenue figure, no EPS, no margin data
- All financial commentary is qualitative: "We saw strong performance across segments," "Results were in line with our expectations"
- Guidance section uses language like "We remain optimistic about the coming year" with no specific targets
- Transcript is otherwise well-formatted with normal speaker turns

**What a Good Output Should Do**
- Leave financial metrics fields blank or marked "Not available in transcript"
- Must NOT fabricate numbers or infer figures from company name or prior knowledge
- Guidance section should reflect the vague language used, not invent targets
- Sentiment can still be assessed (positive/optimistic) based on qualitative language
- Executive summary should explicitly note that the transcript did not contain quantitative disclosures
- This is the primary hallucination stress test: any invented figure is a failure
