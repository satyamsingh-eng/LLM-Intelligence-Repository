import json

with open('models/executive_report_runtime.json') as f:
    data = json.load(f)

catalog = data.get('pricing_catalog', [])
fx = 96.567636

print(f"Total models in catalog: {len(catalog)}")
print(f"FX Rate: ₹{fx} / USD\n")

print(f"{'#':2s} | {'Model Name':26s} | {'Input / 1M':16s} | {'Output / 1M':16s} | {'10k Monthly Cost':22s} | {'Superpower / Best Part'}")
print("-" * 120)

for i, m in enumerate(catalog, 1):
    name = m.get('name', m.get('id'))
    in_usd = float(m.get('input_usd', 0))
    out_usd = float(m.get('output_usd', 0))
    cached_usd = float(m.get('cached_usd', in_usd))
    
    in_inr = in_usd * fx
    out_inr = out_usd * fx
    
    # Tier 2 Standard Review (35k in / 3.5k out, 80% cached)
    effective_in_usd = 0.8 * cached_usd + 0.2 * in_usd
    cost_per_run_usd = (35000 * effective_in_usd + 3500 * out_usd) / 1000000.0
    monthly_10k_usd = cost_per_run_usd * 10000
    monthly_10k_inr = monthly_10k_usd * fx
    
    superpower = m.get('superpower', m.get('best_for', m.get('description', 'High performance model')))
    
    print(f"{i:2d} | {name:26s} | ${in_usd:6.3f} (₹{in_inr:6.2f}) | ${out_usd:6.3f} (₹{out_inr:6.2f}) | ₹{monthly_10k_inr:9.2f} (${monthly_10k_usd:6.1f}) | {superpower}")
