"""Locate the two SMIM45 protein sequences (UniProt A0A590UK83 sequence v1, 107 aa,
and v2, 68 aa) in the Ensembl SMIM45 transcripts and report frame/overlap.

Fetches live data from UniProt UniSave and Ensembl REST; prints results only.
Usage: python3 -I orf_check.py
"""
import json
import urllib.request

CODON = {}
bases = "TCAG"
aas = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
i = 0
for a in bases:
    for b in bases:
        for c in bases:
            CODON[a + b + c] = aas[i]
            i += 1


def get(url, accept=None):
    req = urllib.request.Request(url, headers={"Accept": accept} if accept else {})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()


def unisave_seq(acc, version):
    txt = get(f"https://rest.uniprot.org/unisave/{acc}?format=fasta&versions={version}")
    return "".join(l.strip() for l in txt.splitlines() if not l.startswith(">"))


def translate(nt):
    return "".join(CODON.get(nt[i:i + 3], "X") for i in range(0, len(nt) - 2, 3))


PRIMERS = {
    "KO-GT-F": "ATGTCTATGGCTGCCTGTCCTG",
    "ORF-RT-F": "CGGAGCCCTCATTTCTTCGT",
}


def main():
    gene = "ENSG00000205704"
    seqs = {"v1_107aa(entry v11)": unisave_seq("A0A590UK83", 11),
            "v2_68aa(entry v12)": unisave_seq("A0A590UK83", 12)}
    for k, s in seqs.items():
        print(k, len(s), s)
    lookup = json.loads(get(f"https://rest.ensembl.org/lookup/id/{gene}?expand=1",
                            "application/json"))
    print("Ensembl gene", gene, lookup.get("display_name"), lookup.get("biotype"))
    for tr in lookup.get("Transcript", []):
        tid = tr["id"]
        cdna = get(f"https://rest.ensembl.org/sequence/id/{tid}?type=cdna",
                   "text/plain").strip().upper()
        hits = []
        for name, prot in seqs.items():
            for f in range(3):
                pep = translate(cdna[f:])
                pos = pep.find(prot)
                if pos >= 0:
                    nt_start = f + 3 * pos
                    hits.append((name, f, nt_start, nt_start + 3 * len(prot) + 3))
        print(tid, tr.get("biotype"), len(cdna), "nt; hits:", hits or "none")
        names = {h[0]: h for h in hits}
        if len(names) == 2:
            a, b = list(names.values())
            ov = max(0, min(a[3], b[3]) - max(a[2], b[2]))
            print("   overlap between ORFs (nt):", ov,
                  "| same frame:", (a[2] - b[2]) % 3 == 0)
        # Primers reported in PMID:36593289 Methods (forward primers, sense strand)
        for pname, p in PRIMERS.items():
            pos = cdna.find(p)
            where = "not found"
            if pos >= 0:
                where = f"nt {pos}"
                for name, f, st, en in hits:
                    if st <= pos < en:
                        where += f" (inside {name} ORF)"
            print(f"   primer {pname}: {where}")


if __name__ == "__main__":
    main()
