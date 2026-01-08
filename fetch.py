import requests, json

url = "https://jobsearch.api.jobtechdev.se/search"

# mycket bredare sökning, utan regionfilter
params = {
    "q": "HR",         # ett säkert sökord med många träffar
    "limit": 5,
    "sort": "pubdate-desc"
}

r = requests.get(url, params=params, timeout=20)
r.raise_for_status()
data = r.json()

# hantera totalfältets struktur
total = data.get("total", 0)
if isinstance(total, dict):
    total = total.get("value", 0)

print(f"Totalt antal annonser hittade: {total}\n")

hits = data.get("hits", [])
if not hits:
    print("Inga annonser hittades – prova annat sökord.")
else:
    for i, job in enumerate(hits, start=1):
        title = job.get("headline", "saknar titel")
        company = job.get("employer", {}).get("name", "okänd arbetsgivare")
        place = job.get("workplace_address", {}).get("municipality", "okänd plats")
        print(f"{i}. {title} – {company} ({place})")
