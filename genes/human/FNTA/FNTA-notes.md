# FNTA review notes

Gene: FNTA (HGNC:3782), UniProt P49354, human (NCBITaxon:9606), 379 aa.
Product: Protein farnesyltransferase/geranylgeranyltransferase type-1 subunit alpha.

## Core biology (from UniProt P49354 = file:human/FNTA/FNTA-uniprot.txt)

FNTA is the **shared alpha subunit** of two heterodimeric CaaX prenyltransferases:
- **Protein farnesyltransferase (FTase)** = FNTA (alpha) + FNTB (beta); EC 2.5.1.58.
- **Protein geranylgeranyltransferase type-I (GGTase-I)** = FNTA (alpha) + PGGT1B (beta); EC 2.5.1.59.

UniProt FUNCTION: "Essential subunit of both the farnesyltransferase and the
geranylgeranyltransferase complex. Contributes to the transfer of a farnesyl or
geranylgeranyl moiety from farnesyl or geranylgeranyl diphosphate to a cysteine at the
fourth position from the C-terminus of several proteins having the C-terminal sequence
Cys-aliphatic-aliphatic-X." [file:human/FNTA/FNTA-uniprot.txt]

UniProt SUBUNIT: "Heterodimer of FNTA and FNTB (farnesyltransferase) ... Heterodimer of
FNTA and PGGT1B (geranylgeranyltransferase)." [file:human/FNTA/FNTA-uniprot.txt]

UniProt COFACTOR: Mg(2+). The catalytic Zn(2+) resides in the beta subunit; FNTA (alpha)
partially envelops the beta subunit as a crescent-shaped, alpha-helical repeat protein.

ComplexPortal cross-refs in UniProt confirm both complexes:
- CPX-2165 Protein farnesyltransferase complex.
- CPX-2157 Protein geranylgeranyl transferase type I complex.

## The prenylation reaction and substrates

FTase/GGTase-I attach a C15 farnesyl (from farnesyl-PP) or C20 geranylgeranyl (from
geranylgeranyl-PP) isoprenoid to the cysteine of a C-terminal CaaX motif, enabling
membrane association of the target. Substrates include Ras-superfamily GTPases (H/K/N-RAS,
Rho, Rac), nuclear lamins, heterotrimeric G-protein gamma subunits, centromeric proteins,
GBP guanylate-binding proteins, etc.

- FTase "catalyzes the transfer of a 15-carbon isoprenoid lipid moiety to the C terminus
  of more than 60 signal transduction proteins in the eukaryotic cell, including members
  of the Rho and Ras superfamily of G proteins" [PMID:19246009 full text].
- Substrates modified "at a carboxy-terminal peptide with a Ca1a2X motif, which consists
  of a cysteine (the gamma sulfur is lipid modified), two generally aliphatic residues
  (a1a2), and a variable C-terminal (X) residue" [PMID:19246009 full text].
- "FTase and GGTase-I (also called the CaaX prenyltransferases) recognize protein
  substrates with a C-terminal tetrapeptide recognition motif called the Ca1a2X box"
  [PMID:15451670 abstract].

## Alpha subunit's role: structural + catalytic contribution (NOT purely passive)

PMID:8419339 (Andres et al., mutagenesis of the rat alpha subunit; abstract-only cache,
full_text_available: false): "The beta-subunit functions in the Zn(2+)-dependent binding
of the protein substrate. The role of the alpha-subunit is unknown." They showed the
K164->N substitution "stabilized the beta-subunit normally and permitted normal binding
of the two substrates ... Nevertheless, the rate of transfer of the bound farnesyl group
to p21H-ras was markedly reduced. The latter finding suggests that the alpha-subunit
plays a direct role in the catalytic reaction in addition to its role in the stabilization
of the beta-subunit." UniProt maps Lys-164 mutagenesis to human FNTA.

PMID:8494894 (Omer et al., recombinant human FPTase; abstract-only): neither individual
subunit binds isoprenoid alone; FPP photo-cross-links to the beta subunit of holoenzyme.
Alpha-subunit substitutions homologous to yeast mutants impair FPTase (Km/kcat changes).
Establishes FNTA as an essential subunit whose alpha-subunit residues affect catalysis.

