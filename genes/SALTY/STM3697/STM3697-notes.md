# STM3697 (Q8ZL58, TalrD/GalrD) — curation notes

Gene: *Salmonella enterica* subsp. *enterica* serovar Typhimurium str. LT2, ordered locus
`STM3697`. UniProt Q8ZL58 (`TAGAD_SALTY`), L-talarate/galactarate dehydratase, EC 4.2.1.156
and EC 4.2.1.42.

**Provenance caveat.** No deep-research provider API keys are available in this container, so
`just deep-research` was not run and no `-deep-research-<provider>.md` file exists for this
gene. The research below was done directly: cached publications in `publications/`, the
UniProt flat file, PubMed (MCP) searches, the UniProt REST API for the *Salmonella* gar-operon
paralogue, and OLS/QuickGO for term definitions and hierarchy. The two primary papers
(PMID:17649980, PMID:29248502) are cached **abstract-only**
(`full_text_available: false`); PMID:19883118 is cached with PMC full text.

## Gene symbol

UniProt gives **no** gene name for this entry, only `GN   OrderedLocusNames=STM3697;`. The
seeded stub therefore fell back to the accession (`gene_symbol: Q8ZL58`). GOA itself uses
`STM3697` in the SYMBOL column of `STM3697-goa.tsv`, the folder is `genes/SALTY/STM3697/`, and
the ordered locus name is how the protein is referred to throughout the primary literature
("the protein encoded by the Salmonella typhimurium LT2 genome (GI:16766982; STM3697)"
[PMID:17649980]). `gene_symbol: STM3697` was therefore set — appropriate, and consistent with
the repository's convention of using the locus tag when no mnemonic symbol exists. No
three-letter mnemonic (e.g. a `tgd`/`talD` name) has been assigned by any nomenclature body
that I could find.

## Function

The function was assigned by **physical library screening of acid sugars**, not by pathway or
homology inference: "We discovered the function of STM3697 by screening a library of acid
sugars; it catalyzes the efficient dehydration of both l-talarate (kcat = 2.1 s-1, kcat/Km =
9.1 x 10(3) M-1 s-1) and galactarate (kcat = 3.5 s-1, kcat/Km = 1.1 x 10(4) M-1 s-1)"
[PMID:17649980]. Both activities are kinetically efficient and within ~20% of each other in
kcat/Km, so neither is a trace side activity. The product in both cases is
5-dehydro-4-deoxy-D-glucarate (5-KDG) [UniProt CC CATALYTIC ACTIVITY; Rhea:44028, Rhea:16005].

The enzyme is a member of the mandelate racemase (MR) subgroup of the enolase superfamily. It
shares the subgroup's active-site machinery: "the active site of TalrD/GalrD contains a general
acid/base Lys 197 at the end of the second beta-strand in the (beta/alpha)7beta-barrel domain,
Asp 226, Glu 252, and Glu 278 as ligands for the essential Mg2+ at the ends of the third,
fourth, and fifth beta-strands, a general acid/base His 328-Asp 301 dyad at the ends of the
seventh and sixth beta-strands, and an electrophilic Glu 348 at the end of the eighth
beta-strand" [PMID:17649980]. The two substrates use **different** bases: "we conclude that Lys
197 functions as the galactarate-specific base and His 328 functions as the l-talarate-specific
base" [PMID:17649980]. Both K197A and H328N/H328A abolish dehydration of *both* substrates and
epimerization [UniProt FT MUTAGEN], i.e. the two activities share one active site and one
enolate intermediate, as stated independently in the later paper: "We previously characterized
a promiscuous acid sugar dehydratase in the MR subgroup that catalyzes both L-talarate
dehydratase (TalrD) and GalrD reactions via a common enolate intermediate" [PMID:19883118].

Magnesium is a genuine catalytic cofactor, not an inferred metal-binding activity: the crystal
structures (PDB 2PP0/2PP1/2PP3) were solved "in complexes with an analog of the enolate
intermediate; L-glucarate and magnesium" [UniProt RN[4] RP line], and UniProt records "Binds 1
Mg(2+) ion per subunit." with ECO:0000269|PubMed:17649980. The quaternary structure is a
"Homooctamer; tetramer of dimers." [UniProt CC SUBUNIT].

A third, non-dehydratase activity is also demonstrated: epimerization of L-talarate to
galactarate. "The dehydration of l-talarate is accompanied by competing epimerization to
galactarate; little epimerization to l-talarate is observed in the dehydration of galactarate"
[PMID:17649980], rationalized as partitioning of the shared enolate intermediate. UniProt
records this as a separate catalytic activity (`L-altrarate = galactarate`, Rhea:64172,
ECO:0000269|PubMed:17649980). **GO has no term for this epimerase reaction** — the closest is
GO:0016857 "racemase and epimerase activity, acting on carbohydrates and derivatives" (checked
in OLS; no galactarate/altrarate epimerase term exists). Recorded as a `proposed_new_terms`
entry.

Specificity is narrow: "Is not active on other acid sugars (PubMed:17649980)" [UniProt CC
FUNCTION]. This matters for the CACAO review: the paper's own phrase "The promiscuous catalytic
activities discovered for STM3697" [PMID:17649980] refers to *dual substrate* use within one
active site, not to a laboratory artefact — it is not a screen hit with no in vivo follow-up.

## Physiological role, and the garD caveat

Unusually for a structure/screening-driven functional assignment, the primary paper supplies
in vivo genetics for both substrates:

