# SMS (Spermine synthase) — review notes

UniProt: P52788 (SPSY_HUMAN), gene SMS, HGNC:11123, chromosome Xp22.1. 366 aa, ~41 kDa.
EC 2.5.1.22. All assertions below are grounded in local files.

## Core function

SMS is **spermine synthase** (a.k.a. spermidine aminopropyltransferase), which catalyzes
the **final, committed step of polyamine biosynthesis**: transfer of an aminopropyl group
from decarboxylated S-adenosylmethionine (dcSAM/dcAdoMet) onto spermidine, producing
**spermine** plus 5'-methylthioadenosine (MTA).

- UniProt FUNCTION: "Catalyzes the production of spermine from spermidine and
  decarboxylated S-adenosylmethionine (dcSAM)." [file:human/SMS/SMS-uniprot.txt]
- UniProt CATALYTIC ACTIVITY: "S-adenosyl 3-(methylsulfanyl)propylamine + spermidine =
  spermine + S-methyl-5'-thioadenosine + H(+)"; Rhea:RHEA:19973; EC=2.5.1.22
  (ECO:0000269|PubMed:18367445). [file:human/SMS/SMS-uniprot.txt]
- UniProt PATHWAY: "Amine and polyamine biosynthesis; spermine biosynthesis; spermine
  from spermidine: step 1/1." [file:human/SMS/SMS-uniprot.txt] (UniPathway UPA00249/UER00315)
- Reactome R-HSA-351210: "Spermine synthase (SMS)... transfers an aminopropyl group from
  decarboxylated S-adenosylmethionine (dc-AdoMet) to spermidine (SPM) to form spermine (SPN)"
  [reactome/R-HSA-351210.md]
- GO term GO:0016768 spermine synthase activity def (OLS): "S-adenosylmethioninamine +
  spermidine = 5'-methylthioadenosine + spermine." Matches the UniProt reaction.

## Structure / mechanism (PMID:18367445, full text available)

Crystal structures of two ternary complexes (with MTA+spermidine; with MTA+spermine),
solved at 1.95 and 2.45 Å.
- "They show that the enzyme is a dimer of two identical subunits." — obligate **homodimer**.
- Each monomer has three domains: a C-terminal catalytic domain similar to spermidine
  synthase; a central four-β-strand domain; and an N-terminal domain with "remarkable
  structural similarity to S-adenosylmethionine decarboxylase." [PMID:18367445]
- "Dimerization occurs mainly through interactions between the N-terminal domains. Deletion
  of the N-terminal domain led to a complete loss of spermine synthase activity, suggesting
  that dimerization may be required for activity." [PMID:18367445]
- Catalytic residues: Asp201 and Asp276 (conserved in aminopropyltransferases), Glu353.
  Mutagenesis: D276N reduces kcat/Km >200,000-fold; D201A/N >100,000-fold; E353Q 800-fold.
  [PMID:18367445; also UniProt MUTAGEN 201/276/353]
- Product inhibition by MTA (Ki ~0.3 µM), stronger than for spermidine synthase.
- UniProt SUBUNIT: "Homodimer. Dimerization is mediated through the N-terminal domain and
  seems to be required for activity." [file:human/SMS/SMS-uniprot.txt]

## Localization

- Cytosol: GO:0005829 supported by Reactome (TAS) and ARBA (IEA). Consistent with a soluble
  cytosolic biosynthetic enzyme (no signal peptide, no TM segments in UniProt record).
- GO:0070062 extracellular exosome (HDA, PMID:23533145): from a shotgun proteomic survey of
  ~900 proteins in urine/expressed-prostatic-secretion exosome preparations. Abstract only
  (full_text_available: false); SMS not individually characterized. This is a bulk-proteomics
  co-purification, not evidence of a spermine-synthase function in exosomes → over-annotation
  for a cytosolic metabolic enzyme; kept but flagged (HDA, so not removed).

## Disease

- Snyder-Robinson syndrome (MRXSSR; MIM:309583): X-linked recessive syndromic intellectual
  disability. UniProt DISEASE: "characterized by a collection of clinical features including
  facial asymmetry, marfanoid habitus, hypertonia, osteoporosis and unsteady gait."
  [file:human/SMS/SMS-uniprot.txt] Caused by SMS loss-of-function variants (e.g. G56S, F58L,
  G67E, V132G, Y328C), which reduce the spermine/spermidine ratio in patient cells consistent
  with impaired spermine biosynthesis. This is the disease consequence of the core enzymatic
  function; not a distinct GO annotation in GOA.

## Family / evolution (PMID:18367445)

Belongs to the spermidine/spermine synthase (aminopropyltransferase / PABS) family. The
AdoMetDC-like N-terminal fusion domain is found in vertebrates, arthropods, and some other
metazoans/choanoflagellates but is absent in nematodes, plants, and fungi; SMS has no AdoMetDC
catalytic activity (lacks the Ser that generates the pyruvoyl cofactor).

## Annotation review summary (11 GOA annotations)

- MF spermine synthase activity (GO:0016768): IBA, IEA, and EXP(PMID:18367445) → all ACCEPT; core.
- BP spermine biosynthetic process (GO:0006597): IBA + IEA → ACCEPT; core.
- BP polyamine metabolic process (GO:0006595): TAS x2 + IEA(ARBA) → correct but a general
  parent grouping; KEEP_AS_NON_CORE (spermine biosynthetic process is the specific term).
- CC cytosol (GO:0005829): TAS(Reactome) + IEA(ARBA) → ACCEPT; core location.
- CC extracellular exosome (GO:0070062): HDA(PMID:23533145) → MARK_AS_OVER_ANNOTATED (bulk
  exosome proteomics; no functional role at that site).

## Core functions (for YAML)

- MF: GO:0016768 spermine synthase activity (enables). Reaction: dcSAM + spermidine → spermine + MTA.
- BP: GO:0006597 spermine biosynthetic process (involved_in).
- CC: GO:0005829 cytosol (located_in).
</content>
</invoke>
