"""GH57 catalytic residues and domain architecture of GSU2359 (Q74AJ5), A2cp1_1916 (B8J768)
and the comparator DVU_2472 (Q728Y0).

GH57 enzymes use a Glu nucleophile on strand b4 (CSR-3) and an Asp proton donor on b7 (CSR-4)
(Zona et al. 2004, PMID:15233783; Martinovicova & Janecek 2018, PMID:29998051).
Method: every sequence is aligned with hmmalign (pyhmmer) to the Pfam GH57 HMM (PF03065).
Reference GH57 enzymes with UniProt ACT_SITE features (nucleophile / proton donor) define
the HMM match columns of the two catalytic residues; the residues of the queries, of the
characterized GH57_6 members (Amo45 D3SMQ0, PoGH57 QCR22797.1) and of every UniProtKB protein
carrying DUF3536 (PF12055) are read at those columns. CSR windows are read at the columns of
the T. litoralis 4-alpha-glucanotransferase (O32462) motifs given by Zona et al. 2004.
Domain coordinates: hmmsearch with PF03065 and PF12055 (Pfam HMMs from InterPro).
Writes $BERIL_RUN_DIR/results.json and tables/*.tsv.
"""
import gzip, io, json, os, re, collections, urllib.request
from pathlib import Path
import pyhmmer

OUT = Path(os.environ.get("BERIL_RUN_DIR", "/tmp/gh57_cat"))
(OUT / "tables").mkdir(parents=True, exist_ok=True)

def get(url, timeout=300):
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return r.read()

def parse_fasta(txt):
    seqs, k = {}, None
    for line in txt.splitlines():
        if line.startswith(">"):
            k = line[1:].split()[0]; seqs[k] = []
        elif k:
            seqs[k].append(line.strip())
    return {k: "".join(v) for k, v in seqs.items()}

