# vanR (Enterococcus faecium, Q06239) — curation notes

## Literature search record

No deep-research provider key exists here and there is no model organism
database description for Enterococcus. `just fetch-fitness ENTFC vanR` was not
attempted; no fitness data set exists for this organism.

Sources checked:

- `genes/ENTFC/vanR/vanR-uniprot.txt` (Swiss-Prot Q06239): FUNCTION, SUBUNIT,
  SUBCELLULAR LOCATION, PTM, the response-regulatory domain (4-117), the
  OmpR/PhoB-type DNA-binding domain (131-231), the 4-aspartylphosphate at
  residue 53, and the keyword list, which carries both Activator and Repressor.
- GOA cites no publication for this gene: all eight rows are electronic. The
  primary literature was found through the UniProt evidence tags and fetched:
  PMID:1556077 (the in vivo genetics), PMID:8494882 (purification,
  phosphorylation and dephosphorylation by VanS), PMID:8664263 (phosphotransfer
  kinetics), PMID:30677074 (full-length VanS, including the phosphatase arm).
  PMID:8161518 and PMID:1320585, also cited by UniProt, were not retrieved; what
  the review uses from them is only what the curated record states.
- Context read but not edited: a glycopeptide-resistance pathway module and a
  review of the vanA-operon GO-CAM, both proposed in
  ai4curation/ai-gene-review#5904 and not part of this branch; nothing in this
  review rests on them.
- GO relations checked against the local GO build, 2026-11-04: `GO:0003677 DNA
  binding` is an `is_a` ancestor of `GO:0000976 transcription cis-regulatory
  region binding`; `GO:0006355` is an ancestor of `GO:0045893 positive regulation
  of DNA-templated transcription`; `GO:0000156 phosphorelay response regulator
  activity` is **not** an ancestor of `GO:0001216 DNA-binding transcription
  activator activity`, so the two are independent claims; `GO:0005829 cytosol` is
  a `part_of` descendant of `GO:0005737 cytoplasm`.

## What VanR does

VanR is the response regulator of the pair, a two-domain OmpR-subclass protein:
a receiver domain phosphorylated on Asp53 and a winged-helix DNA-binding domain.

[PMID:1556077 "VanR was a transcriptional activator related to response regulators of the OmpR subclass."]
[PMID:1556077 "Analysis of transcriptional fusions with a reporter gene and RNA mapping indicated that the VanR-VanS two-component regulatory system activates a promoter used for cotranscription of the vanH, vanA, and vanX resistance genes."]

Its phosphorylation state is set by VanS in both directions:
[PMID:8494882 "32P-PhosphoMBP-VanS transferred the phosphoryl group to VanR."]
[PMID:8494882 "32P-Phospho VanR showed chemical stability anticipated for an aspartyl phosphate and was relatively stable to hydrolysis (t1/2 = 10-12 h)."]
[PMID:30677074 "In the absence of vancomycin, VanS dephosphorylates VanR, thereby maintaining it in a transcriptionally inactive state."]
and the relay is specific rather than promiscuous:
[PMID:8664263 "A KM of 3 microM was estimated for VanR, leading to a 10(4)-fold preference in kxfer/KM for phosphotransfer to VanR compared to PhoB."]

UniProt adds the DNA side from PMID:8161518: VanR binds the promoter regions of
vanH and vanR, and phosphorylation increases that binding affinity
significantly. The long half-life of the phosphoaspartate (10-12 hours in vitro)
is what makes the VanS phosphatase arm necessary: without active removal the
regulator would stay on.

## Annotation decisions worth noting

All eight rows are electronic, with no publication cited anywhere, so each was
judged against the primary literature and the curated record.

- `GO:0000156 phosphorelay response regulator activity` is the core function and
  is accepted: the receiver domain, the 4-aspartylphosphate at residue 53, the
  measured phosphotransfer from VanS and the measured dephosphorylation all
  support it.
- `GO:0000976 transcription cis-regulatory region binding` is accepted as the
  promoter-binding claim, and `GO:0003677 DNA binding`, its ancestor, is marked
  `TOO_GENERAL`.
- `GO:0006355 regulation of DNA-templated transcription` is modified to
  `GO:0045893 positive regulation of DNA-templated transcription`: the direction
  is known, since VanR activates the vanH-vanA-vanX promoter. Note that UniProt's
  keyword list carries both Activator and Repressor while the FUNCTION text
  describes only activation; the Repressor keyword is not explained by anything in
  the record or in the literature read here, and it is raised as a question
  rather than acted on.
- `GO:0032993 protein-DNA complex` is kept as non-core. It is a true consequence
  of promoter binding, but it is an entailment of the DNA-binding function rather
  than an independent localisation finding, and no VanR-DNA complex has been
  characterised structurally in this organism.
- `GO:0005737 cytoplasm` is refined to `GO:0005829 cytosol`, which is already
  annotated from the PANTHER node.

Two things are missing from GOA and are proposed as `NEW` rows. First,
`GO:0001216 DNA-binding transcription activator activity`: VanR's molecular
function is not only to receive a phosphoryl group but to activate transcription
through its OmpR/PhoB-type DNA-binding domain, and `GO:0000156` does not entail
that (the two terms are unrelated in the hierarchy). Second, `GO:0046677
response to antibiotic`, which no gene of the cluster carries.

The development GO-CAM model gomodel:671ae02600002832 represents VanR twice with
the same gene product, function and process, splitting the kinase and phosphatase
edges between the two copies, so that the inhibitory branch regulates a node with
no outgoing edges; and it gives the activity `has_input UniProtKB:Q05709`, the
VanH protein, where the targets are really the operon's genes. Both points are
recorded here as `source_defects` entries (resource `GO_CAM`,
`requested_change: CHECK`) on the `GO:0001216` row.