Crystal structures (Beese lab) repeatedly show the heterodimer: "The beta subunit ...
contains most of the substrate-binding residues and is partially enveloped by the crescent
shaped alpha subunit" [PMID:19246009 full text]. FNTA contacts the CaaX X-residue binding
pocket via residues A129alpha, Y131alpha, N167alpha (PMID:19246009).

Because catalysis is a property of the assembled heterodimer (the Zn2+ and most substrate
contacts are in beta), the appropriate GO-CAM-style modeling gives FNTA a subunit-level
molecular_function (molecular adaptor activity, GO:0060090; DisProt DP00558 / PMID:11687658
EXP) and has it CONTRIBUTE TO the complex-level transferase activities (GO:0004660 FTase;
GO:0004662 CAAX GGTase), rather than "enable" them independently.

## GGTase-I / geranylgeranyltransferase

PMID:8106351 (Zhang et al., cloning of rat/human GGTase-I; abstract-only): "Peptides
isolated from the alpha subunit of GGTase-I were shown to be identical with the alpha
subunit of a related enzyme, protein farnesyltransferase." "Co-expression of the GGTase-I
beta subunit cDNA together with the alpha subunit of protein farnesyltransferase in
Escherichia coli produced recombinant GGTase-I ..." -> confirms FNTA is the shared alpha
subunit and GGTase-I = FNTA + PGGT1B (beta). GGTase-I transfers geranylgeranyl to CaaX
substrates where X = leucine.

PMID:16893176 (Terry, Casey, Beese; abstract-only) — the source for several IDA
annotations. Presents "both crystallographic and kinetic analyses of mutants designed to
explore this isoprenoid specificity" for FTase vs GGTase-I; isoprenoid specificity is
"dependent upon two enzyme residues in the beta subunits." Human recombinant enzyme; used
by UniProtKB curators for FTase activity (GO:0004660), GGTase activity (GO:0004661),
farnesylation (GO:0018343), geranylgeranylation (GO:0018344), and both complexes
(GO:0005965, GO:0005953) IDA annotations.

## Microtubule / HDAC6 regulatory role (secondary/moonlighting)

PMID:19228685 (Zhou et al., 2009; abstract-only, PMC2665085): "FTase binds microtubules
directly via its alpha subunit, and this association requires the C terminus of tubulin."
FTase + HDAC6 + microtubules form a complex in vivo and in vitro; "the removal of FTase
from microtubules abrogated HDAC6 activity, as did a stable knockdown of the alpha subunit
of FTase." So FNTA (as the tubulin-binding subunit) is an upstream regulator of the
cytoplasmic deacetylase HDAC6. This is the source of the BHF-UCL IDA/IPI annotations:
- GO:0008017 microtubule binding, GO:0043014 alpha-tubulin binding (IDA) — well supported.
- GO:0005875 microtubule associated complex (IDA) — FTase-microtubule complex.
- GO:0010698 acetyltransferase activator activity (IDA) — NOTE: the paper shows FTase is
  required for HDAC6 *deacetylase* activity, i.e. it regulates a *de*acetylase, not an
  acetyltransferase. The "acetyltransferase activator activity" MF label does not match
  the deacetylase biology in the abstract; flag as questionable / over-annotated.
- GO:0060632 regulation of microtubule-based movement (IDA) — HDAC6 deacetylates tubulin
  and affects microtubule-based motility; plausible but a downstream/non-core process.
- GO:0019899 enzyme binding (IPI, partner Q9UBN7 = HDAC6) — binds the enzyme HDAC6.

## TGF-beta / activin receptor interaction (secondary)

PMID:8599089 (Wang et al., Science 1996; abstract-only): FNTA "was isolated as a specific
cytoplasmic interactor of the transforming growth factor-beta (TGF-beta) and activin type
I receptors ... FNTA interacts specifically with ligand-free TGF-beta type I receptor but
is phosphorylated and released upon ligand binding." Basis for TAS annotations to
GO:0007179 (TGF-beta receptor signaling) and cytoplasm (GO:0005737). A moonlighting/
regulatory interaction; the receptor-tyrosine-kinase-binding IEA (GO:0030971) and NMJ
IEA annotations trace to the mouse ortholog (Q61239/Q541Z2) MUSK/AGRIN work; UniProt
records "May positively regulate neuromuscular junction development downstream of MUSK via
its function in RAC1 prenylation and activation" (By similarity).

