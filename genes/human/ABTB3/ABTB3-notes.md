# ABTB3 Gene Review Notes

## 2026-06-03 - Proteostasis PN batch review

ABTB3 was newly fetched for the human Proteostasis PN batch. The local GOA set
contains five annotations: membrane, protein heterodimerization activity, PDZ
domain binding, glutamatergic synapse, and nucleoplasm. UniProt also lists
Ensembl-transferred biological-process annotations for exploration behavior,
protein stabilization, and synaptic transmission, glutamatergic, but these were
not present in the fetched GOA TSV.

Deep research status: `just deep-research-falcon human ABTB3 --fallback
perplexity-lite` was run. Falcon timed out after 600 seconds, then
`perplexity-lite` failed with a Perplexity API quota 401. Per project guidance,
I recorded the evidence synthesis in `ABTB3-deep-research-manual.md` rather than
creating a fake provider-named deep-research file.

The strongest gene-specific biology comes from mouse Btbd11. Bygrave et al.
identify Btbd11 as an inhibitory interneuron-specific synapse-enriched protein
that is highly conserved and binds Psd-95: [PMID:37261953 "identifying Btbd11 as
an inhibitory interneuron-specific, synapse-enriched protein"] and
[PMID:37261953 "Btbd11 is highly conserved across species and binds to core
postsynaptic proteins, including Psd-95."]. The paper directly supports the
orthology-derived human GOA terms for PDZ domain binding and glutamatergic
synapse: [PMID:37261953 "Btbd11 contains a PDZ binding motif that interacts with
PDZ1,2 of Psd-95"] and [PMID:37261953 "These data indicate that Btbd11 is
localized at glutamatergic synapses."].

The same mouse study supports adding two missing, conservative BP terms by
orthology. For protein stabilization, the relevant evidence is Psd-95 FRAP and
puncta-size data: [PMID:37261953 "Exogenous expression of Btbd11 stabilizes
Psd-95 at glutamatergic synapses"] and [PMID:37261953 "Psd-95-mCherry FRAP was
slower in the presence of overexpressed Btbd11"]. For glutamatergic synaptic
transmission, the direct phenotype is reduced excitatory signaling onto PV
interneurons: [PMID:37261953 "Knockout of Btbd11 decreased glutamatergic
signaling onto parvalbumin-positive interneurons."].

Conservative calls:

- Keep `GO:0016020 membrane` as non-core. UniProt has predicted membrane
  association, but the functional localization is better captured by
  `GO:0098978 glutamatergic synapse`.
- Mark `GO:0046982 protein heterodimerization activity` as over-annotated. It is
  inferred from a histone-fold InterPro signature [UniProt:A6QL63 "InterPro;
  IPR009072; Histone-fold."], whereas the direct interaction evidence maps the
  PSD-95 interaction to the C-terminal PDZ-binding motif.
- Keep `GO:0005654 nucleoplasm` as non-core. It is HPA immunofluorescence-derived
  and does not explain the currently supported synaptic role.
- Do not add `GO:0035640 exploration behavior`; that is a downstream organismal
  phenotype from mouse knockout behavior, not the core gene-product function.

### PN projected context

The Proteostasis PN projection proposes `GO:1990756 ubiquitin-like
ligase-substrate adaptor activity` for ABTB3 from
`Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate
receptor|BTB-BACK, variant|ankyrin, transmembrane`
[file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_new_to_goa.tsv].
The curated parent mapping says the Cul3 substrate receptor group maps to
`GO:1990756`, but the audit marks it as requiring manual gene-level review before
gene review changes
[file:projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv].

I did not add `GO:1990756` for ABTB3. The evidence found here supports PDZ-domain
binding and synaptic PSD stabilization; it does not show ABTB3-CUL3 binding, CRL3
complex membership, a ubiquitinated substrate, or substrate-adaptor activity.
This is analogous to the KCTD18 exclusion note in the same PN mapping: domain
architecture alone is not enough for a gene-level `GO:1990756` assertion.
