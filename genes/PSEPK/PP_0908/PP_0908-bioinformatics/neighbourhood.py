"""Genomic neighbourhood and N-terminal export-signal check for PP_0908 (Q88PE2).

Fetches, for KT2440 PP_0902-PP_0916 and P. aeruginosa PAO1 PA4366-PA4376, the UniProt
protein name, length, Pfam domains and SignalP/Phobius features, plus NCBI CDS
coordinates for KT2440 PP_0905-PP_0913. Checks the PP_0908 N-terminus for a
twin-arginine (Tat) motif and lists KT2440 proteins carrying EfeU/FTR1 (PF03239),
EfeB/DyP (PF04261), imelysin (PF09375), DHOR (PF06537) or DUF1513 (PF07433).

Usage: python neighbourhood.py OUTDIR
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

UP = "https://rest.uniprot.org/uniprotkb/search?"
FIELDS = "accession,gene_oln,protein_name,length,xref_pfam,ft_signal,ft_transmem,sequence"


def uniprot(query):
    url = UP + urllib.parse.urlencode({"query": query, "fields": FIELDS, "format": "json", "size": 50})
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)["results"]


def summarise(e):
    feats = e.get("features", [])
    return {
        "accession": e["primaryAccession"],
        "locus": [n["value"] for g in e.get("genes", []) for n in g.get("orderedLocusNames", [])],
        "protein": e["proteinDescription"].get("recommendedName", e["proteinDescription"].get("submissionNames", [{}])[0]).get("fullName", {}).get("value"),
        "length": e["sequence"]["length"],
        "pfam": [x["id"] for x in e.get("uniProtKBCrossReferences", []) if x["database"] == "Pfam"],
        "signal": [f"{f['location']['start']['value']}-{f['location']['end']['value']}" for f in feats if f["type"] == "Signal"],
        "n_transmem": sum(1 for f in feats if f["type"] == "Transmembrane"),
    }


def ncbi_cds(protein_acc):
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&rettype=gb&id=" + protein_acc)
    with urllib.request.urlopen(url, timeout=60) as r:
        txt = r.read().decode()
    m = re.search(r'/coded_by="([^"]+)"', txt)
    lt = re.search(r'/locus_tag="([^"]+)"', txt)
    return {"protein_id": protein_acc, "locus_tag": lt.group(1) if lt else None, "coded_by": m.group(1) if m else None}


def main(outdir):
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    res = {}
    kt = []
    for i in range(902, 917):
        lt = f"PP_{i:04d}"
        hits = [summarise(e) for e in uniprot(f"gene:{lt} AND organism_id:160488")]
        kt.extend(h for h in hits if lt in h["locus"])
        time.sleep(0.2)
    res["kt2440_neighbourhood"] = kt
    pa = []
    for i in range(4366, 4377):
        lt = f"PA{i}"
        hits = [summarise(e) for e in uniprot(f"gene:{lt} AND organism_id:208964")]
        pa.extend(h for h in hits if lt in h["locus"])
        time.sleep(0.2)
    res["pao1_neighbourhood"] = pa
    # NCBI CDS coordinates (AE015451.2) for PP_0905-PP_0913
    cds = []
    for acc in ["AAN66530.1", "AAN66531.1", "AAN66532.1", "AAN66533.1", "AAN66534.1",
                "AAN66535.1", "AAN66536.1", "AAN66537.1", "AAN66538.1"]:
        cds.append(ncbi_cds(acc))
        time.sleep(0.4)
    res["kt2440_cds_coordinates"] = cds
    # KT2440 proteins in the relevant Pfam families
    q = ("organism_id:160488 AND (xref:pfam-PF03239 OR xref:pfam-PF04261 OR xref:pfam-PF09375 "
         "OR xref:pfam-PF07433 OR xref:pfam-PF06537)")
    res["kt2440_family_members"] = [summarise(e) for e in uniprot(q)]
    # PP_0908 N-terminus
    q0908 = uniprot("accession:Q88PE2")[0]
    seq = q0908["sequence"]["value"]
    nterm = seq[:40]
    tat = re.search(r"[ST]?RR.[FLIVMA][LIVMF]K", nterm)
    res["pp0908_nterm"] = {
        "first_40": nterm,
        "tat_like_motif": tat.group(0) if tat else None,
        "tat_like_motif_start": (tat.start() + 1) if tat else None,
        "uniprot_signalp_feature": summarise(q0908)["signal"],
        "length": len(seq),
        "n_cys_mature_26_end": seq[25:].count("C"),
    }
    (out / "neighbourhood_results.json").write_text(json.dumps(res, indent=2))
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
