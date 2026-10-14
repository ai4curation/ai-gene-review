# JAR1 (At2g46370; UniProt Q9SKE2) curation notes

## 2026-10-06 — initial review (jasmonate_coi1_jaz_signaling module)

- Fetched with `just fetch-gene ARATH JAR1`; UniProt record checked: JAR1_ARATH, Q9SKE2, At2g46370, synonym FIN219.
- `just deep-research-falcon ARATH JAR1` failed (provider rate limit / HTTP 429); no deep-research file. Review based on cached publications.

### Biochemistry
- JAR1 is a GH3 acyl acid-amido synthetase of the ANL adenylating superfamily; adenylation activity specific for JA [PMID:12084835 "Activity was specific for JA, suggesting that covalent modification of JA is important for its function."].
- Forms JA-Ile; jar1 has strongly reduced JA-Ile [PMID:15258265 "JA-Ile was found at 29.6 pmole g(-1) fresh weight (FW) in the wild type but was more than sevenfold lower in two jar1 alleles."]; JA-Ile rescues jar1 root inhibition [PMID:15258265 "Unlike free JA, JA-Ile inhibited root growth in jar1-1 to the same extent as in the wild type"].
- Ile preference [PMID:18247047 "Kinetic analysis showed that JAR1 had a K (m) of 0.03 mM for Ile, which was 60-80-fold lower than for Leu, Val and Phe."].
- Structures: AtGH3.11/JAR1 [PMID:22628555]; FIN219-FIP1 complex, ordered binding (JA first) and FIP1 doubles adenylation activity [PMID:28223489].
- Side reaction: p4A synthesis [PMID:17291501].

### Localization
- Cytoplasm [PMID:10921909 "GUS–FIN219 was located in the cytoplasm both in darkness and in the light"]. Nuclear ISM prediction and vacuole HDA marked over-annotated.

### Decisions worth flagging
- GO:0018117 protein adenylylation (IDA, PMID:28223489) is a mis-mapping: the assay adenylates JA (PPi release), not a protein -> MODIFY to GO:0009694.
- Protein binding (FIP1/GSTU20) -> MODIFY to enzyme binding (already annotated from PMID:17220357).
- SAR IEP (PMID:17419843) marked over-annotated (expression only; SAR is SA-dependent).
- Negative regulation of defense response (PMID:16732289, mlo paper) left UNDECIDED: abstract-only, states mlo resistance is JA-independent; jar1-specific result not visible.
- Many physiological IMPs (ISR, ozone, fumonisin, UV-B, stomata, far-red light) kept as non-core outputs of JA-Ile formation / phyA crosstalk.

## 2026-10-06 — resolved UNDECIDED row
- GO:0031348 negative regulation of defense response (IMP, PMID:16732289): Europe PMC reports no PMC/open-access full text; WebSearch summaries say mlo2 early senescence is SA- but not JA-dependent, and the JAR1-specific experiment could not be seen. Changed UNDECIDED -> KEEP_AS_NON_CORE, deferring to the GOA curator (CLAUDE.md), as plausible via JA-SA antagonism (cf. jar1 in ozone cell death, PMID:11006337). Non-core, indirect.
