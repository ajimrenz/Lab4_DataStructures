from collections import Counter, defaultdict
from config import *

show_inputs()
print("=== 3. TRANSACTION HISTORY ANALYZER ===")

customers = [f"{LAST_NAME}-C{i}" for i in range(1, 6)]
prices = {"NOTEBOOK": 45, "PEN": 12, "USB": 350, "HEADPHONES": 800, "CALCULATOR": 650}
products = list(prices)

# 1. Generated transactions: (customer, product, qty, value)
transactions = []
for j in range(7):
    cust = customers[j % 5]
    prod = products[(j * 2) % 5]
    qty = (SEED_NUM * POSITIONS[j % len(POSITIONS)]) % 5 + 1
    transactions.append((cust, prod, qty, qty * prices[prod]))
print("\n[1] Generated Transaction Records (customer, product, qty, value)")
for t in transactions:
    print("   ", t)

# 2. Organized: customer -> product -> list of (qty, value)
organized = defaultdict(lambda: defaultdict(list))
for c, p, q, v in transactions:
    organized[c][p].append((q, v))
print("\n[2] Organized Transaction Data")
for c in sorted(organized):
    print(f"    {c}: {dict(organized[c])}")

# 3. Transaction values
total = sum(t[3] for t in transactions)
print("\n[3] Transaction Values")
for t in transactions:
    print(f"    {t[0]} bought {t[2]} x {t[1]} = {t[3]}")
print("    Overall dataset total:", total)

# 4. Repeated / distinct
pair_counts = Counter((c, p) for c, p, _, _ in transactions)
repeated = {k: n for k, n in pair_counts.items() if n > 1}
print("\n[4] Repeated / Distinct Transactions")
print("    Repeated customer-product:", repeated)
print("    Distinct customers:", sorted({t[0] for t in transactions}))
print("    Distinct products :", sorted({t[1] for t in transactions}))

# 5. Customer summaries
cust_sum = defaultdict(lambda: {"transactions": 0, "qty": 0, "value": 0})
for c, p, q, v in transactions:
    cust_sum[c]["transactions"] += 1
    cust_sum[c]["qty"] += q
    cust_sum[c]["value"] += v
print("\n[5] Customer Summaries")
for c in sorted(cust_sum):
    print(f"    {c}: {cust_sum[c]}")

# 6. Product summaries
prod_sum = defaultdict(lambda: {"transactions": 0, "qty": 0, "value": 0})
for c, p, q, v in transactions:
    prod_sum[p]["transactions"] += 1
    prod_sum[p]["qty"] += q
    prod_sum[p]["value"] += v
print("\n[6] Product Summaries")
for p in sorted(prod_sum):
    print(f"    {p}: {prod_sum[p]}")

# 7. Ordered results
print("\n[7] Ordered Results")
print("    Customers by total value (highest first):")
for c, s in sorted(cust_sum.items(), key=lambda kv: kv[1]["value"], reverse=True):
    print(f"      {c}: {s['value']}")
print("    Products by total value (highest first):")
for p, s in sorted(prod_sum.items(), key=lambda kv: kv[1]["value"], reverse=True):
    print(f"      {p}: {s['value']}")

# 8. Overall summary
print("\n[8] Overall Transaction Summary")
print(f"    Transactions: {len(transactions)} | total quantity: {sum(t[2] for t in transactions)} | total value: {total}")
print(f"    Average transaction value: {round(total/len(transactions), 2)}")
print(f"    Top customer: {max(cust_sum, key=lambda k: cust_sum[k]['value'])}")
print(f"    Top product : {max(prod_sum, key=lambda k: prod_sum[k]['value'])}")
