# Manual Deep Research: ABTB3

Provider status: `just deep-research-falcon human ABTB3 --fallback
perplexity-lite` was run on 2026-06-03. Falcon timed out after 600 seconds, and
the configured `perplexity-lite` fallback failed with a Perplexity API quota
401. Per project instructions, this file is a manual fallback research summary
and is not named as provider-generated deep research.

## Identity

ABTB3 (UniProt A6QL63; synonym BTBD11) encodes ankyrin repeat- and BTB/POZ
domain-containing protein 3. UniProt lists the protein as reviewed, 1104 amino
acids, with ankyrin repeats, a BTB/POZ domain, a BACK domain, a histone-fold
signature, and five annotated isoforms [UniProt:A6QL63 "RecName: Full=Ankyrin
repeat- and BTB/POZ domain-containing protein 3;"].

The PANTHER family fetched during `just fetch-gene human ABTB3` is PTHR46071,
`Ankyrin repeat and BTB/POZ domain-containing protein`. The reviewed entries in
the local family cache include human ABTB3 and ABTB2, mouse Abtb3 and Abtb2, rat
Abtb2, and zebrafish abtb3a/abtb3b, supporting conserved ABTB2/3 family context.

## Main Experimental Evidence

The key functional study is the mouse Btbd11 Cell Reports paper by Bygrave et
al. 2023 [PMID:37261953]. It identifies Btbd11 as an inhibitory
interneuron-specific postsynaptic protein: [PMID:37261953 "identifying Btbd11
as an inhibitory interneuron-specific, synapse-enriched protein"]. The abstract
states that Btbd11 is conserved and binds Psd-95: [PMID:37261953 "Btbd11 is
highly conserved across species and binds to core postsynaptic proteins,
including Psd-95."].

The paper directly supports PDZ-domain binding. The results section states that
Btbd11 has a PDZ-binding motif and that the conserved C-terminal region is
important: [PMID:37261953 "Btbd11 contains a PDZ binding motif that interacts
with PDZ1,2 of Psd-95"] and [PMID:37261953 "The C-terminal region of Btbd11 is
highly conserved between species"]. The binding assays show dependence on the
PDZ-binding motif: [PMID:37261953 "Btbd11 could pull down Psd-95-mCherry but
only when the PBM was present"].

The same paper supports glutamatergic synapse localization. Endogenous and
tagged Btbd11 puncta colocalized with Psd-95 rather than gephyrin, and the paper
summarizes the result as [PMID:37261953 "These data indicate that Btbd11 is
localized at glutamatergic synapses."].

Btbd11 also stabilizes Psd-95 at glutamatergic synapses. The relevant heading
and FRAP result are [PMID:37261953 "Exogenous expression of Btbd11 stabilizes
Psd-95 at glutamatergic synapses"] and [PMID:37261953 "Psd-95-mCherry FRAP was
slower in the presence of overexpressed Btbd11"]. Knockout data support a
functional role in glutamatergic signaling onto PV interneurons:
[PMID:37261953 "Knockout of Btbd11 decreased glutamatergic signaling onto
parvalbumin-positive interneurons."].

## GO Review Implications

Accepted core annotations:

- `GO:0030165 PDZ domain binding`, because the source mouse study directly maps
  Psd-95 binding to the Btbd11 C-terminal PDZ-binding motif and the region is
  conserved.
- `GO:0098978 glutamatergic synapse`, because Btbd11 colocalizes with Psd-95,
  not gephyrin, and is enriched in PSD fractions.

Kept as non-core:

- `GO:0016020 membrane`, because UniProt predicts membrane association but the
  functional localization is more specifically captured by glutamatergic synapse.
- `GO:0005654 nucleoplasm`, because HPA immunofluorescence supports the source
  observation, but no mechanistic nucleoplasmic function is currently established.

Marked as over-annotated:

- `GO:0046982 protein heterodimerization activity`, because it is an
  InterPro2GO inference from the histone-fold signature rather than a
  demonstrated physiologic heterodimerization function. The experimentally
  supported interaction mechanism is PDZ-motif-mediated binding to Psd-95.

Added as new orthology-supported BP annotations:

- `GO:0050821 protein stabilization`, for Btbd11-mediated stabilization of
  Psd-95 at glutamatergic synapses.
- `GO:0035249 synaptic transmission, glutamatergic`, for the decreased
  glutamatergic signaling in PV interneurons after mouse Btbd11 knockout.

Not added:

- `GO:0035640 exploration behavior`, because it is a downstream organismal
  phenotype and should not be treated as the core gene-product function.
- `GO:1990756 ubiquitin-like ligase-substrate adaptor activity`, because the PN
  projection is based on Cul3 substrate-receptor/domain context and the
  available ABTB3/Btbd11 evidence does not show CUL3 binding, CRL3 complex
  membership, a ubiquitinated substrate, or substrate-adaptor activity.

## Proteostasis PN Context

The PN projection report lists ABTB3 as a candidate for `GO:1990756
ubiquitin-like ligase-substrate adaptor activity` from
`Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate
receptor|BTB-BACK, variant|ankyrin, transmembrane`
[file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_new_to_goa.tsv].
The current mapping audit classifies Cul3 substrate-receptor propagation as
requiring manual gene-level review before gene review changes
[file:projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv].

For ABTB3, the gene-level review does not support propagating the Cul3 adaptor
term. The evidence supports a synaptic PDZ-binding/stabilizer role. It does not
support adding a ubiquitin-like ligase-substrate adaptor activity annotation.
