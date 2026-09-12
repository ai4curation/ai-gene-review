# STS3 (Vitis vinifera) — research notes

UniProt: **P51071** (THS3_VITVI). Stilbene synthase 3 / Resveratrol synthase 3 /
Trihydroxystilbene synthase 3 (StSy 3). EC 2.3.1.95. AltName PSV368.
OrderedLocusNames VIT_16s0100g01030 (chromosome 16). 392 aa, ~42.8 kDa.

## Summary of gene function

STS3 is a **type III polyketide synthase (PKS III)** of the chalcone/stilbene synthase
family. It catalyzes the iterative condensation of one molecule of *p*-coumaroyl-CoA
(4-coumaroyl-CoA) with three molecules of malonyl-CoA, followed by an intramolecular
aldol cyclization and decarboxylation, to produce **trans-resveratrol**
(3,4',5-trihydroxystilbene), the major stilbenoid **phytoalexin** of grapevine.

UniProt catalytic activity (Rhea:RHEA:11936):
`4-coumaroyl-CoA + 3 malonyl-CoA + 3 H+ = trans-resveratrol + 4 CO2 + 4 CoA` (EC 2.3.1.95).
UniProt PATHWAY: "Phytoalexin biosynthesis; 3,4',5-trihydroxystilbene biosynthesis;
3,4',5-trihydroxystilbene from trans-4-coumarate: step 2/2."
UniProt SUBUNIT: homodimer. SUBCELLULAR LOCATION: Cytoplasm. INDUCTION: by stress.
UniProt FUNCTION line: "Mediates resistance to pathogens which are sensitive to
stilbenes" (ECO:0000250, i.e. inferred by similarity, not direct evidence for STS3).

## Type III PKS mechanism — relationship to chalcone synthase (CHS)

STS and CHS are paralogous type III PKS enzymes. They use **the same substrates**
(*p*-coumaroyl-CoA + 3 malonyl-CoA) and build **the same linear tetraketide
intermediate** via a single active-site Cys-His-Asn catalytic triad (the Cys is the
acyl carrier nucleophile; in STS3 the conserved active-site residue is annotated at
position 164, ECO:0000255 PROSITE-ProRule:PRU10023).

The enzymes diverge only at the **cyclization step**:
- CHS performs a **C6→C1 Claisen condensation** giving naringenin chalcone (a flavonoid
  precursor).
- STS performs an alternative **C2→C7 aldol condensation** plus decarboxylation giving
  the stilbene backbone of resveratrol.

[PMID:10426957 "It produces chalcone by condensing one p-coumaroyl- and three
malonyl-coenzyme A thioesters into a polyketide reaction intermediate that cyclizes...
The structure of CHS complexed with resveratrol also suggests how stilbene synthase, a
related enzyme, uses the same substrates and an alternate cyclization pathway to form
resveratrol."]

[PMID:15380179 "Stilbene synthase (STS) and chalcone synthase (CHS) each catalyze the
formation of a tetraketide intermediate from a CoA-tethered phenylpropanoid starter and
three molecules of malonyl-CoA, but use different cyclization mechanisms to produce
distinct chemical scaffolds for a variety of plant natural products... electronic
effects rather than steric factors balance competing cyclization specificities in CHS
and STS."] — this is the "aldol switch" study; an "aldol switch" hydrogen-bonding
network (the "thioesterase-like" pocket) in STS reorients the terminal carbonyl to
favor aldol over Claisen cyclization.

[PMID:10926848 "Chalcone synthase (CHS) and stilbene synthase (STS) catalyse
condensation reactions of p-coumaroyl-CoA and three C2 units from malonyl-CoA up to a
common tetraketide intermediate but then catalyse different cyclization reactions to
produce naringenin chalcone and resveratrol respectively... the G372FGPG loop in CHS
and STS contribute to a determination of the outcome during cyclization reactions."]
Note: STS3 contains the FGPG loop (sequence ...LFGFGPGLTIE... near residues 367–377).

STS arose from CHS by convergent evolution multiple independent times across
stilbene-producing lineages [PMID:22961129 "Stilbene synthases (STSs)... seem to have
evolved from chalcone synthases (CHSs) several times independently in
stilbene-producing plants."].

## The STS gene family in grapevine

Unlike most stilbene-producing plants where STS forms small families of 2–5 paralogs,
grapevine has an **unusually large STS gene family**. Reannotation of the PN40024
reference genome yielded **48 STS genes, ≥32 potentially functional**, all encoding
proteins with bona fide STS activity [PMID:22961129 "Our reannotation of the STS and
CHS gene families yielded 48 STS genes, including at least 32 potentially functional
ones. Functional characterization of nine genes representing most of the STS gene
family diversity clearly indicated that these genes do encode for proteins with STS
activity."]. STS3 (VIT_16s0100g01030, chromosome 16) is one member of this family;
the family is dominated by purifying selection with no strong evidence of neofunctional
divergence [PMID:22961129 "both STS and CHS evolution are dominated by purifying
selection, with no evidence for strong selection for new functions among STS genes"].

The historically best-characterized grapevine STS gene is *Vst1* (also called StSy);
"STS3" / *PSV368* / pSV21–pSV25 are early-isolated grape STS cDNAs. The original
P51071 sequence comes from a stress-/elicitor-induced grape (cv. Optima) cDNA library
[PMID:1898048 "Several independent cDNA clones for PAL and stilbene synthase were
isolated from a cDNA library of fungal cell wall-induced grape cells... The stilbene
synthase cDNA sequence of pSV21 predicted a protein of 392 amino acids and Mr 42,791."].

## Phytoalexin biology and "defense response"

Resveratrol and its derivatives (piceids, viniferins, pterostilbene) are **stilbenic
phytoalexins** — antimicrobial secondary metabolites synthesized de novo by the plant
in response to biotic and abiotic stress.

- STS expression is **elicitor- and stress-inducible**: STS and PAL (phenylalanine
  ammonia-lyase) transcripts are co-induced within 1 h of fungal cell-wall elicitor
  treatment of grape cell cultures [PMID:1898048 "Both PAL and stilbene synthase mRNA...
  were induced within 1 h of addition of fungal cell wall preparations to the cell
  cultures, rose to a maximum by the sixth hour."].
- STS transcripts and stilbenoid content increase upon **powdery mildew** (Erysiphe /
  Uncinula necator) infection [PMID:23116673 "transcripts of selected STS genes
  increased significantly in Cabernet Sauvignon leaves at 24 and 48 h post inoculation
  with PM spores"; PMID:31531782 "the levels of STS expression and stilbenoids
  increased in response to powdery mildew infection"].
- Resveratrol is directly antimicrobial: 1.0 mM resveratrol inhibits mycelial growth of
  *Phytophthora palmivora* in vitro [PMID:15309535 "resveratrol at 1.0 mM inhibited
  mycelium growth of P. palmivora in vitro"].
- **Heterologous transfer confers disease resistance**: expressing grapevine STS genes
  (Vst1) in non-stilbene plants (papaya, tobacco, etc.) raises stilbene content and
  increases pathogen resistance [PMID:15309535 "the transformed papaya lines exhibited
  increased resistance to P. palmivora"]. But this is not universal — transgenic white
  poplar accumulated resveratrol glucosides yet showed **no increased rust resistance**
  [PMID:15359598 "no increased resistance against the pathogen Melampsora pulcherrima...
  was observed"], showing that the STS enzyme itself is one biosynthetic input, not the
  whole defense program.
- STS expression is governed by defense-associated transcription factors, notably
  **MYB14/MYB15**, downstream of oxidative burst, Ca2+ influx, MAPK and jasmonate
  signaling [PMID:26842984 "a RboH-dependent oxidative burst, calcium influx, a MAPK
  cascade, and jasmonate activated the MYB14 promoter"].

### Key curation point — "defense response" (GO:0006952) is process-conflation

STS3's **molecular function is a biosynthetic synthase** (trihydroxystilbene synthase).
Its *product* (resveratrol) is antimicrobial, so the gene is **defense-associated**, but
"defense response" (GO:0006952) as a biological-process annotation conflates the
downstream protective role of the metabolite with the catalytic activity of the enzyme.
The enzyme does not itself sense pathogens or execute a defense response; it
biosynthesizes a stilbene that happens to be a phytoalexin. The accurate biological
process is **stilbene biosynthetic process (GO:0009811)** and/or **phytoalexin
biosynthetic process (GO:0052315)**. GO:0052315 "phytoalexin biosynthetic process" is a
child of both *secondary metabolite biosynthetic process (GO:0044550)* and *toxin
biosynthetic process (GO:0009403)*, and it captures the defense context far more
precisely than the generic GO:0006952 without misrepresenting the enzyme as a defense
effector. This is the classic "biosynthetic-enzyme-labelled-with-the-downstream-process"
over-annotation pattern.

## GO term reference (verified via OLS)

- GO:0050350 trihydroxystilbene synthase activity — "Catalysis of the reaction: 3
  malonyl-CoA + 4-coumaroyl-CoA = 4 CoA + 3,4',5-trihydroxy-stilbene + 4 CO2." Direct
  parent: GO:0016747. This is the precise MF for STS3 and matches EC 2.3.1.95 and
  Rhea:11936 exactly.
- GO:0016747 acyltransferase activity, transferring groups other than amino-acyl groups
  — parent of GO:0050350.
- GO:0016746 acyltransferase activity — grandparent of GO:0050350.
- GO:0009811 stilbene biosynthetic process — "formation of stilbenes, a class of
  polyketide compounds formed from cinnamic acid and three molecules of malonyl CoA."
  Precise BP for STS3.
- GO:0052315 phytoalexin biosynthetic process — child of GO:0044550 (secondary
  metabolite biosynthetic process) and GO:0009403 (toxin biosynthetic process).
- GO:0044550 secondary metabolite biosynthetic process — broader BP.
- GO:0006952 defense response — the retired SPKW annotation; over-broad / process-
  conflation for a biosynthetic enzyme.
- GO:0005737 cytoplasm — consistent with UniProt SUBCELLULAR LOCATION.

## Provenance notes

- All four directly cited primary PMIDs (1898048, 22961129, 15380179, 10426957) are
  cached abstract-only (no PMC full text); supporting quotes are from the abstracts.
- PMID:23116673, PMID:31531782, PMID:15309535, PMID:15359598, PMID:26842984 used for
  context (phytoalexin/defense biology); abstracts retrieved via PubMed.
- Bibliographic data retrieved from PubMed.
