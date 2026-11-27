#!/usr/bin/env python3
"""SNRPGP15 (A8MWD9) vs SNRPG (P62308): reading frame, Sm-ring/RNA contacts, proteomics.

Run: uv run --with biopython --with requests python analyze.py > analysis_output.txt

Everything is fetched live; no results are hardcoded.
  1. UniProt sequences -> global alignment, list substitutions.
  2. Ensembl genomic locus of ENSG00000224543 (+/- flank) -> 6-frame translation,
     locate the A8MWD9 ORF, check for in-frame stops / frameshifts.
  3. PDB 4PJO (human minimal U1 snRNP, Sm ring + U1 snRNA) -> residues of SmG within
     4.0 A of RNA and of neighbouring Sm subunits; report status of each substituted
     position.
  4. EBI Proteins API proteomics features for A8MWD9 -> which observed peptides are
     unique to the entry; in-silico tryptic peptides that would discriminate the
     product from SNRPG.
"""
import io
import json
import re
import sys

import requests
from Bio import Align
from Bio.Align import substitution_matrices
from Bio.PDB import MMCIFParser, NeighborSearch
from Bio.PDB.Polypeptide import three_to_index, index_to_one
from Bio.Seq import Seq

TARGET, PARENT = "A8MWD9", "P62308"
ENSG = "ENSG00000224543"
PDB_ID = "4PJO"
CUTOFF = 4.0


def uniprot_seq(acc):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def align(a, b):
    al = Align.PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    return al.align(a, b)[0]


def residue_map(aln):
    """Map parent position -> target position (1-based) from an alignment."""
    m = {}
    for (ts, te), (ps, pe) in zip(*aln.aligned):
        for i in range(te - ts):
            m[ps + i + 1] = ts + i + 1
    return m


print("## 1. Pairwise alignment SNRPGP15 (A8MWD9) vs SNRPG (P62308)")
t, p = uniprot_seq(TARGET), uniprot_seq(PARENT)
print(f"len target={len(t)} parent={len(p)}")
aln = align(t, p)
print(aln)
pmap = residue_map(aln)
subs = []
gaps = len(t) - sum(te - ts for ts, te in aln.aligned[0]) + len(p) - sum(pe - ps for ps, pe in aln.aligned[1])
for ppos, tpos in sorted(pmap.items()):
    if p[ppos - 1] != t[tpos - 1]:
        subs.append((ppos, p[ppos - 1], tpos, t[tpos - 1]))
ident = sum(1 for pp, tp in pmap.items() if p[pp - 1] == t[tp - 1])
print(f"identical={ident}/{len(p)} ({100*ident/len(p):.1f}%), unaligned residues={gaps}")
print("substitutions (parent pos/aa -> target pos/aa):")
for s in subs:
    print(f"  SNRPG {s[1]}{s[0]} -> SNRPGP15 {s[3]}{s[2]}")

