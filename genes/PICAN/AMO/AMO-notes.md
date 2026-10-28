# AMO (P12807, Hansenula polymorpha / Ogataea angusta) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: AMO (HPAO, HPAO-1) is being reviewed in its own right as the closest
experimentally characterised relative of S. pombe cao1 (Q9P7F2). No ProtNLM2
output was opened or used.

### Deep research

`just deep-research-falcon PICAN AMO --fallback perplexity-lite` failed: falcon
returned "Failed to authenticate" (Edison client) and the perplexity-lite fallback
returned HTTP 401 "insufficient_quota". No deep-research file exists. The review is
based on the UniProt record and on cached primary literature (PubMed search for
"Hansenula polymorpha amine oxidase" + peroxisome/methylamine; 34 hits screened by
title; the relevant ones cached in `publications/`).

### Identity and evolutionary placement

- UniProt P12807 AMO_PICAN, 692 aa; PANTHER PTHR10638:SF86 (COPPER AMINE OXIDASE
  1-RELATED). The same subfamily holds S. pombe Cao1 (Q9P7F2) and Cao2 (O42890) and
  several Arthrobacter amine oxidases (`interpro/panther/PTHR10638/PTHR10638-entries.csv`),
  so SF86 is not fungus-specific.
- PAINT (`interpro/panther/PTHR10638/PTHR10638-paint.tsv`): IBDs at the family root
  PTN000067313 for GO:0008131 primary methylamine oxidase activity, GO:0005507 copper
  ion binding and GO:0009308 amine metabolic process. P12807 is not among the IBD
  seeds and GOA carries no IBA row for it (H. polymorpha is not a PAINT-propagated
  genome); its GOA rows are EXP (UniProt) plus IEA. Location IBDs (plasma membrane,
  Golgi/ER/endosome) sit on mammalian nodes and do not apply.
- H. polymorpha has a paralogous CAO, HPAO-2, 34% identical, that prefers aromatic
  amines (benzylamine) [PMID:20155950 "Despite 34% sequence identity and superimposable"].
  HPAO-1 (= AMO, P12807) prefers small aliphatic amines: kcat/Km methylamine 330-fold
  over benzylamine [PMID:20155950]. Ethylamine is the best known substrate
  [PMID:23452079 "Ethylamine is the most efficient known substrate for HPAO-1."].
- Cao1 is 57% identical to HPAO, the highest identity to any characterised CAO
  [PMID:18723604]. Relationship to cao1 is family_member in the same subfamily; strict
  orthology not established.

### Experimentally established for AMO itself (this species' protein)

Activity / chemistry (mostly recombinant protein expressed in S. cerevisiae):
- Active quinoprotein methylamine oxidase, TPQ cofactor, recombinant enzyme as active as native
  [PMID:8011631 "The recombinant enzyme is as active as the native enzyme in catalyzing methylamine oxidation."].
- Native enzyme from methylamine-grown cells oxidises methylamine + O2 to ammonia,
  formaldehyde and H2O2 [PMID:7192080].
- Crystal structures: type 2 copper + TPQ (Tyr405), homodimer, Asp319 catalytic base
  (D319N inactive) [PMID:9551552; PMID:10387066]; precursor Tyr structure with Zn
  [PMID:10933787]; apo/Cu(I)/Co(II) precursor forms [PMID:22691777]; O2 channels
  [PMID:17409383]; Y305 mutants [PMID:20684524]; ethylamine/benzylamine complexes
  [PMID:23452079].
- TPQ biogenesis is self-catalysed, needs only Cu and O2 [PMID:22691777]; Ni(II) can
  substitute [PMID:16245947]. GO topaquinone-biosynthesis terms (GO:0018068 etc.) are
  obsolete, so this is not annotatable as a process.
- Homodimer with intersubunit communication (Zn-Cu heterodimers inactive) [PMID:16584203].

Localization (native host):
- Amine oxidase activity cytochemically localised to peroxisomes in methylamine-grown
  H. polymorpha [PMID:7192080].
- Peroxisomal matrix protein; the C-terminal SRL is not needed for import [PMID:8511963];
  targeting information is in the N-terminal 16 residues (PTS2) [PMID:7805876];
  imported by an amine-inducible PTS2 pathway [PMID:7809160]. Note: UniProt's MOTIF
  690..692 "Microbody targeting signal" (ECO:0000255) is contradicted by these papers.
- In S. cerevisiae heterologous expression it is cytosolic [PMID:20155950].

Physiology:
- Induced on primary amines as sole N source [PMID:8511963]; key enzyme of methylamine
  metabolism [PMID:7192080]. No published amo deletion growth phenotype found. Also
  implicated (enzyme activity level, not gene-specific) in choline/ethanolamine
  degradation via methylamines [PMID:6685994] -- not used for annotation because the
  specific gene product and enzyme identity were not established.

### Decisions

- GO:0008131 (EXP x2, IEA): ACCEPT; core.
- GO:0005507 copper ion binding (IEA): ACCEPT; structural evidence in this protein.
- GO:0048038 quinone binding (IEA): MARK_AS_OVER_ANNOTATED -- TPQ is a covalently
  modified residue of AMO, not a bound quinone ligand.
- GO:0005777 peroxisome (IEA SubCell): MODIFY -> GO:0005782 peroxisomal matrix.
- GO:0009308 amine metabolic process (IEA): MODIFY -> GO:0030416 methylamine
  metabolic process (AMO performs the oxidation step) and GO:0009310 amine catabolic process.
- No NEW terms.

### Transfer guidance for cao1

Transferable at family/subfamily level (PAINT root IBDs): primary amine oxidase
activity, copper binding, amine metabolism. Not transferable: peroxisomal (PTS2)
localisation -- Cao1 is cytosolic/forespore in S. pombe; methylamine-specific
physiology (methylotrophic-yeast nitrogen source use); substrate preference.
