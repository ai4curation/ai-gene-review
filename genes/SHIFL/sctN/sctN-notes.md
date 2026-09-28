# Notes: *Shigella flexneri* sctN / Spa47 / SpaL (UniProt P0A1C1)

Curation journal for the AI gene review. All assertions carry provenance.

## Identity

- UniProt **P0A1C1**, `SCTN_SHIFL`, 430 aa, encoded on the large virulence
  plasmid (pWR100 / pWR501 / pMYSH6000 / pCP301; ordered locus CP0149).
- Synonyms in the UniProt record: `sctN` (unified Hueck nomenclature),
  `mxiB`, `spa47`, `spaL`.
- UniProt RecName is **"Type 3 secretion system ATPase"** with
  **EC 7.4.2.8** (`ATP + H2O + cellular protein(Side 1) = ADP + phosphate +
  cellular protein(Side 2)`), i.e. the **protein-translocating export ATPase**
  EC, *not* the ATP-synthase EC 7.1.2.2. This matters: several sibling
  flagellar FliI entries in this corpus still carry the synthase EC and the
  name "Flagellum-specific ATP synthase", which is what drives the ATP-synthase
  keyword cascade there. **P0A1C1 does not have that problem** — its name and EC
  are already correct, so the ATP-synthase GO rows here come only from
  homology pipelines (TreeGrafter, InterPro2GO) and the GOC inference over them.
- PANTHER classification (from `interpro/panther/PTHR15184/PTHR15184-entries.csv`):
  `P0A1C1 ... PTHR15184:SF9, SPI-1 TYPE 3 SECRETION SYSTEM ATPASE`.

## Core biology

**Spa47 is a bona fide, oligomerization-activated ATPase.** The Dickenson lab
produced the first purified active enzyme:
[PMID:26947936 "providing the first direct evidence that Spa47 is a bona fide ATPase"]
and showed activity tracks oligomeric state
[PMID:26947936 "identified multiple oligomeric species of Spa47 with the largest greater than 8 fold more active for ATP hydrolysis than the monomer"].
A Walker-A lysine mutant (K165A) is catalytically dead
[PMID:26947936 "An ATPase inactive Spa47 point mutant was then engineered by targeting a conserved Lysine within the predicted Walker A motif of Spa47"]
and fails to complement a *spa47* null for invasion.

**Kinetics** (UniProt BIOPHYSICOCHEMICAL PROPERTIES, from PMID:29595954):
KM(ATP) = 181 µM monomer / 114 µM trimer; kcat 0.22 s⁻¹ monomer, 0.84 s⁻¹ trimer.
These are hydrolysis rates — there is no reported synthesis activity for this
enzyme anywhere in the literature.

**Structure.** Crystal structures of Spa47(80-430) WT and active-site mutants
(PDB 5SWJ/5SWL/5SYP/5SYR) support an activated hexamer model with shared
inter-protomer active sites
[PMID:27770024 "each of the tested residues are essential for Spa47 ATPase activity"],
[PMID:27770024 "Spa47 oligomerization and ATP hydrolysis are needed for complete T3SS apparatus formation, a proper translocator secretion profile, and Shigella virulence"].
Nucleotide-bound structures (PDB 5YBH/5YBI/5ZT1) define the ATP site
[PMID:30013545 "a catalytic magnesium ion and an ordered water molecule"].
Interfacial residues supporting oligomerization were mapped in
[PMID:31162724 "we developed a model of an activated Spa47 homo-hexamer"],
[PMID:31162724 "many of the engineered mutants are unable to form oligomers and efficiently hydrolyze ATP in vitro"].

**Homo-oligomerization is the activation mechanism**, so the two IntAct
`identical protein binding` rows (GO:0042802, IPI, PMID:30460850 and
PMID:31162724) are informative rather than boilerplate self-interaction. The
inhibitor paper also purified the oligomer
[PMID:30460850 "we leveraged the ability to purify an active oligomeric Shigella T3SS ATPase"]
and showed the inhibitors act without dissolving it
[PMID:30460850 "the inhibitors do not function through disruption of Spa47 oligomers or by preventing T3SA formation"].

**Location and complex.** Native Spa47 is cytoplasmic and in large complexes
[PMID:18657109 "the native T3SS ATPase, Spa47, from the cytoplasm of Shigella flexneri"],
[PMID:18657109 "demonstrating it to be in two distinct high-molecular-weight complexes with Spa33: MxiN and MxiK"].
Cryo-ET of intact *S. flexneri* injectisomes places the hexamer at the hub of
the cytoplasmic sorting platform
[PMID:25583506 "the hub consists mainly of a hexamer of the Spa47 ATPase"],
aligned below the export gate
[PMID:25583506 "Multiple contacts among those components are essential to align the Spa47 ATPase with the central channel of the MxiA protein export gate"].
Interactions with MxiK/SctK and MxiN/SctL were established genetically and
biochemically
[PMID:12864857 "we identified interactions between MxiK and Spa33 and Spa47 and between MxiN and Spa33 and Spa47"];
MxiN/SctL regulates the enzyme differentially by oligomeric state
[PMID:29595954 "interaction of MxiN with Spa47 requires the six N-terminal residues of Spa47 that are also necessary for stable Spa47 oligomer formation and activation"].
Injectisome targeting is a property of the N-terminal domain, not of catalysis
[PMID:31978132 "the N-terminus of Spa47, not ATPase activity, is responsible for incorporation into the injectisome"].

## Energetics: why the proton terms are wrong for Spa47

Spa47 is a soluble cytoplasmic protein with no transmembrane segment. The
proton motive force *is* used by the Shigella T3SS, but it is used by the
**inner-membrane export gate MxiA/SctV**, not by the ATPase:

