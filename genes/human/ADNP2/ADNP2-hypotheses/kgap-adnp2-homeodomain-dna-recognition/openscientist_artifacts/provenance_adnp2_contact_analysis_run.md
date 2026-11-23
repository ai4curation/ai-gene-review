# Provenance: ADNP2 homeodomain DNA-contact analysis

Hypothesis slug: `kgap-adnp2-homeodomain-dna-recognition`. Run 2026-11-23 in the job's
`execute_code` Python executor. All inputs fetched live from UniProt REST, the InterPro API and
QuickGO. No local `*-bioinformatics` file was read. Biopython is not installed in this executor, so
BLOSUM62 and the profile scoring are written out in full below.

Figures produced by these cells: `provenance/plot_3.png` (naive extraction) and
`provenance/plot_4.png` (register corrected). `plot_4.png` is the one the report uses.
`provenance/plot_1.png` and `plot_2.png` are from the earlier exploratory cells in the same session.

## Cell 1: naive extraction, and the problem it exposed

The first pass took the UniProt `DNA binding` feature named "Homeobox" from every reviewed human
Pfam PF00046 protein and assumed each feature starts at canonical homeodomain position 1. Output
excerpt:

```
reviewed human PF00046 entries: 217 | ADNP2 present: False | ADNP present: True
consensus (n=238): GRRKRTAFTPSQLLELEKEFEKNRYPSRAEREELAASLGLTERQVKIWFQNRRAKWKKQE
helix 3, positions 48-53   consensus WFQNRR | ADNP HFSNKR | ADNP2 FFGKRR
base-contact consensus matches (of 6): ADNP2 0 | ADNP 1 | background 3.81 +/- 1.50
DNA-reading-surface log-odds over the 12 contact positions, background 30.5 +/- 13.1 (n=238)
  ADNP2 -8.2  z -2.95  percentile 2.1
  ADNP  1.5  z -2.21  percentile 6.3
background proteins with 0/6 base-contact matches: ZHX1, ZHX2, ZHX3, NANOGNB, POU4F1
   POU4F1    Q01851   matches 0/6  contact score  -13.5  percentile   1.3  helix3 48-53 FCNQRQ
```

POU4F1 is a POU-homeodomain factor with measured sequence-specific DNA binding, and its helix 3
came out as `FCNQRQ` rather than the expected `WFCNRR`. That is an off-register extraction, so the
assumption that every DNA_BIND feature begins at canonical position 1 is wrong for some entries.
Cell 2 fixes it.

## Cell 2: register-corrected analysis (the numbers used in the report)

