import requests
import time

# Read the qsuB sequence
with open('qsuB_sequence.fasta', 'r') as f:
    lines = f.readlines()
    sequence = ''.join(lines[1:]).replace('\n', '')

# Submit BLAST job to UniProt
url = "https://rest.uniprot.org/blast/run"
params = {
    'query': sequence,
    'database': 'uniprotkb',
    'stype': 'protein',
    'threshold': 0.001,
    'matrix': 'BLOSUM62'
}

response = requests.post(url, data=params)
if response.status_code == 303:
    job_id = response.headers['Location'].split('/')[-1]
    print(f"BLAST job submitted: {job_id}")
    
    # Poll for results
    status_url = f"https://rest.uniprot.org/blast/status/{job_id}"
    while True:
        status = requests.get(status_url)
        if status.text == "FINISHED":
            break
        print(f"Status: {status.text}")
        time.sleep(5)
    
    # Get results
    results_url = f"https://rest.uniprot.org/blast/result/{job_id}/tsv"
    results = requests.get(results_url)
    print("\nTop BLAST hits for qsuB:")
    print(results.text[:2000])
else:
    print(f"Error: {response.status_code}")
    print(response.text)
