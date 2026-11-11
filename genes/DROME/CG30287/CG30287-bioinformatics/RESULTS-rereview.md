# CG30287 (Q8MLV8) sequence checks and tree placement, re-review 2026-10-21

## 1. Sequence features

Script: `sequence_features_rereview.py`, run on the cached `CG30287-uniprot.txt` (284 aa, sequence version 1). No external tools and no alignment; positions come from the UniProt feature table, and residues are read off the sequence.

```
length	284
act_site	82	H	context=VLTAAHCKSET
act_site	136	D	context=NFRKNDIALLR
act_site	232	S	context=TCQGDSGGPLT
ser195_segment	226-235	STCQGDSGGP
S1_pocket_pos189	226	S
domain_start	42	preceding=R41	mature_N=VINGK
propeptide	22-41	length=20	cys=1	QPHLLDPQCVTARSEPGLYR
cysteines	10	30,67,83,106,111,156,205,219,228,261
```

Interpretation:

- The catalytic triad is intact: His82 (in TAAHC), Asp136 and Ser232 in the canonical GDSGGP motif.
- The residue six positions N-terminal of the catalytic serine, at the position of chymotrypsinogen residue 189 at the base of the S1 pocket, is Ser226 (segment STCQGDSGGP). It is not the Asp of trypsin-like enzymes, so a strict Arg/Lys P1 preference is not predicted. Ser189 is also found in chymotrypsin. Positions 216 and 226 were not mapped without an alignment, so no P1 specificity is assigned.
- The protease domain starts at Val42 (mature N-terminus VINGK), preceded by Arg41. This is a candidate zymogen activation site cleaved after Arg. Val at position 16 is common in active S1 proteases, but Asn in place of the usual Gly18 is atypical. Activation has not been tested.
- The propeptide between the signal peptide (1-21) and the protease domain is 20 residues long and contains one cysteine (Cys30). It is far too short for a clip domain (about 35-55 residues with six cysteines), so CG30287 is a single-domain S1 protease, not a CLIP-domain protease. This disagrees with UniProt's ARBA-only "CLIP subfamily" statement. Cys30 could form the chymotrypsinogen-type interchain disulfide that keeps the propeptide attached after activation; this connectivity is not verified.

## 2. PANTHER tree placement

Source: PANTHER 19.0 tree for PTHR24256, retrieved from the PANTHER treeinfo service
(`https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR24256`) on 2026-10-21. The ancestors of the Q8MLV8 leaf (PTN000668563) were walked in Python. The JSON was kept in the session scratchpad and not committed.

- Subfamily PTHR24256:SF553 ("IP20273P-RELATED"). In PANTHER 19.0, the D. melanogaster members are CG30083, CG11531, CR30082, CG30088, CG33226, CG30287 (SPH37), CG33225, Jon99Ciii and CG4914 (node PTN002385742, all *Drosophila*). Three *Anopheles* sequences join them at PTN002799502, and two *Tribolium* sequences at PTN002799547.
- PTN002799547 sits in an unresolved polytomy (PTN002799546) with four other insect clades. These are the easter/Sp7/Anopheles CLIPB clade (PTN002799500, which includes Easter, P13582), the SP20/SP22/SP40/tpr clade (PTN002799512), CG11836 (PTN002799496) and the CG30288/CG30289/CG30414/SPH158 clade (PTN008611284).
- The serine-type endopeptidase activity IBD (GO:0004252), and the proteolysis and extracellular-region IBDs, are placed at the much deeper node PTN001207268. Easter (FB:FBgn0000533) is among its donors. Every *Drosophila* NOT|GO:0004252 IKR node in the family PAINT file (for example PTN002385744 = CG33225 alone) lies outside the CG30287 lineage. CG30287 is not under any NOT node. Its full ancestor path is PTN002799329 > PTN001207268 > PTN007783152 > PTN009088552 > PTN007783153 > PTN009088589 > PTN008611263 > PTN002799381 > PTN001208349 > PTN002799546 > PTN002799547 > PTN002799502 > PTN002385742 > PTN000668563 (leaf). The innate-immune-response IBD (GO:0045087, node PTN000667087) is not on this path, so PAINT does not propagate an immune role to CG30287.
- Within SF553, the only experimental GO data found in QuickGO (queried 2026-10-21) are HDA "serine hydrolase activity" rows for CG4914 and Jon99Ciii, from the activity-based profiling atlas PMID:33827210. No SF553 member has a characterised substrate or physiological role.

Conclusion: no experimentally characterised ortholog of CG30287 exists. Its nearest characterised relatives are the members of the sister clades in the PTN002799546 polytomy, of which Easter is the best studied and is the PAINT donor for the inherited catalytic activity. Easter's subfamily-specific roles (dorsoventral patterning, Spätzle processing) cannot be transferred, because CG30287 lies in a different subfamily (SF553 vs SF527) and lacks Easter's clip domain.