```python
# =====================================================================
# Register correction. Each 60-mer is re-anchored by sliding a profile
# built from the first-pass consensus, then everything is recomputed.
# =====================================================================
import requests, numpy as np
from collections import Counter
import matplotlib.pyplot as plt

H = {"User-Agent": "Mozilla/5.0"}
def fa(a):
    return "".join(requests.get("https://rest.uniprot.org/uniprotkb/%s.fasta" % a,
                                timeout=60, headers=H).text.split("\n")[1:])
S2, S1 = fa("Q6IQ32"), fa("Q9H2P0")
HD2, HD1 = S2[1042:1102], S1[755:815]          # UniProt homeodomains 1043-1102 and 756-815

q = ("https://rest.uniprot.org/uniprotkb/search?query=xref:pfam-PF00046+AND+organism_id:9606+AND+reviewed:true"
     "&format=json&size=500&fields=accession,gene_primary,ft_dna_bind,sequence")
j = requests.get(q, timeout=120, headers=H).json()
raw = []   # (acc, gene, full sequence, annotated start)
for e in j["results"]:
    seq = e["sequence"]["value"]
    g = e.get("genes", [{}])[0].get("geneName", {}).get("value", e["primaryAccession"])
    for ft in e.get("features", []):
        if ft["type"] == "DNA binding" and "homeobox" in (ft.get("description") or "").lower():
            s, t = ft["location"]["start"]["value"], ft["location"]["end"]["value"]
            if s and t and 55 <= t - s + 1 <= 80 and s - 1 + 60 <= len(seq):
                raw.append((e["primaryAccession"], g, seq, s))
raw = [r for r in raw if r[0] not in ("Q6IQ32", "Q9H2P0")]   # background independent of the two test cases

BGF = {'A':.0788,'R':.0553,'N':.0419,'D':.0536,'C':.0193,'Q':.0393,'E':.0638,'G':.0707,
       'H':.0227,'I':.0591,'L':.0963,'K':.0595,'M':.0238,'F':.0397,'P':.0469,'S':.0683,
       'T':.0542,'W':.0121,'Y':.0303,'V':.0675}
a0 = 5.0                                        # Dirichlet pseudocount
def build(seqs):
    n = len(seqs)
    cols = [Counter(h[i] for h in seqs) for i in range(60)]
    pssm = [{a: np.log2(((c.get(a, 0) + a0*BGF[a]) / (n + a0)) / BGF[a]) for a in BGF} for c in cols]
    return cols, pssm, n
def score60(h, pssm): return sum(pssm[i].get(h[i], -4.0) for i in range(60))

cur = [seq[s-1:s+59] for _, _, seq, s in raw]   # pass 1: naive extraction at the annotated start
for it in range(4):
    cols, pssm, n = build(cur)
    new, shifts = [], []
    for (acc, g, seq, s), _ in zip(raw, cur):
        best, bo = -1e9, 0
        for off in range(-20, 21):
            st = s - 1 + off
            if st < 0 or st + 60 > len(seq): continue
            v = score60(seq[st:st+60], pssm)
            if v > best: best, bo = v, off
        new.append(seq[s-1+bo:s-1+bo+60]); shifts.append(bo)
    moved = sum(1 for a, b in zip(cur, new) if a != b)
    cur = new
    print("pass %d: %d of %d windows re-anchored, shift range %d to %d"
          % (it + 1, moved, len(cur), min(shifts), max(shifts)))
    if moved == 0: break

cols, pssm, N = build(cur)
cons  = "".join(c.most_common(1)[0][0] for c in cols)
consf = [c.most_common(1)[0][1] / N for c in cols]
bg = [(acc, g, h) for (acc, g, _, _), h in zip(raw, cur)]
print("\nregister-corrected consensus (n=%d):\n%s" % (N, cons))
print("fraction with W at 48: %.3f | F at 49: %.3f" % (consf[47], consf[48]))

BASE  = [3, 5, 47, 50, 51, 54]        # DNA base contacts
BBONE = [25, 28, 31, 53, 55, 57]      # phosphate backbone contacts
CORE  = [16, 20, 38, 40, 45, 48, 49]  # fold core
ANTP = "RKRGRQTYTRYQTLELEKEFHFNRYLTRRRRIEIAHALCLTERQIKIWFQNRRMKWKKEN"   # P02833, canonical 1-60
print("\npos role      Antp cons  freq   ADNP ADNP2 match")
for p in sorted(BASE + BBONE + CORE):
    r = "base" if p in BASE else ("backbone" if p in BBONE else "core")
    print("%3d %-9s %s    %s    %.3f  %s    %s     %s" % (p, r, ANTP[p-1], cons[p-1], consf[p-1],
                                                          HD1[p-1], HD2[p-1], HD2[p-1] == cons[p-1]))
print("\nhelix 3, 48-53   consensus %s | ADNP %s | ADNP2 %s" % (cons[47:53], HD1[47:53], HD2[47:53]))

def nm(h): return sum(h[p-1] == cons[p-1] for p in BASE)
bgm = np.array([nm(h) for _, _, h in bg])
CT = sorted(BASE + BBONE)
def cs(h): return sum(pssm[p-1].get(h[p-1], -4.0) for p in CT)
bgs = np.array([cs(h) for _, _, h in bg])
mu, sd = bgs.mean(), bgs.std(ddof=1)
v2, v1 = cs(HD2), cs(HD1)
print("\nbase-contact consensus matches (of 6): ADNP2 %d | ADNP %d | background %.2f +/- %.2f"
      % (nm(HD2), nm(HD1), bgm.mean(), bgm.std(ddof=1)))
print("DNA-reading-surface log-odds: background %.1f +/- %.1f" % (mu, sd))
print("  ADNP2 %.1f  z %.2f  percentile %.1f" % (v2, (v2-mu)/sd, 100*(bgs < v2).mean()))
print("  ADNP  %.1f  z %.2f  percentile %.1f" % (v1, (v1-mu)/sd, 100*(bgs < v1).mean()))

print("\nbackground entries with 0/6 base-contact matches:")
zs = sorted([(cs(h), g, a, h) for a, g, h in bg if nm(h) == 0])
for v, g, a, h in zs:
    print("   %-9s %-8s contact %6.1f  percentile %5.1f  helix3 48-53 %s" % (g, a, v, 100*(bgs < v).mean(), h[47:53]))
print("total 0/6 entries: %d of %d" % (len(zs), N))

print("\ncontrols:")
for g0 in ["PITX2", "EN2", "HOXB13", "CUX1", "POU4F1", "POU5F1", "ZHX1", "ZHX2", "ZHX3", "NANOG", "NANOGNB"]:
    for a, g, h in bg:
        if g == g0:
            print("   %-8s %-8s %d/6  contact %6.1f  percentile %5.1f  helix3 %s"
                  % (g, a, nm(h), cs(h), 100*(bgs < cs(h)).mean(), h[47:53]))
            break

fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.2))
ax[0].hist(bgs, bins=30, color="#9aa7c7", edgecolor="white")
ax[0].axvline(v2, color="#d1495b", lw=2.5); ax[0].axvline(v1, color="#2a9d8f", lw=2.5)
ax[0].annotate("ADNP2 %.1f" % v2, (v2, ax[0].get_ylim()[1]*0.90), color="#d1495b", fontsize=10)
ax[0].annotate("ADNP %.1f" % v1, (v1, ax[0].get_ylim()[1]*0.74), color="#2a9d8f", fontsize=10)
ax[0].set_xlabel("DNA-reading-surface log-odds, 12 contact positions")
ax[0].set_ylabel("human homeodomains (n=%d)" % N)
ax[0].set_title("Contact-surface score, register corrected")
vals, cnts = np.unique(bgm, return_counts=True)
ax[1].bar(vals, cnts, color="#9aa7c7", edgecolor="white")
if 0 in list(vals): ax[1].bar([0], [cnts[list(vals).index(0)]], color="#d1495b")
ax[1].set_xlabel("base-contact positions matching consensus, of 6")
ax[1].set_ylabel("human homeodomains")
ax[1].set_title("ADNP2 %d/6, ADNP %d/6, background mean %.2f" % (nm(HD2), nm(HD1), bgm.mean()))
plt.tight_layout(); plt.show()
```