print("\n## 2. Genomic locus: is the reading frame intact?")
lk = requests.get(f"https://rest.ensembl.org/lookup/id/{ENSG}", headers={"Content-Type": "application/json"}, timeout=60).json()
print(f"{ENSG} biotype={lk.get('biotype')} {lk['seq_region_name']}:{lk['start']}-{lk['end']} strand={lk['strand']}")
flank = 300
reg = f"{lk['seq_region_name']}:{lk['start']-flank}..{lk['end']+flank}:{lk['strand']}"
dna = requests.get(f"https://rest.ensembl.org/sequence/region/human/{reg}", headers={"Content-Type": "text/plain"}, timeout=60).text.strip()
found = False
for strand_name, s in (("+", Seq(dna)), ("-", Seq(dna).reverse_complement())):
    for f in range(3):
        sub = s[f:]
        sub = sub[: len(sub) // 3 * 3]
        prot = str(sub.translate())
        idx = prot.find(t)
        if idx >= 0:
            found = True
            nxt = prot[idx + len(t): idx + len(t) + 1]
            print(f"A8MWD9 found exactly, strand {strand_name} frame {f}; codon after last residue translates to '{nxt}' (* = stop)")
            print(f"internal stops within ORF: {prot[idx:idx+len(t)].count('*')}")
if not found:
    # report best partial match per frame
    print("A8MWD9 NOT found as an exact uninterrupted translation; best frames:")
    for strand_name, s in (("+", Seq(dna)), ("-", Seq(dna).reverse_complement())):
        for f in range(3):
            sub = s[f:]
            sub = sub[: len(sub) // 3 * 3]
            prot = str(sub.translate())
            a = align(prot, t)
            print(f"  strand {strand_name} frame {f}: score {a.score:.0f}")
            if a.score > 100:
                print(a)
                (ps0, pe0) = (a.aligned[0][0][0], a.aligned[0][-1][1])
                seg = prot[ps0:pe0]
                print(f"  genomic translation of aligned segment: {seg}")
                print(f"  in-frame stop codons within segment: {seg.count('*')} at offsets {[i+1 for i,c in enumerate(seg) if c=='*']}")
                print(f"  number of gapped blocks (indels => frameshift/insertion): {len(a.aligned[0])}")
                nt0 = f + ps0 * 3
                codons = [str(sub[i:i+3]) for i in range(ps0 * 3, (ps0 + len(t) + 1) * 3, 3)]
                print("  codons for target positions 70..end+1 (genomic, GRCh38):")
                for k in range(69, min(len(codons), len(t) + 1)):
                    aa = str(Seq(codons[k]).translate())
                    exp = t[k] if k < len(t) else "(after end)"
                    gpos = lk["start"] - flank + nt0 + 3 * (k) if lk["strand"] == 1 else None
                    print(f"    pos {k+1}: {codons[k]} -> {aa}  (UniProt A8MWD9: {exp}; chr{lk['seq_region_name']}:{gpos}-{gpos+2 if gpos else ''})")

print("\n## 2b. Same locus in the EMBL clone cited by UniProt (AC012318)")
emb = requests.get("https://www.ebi.ac.uk/ena/browser/api/fasta/AC012318", timeout=120).text
embseq = Seq("".join(emb.splitlines()[1:]).upper())
print("AC012318 header:", emb.splitlines()[0][:120], "len", len(embseq))
hit = False
for strand_name, s2 in (("+", embseq), ("-", embseq.reverse_complement())):
    for f in range(3):
        sub2 = s2[f:]
        sub2 = sub2[: len(sub2) // 3 * 3]
        prot2 = str(sub2.translate())
        for probe in (t[:40],):
            i = prot2.find(probe)
            if i >= 0:
                hit = True
                seg2 = prot2[i:i + len(t) + 2]
                print(f"strand {strand_name} frame {f}: translation from Met1: {seg2}")
                print(f"  codon 75 in clone: {sub2[(i+74)*3:(i+75)*3]}; matches UniProt sequence exactly: {seg2[:len(t)] == t}")
if not hit:
    print("A8MWD9 N-terminal 40 aa not found in AC012318 translation")

print("\n## 2c. Known variants at codon 75 (Ensembl variation, GRCh38)")
c75 = lk["start"] + 74 * 3  # first base of codon 75 (plus strand gene)
ov = requests.get(f"https://rest.ensembl.org/overlap/region/human/{lk['seq_region_name']}:{c75}-{c75+2}?feature=variation",
                  headers={"Content-Type": "application/json"}, timeout=60).json()
for v in ov:
    det = requests.get(f"https://rest.ensembl.org/variation/human/{v['id']}?pops=1", headers={"Content-Type": "application/json"}, timeout=60).json()
    locs = [(m["location"], m["allele_string"]) for m in det.get("mappings", [])]
    freqs = [(pp["population"], pp["allele"], pp["frequency"]) for pp in det.get("populations", []) if pp["population"].startswith("gnomAD") and pp["population"].endswith(":ALL")]
    print(f"  {v['id']} {locs} gnomAD ALL allele freqs: {freqs}")

print("\n## 2d. EST CK005235 (cited by UniProt, frontal cortex) translation")
est = requests.get("https://www.ebi.ac.uk/ena/browser/api/fasta/CK005235", timeout=60).text
estseq = Seq("".join(est.splitlines()[1:]).upper())
print("header:", est.splitlines()[0][:120], "len", len(estseq))
for strand_name, s3 in (("+", estseq), ("-", estseq.reverse_complement())):
    for f in range(3):
        sub3 = s3[f:]
        sub3 = sub3[: len(sub3) // 3 * 3]
        prot3 = str(sub3.translate())
        i = prot3.find("MSKAHPP")
        if i >= 0:
            seg3 = prot3[i:i + len(t) + 1]
            print(f"  strand {strand_name} frame {f}: {seg3}")
            print(f"  identity to SNRPGP15: {sum(a==b for a,b in zip(seg3,t))}/{len(t)}; to SNRPG: {sum(a==b for a,b in zip(seg3,p))}/{len(p)}")
            print(f"  differences vs SNRPGP15: {[f'{t[k]}{k+1}{seg3[k]}' for k in range(min(len(seg3),len(t))) if seg3[k]!=t[k]]}")
            print(f"  differences vs SNRPG: {[f'{p[k]}{k+1}{seg3[k]}' for k in range(min(len(seg3),len(p))) if seg3[k]!=p[k]]}")

print(f"\n## 3. Structural contacts of SmG in PDB {PDB_ID} (cutoff {CUTOFF} A)")
cif = requests.get(f"https://files.rcsb.org/download/{PDB_ID}.cif", timeout=120).text
struct = MMCIFParser(QUIET=True).get_structure(PDB_ID, io.StringIO(cif))
model = next(iter(struct))


def chain_seq(ch):
    out = []
    for r in ch:
        try:
            out.append(index_to_one(three_to_index(r.get_resname())))
        except Exception:
            pass
    return "".join(out)


from Bio.PDB.MMCIF2Dict import MMCIF2Dict
cd = MMCIF2Dict(io.StringIO(cif))
ent_desc = dict(zip(cd["_entity.id"], cd["_entity.pdbx_description"]))
chain_desc = {}
for eid, strands in zip(cd["_entity_poly.entity_id"], cd["_entity_poly.pdbx_strand_id"]):
    for c in strands.split(","):
        chain_desc[c.strip()] = ent_desc.get(eid, "?").strip()
prot_chains, rna_chains = [], []
for ch in model:
    res = list(ch)
    nuc = sum(1 for r in res if "C1'" in r)
    if res and nuc > len(res) / 2:
        rna_chains.append(ch)
    else:
        prot_chains.append(ch)
# identify SmG chains: best alignment to SNRPG with high identity
smg = []
for ch in prot_chains:
    cs = chain_seq(ch)
    if len(cs) < 40:
        continue
    a = align(cs, p)
    idn = sum(1 for (cs0, ce), (ps0, pe) in zip(*a.aligned) for i in range(ce - cs0) if cs[cs0 + i] == p[ps0 + i])
    if idn / len(cs) > 0.9 and len(cs) < 100:
        smg.append(ch)
print("SmG chain(s):", [c.id for c in smg], "| RNA chains:", [c.id for c in rna_chains])
atoms = [a for a in model.get_atoms()]
ns = NeighborSearch(atoms)
for ch in smg[:1]:  # first SmG copy; RNA/ring contacts are equivalent across copies
    print(f'Using SmG chain {ch.id}; RNA chains = ' + str({c.id: chain_desc.get(c.id) for c in rna_chains}))
    # residue numbering in 4PJO follows UniProt numbering for SmG? verify by sequence
    cs_res = [r for r in ch if r.id[0] == " "]
    cs = chain_seq(ch)
    a = align(cs, p)
    chain_to_parent = {}
    for (cs0, ce), (ps0, pe) in zip(*a.aligned):
        for i in range(ce - cs0):
            chain_to_parent[cs0 + i] = ps0 + i + 1
    contacts = {}
    for i, r in enumerate(cs_res):
        ppos = chain_to_parent.get(i)
        if ppos is None:
            continue
        partners = set()
        for at in r:
            for nb in ns.search(at.coord, CUTOFF):
                pc = nb.get_parent().get_parent()
                if pc.id == ch.id:
                    continue
                kind = "RNA:" if pc.id in {c.id for c in rna_chains} else "protein:"
                partners.add(kind + chain_desc.get(pc.id, pc.id))
        contacts[ppos] = partners
    rna_contacts = sorted(k for k, v in contacts.items() if any(x.startswith("RNA") for x in v))
    prot_contacts = sorted(k for k, v in contacts.items() if any(x.startswith("protein") for x in v))
    print(f"SmG positions modelled: {min(contacts)}-{max(contacts)} ({len(contacts)} residues)")
    print("SmG residues contacting RNA:", ", ".join(f"{p[k-1]}{k}" for k in rna_contacts))
    print("SmG residues contacting other protein chains:", ", ".join(f"{p[k-1]}{k}" for k in prot_contacts))
    print("Status of SNRPGP15 substitutions:")
    for ppos, paa, tpos, taa in subs:
        if ppos not in contacts:
            st = "not modelled in structure"
        else:
            st = ", ".join(sorted(contacts[ppos])) or "no contacts (surface/core, no partner within cutoff)"
        print(f"  {paa}{ppos}->{taa}: {st}")
    print("Side-chain-only contacts (atoms beyond CB excluded backbone N/CA/C/O) at substituted positions:")
    for ppos, paa, tpos, taa in subs:
        r = next((rr for i, rr in enumerate(cs_res) if chain_to_parent.get(i) == ppos), None)
        if r is None:
            continue
        sc = [a for a in r if a.get_id() not in ("N", "CA", "C", "O")]
        parts = {}
        for at in sc:
            for nb in ns.search(at.coord, CUTOFF):
                pr_ = nb.get_parent()
                pc = pr_.get_parent()
                if pc.id == ch.id:
                    continue
                parts.setdefault(chain_desc.get(pc.id, pc.id), set()).add(f"{pr_.get_resname()}{pr_.id[1]}")
        print(f"  {paa}{ppos}->{taa}: {parts or 'none'}")
    print("Retention of RNA- and protein-contact residues in SNRPGP15:")
    for k in sorted(set(rna_contacts) | set(prot_contacts)):
        tk = pmap.get(k)
        print(f"  SNRPG {p[k-1]}{k} -> SNRPGP15 {t[tk-1] if tk else '-'}{tk or ''} {'RETAINED' if tk and t[tk-1]==p[k-1] else 'CHANGED'}")

print("\n## 4. Proteomics evidence (EBI Proteins API)")
pr = requests.get(f"https://www.ebi.ac.uk/proteins/api/proteomics?accession={TARGET}", headers={"Accept": "application/json"}, timeout=60).json()
feats = pr[0]["features"] if pr else []
uniq = 0
for f in feats:
    srcs = []
    for e in f.get("evidences", []):
        s = e.get("source", {})
        srcs.append(f"{s.get('name')}(maps={s.get('properties',{}).get('Number of protein mappings','?')})")
    uniq += bool(f.get("unique"))
    print(f"  {f['begin']}-{f['end']} {f['peptide']} api_unique_flag={f.get('unique')} also_in_SNRPG={f['peptide'] in p} {' '.join(srcs)}")
print(f"observed peptides: {len(feats)}; flagged unique by API: {uniq}; NOT a substring of SNRPG: {sum(1 for f in feats if f['peptide'] not in p)}")
covered_subs = [s for s in subs if any(int(f['begin']) <= s[2] <= int(f['end']) for f in feats)]
print("observed peptides spanning a SNRPGP15-specific residue:", [f"{s[3]}{s[2]}" for s in covered_subs] or "none")


def tryptic(seq):
    return [x for x in re.sub(r"(?<=[KR])(?!P)", ",", seq).split(",") if x]


tp, pp = set(tryptic(t)), set(tryptic(p))
disc = sorted(x for x in tp - pp if 6 <= len(x) <= 30)
print("in-silico tryptic peptides (6-30 aa) present in SNRPGP15 but not SNRPG:", disc)
obs = {f["peptide"] for f in feats}
print("of which observed:", sorted(obs & set(disc)) or "none")
