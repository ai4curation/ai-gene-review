# AVR-Pita (F7J183, *Pyricularia oryzae*) — curation notes

Research journal for the GO annotation review. No `-deep-research-falcon.md` file was
present in this folder at the time of writing (a background retry was reported as
running but had not produced a file), so this review was built from UniProt
(`AVR-Pita-uniprot.txt`), the cached publications in `publications/`, and PubMed
metadata lookups. No deep-research file is cited as a reference.

## What the gene is

- Cloned as the avirulence gene matching the rice *Pi-ta* locus, from a telomeric
  region of chromosome 3: "Genetic mapping showed that the rice blast avirulence gene
  AVR-Pita is tightly linked to a telomere on chromosome 3 in the plant pathogenic
  fungus Magnaporthe grisea" and "When introduced into virulent rice pathogens, the
  cloned gene specifically confers avirulence toward rice cultivars that contain
  Pi-ta." [PMID:11090206]
- Sequence relationships place it in the fungal aspzincin (M35) zinc metalloprotease
  group: "The fungal metalloproteases showing the greatest sequence identity to
  AVR-Pita fall into families M35 and M36 in this superfamily of zinc-dependent
  metalloproteases." and "AVR-Pita appears to encode a neutral zinc metalloprotease,
  given its amino acid sequence similarity to fungal metalloproteases" [PMID:11090206].
  UniProt concurs ("Belongs to the peptidase M35 family", Pfam PF14521 Aspzincin_M35,
  PANTHER PTHR37016:SF7, signal peptide 1-17, Zn(2+) cofactor).
- **Catalytic motif check** (requested): the F7J183 224-residue precursor contains the
  aspzincin HExxH zinc-binding motif `...DTAIL HEMLH IILNEWEDYGY...`, i.e. H-E-M-L-H
  beginning at position 177 of this sequence, with the downstream GTxDxxYG-type
  region represented by `NEWEDYGYEWDEI`. The motif is therefore intact in this allele.
  The residue mutated in the classical virulent allele (active-site glutamate,
  numbered E177 in the 223-residue AVR-Pita form used by the original papers) is the
  Glu of this HExxH motif.
- Importantly, protease activity has never been demonstrated: "Although protease
  activity by this protein has not been demonstrated biochemically, it is implicated."
  [PMID:11090206]. Mutating the predicted active site abolishes avirulence, but the
  authors explicitly allow the alternative reading that the mutations change
  recognition rather than catalysis: "However, we do not rule out an alternative
  explanation for the effect of these missense mutations on AVR-Pita avirulence
  function" [PMID:11090206]. The 25 years since have added no catalytic assay and no
  substrate; the "Lysine-specific metallo-endopeptidase" name on the UniProt entry is
  a domain-family label, not a measured specificity.
- AVR-Pita is not required for pathogenicity: "AVR-Pita from the rice (Oryza sativa)
  pathogen Magnaporthe grisea encodes a putative zinc-dependent metalloprotease that
  is dispensable for pathogenicity" [PMID:15319478].

## Secretion and where the protein acts

- Signal peptide plus UniProt "Secreted" subcellular location; it behaves as a
  *cytoplasmic* (host-translocated) effector in live-cell imaging work: "we tested
  additional cytoplasmic effectors AVR-Pita (ref. 8) (Fig. 4c), Bas1 (ref. 25)
  (Fig. 4c) and Bas107" — secretion and BIC localisation continued in brefeldin A,
  placing it in the Golgi-independent, BIC-associated secretion route
  [PMID:23774898]. The same classification is repeated in [PMID:38722963]
  ("The cytoplasmic effectors include known AVR effectors, such as Pwl2, Avr-Pita,
  and AvrPiz-t").
- Inside plant cells the protein localises to mitochondria: "Avr-Pita:YFP perfectly
  co-localized with the mitochondrial marker Rflb:mCherry (Wang et al., 2006) in rice
  protoplasts and with the mitochondrial dye MitoTracker in onion epidermal cells"
  [PMID:33443630].

## Virulence activity (the only mechanistic function evidence)

Han et al. 2021 [PMID:33443630] is the key paper:

- "ectopically expressing Avr-Pita in rice enhances susceptibility to M. oryzae and
  suppresses pathogen-associated molecular pattern (PAMP)-triggered defense responses"
- Target: "we conducted yeast two-hybrid (Y2H) assays using Avr-Pita49–224 (processed
  mature protease) as bait and identified six candidate proteins" → the COX assembly
  protein OsCOX11, confirmed by pull-down.
- Output: "ROS accumulation was significantly suppressed in PUbi::Avr-Pita and
  PUbi::OsCOX11 plants, whereas the ROS burst was strongly delayed in oscox11/OsCOX11
  cells after chitin treatment" and "COX activity was much higher in PUbi::Avr-Pita and
  PUbi::OsCOX11 plants than in the WT both before and after chitin treatment".