### Verbatim output

```
pass 1: 6 of 240 windows re-anchored, shift range -7 to 2
pass 2: 0 of 240 windows re-anchored, shift range -7 to 2

register-corrected consensus (n=240):
GRRKRTAFTSSQLLELEKEFEKNRYPSRAEREELAAALGLTERQVKIWFQNRRAKWKKQE
fraction with W at 48: 0.975 | F at 49: 0.979

pos role      Antp cons  freq   ADNP ADNP2 match
  3 base      R    R    0.521  G    K     False
  5 base      R    R    0.875  E    E     False
 16 core      L    L    0.946  L    L     True
 20 core      F    F    0.887  F    F     True
 25 backbone  Y    Y    0.688  Y    Y     True
 28 backbone  R    R    0.208  R    K     False
 31 backbone  R    R    0.696  I    I     False
 38 core      L    L    0.525  L    F     False
 40 core      L    L    0.838  L    V     False
 45 core      I    V    0.688  I    V     True
 47 base      I    I    0.421  S    S     False
 48 core      W    W    0.975  H    F     False
 49 core      F    F    0.979  F    F     True
 50 base      Q    Q    0.725  S    G     False
 51 base      N    N    0.921  N    K     False
 53 backbone  R    R    0.963  R    R     True
 54 base      M    A    0.346  K    Y     False
 55 backbone  K    K    0.742  K    I     False
 57 backbone  K    K    0.512  V    M     False

helix 3, 48-53   consensus WFQNRR | ADNP HFSNKR | ADNP2 FFGKRR

base-contact consensus matches (of 6): ADNP2 0 | ADNP 1 | background 3.81 +/- 1.50
DNA-reading-surface log-odds: background 30.4 +/- 13.1
  ADNP2 -8.2  z -2.94  percentile 2.1
  ADNP  2.6  z -2.12  percentile 6.7

background entries with 0/6 base-contact matches:
   ZHX3      Q9H4I2   contact  -27.7  percentile   0.0  helix3 48-53 WFAEKM
   ZHX1      Q9UKY1   contact  -26.9  percentile   0.4  helix3 48-53 WFTEKK
   ZHX1      Q9UKY1   contact  -16.3  percentile   0.8  helix3 48-53 WFAERQ
   ZHX2      Q9Y6X8   contact  -10.3  percentile   1.2  helix3 48-53 WFSERR
   ZHX3      Q9H4I2   contact   -9.2  percentile   1.7  helix3 48-53 WFSERR
   ZHX2      Q9Y6X8   contact   -5.9  percentile   2.1  helix3 48-53 WFKENR
   NANOGNB   Q7Z5D8   contact   -5.6  percentile   2.5  helix3 48-53 WFCKTR
   ZHX2      Q9Y6X8   contact   -5.4  percentile   2.9  helix3 48-53 WFSDHR
   ZHX3      Q9H4I2   contact   -4.7  percentile   3.3  helix3 48-53 WFGDSR
   ZHX1      Q9UKY1   contact   -4.2  percentile   3.8  helix3 48-53 WFGDTR
   ZHX3      Q9H4I2   contact   -2.0  percentile   5.0  helix3 48-53 WFSDRR
total 0/6 entries: 11 of 240

controls:
   PITX2    Q99697   4/6  contact   35.3  percentile  51.2  helix3 WFKNRR
   EN2      P19622   6/6  contact   39.0  percentile  76.2  helix3 WFQNKR
   HOXB13   Q92826   4/6  contact   32.6  percentile  37.1  helix3 WFQNRR
   CUX1     P39880   2/6  contact   23.7  percentile  17.5  helix3 WFHNYR
   POU4F1   Q01851   3/6  contact   27.8  percentile  22.9  helix3 WFCNQR
   POU5F1   Q01860   3/6  contact   27.8  percentile  22.5  helix3 WFCNRR
   ZHX1     Q9UKY1   1/6  contact    4.5  percentile   6.7  helix3 WFSAQR
   ZHX2     Q9Y6X8   1/6  contact   -0.6  percentile   5.8  helix3 WFATQR
   ZHX3     Q9H4I2   1/6  contact    0.9  percentile   6.2  helix3 WFTAQR
   NANOG    Q9H9S0   3/6  contact   31.4  percentile  34.6  helix3 WFQNQR
   NANOGNB  Q7Z5D8   0/6  contact   -5.6  percentile   2.5  helix3 WFCKTR
```

