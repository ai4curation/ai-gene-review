# PTHR45633: source excerpts

Raw provenance: [family snapshot](family-sources/PTHR45633.json); [UniProt snapshot](uniprot-records.jsonl.gz), supplemented by [successful retries](uniprot-retries.jsonl.gz).

## Integrated InterPro IPR001844

Generated description flag: False; reviewed generated text flag: False. Generated prose is a source lead, not independent biological validation.

The assembly of proteins has been thought to be the sole result of properties inherent in the primary sequence of polypeptides themselves. In some cases, however, structural information from other protein molecules is required for correct folding and subsequent assembly into oligomers [[cite:PUB00004022]]. These `helper' molecules are referred to as molecular chaperones, a subfamily of which are the chaperonins [[cite:PUB00004550]]. They are required for normal cell growth (as demonstrated by the fact that no temperature sensitive mutants for the chaperonin genes can be found in the temperature range 20 to 43 degrees centigrade [[cite:PUB00004022]]), and are stress-induced, acting to stabilise or protect disassembled polypeptides under heat-shock conditions [[cite:PUB00004550]]. This entry represents the 60kDa chaperonin (Cpn60), its bacterial homologue groEL and RuBisCO subunit-binding protein [[cite:PUB00099589]]), which are mainly present in bacteria and eukaryots.

The 60kDa form of chaperonin is the immunodominant antigen of patients with Legionnaire's disease [[cite:PUB00001725]], and is thought to play a role in the protection of the Legionella spp. bacteria from oxygen radicals within macrophages. This hypothesis is based on the finding that the cpn60 gene is upregulated in response to hydrogen peroxide, a source of oxygen radicals. Cpn60 has also been found to display strong antigenicity in many bacterial species [[cite:PUB00000632]], and has the potential for inducing immune protection against unrelated bacterial infections. The RuBisCO subunit binding protein (which has been implicated in the assembly of RuBisCO) and cpn60 have been found to be evolutionary homologues, the RuBisCO subunit binding protein having the C-terminal Gly-Gly-Met repeat found in all bacterial cpn60 sequences. Although the precise function of this repeat is unknown, it is thought to be important as it is also found in 70kDa heat-shock proteins [[cite:PUB00001725]]. The crystal structure of Escherichia coli GroEL has been resolved to 2.8A [[cite:PUB00004190]].

## Exact benchmark records

### HORSE/HSPD1 — F6Z587
UniProt record: https://www.uniprot.org/uniprotkb/F6Z587/entry
Status: UniProtKB unreviewed (TrEMBL); length: 541 aa; sequence version: 3.

**FUNCTION**
Chaperonin implicated in mitochondrial protein import and macromolecular assembly. Together with Hsp10, facilitates the correct folding of imported proteins. May also prevent misfolding and promote the refolding and proper assembly of unfolded polypeptides generated under stress conditions in the mitochondrial matrix. The functional units of these chaperonins consist of heptameric rings of the large subunit Hsp60, which function as a back-to-back double ring. In a cyclic reaction, Hsp60 ring complexes bind one unfolded substrate protein per ring, followed by the binding of ATP and association with 2 heptameric rings of the co-chaperonin Hsp10. This leads to sequestration of the substrate protein in the inner cavity of Hsp60 where, for a certain period of time, it can fold undisturbed by other cell components. Synchronous hydrolysis of ATP in all Hsp60 subunits results in the dissociation of the chaperonin rings and the release of ADP and the folded substrate protein
Evidence: [{"evidenceCode": "ECO:0000256", "source": "ARBA", "id": "ARBA00037436"}]
**CATALYTIC ACTIVITY**
{"name": "ATP + H2O + an unfolded polypeptide = ADP + phosphate + a folded polypeptide.", "ecNumber": "5.6.1.7", "evidences": [{"evidenceCode": "ECO:0000256", "source": "ARBA", "id": "ARBA00094037"}]}
**SUBCELLULAR LOCATION**
{"location": {"evidences": [{"evidenceCode": "ECO:0000256", "source": "ARBA", "id": "ARBA00004305"}], "value": "Mitochondrion matrix", "id": "SL-0170"}}
**SIMILARITY**
Belongs to the TCP-1 chaperonin family
Evidence: [{"evidenceCode": "ECO:0000256", "source": "ARBA", "id": "ARBA00008020"}]
**SIMILARITY**
Belongs to the chaperonin (HSP60) family
Evidence: [{"evidenceCode": "ECO:0000256", "source": "ARBA", "id": "ARBA00006607"}]
InterPro: IPR018370 [{"key": "EntryName", "value": "Chaperonin_Cpn60_CS"}]
InterPro: IPR001844 [{"key": "EntryName", "value": "Cpn60/GroEL"}]
InterPro: IPR002423 [{"key": "EntryName", "value": "Cpn60/GroEL/TCP-1"}]
InterPro: IPR027409 [{"key": "EntryName", "value": "GroEL-like_apical_dom_sf"}]
InterPro: IPR027413 [{"key": "EntryName", "value": "GROEL-like_equatorial_sf"}]
InterPro: IPR017998 [{"key": "EntryName", "value": "TCP-1"}]
PANTHER: PTHR45633 [{"key": "EntryName", "value": "60 KDA HEAT SHOCK PROTEIN, MITOCHONDRIAL"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF00118 [{"key": "EntryName", "value": "Cpn60_TCP1"}, {"key": "MatchStatus", "value": "2"}]

### human/HSPD1 — P10809
UniProt record: https://www.uniprot.org/uniprotkb/P10809/entry
Status: UniProtKB reviewed (Swiss-Prot); length: 573 aa; sequence version: 2.

**FUNCTION**
Chaperonin implicated in mitochondrial protein import and macromolecular assembly. Together with Hsp10, facilitates the correct folding of imported proteins. May also prevent misfolding and promote the refolding and proper assembly of unfolded polypeptides generated under stress conditions in the mitochondrial matrix (PubMed:11422376, PubMed:1346131). The functional units of these chaperonins consist of heptameric rings of the large subunit Hsp60, which function as a back-to-back double ring. In a cyclic reaction, Hsp60 ring complexes bind one unfolded substrate protein per ring, followed by the binding of ATP and association with 2 heptameric rings of the co-chaperonin Hsp10. This leads to sequestration of the substrate protein in the inner cavity of Hsp60 where, for a certain period of time, it can fold undisturbed by other cell components. Synchronous hydrolysis of ATP in all Hsp60 subunits results in the dissociation of the chaperonin rings and the release of ADP and the folded substrate protein (Probable)
Evidence: [{"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "11422376"}, {"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "1346131"}, {"evidenceCode": "ECO:0000305", "source": "PubMed", "id": "25918392"}]
**CATALYTIC ACTIVITY**
{"name": "ATP + H2O + an unfolded polypeptide = ADP + phosphate + a folded polypeptide.", "ecNumber": "5.6.1.7", "evidences": [{"evidenceCode": "ECO:0000305"}]}
**SUBCELLULAR LOCATION**
{"location": {"value": "Mitochondrion matrix", "id": "SL-0170"}}
**SIMILARITY**
Belongs to the chaperonin (HSP60) family
Evidence: [{"evidenceCode": "ECO:0000305"}]
InterPro: IPR018370 [{"key": "EntryName", "value": "Chaperonin_Cpn60_CS"}]
InterPro: IPR001844 [{"key": "EntryName", "value": "Cpn60/GroEL"}]
InterPro: IPR002423 [{"key": "EntryName", "value": "Cpn60/GroEL/TCP-1"}]
InterPro: IPR027409 [{"key": "EntryName", "value": "GroEL-like_apical_dom_sf"}]
InterPro: IPR027413 [{"key": "EntryName", "value": "GROEL-like_equatorial_sf"}]
InterPro: IPR027410 [{"key": "EntryName", "value": "TCP-1-like_intermed_sf"}]
PANTHER: PTHR45633 [{"key": "EntryName", "value": "60 KDA HEAT SHOCK PROTEIN, MITOCHONDRIAL"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF00118 [{"key": "EntryName", "value": "Cpn60_TCP1"}, {"key": "MatchStatus", "value": "1"}]

