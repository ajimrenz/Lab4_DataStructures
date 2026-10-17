from collections import Counter, defaultdict
from config import *

show_inputs()
print("=== 1. ENGINEERING TEST DATA ORGANIZER ===")

sources = [f"{LAST_NAME}-T{i}" for i in range(1, 6)]
categories = ["TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"]


def value(i):
    return SEED_NUM * POSITIONS[i % len(POSITIONS)]


# 1. Generated test data: (source, category, value)
records = [(sources[i], categories[i], value(i)) for i in range(5)]
records.append((sources[0], categories[0], value(5)))   # repeated source/category
records.append((sources[3], categories[0], value(6)))   # additional: TEMPERATURE
records.append((sources[4], categories[1], value(7)))   # additional: VOLTAGE
print("\n[1] Generated Test Data")
for r in records:
    print("   ", r)

# 2. Organized: source -> category -> list of values
organized = defaultdict(lambda: defaultdict(list))
for s, c, v in records:
    organized[s][c].append(v)
print("\n[2] Organized Test Data")
for s in sorted(organized):
    print(f"    {s}: {dict(organized[s])}")

# 3. Repeated / distinct
pair_counts = Counter((s, c) for s, c, _ in records)
repeated = {k: n for k, n in pair_counts.items() if n > 1}
print("\n[3] Repeated / Distinct Data")
print("    Repeated source/category:", repeated)
print("    Distinct sources   :", sorted({s for s, _, _ in records}))
print("    Distinct categories:", sorted({c for _, c, _ in records}))
print("    Distinct values    :", sorted({v for _, _, v in records}))

# 4. Numerical and categorical summaries
by_cat = defaultdict(list)
for _, c, v in records:
    by_cat[c].append(v)
summaries = {c: {"count": len(vs), "min": min(vs), "max": max(vs),
                 "avg": round(sum(vs) / len(vs), 2)} for c, vs in by_cat.items()}
print("\n[4] Numerical and Categorical Summaries")
for c, s in summaries.items():
    print(f"    {c:<12} {s}")
print("    Records per source:", dict(Counter(s for s, _, _ in records)))

# 5. Processed results
processed = sorted(summaries.items(), key=lambda kv: kv[1]["avg"], reverse=True)
print("\n[5] Processed Results (category averages)")
for c, s in processed:
    print(f"    {c:<12} avg={s['avg']}")

# 6. Ordered results (by category, then value descending)
ordered = sorted(records, key=lambda r: (r[1], -r[2]))
print("\n[6] Ordered Results (by category, highest value first)")
for r in ordered:
    print("   ", r)

# 7. Final summary
all_vals = [v for _, _, v in records]
print("\n[7] Final Summary")
print(f"    Total records   : {len(records)}")
print(f"    Distinct sources: {len(sources)} | categories: {len(by_cat)}")
print(f"    Repeated records: {len(repeated)}")
print(f"    Overall min/max/avg: {min(all_vals)} / {max(all_vals)} / {round(sum(all_vals)/len(all_vals), 2)}")
print(f"    Highest avg category: {processed[0][0]}")