Register correction moved 6 of 240 windows, converged after one pass, and put POU4F1 and POU5F1
back on `WFCNQR` and `WFCNRR` at 3/6 and the 23rd percentile. The 0/6 set is then 11 of 240 entries,
all ZHX1, ZHX2, ZHX3 or NANOGNB. ADNP2 and ADNP are unaffected, since their own 60-mers come from
the UniProt homeodomain boundaries and were held out of the background.

## Cell 3: net charge, InterPro signatures, QuickGO provenance

Same session, same fetch pattern. Verbatim output:

```
net charge: ADNP2 +8.1 (percentile 45) | ADNP +6.2 | background 8.2 +/- 3.3

ADNP2 (Q6IQ32) signatures over the homeodomain region:
    cdd        cd00086          1044-1100
    smart      SM00389          1043-1105
    ssf        SSF46689         1042-1106

ADNP (Q9H2P0) signatures over the homeodomain region:
    cathgene3d G3DSA:1.10.10.60  764- 819
    cdd        cd00086           768- 813
    pfam       PF00046           769- 810
    profile    PS50071           771- 814
    smart      SM00389           757- 818
    ssf        SSF46689          769- 818

QuickGO annotations for UniProtKB:Q6IQ32 (18 rows)
   GO:0000981  ISA  ECO:0005556  GO_REF:0000113  NTNU_SB
   GO:0003677  IEA  ECO:0000256  GO_REF:0000002  InterPro
   GO:0005515  IPI  ECO:0000353  PMID:21888893   IntAct
   GO:0005515  IPI  ECO:0000353  PMID:24981860   IntAct
   GO:0005515  IPI  ECO:0000353  PMID:27705803   IntAct
   GO:0005515  IPI  ECO:0000353  PMID:32296183   IntAct
   GO:0005515  IPI  ECO:0000353  PMID:33961781   IntAct
   GO:0005515  IPI  ECO:0000353  PMID:35271311   IntAct
   GO:0006357  IEA  ECO:0000364  GO_REF:0000108  GOC
   GO:0007399  ISS  ECO:0000250  GO_REF:0000024  UniProt
   GO:0007399  IEA  ECO:0000265  GO_REF:0000107  Ensembl
   GO:0010468  IBA  ECO:0000318  GO_REF:0000033  GO_Central
   GO:0005634  IBA  ECO:0000318  GO_REF:0000033  GO_Central
   GO:0000785  ISA  ECO:0005556  GO_REF:0000113  NTNU_SB
   GO:0005634  IEA  ECO:0007322  GO_REF:0000044  UniProt
```