def uniprot(acc):
    return "".join(get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").decode().splitlines()[1:])

def act_sites(acc):
    t = get(f"https://rest.uniprot.org/uniprotkb/{acc}.tsv?fields=ft_act_site").decode().splitlines()[1]
    return {m.group(2): int(m.group(1)) for m in re.finditer(r'ACT_SITE (\d+); /note="([^"]+)"', t)}

QUERIES = {"Q74AJ5": "GSU2359 G. sulfurreducens", "B8J768": "A2cp1_1916 A. dehalogenans",
           "Q728Y0": "DVU_2472 N. vulgaris"}
GH57_6_CHAR = {"D3SMQ0": "Amo45 Thermocrinis albus (GH57_6, alpha-amylase)"}
NCBI_CHAR = {"QCR22797.1": "PoGH57 Pontibacter sp. SGAir0037 (GH57_6, 4-alpha-glucanotransferase)"}
REFS = {"O32462": "T. litoralis 4-alpha-glucanotransferase (structure)",
        "Q5JDJ7": "T. kodakarensis GH57 branching enzyme (mutagenesis)",
        "Q5SH28": "T. thermophilus GH57 branching enzyme (structure)",
        "O50094": "P. horikoshii GH57 branching enzyme"}
# T. litoralis 4AGT CSR motifs (Zona et al. 2004): start positions and motif strings
CSR = {"CSR-1": (13, "HQP"), "CSR-2": (76, "GQLEIV"), "CSR-3": (120, "WLTERV"),
       "CSR-4": (212, "HDDGEKFGVW"), "CSR-5": (350, "AQCNDAYWH")}

seqs, labels = {}, {}
for a, l in {**QUERIES, **GH57_6_CHAR, **REFS}.items():
    seqs[a] = uniprot(a); labels[a] = l
for a, l in NCBI_CHAR.items():
    f = get(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id={a}&rettype=fasta").decode()
    seqs[a] = "".join(f.splitlines()[1:]); labels[a] = l
fam = parse_fasta(get("https://rest.uniprot.org/uniprotkb/stream?query=xref:pfam-PF12055&format=fasta", 600).decode())
fam = {k.split("|")[1]: v for k, v in fam.items()}

hmms = {}
for pf in ["PF03065", "PF12055"]:
    raw = gzip.decompress(get(f"https://www.ebi.ac.uk/interpro/api/entry/pfam/{pf}?annotation=hmm"))
    with pyhmmer.plan7.HMMFile(io.BytesIO(raw)) as hf:
        hmms[pf] = hf.read()
alpha = pyhmmer.easel.Alphabet.amino()

def dig(d):
    return [pyhmmer.easel.TextSequence(name=k.encode(), sequence=v.replace("*", "")).digitize(alpha) for k, v in d.items()]

# domain coordinates
dom_rows = []
allseq = {**seqs}
for pf, hmm in hmms.items():
    for hits in pyhmmer.hmmsearch([hmm], dig(allseq), E=1e-3, domE=1e-3):
        for h in hits:
            for d in h.domains.included:
                dom_rows.append((h.name.decode() if isinstance(h.name, bytes) else h.name, pf,
                                 d.env_from, d.env_to, f"{d.i_evalue:.1e}"))
with open(OUT / "tables" / "domains.tsv", "w") as fh:
    fh.write("seq\tpfam\tenv_from\tenv_to\ti_evalue\n")
    for r in sorted(dom_rows):
        fh.write("\t".join(map(str, r)) + "\n")

# hmmalign everything (named set + DUF3536 family) to PF03065
named_keys = list(seqs)
allin = {**seqs, **{k: v for k, v in fam.items() if k not in seqs}}
msa = pyhmmer.hmmalign(hmms["PF03065"], dig(allin), trim=False)
names = [n.decode() if isinstance(n, bytes) else n for n in msa.names]
rows = dict(zip(names, [str(s) for s in msa.alignment]))
# match-state columns: in hmmalign output uppercase/'-' are match states, lowercase/'.' inserts
def colmap(row):
    """seq position (1-based) -> HMM match column (1-based) or None, and reverse"""
    pos, mcol, p2c, c2r = 0, 0, {}, {}
    for ch in row:
        is_match = ch.isupper() or ch == "-"
        if is_match:
            mcol += 1
        if ch.isalpha():
            pos += 1
            if is_match:
                p2c[pos] = mcol; c2r[mcol] = (pos, ch)
    return p2c, c2r
maps = {n: colmap(rows[n]) for n in names}

ref_cols = collections.defaultdict(dict)
ref_check = {}
for a in REFS:
    sites = act_sites(a)
    for note, pos in sites.items():
        role = "nucleophile" if "ucleophile" in note else ("acid_base" if "donor" in note else note)
        col = maps[a][0].get(pos)
        ref_cols[role][a] = col
        ref_check[f"{a}:{role}"] = {"pos": pos, "residue": seqs[a][pos - 1], "hmm_col": col}

def consensus_col(d):
    vals = [v for v in d.values() if v]
    return collections.Counter(vals).most_common(1)[0][0] if vals else None
NUC, AB = consensus_col(ref_cols["nucleophile"]), consensus_col(ref_cols["acid_base"])

def at(name, col):
    if col is None: return None
    r = maps[name][1].get(col)
    return {"pos": r[0], "aa": r[1]} if r else None

per = {}
for n in named_keys:
    per[n] = {"label": labels[n], "length": len(seqs[n]), "nucleophile": at(n, NUC), "acid_base": at(n, AB)}
    csr = {}
    for cname, (start, motif) in CSR.items():
        cols = [maps["O32462"][0].get(start + i) for i in range(len(motif))]
        got = []
        for c in cols:
            r = maps[n][1].get(c) if c else None
            got.append(r[1] if r else "-")
        csr[cname] = {"tlgt_motif": motif, "tlgt_mapped": all(cols), "query": "".join(got),
                      "query_start": next((maps[n][1][c][0] for c in cols if c and c in maps[n][1]), None)}
    per[n]["csr"] = csr

# conservation across UniProtKB DUF3536 proteins
fam_names = [k for k in names if k in fam]
def frac(col, aa):
    obs = [maps[k][1].get(col) for k in fam_names]
    obs = [o[1] for o in obs if o]
    c = collections.Counter(obs)
    return {"n_aligned": len(obs), "frac_" + aa: round(c[aa] / len(obs), 4) if obs else None,
            "top": c.most_common(4), "n_family": len(fam_names)}
cons = {"nucleophile_col": NUC, "acid_base_col": AB,
        "nucleophile_Glu": frac(NUC, "E") if NUC else None, "acid_base_Asp": frac(AB, "D") if AB else None}
with open(OUT / "tables" / "duf3536_catalytic_residues.tsv", "w") as fh:
    fh.write("acc\tnuc_pos\tnuc_aa\tab_pos\tab_aa\n")
    for k in fam_names:
        a, b = at(k, NUC), at(k, AB)
        fh.write(f"{k}\t{a and a['pos']}\t{a and a['aa']}\t{b and b['pos']}\t{b and b['aa']}\n")
res = {"reference_active_sites": ref_check, "consensus_columns": {"nucleophile": NUC, "acid_base": AB},
       "per_sequence": per, "duf3536_family_conservation": cons, "domains": dom_rows}
json.dump(res, open(OUT / "results.json", "w"), indent=1)
print(json.dumps({k: res[k] for k in ["reference_active_sites", "consensus_columns", "duf3536_family_conservation"]}, indent=1))
for n, v in per.items():
    print(n, v["label"], v["nucleophile"], v["acid_base"], {c: x["query"] for c, x in v["csr"].items()})
for r in sorted(dom_rows): print(r)
