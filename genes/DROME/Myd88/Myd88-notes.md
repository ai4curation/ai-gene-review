# Myd88 (krapfen) notes

UniProt A1Z7T8 (TrEMBL; the project page lists Q7K105, which fetch-gene resolved to A1Z7T8). 537 aa; death domain, TIR domain (241-375), C-terminal extension that binds phosphoinositides.

## Core biology (with provenance)
- Toll adaptor: "dMyD88 is an adapter in the Toll signaling pathway that associates with both the Toll receptor and the downstream kinase Pelle" [PMID:11606776].
- TIR-mediated Toll binding and Tube/Pelle requirement: "DmMyD88 interacted with Toll through its TIR domain and required the death domain proteins Tube and Pelle to activate expression of Drs, which encodes Drosomycin." [PMID:11743586]
- Immunity phenotype: "DmMyD88-mutant flies were highly susceptible to infection by fungi and Gram-positive bacteria, but resisted Gram-negative bacterial infection much as did wild-type flies." [PMID:11743586]
- Heterotrimer: "we find a heterotrimeric association of the death domains of MyD88, Tube, and the protein kinase Pelle" [PMID:12351681].
- D/V patterning: "Epistasis experiments reveal that kra acts between the receptor Toll and the cytoplasmic factor Tube." [PMID:12559494]; "These results show that DmMyD88 encodes an essential component of the Toll pathway in dorsoventral pattern formation." [PMID:12524523]
- PI(4,5)P2 binding: "dMyD88 was located at the plasma membrane by a process dependent on a C-terminal phosphoinositide-binding domain." and "GST-dMyD88 interacted preferentially with liposomes containing PI(4,5)P2 and to a lesser extent liposomes containing PI(4)P (Figure 2c)." [PMID:22464168]; the authors propose "dMyD88 is the functional homolog of TIRAP" [PMID:22464168].
- Weckle: "Moreover, Wek binds to and localizes DmMyD88 to the plasma membrane." [PMID:16782008]
- FADD: "that dMyD88 can interact with dFADD through death domains" [PMID:11606776] (overexpression in S2 cells).

## Curation decisions
- Core MF: GO:0035591 signaling adaptor activity; also GO:0005121 Toll binding and GO:0005546 PI(4,5)P2 binding; location GO:0009898.
- IEA GO:0043123 positive regulation of canonical NF-kappaB signal transduction REMOVE: GO defines canonical NF-kB as IKK-dependent; the fly Toll pathway is IKK-independent ("without involvement of IKK", PMID:24086459). InterPro2GO mapping from IPR017281.
- Protein binding: FADD row MODIFY to GO:0070513 death domain binding; two Wek rows REMOVE (uninformative).
- GO:0045944 (IMP, Akirin paper) MARK_AS_OVER_ANNOTATED: MyD88 is a membrane adaptor, not a transcription regulator.
- Response to mycotoxin and response to tumor cell: KEEP_AS_NON_CORE.
- No GO:0002224 or PRR terms on Myd88; GO:0008063 is used consistently.

## Deep-research cross-check (2026-09-30)
Compared Myd88-deep-research-falcon.md with the review.
- Agrees: non-enzymatic Toll adaptor; TIR binding to Toll, death-domain complex with Tube and Pelle; Cactus degradation and Dif/Dorsal release; requirement for antifungal and Gram-positive defence; phosphoinositide binding.
- Conflicts, not acted on: the report calls Myd88 "predominantly cytoplasmic" and says Myd88-specific developmental evidence is "limited". Both are contradicted by cached primary papers already used: plasma membrane localisation via PI(4,5)P2 [PMID:22464168] and maternal dorsalised phenotypes with transgene rescue [PMID:12524523, PMID:12559494]. The report's "C-terminal TIR domain" ignores the C-terminal lipid-binding extension (UniProt TIR 241-375 of 537).
- Adds: Zhang et al. 2024 (fetched, PMID:38292423, full text) - in S2 cells expressing Toll TIR domains, "Toll-1 but not Toll-7 activated autophagy is dMyd88 dependent", and "RNAi of dMyd88 suppressed both TIR-1 and TIR-7 activated expression of Drs". Cell-culture only, so no autophagy annotation proposed; added as reference and suggested question.
- Changes: references (+PMID:38292423) and suggested_questions (+1). No annotation actions changed.
