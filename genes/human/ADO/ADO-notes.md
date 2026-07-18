# ADO (2-aminoethanethiol / cysteamine dioxygenase) — curation notes

UniProt: Q96SZ5 (AEDO_HUMAN). Gene ADO (synonym C10orf22). Human, 270 aa, cytosolic.
EC 1.13.11.19. HGNC:23506. Chromosome 10.

## Overview / core biology

ADO is a **cytosolic non-heme mononuclear Fe(II) thiol dioxygenase** of the cupin
superfamily. It is one of only two mammalian thiol dioxygenases (the other is
cysteine dioxygenase, CDO1), and is unusual in having **two well-established
activities acting on chemically distinct substrate classes**:

1. **Cysteamine (2-aminoethanethiol) dioxygenase** — oxidizes the sulfur of the
   small molecule cysteamine to hypotaurine (a sulfinic acid), the second route of
   hypotaurine/taurine biosynthesis complementing the CDO1/CSAD cysteinesulfinate
   route. This was the founding assigned activity.
   [file:human/ADO/ADO-uniprot.txt "Catalyzes the oxidation of cysteamine (2-aminoethanethiol) to hypotaurine"]
   [PMID:17581819 "When expressed as a recombinant protein, ADO exhibited significant cysteamine dioxygenase activity in vitro."]

2. **N-terminal cysteine dioxygenase of the Cys/N-degron (oxygen-sensing) pathway**
   — oxidizes the thiol of N-terminal cysteine residues of substrate proteins to
   Cys-sulfinic acid, priming them for arginylation (by ATE1) and downstream
   ubiquitin-mediated degradation. This makes ADO an enzymatic **cellular O2 sensor**.
   Verified substrates: RGS4, RGS5, IL-32 (and, in reporter assays, the plant
   ERF-VII RAP2.12 N-terminus).
   [PMID:31273118 "ADO catalyzes the conversion of amino-terminal cysteine to cysteine sulfinic acid"]
   [PMID:31273118 "human ADO catalyzes the dioxygenation of N-Cys residues in RGS4 and RGS5 to cysteine sulfinic acid"]

Both activities use O2 as a co-substrate and incorporate both oxygen atoms
(true dioxygenase). ADO has a high KmO2 (>500 uM for peptide substrates),
significantly above the physiological range, which underpins its oxygen-sensing role.
[PMID:31273118 "marked sensitivity to oxygen (KmO2app >500 μM)"]
[PMID:31273118 "ADO resembles the HIF prolyl hydroxylase enzymes in manifesting a KmO2 that is significantly above the physiological range, a property that may underpin a role in oxygen homeostasis"]

## Cofactor / metal center

- Non-heme mononuclear iron center, 3-His facial triad (His112, His114, His193).
  [file:human/ADO/ADO-uniprot.txt "Name=Fe cation"] (COFACTOR block, ECO:0000269|PubMed:34508780)
  [PMID:34508780 "The protein-derived ligands are His112 and His114 from Loop 3 and His193 from β6."]
- First crystal structure (1.78 Å, Ni-substituted C18S/C239S mutant, PDB 7REI).
  Monomer. Cupin jelly-roll β-barrel with unusually extensive flexible loops that
  accommodate both small-molecule and protein substrates; active-site architecture
  resembles plant cysteine oxidases (PCOs) rather than CDO.
  [PMID:34508780 "we report the first crystal structure of human ADO at a resolution of 1.78 Å with a nickel-bound metal center"]
  [PMID:34508780 "Our findings also elucidate the structural basis for ADO functioning as an oxygen sensor by modifying N-degron substrates to transduce responses to hypoxia."]
- Autocatalytically forms a Cys220–Tyr222 thioether cross-linked cofactor that acts
  as a "catalytic amplifier" (boosts efficiency, not strictly required).
  [PMID:29752763 "the discovery and elucidation of a Cys-Tyr cofactor in human ADO, crosslinked between Cys220 and Tyr222 through a thioether (C-S) bond"]
