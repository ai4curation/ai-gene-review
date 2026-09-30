# Scn9a (naked mole-rat NaV1.7) — domain IV P-loop motif and fragment extent

Reproduce with:

```bash
python3 genes/HETGA/Scn9a/Scn9a-bioinformatics/div_ploop_motif.py
```

Standard library only; UniProt FASTA downloads are cached under `data/`. The naked
mole-rat sequence is read from `genes/HETGA/Scn9a/Scn9a-uniprot.txt` (UniProt G9DCX3),
which is the sequence submitted with EMBL JF912494 by the Smith et al. authors
(PMID:22174253).

## Question

Smith, Park & Lewin (PMID:32206859) describe the naked mole-rat NaV1.7 acid-block
variant as a charge-changing substitution in a trio of amino acids in domain IV:
KKV (+/+/0) in mouse and human, EKD or EKE in subterranean African mole-rats. Harms
et al. (PMID:28939386) place the motif specifically in the domain IV P-loop. The
primary papers that report this (PMID:22174253, PMID:31147513) are abstract-only in
this repository's publication cache and give no residue numbers, so the motif is
checked directly against the sequences rather than quoted from memory.

## Method

The triplet is located by the regular expression `D[CS][DN]P(...)HPG`, anchored on
residues of the domain IV extracellular S5-S6 loop that are invariant across the whole
panel. A sequence lacking the anchor is reported as NOT FOUND rather than silently
mis-assigned. Fragment extent is estimated from `difflib` matching blocks of at
least five residues against full-length human Q15858.

## Result

| species | accession | length | triplet | position | context |
|---|---|---|---|---|---|
| naked mole-rat (*Heterocephalus glaber*) | G9DCX3 | 1884 | **EKE** | 1698 | SGPPDCDP**EKE**HPGSSVKGD |
| human (*Homo sapiens*) | Q15858 | 1988 | KKV | 1718 | SKPPDCDP**KKV**HPGSSVEGD |
| mouse (*Mus musculus*) | Q62205 | 1984 | KKV | 1716 | SAPPDCDP**KKV**HPGSSVEGD |
| rat (*Rattus norvegicus*) | O08562 | 1984 | KKV | 1716 | SAPPDCDP**KKV**HPGSSVEGD |
| rabbit (*Oryctolagus cuniculus*) | Q28644 | 1984 | KKV | 1715 | SAPPDCDP**KKV**HPGSSTEGD |
| guinea pig (*Cavia porcellus*) | H0VMS3 | 1986 | HKV | 1716 | SGPPDCDP**HKV**HPGSLTEGD |
| 13-lined ground squirrel (*Ictidomys tridecemlineatus*) | I3M736 | 1976 | KKV | 1706 | NGPPDCDP**KKV**HPGSSVEGD |

The naked mole-rat NaV1.7 sequence G9DCX3 carries EKE at fragment positions 1698-1700, where human Q15858 carries KKV at 1718-1720, in the domain IV extracellular P-loop.

The charge change is exactly the one described in the literature: two of the three
positions lose a positive charge and gain a negative one, giving a net swap of
+2 to -2. Guinea pig, the closest sampled hystricomorph relative, retains the
ancestral-type KV with only a conservative K-to-H change at the first position, so the
EKE motif is not a general hystricomorph feature. The one hibernator sampled here
retains KKV; no attempt was made to reproduce the broad hibernator survey of
PMID:24352952.

## Where the motif sits in the topology

Taking the UniProt feature table for G9DCX3 at face value, the domain IV transmembrane
helices flanking the pore are 1613-1641 (S5) and 1717-1740 (S6). The intervening
1642-1716 stretch is the extracellular P-loop, and it reads:

```
GMSNFAYVKKEAGIDDMFNFETFGNSMICLFQITTSAGWDGLLAPILNSGPPDCDPEKEHPGSSVKGDCGNPSVG
```

The EKE triplet at 1698-1700 therefore lies in the distal, C-terminal half of that
loop, well after the pore-helix/selectivity-filter region and shortly before S6.

**This is a location, not a mechanism.** Harms et al. (PMID:28939386) modelled the
corresponding human residues and concluded that they do not line the pore lumen and
are too far from the pore mouth for simple steric occlusion to explain the proton
block, and that motif charge alone does not predict proton sensitivity across other
NaV alpha subunits. Their patch-clamp work does confirm the core observation — putting
the naked mole-rat EKE motif into human NaV1.7 increases proton-evoked tonic
inhibition — but also reports that it reduces channel function. So the sequence
difference reported here should be read as the well-replicated sequence correlate of
enhanced proton block, with the physical mechanism still open.

## Fragment extent

| quantity | value |
|---|---|
| G9DCX3 length | 1884 aa (UniProt `Flags: Fragment`, `NON_TER` at both 1 and 1884) |
| Q15858 length | 1988 aa |
| fragment spans human residues | ~23-1901 |
| human residues missing at N-terminus | 22 |
| human residues missing at C-terminus | 87 |
| identity within matched blocks | 92.1% of the fragment |

The missing segments are the short N-terminal cytoplasmic head and the distal
cytoplasmic C-terminal tail. Everything between is present: the UniProt feature
table records four complete Pfam PF00520 ion-transport (S1-S6) domains at 105-390,
724-955, 1171-1446 and 1495-1750, the PF11933 domain III-IV cytoplasmic
inactivation-gate region at 515-674 (plus the CDD Na_channel_gate match), the
PF06512 sodium-ion-transport-associated domain at 962-1167, and the PF24609
SCN5A-like C-terminal IQ motif at 1862-1883.

The pore-forming and voltage-sensing machinery of the channel is therefore complete in this entry, and the truncation does not undercut molecular-function or cellular-component claims about the channel. It does mean the entry cannot support
claims about the distal C-terminal tail, and the UniProt `CAUTION` line ("Lacks
conserved residue(s) required for the propagation of feature annotation") should be
read against that truncation rather than as a statement about the channel core.
