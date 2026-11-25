# Vps35 (CG5625) notes

Accession: the symbol lookup returned Q7KVL7 (46 GOA rows); the expected accession Q9W277 has more GOA rows and was used (fetched with `just fetch-gene DROME Q9W277 --alias Vps35`).

- Wls retrieval for Wg secretion [PMID:18193037 "Following dissociation from Wingless, Wntless is internalized and returns to the Golgi apparatus in a retromer-dependent manner."].
- Serpentine retrieval via Rab9 late endosomes in trachea; Rab9 binds Vps35 [PMID:23322046 "both GTP- and GDP-loaded forms of GST-Rab9, but not GST pulled down myc-Vps35"].
- Notch cargo [PMID:30176986 "Notch-V5 expressed in central brain neuroblast lineages was specifically coimmunoprecipitated with Vps35-FLAG from fly larval brain extracts"].
- Early endosome with Snx3 [PMID:22041890 "co-localize with Vps35 in early endosomes"].
- Endocytosis screen in S2 cells [PMID:18057029]; synaptic vesicle recycling, LRRK2 interplay [PMID:28482024]; rotenone protection by overexpression [PMID:24915984].

Decisions: cargo receptor -> cargo adaptor (contributes_to); obsolete endosome-to-PM transport -> endocytic recycling; synaptic rows non-core; response to rotenone over-annotated (overexpression modifier).
Deep research: falcon completed (Vps35-deep-research-falcon.md) after the initial review; consistent with the review (non-enzymatic retromer scaffold acting on endosomes) [file:DROME/Vps35/Vps35-deep-research-falcon.md "Vps35 performs its sorting function on **intracellular endosomal membranes and associated trafficking carriers**"]. It adds NMJ pre/postsynaptic localization and APP extracellular-vesicle cargo sorting (Walsh et al. 2021) and wing-epithelium trafficking-hub data, none of which is in GOA. No annotation actions changed.