- Substrates bind the ferrous iron through their free thiol in a monodentate mode
  (distinct from CDO's bidentate binding).
  [PMID:32601061 "both the small molecule and the peptide substrates coordinate the iron center with their free thiols in a monodentate binding mode"]

## Subcellular location

- **Cytosol** is the authoritative location.
  [file:human/ADO/ADO-uniprot.txt "GO:0005829; C:cytosol; TAS:Reactome."]
  Reactome R-HSA-6814153 places the cysteamine→hypotaurine reaction in the cytosol.
- **Mitochondrion** appears in GOA via IBA (GO_REF:0000033), Ensembl-Compara IEA
  (GO_REF:0000107), and a large-scale HTP mito-proteome dataset (PMID:34800366).
  These are inconsistent with the curated cytosolic localization in UniProt (which
  gives no mitochondrial location) and with the enzyme's known cytosolic substrates
  (cytosolic RGS4/5, IL-32; cytosolic N-degron pathway). The HTP mitochondrial
  detection is likely co-purification/contaminant signal; ADO is not mentioned by
  name in the cached full text of PMID:34800366 (its listing is in supplementary
  tables). Treated as over-annotation / non-core, not the primary function.

## Existing-annotation decisions (summary)

- GO:0047800 cysteamine dioxygenase activity — CORE MF. IMP/IDA (PMID:17581819,
  29752763, 31273118, 32601061) ACCEPT; the IEA (GO_REF:0000120) is a redundant but
  correct electronic call → ACCEPT.
- GO:0005506 iron ion binding — CORE cofactor MF. IDA (PMID:34508780) ACCEPT;
  ISS/IEA redundant-correct → ACCEPT.
- GO:0071456 cellular response to hypoxia — CORE BP (oxygen sensing). IDA
  (PMID:31273118) ACCEPT.
- GO:0042412 taurine biosynthetic process — CORE BP (via hypotaurine). IEA ACCEPT.
- GO:0005829 cytosol — CORE CC. TAS (Reactome) ACCEPT; the IEA cytosol is redundant.
- GO:0016702 (oxidoreductase, single donors, 2 O atoms incorporated) — correct
  parent MF but generic; MODIFY → GO:0047800.
- GO:0005739 mitochondrion (IBA, IEA, HTP) — likely mislocalization / contaminant;
  MARK_AS_OVER_ANNOTATED (IBA/HTP cannot be REMOVEd per policy; IEA-Compara → REMOVE
  is permissible but conservatively MARK_AS_OVER_ANNOTATED given the two experimental
  siblings). See below.
- GO:0005515 protein binding (IPI, x3 rows) — high-throughput interactome hits
  (FAM76B, CAP2, DISC1); uninformative bare protein binding →
  MARK_AS_OVER_ANNOTATED. Interactors confirmed in the UniProt INTERACTION block.
  [file:human/ADO/ADO-uniprot.txt "Q96SZ5; P40123: CAP2"]

## Missing GO term (proposed)

GO currently has **no dedicated molecular-function term** for "oxygen-dependent
protein/peptidyl N-terminal cysteine dioxygenase activity" (the RHEA:70895 reaction:
N-terminal L-cysteinyl-[protein] + O2 = N-terminal S-hydroxy-S-oxy-L-cysteinyl-[protein]).
The nearest existing terms are GO:0047800 (cysteamine dioxygenase activity, the
small-molecule reaction), GO:0017172 (cysteine dioxygenase activity, the CDO1
reaction), and the BP term GO:0018171 (peptidyl-cysteine oxidation). This second
core catalytic activity of ADO is therefore proposed as a new MF term and, in the
interim, modeled through the process terms GO:0018171 (peptidyl-cysteine oxidation)
and GO:0031648 (protein destabilization) plus GO:0071456 (cellular response to hypoxia).

## Key references

- PMID:17581819 — discovery of ADO as the mammalian cysteamine dioxygenase (mouse
  Gm237 / human C10orf22); RNAi in HepG2 reduces hypotaurine. full_text_available: false (abstract only).
- PMID:29752763 — Cys220–Tyr222 cross-linked cofactor; mutagenesis of Tyr87/Tyr222/Tyr223. Full text.
- PMID:31273118 (Science) — ADO is the N-terminal cysteine dioxygenase of the Cys/N-degron
  pathway; RGS4/5, IL-32 substrates; O2 sensor; high KmO2. Full text.
- PMID:32601061 — non-heme iron center; monodentate thiol substrate binding; ferrous form. Full text.
- PMID:34508780 — first crystal structure (7REI); 3-His iron center; monomer; open,
  loop-rich cavity for protein substrates; structural basis for oxygen sensing. Full text.
- Reactome R-HSA-6814153 — "ADO oxidises 2AET to HTAU" (cytosolic).
- PMID:28514442, 32296183, 33961781 — large-scale interactome maps (bare protein-binding IPI).
- PMID:34800366 — HTP mitochondrial proteome (ADO listed; localization not corroborated by UniProt).
