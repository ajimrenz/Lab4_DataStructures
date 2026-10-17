
from collections import Counter, defaultdict
from config import *

show_inputs()
print("=== 2. STUDENT PERFORMANCE DATA ANALYZER ===")

students = [f"{LAST_NAME}-S{i}" for i in range(1, 6)]
subjects = ["PROGRAMMING", "MATHEMATICS", "ELECTRONICS", "PHYSICS", "ENGLISH"]


def score(i):
    return (SEED_NUM * POSITIONS[i % len(POSITIONS)] + 7 * i) % 41 + 60   # 60-100


def category(s):
    if s >= 90: return "Excellent"
    if s >= 85: return "Very Good"
    if s >= 75: return "Good"
    return "Needs Improvement"


# 1. Generated records: (student, subject, score)
records = []
for i in range(5):
    records.append((students[i], subjects[i], score(i)))
    records.append((students[i], subjects[(i + 1) % 5], score(i + 5)))
records.append((students[0], subjects[0], score(10)))   # repeated student-subject
records[3] = (records[3][0], records[3][1], None)       # incomplete (missing score)
print("\n[1] Generated Performance Records")
for r in records:
    print("   ", r)

# 2. Organized: student -> subject -> list of scores
organized = defaultdict(lambda: defaultdict(list))
for st, sub, sc in records:
    organized[st][sub].append(sc)
print("\n[2] Organized Student/Subject Data")
for st in sorted(organized):
    print(f"    {st}: {dict(organized[st])}")

# 3. Repeated / incomplete
pair_counts = Counter((st, sub) for st, sub, _ in records)
repeated = {k: n for k, n in pair_counts.items() if n > 1}
incomplete = [r for r in records if r[2] is None]
print("\n[3] Repeated / Incomplete Records")
print("    Repeated  :", repeated)
print("    Incomplete:", incomplete)

# 4. Performance categories (valid scores; repeated -> keep first occurrence)
seen, valid = set(), []
for st, sub, sc in records:
    if sc is None or (st, sub) in seen:
        continue
    seen.add((st, sub))
    valid.append((st, sub, sc, category(sc)))
print("\n[4] Performance Categories")
for r in valid:
    print("   ", r)

# 5. Student and subject summaries
stu = defaultdict(list)
sub_ = defaultdict(list)
for st, sb, sc, _ in valid:
    stu[st].append(sc)
    sub_[sb].append(sc)
stu_avg = {k: round(sum(v) / len(v), 2) for k, v in stu.items()}
sub_avg = {k: round(sum(v) / len(v), 2) for k, v in sub_.items()}
print("\n[5] Student and Subject Summaries")
print("    Student averages:", stu_avg)
print("    Subject averages:", sub_avg)
print("    Category counts :", dict(Counter(r[3] for r in valid)))

# 6. Ordered results
print("\n[6] Ordered Results")
print("    Students (highest avg first):")
for k, v in sorted(stu_avg.items(), key=lambda kv: kv[1], reverse=True):
    print(f"      {k}: {v}")
print("    Subjects (highest avg first):")
for k, v in sorted(sub_avg.items(), key=lambda kv: kv[1], reverse=True):
    print(f"      {k}: {v}")

# 7. Final report
scores = [r[2] for r in valid]
print("\n[7] Final Student Performance Report")
print(f"    Total records: {len(records)} | valid: {len(valid)} | repeated: {len(repeated)} | incomplete: {len(incomplete)}")
print(f"    Class average: {round(sum(scores)/len(scores), 2)}")
print(f"    Top student : {max(stu_avg, key=stu_avg.get)}")
print(f"    Top subject : {max(sub_avg, key=sub_avg.get)}")
