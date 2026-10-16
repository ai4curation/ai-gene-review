# ade8 (SPBC14F5.09c, UniProt O60105) notes

Naming: S. pombe ade8 = adenylosuccinate lyase (PurB/ASL), ortholog of S. cerevisiae ADE13 (not budding-yeast ADE8, which is GAR transformylase). Accession O60105 (PUR8_SCHPO) fetched correctly.

## Evidence
- Two reactions: adenylosuccinate -> AMP + fumarate and SAICAR -> AICAR + fumarate [file:SCHPO/ade8/ade8-uniprot.txt "Reaction=N(6)-(1,2-dicarboxyethyl)-AMP = fumarate + AMP;"; "Reaction=(2S)-2-[5-amino-1-(5-phospho-beta-D-ribosyl)imidazole-4-"]. Homotetramer, lyase 1 family [UniProt:O60105].
- Partially purified S. pombe ASL assayed; does not process the cysteine-sulfinate-derived analogues [PMID:8346915 "Adenylosuccinate lyase, however, fails to catalyze further conversion of these sulfur derivatives"]. Abstract-only; IDA annotations deferred to curator.
- Cytosol (+ nucleus) in ORFeome screen [PMID:16823372].

## Decisions
- 17 rows: 15 ACCEPT, 1 KEEP_AS_NON_CORE (nucleus HDA), 1 MODIFY (catalytic activity -> GO:0004018).
- Two core functions, mirroring S. cerevisiae ADE13 review: GO:0070626 (de novo IMP) and GO:0004018 (de novo AMP).
- GO-CAM 663d668500001911 models only the SAICAR lyase (GO:0070626) activity; the AMP-branch activity belongs in an IMP->AMP model/module (purine_nucleotide_interconversion).