- L-talarate: "Because l-talarate is a previously unknown metabolite, we demonstrated that S.
  typhimurium LT2 can utilize l-talarate as carbon source. Insertional disruption of the gene
  encoding STM3697 abolishes this phenotype" [PMID:17649980]. Complete loss ⇒ STM3697 is the
  sole route for L-talarate catabolism. This is the **core** biological role.
- Galactarate: the same disruption "also diminishes, but does not eliminate, the ability of the
  organism to utilize galactarate as carbon source" [PMID:17649980]. Partial loss.

The partial galactarate phenotype has a clear explanation that is not stated in the abstract:
*S.* Typhimurium LT2 encodes a **dedicated, canonical galactarate catabolic operon**. A UniProt
REST query of taxon 99287 returns `garR` (STM3248, 2-hydroxy-3-oxopropionate reductase), `garL`
(STM3249, 5-keto-4-deoxy-D-glucarate aldolase, EC 4.1.2.20) and `garD` (STM3250, "Galactarate
dehydratase (L-threo-forming)", EC 4.2.1.42) — the *E. coli*-type gar pathway, in an adjacent
gene cluster at a locus ~450 genes away from STM3697. GarD, not STM3697, is the dedicated
galactarate dehydratase; STM3697 contributes an accessory, partially redundant route.
Consistently, GarD and TalrD/GalrD make the **same** product enantiomer: TalrD/GalrD "produces a
product with a positive rotation (2-keto-L-threo-4,5-dihydroxyadipate; 2 in Scheme I)"
[PMID:19883118] and UniProt names GarD "(L-threo-forming)". (The *Oceanobacillus iheyensis*
Ob2843 GalrD-II enzyme makes the opposite enantiomer, "establishing that the products are
enantiomers and that the enzymes differ in their regiochemistry of dehydration"
[PMID:19883118]; that regiochemical distinction is not represented in GO, where GO:0008867
covers both.)

Reading of the review consequence: the **molecular function** galactarate dehydratase activity
(GO:0008867) is fully established for STM3697 and is accepted; the **biological process**
D-galactarate catabolic process (GO:0046392) is real but accessory given GarD, so it is kept as
non-core rather than as a core function.

## Later work

PMID:29248502 (Easton, Aboushawareb & Bearne 2018) re-measured the galactarate dehydratase
reaction on recombinant *Salmonella* enzyme with a new continuous circular-dichroism assay:
"Using recombinant enzyme from Salmonella typhimurium (StTGD), the rates of StTGD-catalyzed
conversion of m-galactarate to 5-KDG were determined by following the change in ellipticity at
323 nm", giving "Km, kcat, and kcat/Km were 0.38 ± 0.05 mM, 4.8 ± 0.1 s-1, and 1.3 (±0.2) × 104
M-1s-1" which "are in excellent agreement with those published previously" [PMID:29248502].
Independent replication in a second laboratory. The same paper establishes tartronate as a
competitive inhibitor (Ki = 10.7 ± 0.4 mM).

PMID:39835335 (Kumar et al. 2025) used differential scanning calorimetry on four MR-subgroup
enzymes including "l-talarate/galactarate dehydratase" and found that the active-site Lys
Brønsted acid–base catalyst destabilizes the protein; relevant to mechanism, not to function
assignment.

PubMed returns only four papers for `talarate dehydratase OR "L-talarate" OR STM3697`
(17649980, 19883118, 29248502, 39835335), all accounted for above. There is no transport,
regulation, or host-infection literature on this gene.

## GONUTS

All four CACAO-assigned rows (ASSIGNED BY = CACAO in `STM3697-goa.tsv`) cite PMID:17649980 and
are dated 2014-10-21 / 2014-11-18. The GONUTS wiki pages
`https://gowiki.tamu.edu/wiki/index.php/PMID:17649980` and
`https://gowiki.tamu.edu/wiki/index.php/SALTY:TAGAD` were both fetched on 2026-10-29 and both
return only "This site is temporarily offline while we perform upgrades. Please check back at a
later date." — the student's recorded evidence text could not be retrieved. The review
therefore reasons from the abstract and UniProt curation, which in this case state the assays
explicitly enough (kinetics for the two IDA rows; the insertional-disruption carbon-source
phenotypes for the two IMP rows) that no row needed `UNDECIDED`.

## Problem annotations

`GO:0009063 amino acid catabolic process` (IEA, GO_REF:0000002, from `InterPro:IPR018110`) is a
mis-propagation. IPR018110 is the mandelate racemase / muconate lactonizing enzyme **conserved
site** — a superfamily-wide PROSITE-pattern signature (PS00909 `MR_MLE_2` in this entry's `DR`
lines), present in enzymes acting on mandelate, muconate, acid sugars and, in some members,
amino acid derivatives. Nothing about STM3697 touches amino acid catabolism: its substrates are
aldarates, its product is 5-KDG, and it "Is not active on other acid sugars" [UniProt CC
FUNCTION]. Flagged for removal and as an upstream InterPro2GO defect.

## Open questions

- What is the biological source of L-talarate? It was "a previously unknown metabolite"
  [PMID:17649980], so the organism maintains a dedicated catabolic enzyme for a compound whose
  provenance in the environment or host is unestablished. Genuine biological unknown (recorded
  as a `knowledge_gaps` entry).
- Is STM3697 transcriptionally induced by L-talarate or galactarate, and which transporter
  brings L-talarate in? No regulator or transporter has been identified.
- Is the epimerization activity used in vivo (e.g. to feed L-talarate into the GarD route as
  galactarate), or is it purely a mechanistic consequence of enolate partitioning?
