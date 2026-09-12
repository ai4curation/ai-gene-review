# PR1B1 (tomato) — research notes

UniProt: **P04284** (PR06_SOLLC). RecName "Pathogenesis-related leaf protein 6";
Short "P6"; AltNames "Ethylene-induced protein P1", "P14", "P14A", "P14a", "PR protein".
Gene name **PR1B1**. Solanum lycopersicum, NCBI:txid4081. 159 aa precursor, signal
peptide 1-24, mature chain 25-159, pyroglutamate at Gln-25. SCP/CAP domain 32-147,
three disulfide bonds. Member of the PR-1 / CAP (CRISP) superfamily.

## Identity: PR1B1 = P6 = P14a

The UniProt entry is explicit that P04284 (PR1B1) carries the historical names "P14"
and "P14A"/"P14a". The seminal NMR structure (PDB 1CFE) was solved for "P14a"
[PMID:9067611 "The nuclear magnetic resonance (NMR) structure of the 15 kDa
pathogenesis-related protein P14a, which displays antifungicidal activity and is
induced in tomato leaves as a response to pathogen infection"]. The cDNA clones for
PR1B1 (P6/P14 isomer P6) were reported by van Kan et al. [PMID:1421154 "the isolation
and characterization of cDNA clones encoding the two extracellular P14 isomers P4 and
P6"]. Tornero et al. cloned PR1b1 (basic) and PR1a2 (acidic) tomato PR-1 genes
[PMID:9204567 "the cloning and characterization of two closely related genes encoding
a basic and an acidic PR-1 protein (PR1b1 and PR1a2) from tomato"].

So this gene = the canonical tomato leaf PR-1 protein, the original "pathogenesis-related
leaf protein p14" whose 1985 sequencing revealed a "new type of structurally unfamiliar
protein" (the founding CAP-superfamily sequence).

## PR-1 family biology and the CAP superfamily

PR-1 was the first founding member of the CAP superfamily (Cysteine-rich secretory
proteins, Antigen 5, and Pathogenesis-related 1 proteins; also SCP/TAPS). CAP proteins
occur across plants, animals, fungi and pathogens. PR-1 proteins are small (~14-15 kDa
mature), secreted, cysteine-rich, and built around a single CAP/SCP domain
[PMID:36932700 review].

PR-1 genes are the canonical molecular **markers** of salicylic-acid-dependent
systemic acquired resistance (SAR). "Up-regulation of the PR-1 gene was considered to
be the main marker of SAR elicitation"; PR-1/PR-2/PR-5 are "considered as markers for
salicylic acid (SA)-dependent systemic acquired resistance". They are massively
transcriptionally induced upon pathogen challenge.

Expression of tomato PR1b1 specifically: it is NOT constitutively expressed; it is
transcriptionally activated by pathogen attack, locally in HR tissue, and is induced
by salicylic acid AND ethylene precursors [PMID:9204567 "the chimeric PR1b1/GUS gene
does not show any constitutive expression in the plant, but it is transcriptionally
activated following pathogen attack. Upon infection by tobacco mosaic virus, the
PR1b1 gene is strongly activated locally in tissues undergoing the hypersensitive
response... its expression is induced by both salicylic acid and ethylene precursors"].
The UniProt INDUCTION line: "Upon infection by virulent and avirulent races of
pathogens, for example fungal pathogen C.fulvum. Also induced by ethylene."

## Direct antifungal/antimicrobial activity — what is actually demonstrated

The landmark demonstration of direct antimicrobial activity: Niderman et al. 1995
isolated three basic 14-kD tomato proteins P14a, P14b, P14c from P. infestans-infected
tomato leaves [PMID:7784503 "Three distinct basic 14-kD proteins, P14a, P14b, and P14c,
were isolated from tomato... They exhibited antifungal activity against P. infestans
both in vitro (inhibition of zoospore germination) and in vivo with a tomato leaf disc
assay (decrease in infected leaf surface)"]. Crucially the paper found **differential**
activity: "The various tomato and tobacco PR-1 proteins were compared for their
biological activity and found to display differential fungicidal activity against
P. infestans... the most efficient being the newly characterized tomato P14c and
tobacco PR-1g." So among the tomato P14 proteins, P14a (= PR1B1) was the LESS efficient;
the strongest activity was P14c (a different, more basic PR-1). The 2023 review
attributes the founding antimicrobial demonstration to this study: "A strong
antimicrobial activity of PR1 was first established in 1995, when zoospores of
Phytophthora infestans were challenged with purified PR1 proteins from tobacco or
tomato (Niderman et al.)" [PMID:36932700].

Note: P. infestans is an **oomycete**, not a true fungus. The historical literature
(and UniProt's "Antifungal"/"Fungicide" keywords, FUNCTION line "Has antifungal
activity") loosely calls oomycete-inhibitory activity "antifungal".

So: P14a/PR1B1 specifically WAS tested and DID show measurable in-vitro and in-planta
inhibitory activity against P. infestans, but it was the weakest of the tomato P14
proteins tested. This is genuine direct evidence of antimicrobial/antioomycete
activity for this protein, albeit modest.

## Mechanism: sterol binding / CAP activity

The mechanistic basis of PR-1 antimicrobial action was clarified by Gamir et al. 2017:
PR-1 proteins bind sterols, and the inhibitory effect on pathogen growth is caused by
sequestration of sterol away from the pathogen [PMID:27747953 "we provide genetic and
biochemical evidence for the capacity of PR-1 proteins to bind sterols, and demonstrate
that the inhibitory effect on pathogen growth is caused by the sequestration of sterol
from pathogens. In support of our findings, sterol-auxotroph pathogens such as the
oomycete Phytophthora are particularly sensitive to PR-1, whereas sterol-prototroph
fungal pathogens become highly sensitive only when sterol biosynthesis is compromised"].
This explains why oomycetes (sterol auxotrophs that require exogenous sterol) are the
most sensitive targets. The CAP domain has a caveolin-binding motif and a flexible loop
with aromatic residues important for binding sterols and small hydrophobic compounds
[PMID:36932700]. CAP/PRY proteins are secreted sterol-binding proteins (PNAS 2009,
Choudhary & Schneiter). The Gamir 2017 work was done largely with Arabidopsis PR-1 and
recombinant CAP proteins; it provides the family-level molecular function rather than a
tomato-PR1B1-specific assay, but it is the accepted mode of action for the family.

## CAPE1 — the C-terminal signalling peptide derived from tomato PR-1b

A major modern reinterpretation of PR-1 function: tomato **PR-1b is the precursor of
the CAPE1 immune-signalling peptide**. Chen et al. 2014 used quantitative peptidomics
and found "a wounding or wounding plus MeJA-induced peptide derived from the
pathogenesis-related protein 1 (PR-1) family was found to induce significant
antipathogen and minor antiherbivore responses in tomato" — "The third peptide
(designated as CAPE1) was derived from PR-1b, a protein of unclear function"
[PMID:25361956]. CAPE1 is the C-terminal ~11 residues of PR-1b, released proteolytically
(in Arabidopsis by the cysteine protease XCP1). CAPE1 acts as a DAMP elicitor: "CAPE1
was shown to be a DAMP elicitor in this study as it was induced by wounding and
activated defense responses"; "CAPE1 significantly induced several pathogen-related
marker genes, including PR-2, PR-7, Chi2;1, and the precursor of CAPE1 (PR-1b)"; and it
activates SA- and JA-dependent defense and SAR-related responses. "This study
highlights a role for PR-1 in immune signaling." The 2023 review confirms: "plant PR1
is proteolytically cleaved to release a C-terminal CAPE1 peptide, which is sufficient
to activate an immune response. The release of this signalling peptide is blocked by
pathogenic effectors to evade immune defence" [PMID:36932700].

So PR1B1 has (at least) TWO defense-related roles: (1) a modest direct
antimicrobial/sterol-sequestering CAP protein, and (2) the proprotein source of the
CAPE1 immune-signalling peptide. Both are "defense response", broadly.

## Subcellular location

PR1B1 has an N-terminal signal peptide (1-24) and is a classic **extracellular /
apoplastic** PR protein. UniProt classifies it as one of the *extracellular* PR
proteins; van Kan et al. studied "extracellular and intracellular PR proteins" and P6
is in the extracellular group [PMID:1421154 "five extracellular PR proteins: P2, P4,
P6, a chitinase and a beta-1,3-glucanase"]. The InterPro IPR018244-derived GO
annotation "extracellular region" is well supported. PR1/CAPE1 biology occurs in the
apoplastic space.

## Marker vs effector — the key distinction for this review

PR-1 is the textbook **marker** of SAR — its transcript abundance reports SA signalling
status. But it is also a genuine defense **participant/effector**: (a) it has direct
(if modest, isoform-variable) antimicrobial activity demonstrated for P14a/PR1B1
itself [PMID:7784503]; (b) it is the precursor of the CAPE1 immune-signalling peptide
[PMID:25361956]; (c) overexpression of PR-1 increases pathogen resistance
[PMID:36932700]. So PR1B1 is both a marker and an effector — it is not "merely
co-induced".

## Assessment of the retired SPKW annotations

### GO:0031640 "killing of cells of another organism"
This term implies a direct cytotoxic/cell-killing activity. For PR1B1/P14a specifically,
Niderman et al. 1995 showed direct inhibition of P. infestans zoospore germination and
reduction of infected leaf surface — i.e., direct antioomycete activity. UniProt carries
"Antimicrobial", "Fungicide" keywords and FUNCTION "Has antifungal activity". The CAP
sterol-sequestration mechanism (Gamir 2017) provides a plausible direct
growth-inhibitory/killing mechanism. So this annotation is NOT baseless — it traces to
the UniProt Antimicrobial/Fungicide keywords which are themselves grounded in
experimental work on this protein. However, "killing of cells of another organism" is
a fairly strong/specific BP term; the demonstrated activity for P14a is modest
(weakest of the P14 set) and is better described as growth inhibition / antimicrobial
than outright cytotoxic "killing". GOA's removal of the SPKW annotation removed a
correct-in-spirit annotation; this is a case where the SPKW removal was only PARTLY
justified — the activity is real but the keyword pipeline produced a term that is
arguably stronger than the literature warrants for this specific protein. A better
annotation would be a "defense response" / "response to oomycete" BP plus a sterol-
binding MF, rather than the cytotoxic-sounding "killing of cells of another organism".

### GO:0050832 "defense response to fungus"
PR1B1 is induced by and tested against pathogens. The direct in-vitro/in-planta target
in Niderman 1995 is *Phytophthora infestans*, an **oomycete**, not a true fungus.
UniProt INDUCTION cites the fungus *Cladosporium fulvum* as an inducer. So PR1B1 is
genuinely a participant in antimicrobial defense, and is induced during fungal
infection — "defense response to fungus" is essentially correct as a process the
protein participates in (it is more than mere co-induction: it has antimicrobial
activity and yields CAPE1). The most precisely demonstrated direct target is an
oomycete, so "defense response to oomycetes" (GO:0002229) would be the most accurate
specific term; "defense response to fungus" is reasonable but slightly imprecise.
GOA's removal of this SPKW annotation removed a substantially correct annotation.

### Current ARBA annotation GO:0098542 "defense response to other organism"
This is the broad parent that the ARBA model assigned. It is unambiguously correct and
well supported (PR1B1 participates in defense against pathogens; antimicrobial activity
+ CAPE1 signalling). It is broad but accurate, and it appropriately covers both the
oomycete and fungal contexts. This is a reasonable replacement / retention.

## Summary of core function

PR1B1 is the canonical extracellular (apoplastic) tomato PR-1 / CAP-superfamily defense
protein, strongly transcriptionally induced by pathogen attack, salicylic acid and
ethylene. It functions in plant defense against pathogens in two ways: as a sterol-
binding CAP protein with direct (modest) antimicrobial/antioomycete activity, and as
the proprotein precursor of the CAPE1 C-terminal immune-signalling peptide. It is the
textbook molecular marker of systemic acquired resistance.

## Key references
- PMID:16453639 — 1985, original p14 protein sequencing; "new type of structurally unfamiliar protein" (founding CAP sequence)
- PMID:1421154 — 1992, cDNA cloning of extracellular P14 isomers P4 (PR1A2) and P6 (PR1B1); induced by C. fulvum
- PMID:9067611 — 1997, NMR structure of P14a (= PR1B1); PDB 1CFE; alpha-beta-alpha sandwich CAP fold
- PMID:9204567 — 1997, PR1b1 vs PR1a2 differential regulation; PR1b1 pathogen/HR-inducible, SA + ethylene responsive
- PMID:7784503 — 1995, Niderman et al.; tomato P14a/b/c are antifungal vs P. infestans; differential activity, P14c strongest
- PMID:27747953 — 2017, Gamir et al.; PR-1 proteins bind sterols; antimicrobial action via sterol sequestration
- PMID:25361956 — 2014, Chen et al.; CAPE1 immune-signalling peptide derived from tomato PR-1b
- PMID:36932700 — 2023, Han et al. review; function of plant PR1 / CAP superfamily in plant-pathogen interactions
