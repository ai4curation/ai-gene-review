# snn-1 (C. elegans synapsin, UniProt G5EGI2) - curation notes

## Identity
- The scaffold for this review was fetched as TrEMBL entry G5EGI2_CAEEL, 401 aa, ORF Y38C1BA.2,
  described as "ATP-grasp domain-containing protein", assigned to the synapsin family and to the
  synapse by ARBA [file:worm/snn-1/snn-1-uniprot.txt]. This is an alternative UniProt entry for the
  same gene as Q8MXU3, the accession used for snn-1 in modules/synaptic_vesicle_cycle.yaml; the
  review is filed under the accession in the scaffold.
- snn-1 is the single worm synapsin ortholog, most similar to vertebrate synapsin II
  [file:worm/snn-1/snn-1-deep-research-falcon.md "**snn-1** is the single *C. elegans* synapsin ortholog"].

## Core biology: presynaptic phosphoprotein that clusters vesicles in the reserve pool
- SNN-1 is a presynaptic vesicle-organizing scaffold rather than an enzyme: no catalytic reaction or
  small-molecule substrate has been demonstrated for the worm protein, although the ATP-grasp-like
  core supports family-level ATP binding
  [file:worm/snn-1/snn-1-deep-research-falcon.md "**No intrinsic catalytic reaction, physiological small-molecule substrate, or ATP-dependent product has been demonstrated for worm SNN-1.**"].
- Localization: GFP-SNN-1 is at presynaptic regions of the AIY interneuron, colocalized with the
  vesicle marker RAB-3
  [file:worm/snn-1/snn-1-deep-research-falcon.md "In AIY, GFP–SNN-1 colocalizes with RAB-3 at presynaptic regions"];
  the GOA IDA places it in the presynaptic periactive zone, the vesicle-cluster region flanking the
  active zone.
- Vesicle clustering: SNN-1 acts downstream of a netrin/actin pathway to cluster synaptic vesicles at
  the AIY presynaptic site; SNN-1 enrichment requires mig-10, whereas MIG-10B localization does not
  require snn-1, fixing SNN-1 at the vesicle-clustering step
  [file:worm/snn-1/snn-1-deep-research-falcon.md "SNN-1 then acts downstream to cluster vesicles"].
- Reserve pool: loss of snn-1 changes vesicle localization and impairs stimulation-evoked
  mobilization of vesicles from the reserve pool
  [file:worm/snn-1/snn-1-deep-research-falcon.md "impairs stimulation-evoked mobilization of vesicles from the reserve pool"],
  the worm counterpart of the reserve-pool stage in modules/synaptic_vesicle_cycle.yaml.
- Mechanism: the defensible description is a regulated adapter linking vesicles and vesicle clusters
  to the presynaptic actin environment
  [file:worm/snn-1/snn-1-deep-research-falcon.md "SNN-1 acts as a **regulated adapter/scaffold linking vesicles, vesicle clusters, and the presynaptic actin environment**"],
  matching the GO:0106006 cytoskeletal protein-membrane anchor activity accepted for human SYN1
  (genes/human/SYN1) and used for the synapsin annoton in the module.
- Regulation: Ser9 phosphorylation state, controlled by the PP1 regulator PHAC-1, modulates
  cholinergic signalling; snn-1(S9A) phenocopies aspects of phac-1 gain of function
  [file:worm/snn-1/snn-1-deep-research-falcon.md "A phosphodeficient *snn-1(S9A)* allele reproduced aspects of the *phac-1* gain-of-function phenotype"].
- Neuromuscular function: snn-1 was recovered in a systematic RNAi screen for genes required for
  acetylcholine secretion, and its product was localized to presynaptic specializations
  [PMID:16049479 "A total of 185 genes were identified in an RNA interference screen for decreased acetylcholine secretion"; "Twenty-four genes encoded proteins that were localized to presynaptic specializations."].

## GO decisions (summary)
- Core: cytoskeletal protein-membrane anchor activity (GO:0106006) proposed as a NEW molecular
  function, with synaptic vesicle clustering (GO:0097091) as a NEW process, in the presynaptic
  periactive zone / on synaptic vesicles. Both are grounded in worm genetics (netrin-pathway vesicle
  clustering in AIY, reserve-pool mobilization defects) plus the family and human-ortholog evidence;
  the primary worm papers are not cached in this repository, which is noted in the reviews.
- Existing rows: ATP/nucleotide binding and metal ion binding are accepted at the domain level but
  kept non-core, since no catalytic or ATP-dependent activity is demonstrated for SNN-1.