So the molecular activity that AVR-Pita has actually been shown to perform on a host
substrate is binding/modulating OsCOX11 at host mitochondria, with the measurable
output being suppression of chitin (PAMP)-triggered ROS. Nothing in that paper tests
proteolysis of OsCOX11, so no catalytic claim follows from it.

## Avirulence / recognition

- Direct binding to the Pi-ta LRD was reported: "These data suggest that the AVR-Pita
  176 protein binds directly to the Pi-ta LRD region inside the plant cell to initiate
  a Pi-ta-mediated defense response" [PMID:10921881], and effector-side mutations that
  abolish avirulence also abolish elicitor activity: "two separate mutations in the
  AVR-Pita protease motif that eliminate avirulence in fungal infection assays also
  eliminate elicitor activity in the transient expression assay" [PMID:10921881].
- That receptor assignment is now contested: "we found that AVR-Pita recognition relies
  solely on Ptr and that the NLR Pi-ta has no role in it, indicating that it is not the
  Pi-ta resistance gene" [PMID:38834685]. Which rice protein recognises AVR-Pita has
  therefore changed, but the effector-side fact — that AVR-Pita is the recognised
  ligand whose presence triggers an R-gene-dependent hypersensitive response and
  race-specific resistance — is unchanged, and is what the symbiont-side GO term
  (GO:0080185) describes. The `genes/ORYSJ/Pi-ta` review in this repository records
  the same reassignment from the host side.
- Population genetics (not function, recorded for context): the gene is highly mobile
  and polymorphic — "AVR-Pita (AVR-Pita1 and AVR-Pita2) is highly variable in its
  genome location" and most homologs "could elicit Pita-mediated resistance"
  [PMID:21829350]; it is a three-member family (AVR-Pita1/2/3) [PMID:18393625]; Pot3
  transposon insertion into the protease-motif-encoding region is one route to
  virulence [PMID:17387027].

## Decisions taken in the review

1. **GO:0008237 metallopeptidase activity (IEA, InterPro IPR024079)** —
   `KEEP_AS_NON_CORE`. The zincin fold and the intact HExxH motif make the
   family-level inference reasonable, and the InterPro mapping is not wrong; but no
   catalytic activity, substrate or product has ever been shown, the gene is
   dispensable for pathogenicity, and the one mechanistic study of its host activity
   found protein binding to OsCOX11 rather than cleavage. So the term is retained at
   family level, not promoted to a core function.
2. **GO:0004222 metalloendopeptidase activity (IEA, InterPro IPR029463 Lys_MEP)** —
   `MARK_AS_OVER_ANNOTATED`. This mapping adds an endopeptidase (and, via the
   "lysine-specific metallo-endopeptidase" family name, a substrate-specificity)
   claim on top of the unverified catalytic claim. Deuterolysin-like M35 members are
   indeed endopeptidases, so it is not wrong in principle — but for this protein
   nothing has been measured, and this is the more specific of two overlapping
   domain-derived rows.
3. **GO:0005576 extracellular region (IEA, SubCell Secreted)** — `ACCEPT`. Signal
   peptide, UniProt Secreted, and imaging work that follows the protein through the
   secretory route into the BIC.
4. **New**: host-side location `GO:0033650 host cell mitochondrion` and the two
   process terms for what the effector itself does — `GO:0052034 effector-mediated
   suppression of host pattern-triggered immunity` (it binds OsCOX11 and raises COX
   activity, which is the step that lowers chitin-triggered ROS) and `GO:0080185
   effector-mediated activation of plant hypersensitive response by symbiont` (it is
   the recognised ligand whose detection triggers the HR). Both pass the
   participation test: the effector performs the binding/modulation step itself, and
   is itself the elicitor, rather than merely being required for an outcome.
   Comparator check for the two process terms: sibling blast effectors curated in this
   repository carry exactly these symbiont-side terms — `genes/PYROR/AVR-Pia` uses
   GO:0080185 for its RGA5-dependent HR activation, and `genes/FULFL/AVR9` the same;
   so the terms are the convention for avirulence effectors, not a gap being invented.
   `GO:0030430 host cell cytoplasm` was considered and left out: AVR-Pita is described
   as a cytoplasmic effector in reviews and BIC-secretion assays, but the only direct
   localisation data in rice cells is mitochondrial, and GO:0033650 already states the
   host-cell compartment.

## 2026-10-10: deep research arrived after the review

The falcon retry finished after the review above was written
(`AVR-Pita-deep-research-falcon.md`). It agrees with every decision here: protease
activity is a sequence/domain inference only ("Its classification as an M35 zinc
metalloprotease is a *sequence/domain inference*, not a demonstrated catalytic
reaction"), the host target is OsCOX11 at mitochondria, and recognition goes through
Ptr rather than the Pi-ta NLR (Xiao 2024). No action changed; the file is now cited
on the metalloendopeptidase row and in references.