## Protein-protein interactions (IntAct/ComplexPortal IPI, bare "protein binding")

Many GO:0005515 IPI annotations from IntAct capture interactions with the beta subunits
(FNTB P49356, PGGT1B P53609) and CaaX substrates (HRAS P01112, KRAS P01116, NRAS P01111),
plus AP4M1 (O00189). These are the expected heterodimer partners and substrates.
- PMID:31209342 (GGTase3 paper): FNTA interactions with FNTB, PGGT1B, and RAS listed in
  IntAct; the paper itself is about a *different* alpha subunit (PTAR1) forming GGTase3.
- PMID:35839996 (RAS interactome, full text available): SILAC-AP-MS interactomes of the
  four RAS isoforms; FNTA appears as a RAS interactor (prenylation substrate binding).
- PMID:32296183 (HuRI binary interactome), PMID:33961781 (BioPlex), PMID:40205054
  (multimodal cell maps): large-scale interactome maps. Bare protein-binding IPIs; per
  policy retained but MARK_AS_OVER_ANNOTATED (uninformative MF).
- PMID:24981860 (chromatin demethylase complex map): FNTA co-purified with FNTB/PGGT1B in
  a large AP-MS study; bare protein binding.

## Annotation-review decisions (summary)

Core, well-supported (ACCEPT):
- FTase activity GO:0004660 (EXP/IDA; contributes_to) and CAAX GGTase activity GO:0004662
  / protein GGTase activity GO:0004661 (IDA), the two complexes GO:0005965 & GO:0005953,
  and protein farnesylation/geranylgeranylation GO:0018343/GO:0018344.
- cytosol/cytoplasm GO:0005829/GO:0005737.
- microtubule binding, alpha-tubulin binding, microtubule associated complex (IDA).

Non-core (KEEP_AS_NON_CORE): HDAC6/microtubule-movement regulation, enzyme binding (HDAC6),
TGF-beta receptor signaling, neuromuscular-junction / AChR-clustering (ortholog IEA),
positive regulation of Rac signaling, CAAX-box protein maturation, peptide pheromone
maturation (fungal-process IBA).

Over-annotation / questionable:
- GO:0010698 acetyltransferase activator activity: MARK_AS_OVER_ANNOTATED — abstract
  describes regulation of the *deacetylase* HDAC6, not an acetyltransferase.
- Bare GO:0005515 protein binding IPIs: MARK_AS_OVER_ANNOTATED (policy: not REMOVE).
- GO:0004663 Rab geranylgeranyltransferase activity (IEA from mouse ortholog): the RabGGTase
  alpha subunit is a *different* protein (RABGGTA); FNTA is the FTase/GGTase-I alpha, not
  the RabGGTase alpha. Electronic ortholog transfer is over-broad -> MARK_AS_OVER_ANNOTATED.
- GO:0008318 protein prenyltransferase activity (IEA/InterPro): correct but generic parent;
  MODIFY toward the specific transferase activities is not needed since specifics already
  annotated -> KEEP_AS_NON_CORE (accurate parent).
- GO:0030971 receptor tyrosine kinase binding (IEA, mouse MUSK): KEEP_AS_NON_CORE.

## Core function modeling (shared-alpha-subunit dual role)

FNTA does not independently catalyze prenyl transfer; catalysis is a property of each
assembled heterodimer (Zn2+ and most substrate contacts are in the beta subunit). Modeled
as two GO-CAM-like core functions plus a regulatory one:
1. FTase: molecular_function = molecular adaptor activity (GO:0060090; subunit role),
   contributes_to = protein farnesyltransferase activity (GO:0004660),
   in_complex = protein farnesyltransferase complex (GO:0005965),
   directly_involved_in = protein farnesylation (GO:0018343).
2. GGTase-I: molecular_function = molecular adaptor activity (GO:0060090),
   contributes_to = CAAX-protein geranylgeranyltransferase activity (GO:0004662),
   in_complex = CAAX-protein geranylgeranyltransferase complex (GO:0005953),
   directly_involved_in = protein geranylgeranylation (GO:0018344).
3. Microtubule-associated regulation of HDAC6: molecular_function = alpha-tubulin binding
   (GO:0043014); location cytosol (GO:0005829).
