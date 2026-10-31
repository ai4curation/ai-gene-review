"""Genomic context and gene-model check for Cgl2304 / cg2530 (Q8NNA0).

1. Fetch the C. glutamicum ATCC 13032 RefSeq chromosome (NC_003450.3) region
   around the gene from NCBI E-utilities and list neighbouring CDSs (locus tags,
   old locus tags, products, strand, coordinates, intergenic distances).
2. Gene-model check: extend the Cgl2304 reading frame upstream to the previous
   in-frame stop codon and report how many codons (and which alternative start
   codons) lie upstream of the annotated start. A truncated model would show a long
   open extension that could encode the missing Mak N-terminal cap.
3. Ortholog lengths: list UniProt entries in the UniRef50 cluster of Q8NNA0 and
   UniProt Corynebacterium / Mycobacteriales entries sharing eggNOG COG3281, with
   their lengths, to see whether ~363 aa is typical for Corynebacterium.

Writes $BERIL_RUN_DIR/genome_context.json (or ./data).
"""
import json
import os
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
ACC = "NC_003450.3"
GENE_ID = "1020255"  # NCBI GeneID from the UniProt DR line


def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return r.read().decode()
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(3)


def revcomp(s):
    return s.translate(str.maketrans("ACGTacgt", "TGCAtgca"))[::-1]


CODON = {}
bases = "TCAG"
aas = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
i = 0
for a in bases:
    for b in bases:
        for c in bases:
            CODON[a + b + c] = aas[i]
            i += 1


def translate(s):
    return "".join(CODON.get(s[i:i + 3], "X") for i in range(0, len(s) - 2, 3))


def parse_features(gb):
    feats = []
    ft = gb.split("\nFEATURES")[1].split("\nORIGIN")[0]
    blocks = re.split(r"\n     (?=\S)", ft)
    for b in blocks:
        m = re.match(r"(CDS|gene)\s+(complement\()?<?(\d+)\.\.>?(\d+)\)?", b)
        if not m or m.group(1) != "CDS":
            continue
        q = {}
        for k, v in re.findall(r'/(\w+)="([^"]*)"', b.replace("\n                     ", " ")):
            q.setdefault(k, v)
        feats.append({
            "start": int(m.group(3)), "end": int(m.group(4)),
            "strand": "-" if m.group(2) else "+",
            "locus_tag": q.get("locus_tag"), "old_locus_tag": q.get("old_locus_tag"),
            "gene": q.get("gene"), "product": q.get("product"),
            "protein_id": q.get("protein_id"),
            "aa_len": len(q.get("translation", "").replace(" ", "")) or None,
        })
    seq = re.sub(r"[^acgt]", "", gb.split("\nORIGIN")[1].lower()).upper()
    return feats, seq


def uniprot_tsv(query, fields="accession,organism_name,length,gene_names,protein_name", size=500):
    url = "https://rest.uniprot.org/uniprotkb/search?" + urllib.parse.urlencode(
        {"query": query, "fields": fields, "format": "tsv", "size": size})
    rows = get(url).strip().splitlines()
    hdr = rows[0].split("\t")
    return [dict(zip(hdr, r.split("\t"))) for r in rows[1:]]