- [PMID:27171191 "Efficient T3S requires a cytoplasmic ATPase and the proton motive force (PMF)"] —
  these are listed as two separate requirements.
- [PMID:27171191 "MxiA family proteins and their regulators are implicated in utilization of the PMF for protein export"] —
  PMF utilization is assigned to MxiA (SctV), the membrane protein.
- [PMID:30107569 "Substrate translocation itself is mainly fueled by the PMF across the bacterial inner membrane"]
  and [PMID:30107569 "Several conserved charged residues reside within the predicted TMD of SctV that seem to be implicated in utilization of the PMF"] —
  again the charged residues that handle protons are in SctV's TMD.

So: depending on the PMF is not the same as transporting protons, and
hydrolysing ATP is not the same as synthesising it. `GO:1902600` and
`GO:0046933`/`GO:0015986` all belong to other proteins (SctV) or to other
families (F1-beta).

## The ATP-synthase propagation

GOA row: `GO:0046933 proton-transporting ATP synthase activity, rotational
mechanism`, IEA, `GO_REF:0000118` (TreeGrafter), `WITH/FROM
PANTHER:PTN001807734`.

From `projects/TREEGRAFTER/rotary_atpase/node_placement.tsv`:

- `PTN008558586` is the **IBD node** carrying GO:0046933 and GO:0045259, and its
  `event_type` is **DUPLICATION**.
- Its two children are `PTN008558588` (the F1-beta clade: subfamilies SF51,
  SF74, SF75, SF76, SF80, SF82, SF83, SF85 — all "ATP SYNTHASE SUBUNIT BETA")
  and `PTN000390097` (a Eubacteria speciation node holding SF62 "SPI-2 TYPE 3
  SECRETION SYSTEM ATPASE", SF81 "FLAGELLUM-SPECIFIC ATP SYNTHASE" and **SF9
  "SPI-1 TYPE 3 SECRETION SYSTEM ATPASE"** — the subfamily P0A1C1 belongs to).
- `PTN001807734`, the TreeGrafter graft node for P0A1C1, is listed as a graft
  node **within clade PTN000390097**.

So the failure is not "the target sits outside the clade the seeds represent" —
it is that **the IBD was placed one node too deep, at the duplication that
separates F1-beta from the T3SS/flagellar export ATPases**. All the experimental
seeds for GO:0046933 (E. coli AtpD, human ATP5F1B, yeast ATP2, S. pombe atp2)
lie in the `PTN008558588` child. Moving the IBD from `PTN008558586` to
`PTN008558588` would keep every seeded annotation and stop the function leaking
into the export-ATPase sister clade. (This is a slightly different — and more
precise — framing than the CAUVC/fliI sibling review, which described the target
as outside the clade; the tables show the clade relationship explicitly, and the
fix is a node move rather than an IRD.)

The InterPro2GO rows `GO:0046034` and `GO:1902600` come from **IPR004100**
(F1/V1/A1 alpha/beta N-terminal domain), a domain genuinely shared with F1
ATPases — the domain is present, but the mapped terms describe rotary
ATP-synthase biology that this protein does not do. `GO:0015986` is a
GOC logical inference (`GO_REF:0000108`) over the wrong `GO:0046933` row and
falls with it.

Note the contrast within the same GOA file: the InterPro2GO rows sourced from
**IPR005714** (Type 3 secretion system ATPase SctN) are all correct
(`GO:0016887`, `GO:0030254`, `GO:0030257`, `GO:0005737`). It is specifically the
IPR004100 (shared F1 domain) and PANTHER-family rows that misfire.

## Decisions taken

| Term | Evidence / source | Action |
|---|---|---|
| GO:0005524 ATP binding | IEA IPR000194, IPR020003 | ACCEPT |
| GO:0005737 cytoplasm | EXP PMID:18657109 | ACCEPT |
| GO:0005737 cytoplasm | EXP PMID:25583506 | ACCEPT |
| GO:0005737 cytoplasm | IEA GO_REF:0000120 | ACCEPT |
| GO:0008564 protein-exporting ATPase activity | IEA EC:7.4.2.8 | ACCEPT (core MF) |
| GO:0015986 PMF-driven ATP synthesis | IEA GO_REF:0000108 from GO:0046933 | REMOVE |
| GO:0016887 ATP hydrolysis activity | IEA IPR005714 | ACCEPT |
| GO:0030254 protein secretion by T3SS | IEA IPR005714 | ACCEPT |
| GO:0030257 T3SS complex | IEA IPR005714 | ACCEPT |
| GO:0042802 identical protein binding | IPI PMID:30460850 | ACCEPT |
| GO:0042802 identical protein binding | IPI PMID:31162724 | ACCEPT |
| GO:0046034 ATP metabolic process | IEA IPR004100 | MARK_AS_OVER_ANNOTATED |
| GO:0046933 ATP synthase activity, rotational | IEA GO_REF:0000118 PTN001807734 | REMOVE |
| GO:1902600 proton transmembrane transport | IEA IPR004100 | REMOVE |

No `NEW` terms proposed. Unlike the CAUVC/fliI sibling (which was missing
`GO:0008564` and the flagellum-assembly child term), this GOA already carries
the full correct set: the export-ATPase MF via the correct EC, ATP hydrolysis,
the T3SS process and complex terms, and the cytoplasm location. Invasion /
virulence phenotypes of *spa47* mutants are downstream consequences of failed
effector secretion (the effectors do the invading), so no host-interaction BP
term is proposed — that would be the indirect-effect over-annotation CLAUDE.md
warns against. There is no GO term for the T3SS cytoplasmic sorting platform;
`GO:0030257` is the most precise CC available (checked against QuickGO — the
only T3SS CC terms are GO:0030257 and the other secretion-system complexes).