The `goName` field came back null for every row in this QuickGO response, so the term labels above
are the standard GO labels for those identifiers rather than strings returned by the API:
GO:0000981 DNA-binding transcription factor activity RNA polymerase II-specific, GO:0003677 DNA
binding, GO:0005515 protein binding, GO:0006357 regulation of transcription by RNA polymerase II,
GO:0007399 nervous system development, GO:0010468 regulation of gene expression, GO:0005634 nucleus,
GO:0000785 chromatin.

## Earlier cells in the same session (not reprinted here)

The AlphaFold and ortholog results quoted in the report came from earlier cells of this session:

- AlphaFold DB `https://alphafold.ebi.ac.uk/api/prediction/Q6IQ32`, model AF-Q6IQ32-F1-model_v6,
  pLDDT read from the PDB B-factor column, helices called from CA(i) to CA(i+4) distances in
  5.0 to 6.8 Angstrom. Residues 1043-1102 mean pLDDT 85.3, min 58.6, 90 % above 70, against a
  whole-chain mean of 56.9. ADNP 756-815 mean pLDDT 88.4, 100 % above 70.
- Ortholog frequencies from UniProt `/search` on gene name with one entry kept per species,
  52 ADNP2 species and 68 ADNP species, aligned to the human 60-mer without gaps.
- Zinc-finger check: the regex `C.{2,4}C.{12}H.{3,5}H` applied to the nine UniProt ZN_FING
  intervals of Q6IQ32 matched 4 (73-96, 155-178, 770-793, 875-898); interval 913-937 contains
  only two histidines.
