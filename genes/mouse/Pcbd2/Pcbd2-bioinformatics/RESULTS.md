# Is the Pcbd2-specific N-terminal extension a mitochondrial presequence?

All numbers below are reproduced by `python3 nterm_mts_analysis.py` and stored in
`results.json`. Nothing is hardcoded. Method, reference sets and limits:
see `README.md` and the module docstring.

## The sequences

| Protein | UniProt | Length | First 32 residues |
|---|---|---|---|
| mouse Pcbd2 (DCoH2) | Q9CZL5 | 136 | `MVAAAAVAVAAVGARSAGRWLAALRSPGASRA` |
| mouse Pcbd1 (DCoH)  | P61458 | 104 | `MAGKAHRLSAEERDQLLPNLRAVGWNEVEGRD` |
| human PCBD2         | Q9H0N5 | 130 | `MAAVLGALGATRRLLAALRGQSLGLAAMSSGT` |
| human PCBD1         | P61457 | 104 | `MAGKAHRLSAEERDQLLPNLRAVGWNELEGRD` |

Mouse Pcbd1 residue 1 aligns to mouse Pcbd2 residue ~34: `MAGKAHRLSAEERDQL`
versus Pcbd2 `MSSDAQWLTAEERDQL` (Pcbd2 34–49). So the Pcbd1/Pcbd2 difference in
length is one N-terminal extension on Pcbd2, not scattered insertions.

Three independent observations say the extension is separable from the functional
core, and that the core is what has actually been characterised:

* Both Pcbd2 crystal structures cover **33/34–136** (PDB 1RU0, 4WIL) — i.e. Rose
  et al. (PMID:15182178) crystallised and assayed the protein *without* the
  extension, and that construct showed dehydratase activity.
* UniProt flags both source mRNAs (`AAH28642.1`, `BAB28260.1`) as
  `Erroneous initiation` — those clones began at the internal Met34; the
  extension was added later (sequence version 2, 2009).
* Mouse residue 34 is a Met, so Met34 is a usable alternative initiation codon.

## Feature percentiles

Scored window = first 32 residues. `pos` = 259 reviewed mouse proteins with a
UniProt `TRANSIT` "Mitochondrion" feature (the presequence itself is scored);
`neg` = 300 reviewed mouse cytosolic (SL-0091) proteins with no transit, signal
or transmembrane feature.

| Feature | mouse Pcbd2 | pos p10/median/p90 | neg p10/median/p90 | %ile in pos | %ile in neg |
|---|---|---|---|---|---|
| net charge   | **+4**   | 3 / 4 / 6 | −4 / 0 / 4 | 41.1 | 88.8 |
| Arg count    | **4**    | 2 / 4 / 6 | 0 / 2 / 4 | 47.9 | 88.5 |
| acidic count | **0**    | 0 / 0 / 1 | 1 / 4 / 7 | 33.0 | 2.3 |
| Ser+Thr frac | 0.094    | 0.044 / 0.125 / 0.219 | 0.063 / 0.125 / 0.219 | 32.8 | 34.7 |
| Ala frac     | **0.406** | 0.044 / 0.125 / 0.250 | 0.031 / 0.063 / 0.156 | 99.6 | 100.0 |
| max ⟨µH⟩     | **0.423** | 0.260 / 0.416 / 0.599 | 0.203 / 0.334 / 0.496 | 52.1 | 77.3 |