def main():
    out = Path(os.environ.get("BERIL_RUN_DIR", "data"))
    out.mkdir(parents=True, exist_ok=True)
    res = {}

    # gene coordinates from NCBI Gene
    gs = json.loads(get(f"{EUTILS}/esummary.fcgi?db=gene&id={GENE_ID}&retmode=json"))
    gi = gs["result"][GENE_ID]["genomicinfo"][0]
    s, e = sorted([int(gi["chrstart"]) + 1, int(gi["chrstop"]) + 1])
    res["ncbi_gene"] = {"name": gs["result"][GENE_ID]["name"],
                        "description": gs["result"][GENE_ID]["description"],
                        "chraccver": gi["chraccver"], "start": s, "end": e}
    win = 9000
    lo, hi = max(1, s - win), e + win
    gb = get(f"{EUTILS}/efetch.fcgi?db=nuccore&id={gi['chraccver']}&rettype=gbwithparts&retmode=text"
             f"&seq_start={lo}&seq_stop={hi}")
    (out / "region.gb").write_text(gb)
    feats, seq = parse_features(gb)
    for f in feats:
        f["start"] += lo - 1
        f["end"] += lo - 1
    feats.sort(key=lambda f: f["start"])
    for a, b in zip(feats, feats[1:]):
        a["gap_to_next"] = b["start"] - a["end"] - 1
    res["neighbourhood"] = feats

    # gene-model check on the target CDS
    tgt = min(feats, key=lambda f: abs(f["start"] - s) + abs(f["end"] - e))
    res["target_cds"] = tgt
    rs, re_ = tgt["start"] - lo, tgt["end"] - lo + 1  # 0-based slice in region seq
    if tgt["strand"] == "+":
        cds = seq[rs:re_]
        upstream = seq[:rs]
    else:
        cds = revcomp(seq[rs:re_])
        upstream = revcomp(seq[re_:])
    prot = translate(cds)
    res["cds_translation_len"] = len(prot.rstrip("*"))
    res["cds_start_codon"] = cds[:3]
    # walk upstream in frame until a stop codon
    ext_codons = []
    k = len(upstream)
    while k - 3 >= 0:
        cod = upstream[k - 3:k]
        if CODON.get(cod) == "*":
            break
        ext_codons.append(cod)
        k -= 3
    ext_codons = ext_codons[::-1]
    alt = [len(ext_codons) - i for i, c in enumerate(ext_codons) if c in ("ATG", "GTG", "TTG")]
    res["upstream_open_extension_codons"] = len(ext_codons)
    res["upstream_alt_starts_codons_upstream"] = sorted(alt)
    res["upstream_extension_translation"] = translate("".join(ext_codons))

    # UniRef50 cluster members
    try:
        ur = json.loads(get("https://rest.uniprot.org/uniref/search?query=uniprot_id:Q8NNA0+AND+identity:0.5&format=json"))
        cid = ur["results"][0]["id"]
        mem = uniprot_tsv(f"uniref_cluster_50:{cid}")
        res["uniref50"] = {"cluster": cid, "n": len(mem), "members": mem}
    except Exception as ex:
        res["uniref50_error"] = repr(ex)

    # COG3281 members in Corynebacterium (taxid 1716) and Mycobacteriales (85007)
    for name, tax in [("Corynebacterium", 1716), ("Mycobacteriales", 85007)]:
        try:
            rows = uniprot_tsv(f"xref:eggnog-COG3281 AND taxonomy_id:{tax} AND reviewed:false", size=500)
            lens = sorted(int(r["Length"]) for r in rows)
            res[f"cog3281_{name}"] = {
                "n": len(rows), "lengths": lens,
                "n_len_le_400": sum(1 for x in lens if x <= 400),
                "n_len_401_500": sum(1 for x in lens if 400 < x <= 500),
                "n_len_gt_500": sum(1 for x in lens if x > 500),
            }
            if name == "Corynebacterium":
                res["cog3281_Corynebacterium"]["rows"] = rows
        except Exception as ex:
            res[f"cog3281_{name}_error"] = repr(ex)

    (out / "genome_context.json").write_text(json.dumps(res, indent=1))
    summary = {k: v for k, v in res.items() if k not in ("uniref50", "cog3281_Corynebacterium")}
    print(json.dumps(summary, indent=1)[:6000])
    if "uniref50" in res:
        print("UniRef50", res["uniref50"]["cluster"], res["uniref50"]["n"])
        for m in res["uniref50"]["members"][:80]:
            print(" ", m["Entry"], m["Length"], m["Organism"][:60])
    if "cog3281_Corynebacterium" in res:
        c = res["cog3281_Corynebacterium"]
        print("COG3281 Corynebacterium", c["n"], c["n_len_le_400"], c["n_len_401_500"], c["n_len_gt_500"])


if __name__ == "__main__":
    main()
