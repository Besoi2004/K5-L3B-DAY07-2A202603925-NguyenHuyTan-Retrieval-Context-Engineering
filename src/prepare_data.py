"""Build Day 7 data files from Day 6 outputs.

    .venv/Scripts/python src/prepare_data.py

Inputs : Day 6 starter/results/chunks_B.jsonl, Day 6 benchmark/questions.json,
         data/new_questions.json (new test questions + unanswerable cases, written for Day 7).
Outputs: data/chunks.json     - index B chunks in the Day 7 chunk schema
         data/questions.json  - answerable questions (baseline.py schema)
         data/cases.json      - every question with `answerable`, for agent runs/metrics
"""
import json
import re
import sys
from pathlib import Path

from day6 import DAY6_DIR

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "starter"))
from convert_day6 import convert_chunk, convert_question  # noqa: E402

# Day 6 test (q18-q22) was evaluated and its failures analysed in the Day 6 report,
# so it is no longer held out: it becomes dev, and data/new_questions.json holds a fresh test.
RESPLIT_TO_DEV = {"q18", "q19", "q20", "q21", "q22"}


def exact_evidence(quote: str, chunks: list[dict]) -> str | None:
    """Day 6 matched quotes after collapsing whitespace; Day 7 baseline.hit needs an exact
    substring, so return the chunk's own text for the quote (same words, its line breaks)."""
    pattern = re.compile(r"\s+".join(map(re.escape, quote.split())))
    for c in chunks:
        m = pattern.search(c["text"])
        if m:
            return m.group(0)
    return None


def main() -> None:
    raw_chunks = [json.loads(line) for line in
                  (DAY6_DIR / "starter/results/chunks_B.jsonl").read_text(encoding="utf-8").splitlines() if line]
    chunks = [convert_chunk(c) for c in raw_chunks]
    day6_qs = json.loads((DAY6_DIR / "benchmark/questions.json").read_text(encoding="utf-8"))
    new = json.loads((ROOT / "data/new_questions.json").read_text(encoding="utf-8"))

    questions, fixed = [], []
    for raw in day6_qs:
        q = convert_question(raw)
        if q["id"] in RESPLIT_TO_DEV:
            q["split"] = "dev"
        if q.get("filter") is None:
            q.pop("filter", None)
        q["type"] = raw.get("type")
        questions.append(q)
    questions += [q for q in new if q.get("answerable", True)]

    for q in questions:
        for g in q["gold"]:
            same_page = [c for c in chunks if c["source_id"] == g["source_id"] and c["page"] == g["page"]]
            ev = exact_evidence(g["evidence"], same_page)
            if ev is None:
                raise ValueError(f"{q['id']}: evidence không nằm trọn trong chunk nào ở trang {g['page']}")
            if ev != g["evidence"]:
                fixed.append(q["id"])
                g["evidence"] = ev
        q.pop("answerable", None)

    unanswerable = [q for q in new if q.get("answerable") is False]
    cases = ([{"id": q["id"], "split": q["split"], "question": q["question"], "answerable": True,
               "expected_behavior": "search_and_answer", **({"filter": q["filter"]} if q.get("filter") else {})}
              for q in questions] +
             [{k: q[k] for k in ("id", "split", "question", "answerable", "expected_behavior", "absence_reason")}
              for q in unanswerable])

    out = ROOT / "data"
    for name, rows in (("chunks.json", chunks), ("questions.json", questions), ("cases.json", cases)):
        (out / name).write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for split in ("dev", "test"):
        ans = sum(c["split"] == split and c["answerable"] for c in cases)
        una = sum(c["split"] == split and not c["answerable"] for c in cases)
        print(f"{split}: {ans} có đáp án + {una} thiếu evidence")
    print(f"{len(chunks)} chunks; evidence chỉnh khoảng trắng theo chunk: {len(fixed)} câu {sorted(set(fixed))}")


if __name__ == "__main__":
    main()