On the four classical presequence features the mouse Pcbd2 extension lands
almost exactly at the **median of real mitochondrial presequences**: net charge
+4 (positives' median is +4), 4 arginines (median 4), zero acidic residues
(median 0), and a maximum mean hydrophobic moment of 0.423 against a positives'
median of 0.416. Against cytosolic N-termini the same values are at the 89th,
89th, 2.3rd (i.e. unusually acidic-free) and 77th percentiles.

**Internal negative control.** Mouse Pcbd1 — the paralog with no mitochondrial
annotation anywhere — behaves as the opposite case over the same window: net
charge −1 (0.2nd percentile of presequences; essentially no real presequence is
that acidic) and 6 acidic residues (99.8th percentile). The discrimination is
therefore not an artefact of the window or the scales.

**The confounder is real and it is large.** The extension is 40.6% alanine, which
is off the top of *both* reference distributions (99.6th and 100th percentile).
A low-complexity Ala tract is acidic-residue-free for reasons that have nothing
to do with targeting, so the single most presequence-like feature in the table —
`acidic count = 0` — is substantially explained by composition bias rather than
by selection for import. What survives that caveat is the positive charge (4 Arg
are real residues, not an absence) and the amphipathicity.

**Human PCBD2** is directionally the same but weaker: net charge +3, 0 acidic,
3 Arg, 25% Ala, ⟨µH⟩ 0.334 (24th percentile of presequences). The extension is
present and basic in both mammals examined.

## Orthologs

Only four reviewed PCBD2 entries exist. Human (130 aa) and mouse (136 aa) carry
the extension; orangutan Q5R7K1 (117 aa) begins mid-extension (`LLAALRGQ…`), so
its entry is N-terminally incomplete rather than informative. Chicken Q9DG45
(103 aa) starts at `MSSQSHWLTAEERTQ…`, which aligns to the mouse core at residue
34 — i.e. it appears to lack the extension entirely.

That chicken entry does **not** establish that the extension is mammal-specific.
It is `PE 2: Evidence at transcript level` from a single mRNA, and mouse's own
mRNAs were flagged `Erroneous initiation` for exactly this failure mode — a clone
that began at the internal Met. Treat the phylogenetic distribution of the
extension as unresolved from reviewed UniProt entries alone.

## A mitochondrial PCD exists elsewhere in the family

PANTHER's PAINT table for PTHR12599 (`interpro/panther/PTHR12599/PTHR12599-paint.tsv`)
contains an IBD for `GO:0005739 mitochondrion` at node PTN000972177, placed at
Embryophyta (taxon:3193, land plants) and seeded by Arabidopsis
`AGI_LocusCode:AT1G29810` — UniProt Q6QJ72, whose recommended name is
"Pterin-4-alpha-carbinolamine dehydratase 2, mitochondrial". A second plant node
(PTN000972175) carries `GO:0009536 plastid`.

So this enzyme family does have organelle-targeted members, and a mitochondrial
PCD is not an a priori oddity. This is context, not evidence: the plant and
mammalian extensions are not homologous presequences, and the vertebrate IBD
node PTN002650414 — seeded by human PCBD1 and rat Pcbd1 — carries only
nucleoplasm, cytosol and `GO:0008124`, with no mitochondrial component.

## Reading

The extension is **compositionally compatible with a cleavable mitochondrial
presequence** — basic, arginine-bearing, acidic-free and amphipathic at the
median of 259 real mouse presequences — while its paralog Pcbd1, which has no
mitochondrial annotation, is not. This supplies a mechanism that the single HDA
`mitochondrion` annotation (PMID:18614015, MitoCarta) otherwise lacks, and it
fits a coherent model in which residues 1–33 are cleaved on import to give the
mature 34–136 species that was crystallised and shown to be an active
dehydratase.

It does **not** demonstrate that this happens. Three things specifically block
that conclusion:

1. Compositional heuristics are not a targeting predictor. No MitoFates/TargetP
   run is included (none is callable from this environment without a licence or
   web upload), and the 40.6% Ala content means the features are partly driven by
   low complexity.
2. UniProt annotates **no** `TRANSIT` feature on Q9CZL5, and its SUBCELLULAR
   LOCATION records only Cytoplasm and Nucleus — the curators saw this sequence
   and did not call a presequence.
3. The best mouse-specific localisation evidence points elsewhere: Kazgan et al.
   (PMID:24389307) report DCoH2 "distributed in both the nucleus and cytoplasm"
   in Hepa1-6 cells with strong nuclear staining, consistent with its
   characterised HNF1A-coactivator role.

Corroboration for a mitochondrial pool is weaker in kind than imaging would be,
but there is more of it than the single HDA row suggests. Three further
independent mitochondrial preparations place a PCD2 there:

* **Human PCBD2 is in MitoCoP.** QuickGO records `Q9H0N5 located_in GO:0005739`
  with **HTP** evidence from PMID:34800366 (Morgenstern et al., *Cell Metab*
  2021) — a study whose whole purpose was to separate genuine residents from
  contaminants: "We classified >8,000 proteins in mitochondrial preparations of
  human cells and defined a mitochondrial high-confidence proteome of >1,100
  proteins (MitoCoP)." This is a deliberately high-confidence list from 2021, not
  a 2008 MS inventory, and it concerns the **ortholog** rather than mouse.
* **Mouse Pcbd2 was detected in a liver mitochondrial acetylome.** UniProt's
  K120/K124/K131 acetylation sites on Q9CZL5 carry
  `ECO:0007744|PubMed:23576753`, from a SIRT3 study of the liver mitochondrial
  lysine acetylome, and K120/K124/K131 succinylation from PMID:23806337 (SIRT5).
  SIRT3 and SIRT5 are both mitochondrial sirtuins.
* The MitoCarta HDA itself (PMID:18614015), in mouse.

These are all the same *class* of evidence — detection in an organellar
preparation — so they do not substitute for a localisation experiment. But four
preparations across two species, one of them explicitly contaminant-filtered,
is not the profile of a single co-purification artefact. Note that the cached
text of PMID:34800366 and PMID:23576753 does not name PCBD2; the checkable facts
are the GOA annotation and the UniProt evidence tags, both verified here.

**Conclusion for curation:** the HDA `mitochondrion` annotation is neither
confirmed nor refuted, but it is better supported than it first looks. It should
be retained as non-core rather than removed — removing it would discard a claim
that has four independent organellar preparations behind it and that this
analysis gives a plausible import mechanism for. The dehydratase and
HNF1-coactivator functions are cytosolic/nuclear and are unaffected either way.

**What would settle it:** N-terminal sequencing or Edman/MS of endogenous Pcbd2
from purified mitochondria to test for cleavage at ~residue 33; an
Pcbd2(1–33)-GFP fusion scored for mitochondrial import; and submitochondrial
fractionation plus protease protection to distinguish a matrix pool from surface
association.
