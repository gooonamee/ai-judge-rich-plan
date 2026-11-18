from pathlib import Path
import os

DAY_ONE = "Day 1: Offer ‘Your video, everywhere in 24 hours’: one podcast or YouTube episode becomes 1 SEO article, 5 captioned shorts and 1 newsletter draft. Charge $40 per episode or $99 for 3. Build a Carrd page ($19/year), open Fiverr and Contra gigs, and send 3 creators with 50–5,000 YouTube subscribers free clips from their public videos and the offer link."
DAILY = "Days 2–30: Find 10 new small creators on YouTube daily; email each a free 60-second clip from their latest video and the Carrd, Fiverr or Contra link. Reply within an hour. Deliver within 24 hours with Whisper transcription and scripts; budget $2 API cost per order. Offer English, Spanish, Japanese and Chinese."
MONEY = "Budget: $19 Carrd, $30 API credits, $51 reserve; no ads. One $40 order daily from day 6 yields 25 orders, $1,000 gross and about $800 after platform fees; likely $400–600, floor about $80. Win on replies in minutes and multilingual overnight delivery while freelancers sleep."

PLAN = "\n".join((DAY_ONE, DAILY, MONEY))

if __name__ == "__main__":
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(PLAN.encode("utf-8"))
