# LuxS manual notes

Automated deep-research providers were unavailable for this host, so this is a compact manual review against the cached UniProt and PMID records.

## Function

- UniProtKB:P45578 describes LuxS as a cytosolic S-ribosylhomocysteine lyase that converts S-ribosylhomocysteine to homocysteine and 4,5-dihydroxy-2,3-pentadione, with one inferred Fe cation per subunit and a homodimeric quaternary structure.
- Schauder et al. showed that LuxS is the AI-2 synthase and that its substrate is S-ribosylhomocysteine, which is cleaved to homocysteine plus the AI-2 precursor/product [PMID:11489131].
- Surette et al. identified luxS-family genes responsible for AI-2 production in Vibrio harveyi, Salmonella typhimurium, and E. coli; the E. coli O157:H7 luxS gene complemented E. coli DH5alpha for AI-2 production [PMID:9990077].
- The DeLisa et al. microarray study used an E. coli W3110 luxS mutant unable to synthesize AI-2 to define an AI-2-responsive transcriptional state, supporting the curated E. coli quorum-sensing process annotation [PMID:11514505].

## Annotation decisions

- Accept S-ribosylhomocysteine lyase activity rows: the molecular function is the experimentally supported core activity.
- Accept quorum sensing rows but treat them as downstream from the same core lyase chemistry: LuxS produces the DPD precursor for AI-2 rather than sensing AI-2 itself.
- Add L-methionine cycle as a new direct process annotation: in bacteria that use the Pfs/MtnN plus LuxS route, LuxS performs the second SAH-processing step and releases homocysteine for remethylation.
- Keep cytosol rows: LuxS has cytosolic proteomics calls and a cytosolic IBA assertion.
- Remove the generic DnaK `protein binding` row: the IntAct row may report a physical interaction, but there is no narrower supported LuxS molecular function to curate from a large-scale pull-down alone.
- Modify generic `metal ion binding` to `iron ion binding`; the more precise term is already asserted from the LuxS family.


## 2026-11-07 independent methionine-cycle audit

All original ordered payloads, qualifiers and historical proposal lifecycle are unchanged; no new rows. Genuine Falcon attempt failed authentication403, without a fabricated provider report. Source scopes and ontology snapshots: `analysis/module_audits/bacterial_methionine_cycle/ecoli-existing-consultation/`. Historical cycle NEW retained after full publisher Methods verified MG1655 GST constructs and purified pathway-step assays. This does not claim native whole-cycle flux. W3110 conditioned-medium evidence supports bounded producer-side quorum participation, not universal signaling from metabolic phenotypes.
