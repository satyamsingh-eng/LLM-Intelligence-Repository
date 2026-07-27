import json

with open('local_knowledge_repository/verified_model_pricing_matrix.json') as f:
    data = json.load(f)

models = data.get('models', [])

print(f"{'Model Name':<22} | {'In / Out Rate':<14} | {'External Uncached':<18} | {'SARVAX Optimized':<18} | {'Savings %':<10}")
print("-" * 95)

for m in models:
    if m.get('status') != 'approved':
        continue
    name = m.get('name')
    rates = m.get('rates_usd', {})
    in_rate = rates.get('input_per_1m', '0.00')
    out_rate = rates.get('output_per_1m', '0.00')
    rate_str = f"${in_rate} / ${out_rate}"
    
    tier2 = m.get('tiers', {}).get('tier_2', {})
    uncached_usd = tier2.get('uncached', {}).get('monthly_10k_usd', 0)
    cached_usd = tier2.get('cached_80_percent', {}).get('monthly_10k_usd', 0)
    
    if uncached_usd > 0:
        savings_pct = ((uncached_usd - cached_usd) / uncached_usd) * 100
    else:
        savings_pct = 0
        
    print(f"{name:<22} | {rate_str:<14} | ${uncached_usd:<17.2f} | ${cached_usd:<17.2f} | {savings_pct:<9.1f}%")
