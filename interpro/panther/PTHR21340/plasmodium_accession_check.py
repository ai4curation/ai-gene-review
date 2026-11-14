"""Check the retired PF3D7_0520600 UniProt accession and NCBI replacements.

Run from this directory: python3 plasmodium_accession_check.py
Writes PTHR21340-plasmodium-accession-check.txt.
"""

import json
import urllib.parse
import urllib.request

UNIPROT_ENTRY = "https://rest.uniprot.org/uniprotkb/{accession}.json"
UNIPROT_SEARCH = "https://rest.uniprot.org/uniprotkb/search"
NCBI_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review"})
    with urllib.request.urlopen(req, timeout=120) as response:
        return response.read().decode()


def get_json(url):
    return json.loads(get(url))


def fasta_records(text):
    current = None
    chunks = []
    for line in text.splitlines():
        if line.startswith(">"):
            if current is not None:
                yield current, "".join(chunks)
            current = line[1:].split()[0]
            chunks = []
        elif current is not None:
            chunks.append(line.strip())
    if current is not None:
        yield current, "".join(chunks)


def main():
    lines = []

    inactive = get_json(UNIPROT_ENTRY.format(accession="C0H4F3"))
    reason = inactive.get("inactiveReason", {})
    lines.append(
        "UniProtKB C0H4F3 "
        f"entryType={inactive.get('entryType')} "
        f"inactiveReasonType={reason.get('inactiveReasonType')} "
        f"deletedReason={reason.get('deletedReason')}"
    )

    query = "gene_exact:PF3D7_0520600 AND proteome:UP000001450"
    search_url = UNIPROT_SEARCH + "?" + urllib.parse.urlencode(
        {
            "query": query,
            "fields": "accession,id,gene_names,organism_name,protein_name,reviewed,length,sequence_version",
            "format": "json",
            "size": 10,
        }
    )
    results = get_json(search_url).get("results", [])
    lines.append(f'UniProtKB query "{query}" returned {len(results)} current entries')
    for result in results:
        lines.append(f"  {result.get('primaryAccession')} {result.get('uniProtkbId')}")

    ncbi_ids = ["XP_002808704.1", "CAX63975.1"]
    efetch_url = NCBI_EFETCH + "?" + urllib.parse.urlencode(
        {
            "db": "protein",
            "id": ",".join(ncbi_ids),
            "rettype": "fasta",
            "retmode": "text",
        }
    )
    records = dict(fasta_records(get(efetch_url)))
    for accession in ncbi_ids:
        sequence = records.get(accession)
        if not sequence:
            lines.append(f"NCBI Protein {accession} missing")
            continue
        lines.append(
            f"NCBI Protein {accession} length={len(sequence)} "
            f"residue64={sequence[63]} residue68={sequence[67]}"
        )

    with open("PTHR21340-plasmodium-accession-check.txt", "w") as output:
        output.write("\n".join(lines) + "\n")
    print(f"{len(lines)} lines written")


if __name__ == "__main__":
    main()
