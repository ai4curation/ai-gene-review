import requests

# Just search UniProt for 3-dehydroshikimate dehydratase
print("Searching UniProt for 3-dehydroshikimate dehydratase proteins...")

url = "https://rest.uniprot.org/uniprotkb/search"
params = {
    'query': '(3-dehydroshikimate dehydratase) AND (reviewed:true)',
    'format': 'tsv',
    'fields': 'accession,id,gene_names,organism_name,protein_name',
    'size': '10'
}

response = requests.get(url, params=params)
print("\nClosest UniProt entries for qsuB-like proteins:")
print(response.text)

# Search for phage tail proteins similar to the Goslar proteins
print("\n" + "="*80)
print("\nSearching for phage tail/structural proteins...")
params['query'] = '(phage tail) AND (Escherichia) AND (reviewed:true)'
response = requests.get(url, params=params)
print(response.text[:1000])
