"""Curation decisions for human APLN, keyed by the GOA row they apply to.

Separated from ``build_review.py`` so that the prose is reviewable on its own and so
that ``source_entities`` are *derived* from each row's seeded ``supporting_entities``
rather than retyped. Every ``supporting_text`` here is a verbatim substring of the cited
cache file; ``build_review.py`` does not invent any.

Key: (GO id, evidence code, reference, tuple(supporting_entities)).
"""

from __future__ import annotations

# --------------------------------------------------------------------------------------
# Verbatim quotes. Each is checked against publications/PMID_<id>.md (or the file: target)
# by checkquotes.py. No square brackets anywhere: the validator strips bracketed spans
# from the query as editorial notes.
# --------------------------------------------------------------------------------------

Q = {
    # PMID:9792798 Tatemoto 1998 (abstract only)
    "TAT98_LIGAND": "Synthetic peptides derived from the C-terminal amino acid sequence of bovine preproapelin were capable of specifically promoting the acidification rate in the cells expressing the APJ receptor in a range from 10(-7) to 10(-10) M, indicating that apelin is an endogenous ligand for the APJ receptor.",
    "TAT98_PRECURSOR": "The preproproteins consisted of 77 amino acid residues, and the apelin sequence was encoded in the C-terminal regions.",
    "TAT98_ISOLATED": "By monitoring this activity, we isolated an APJ receptor ligand, designated apelin, from bovine stomach extracts.",
    # PMID:10525157 Habata 1999 (abstract only)
    "HAB99_COLOSTRUM": "a large amount of apelin (14-93 pmol/ml) was found to be secreted in the bovine colostrum, and it was still detectable even in commercial bovine milk",
    "HAB99_MAMMARY": "Although apelin mRNA was widely detected in a variety of tissues, the highest expression of apelin mRNA was detected in the mammary gland of pregnant rats.",
    "HAB99_PARTURITION": "In the mammary gland, biologically active apelin and its mRNA considerably increased during pregnancy and lactation, and reached a maximal level around parturition.",
    "HAB99_APJLIGAND": "we have recently identified a natural ligand, apelin, for the orphan 7TMR, APJ",
    "HAB99_CYTOKINE": "Since apelin partially suppressed cytokine production by mouse spleen cells in response to T cell receptor/CD3 cross-linking, the oral intake of apelin in the colostrum and milk might modulate immune responses in neonates.",
    # PMID:11359874 Reaux 2001 (abstract only)
    "REA01_FRAGMENTS": "Stimulation of this receptor by the apelin fragments K17F (Lys1-Phe-Arg-Arg-Gln-Arg-Pro-Arg-Leu-Ser-His-Lys-Gly-Pro-Met-Pro-Phe17) and pE13F (pGlu5-Arg-Pro-Arg-Leu-Ser-His-Lys-Gly-Pro-Met-Pro-Phe17) resulted in a dose-dependent inhibition of forskolin-induced cAMP production and promoted its internalization.",
    "REA01_INACTIVE": "In contrast, the apelin fragments R10F (Arg8-Leu-Ser-His-Lys-Gly-Pro-Met-Pro-Phe17) and G5F (Gly13-Pro-Met-Pro-Phe17) were inactive.",
    "REA01_WATER": "central injection of pE13F significantly decreased water intake in dehydrated normotensive rats but did not affect blood pressure",
    "REA01_CHO": "We established a stable Chinese hamster ovary (CHO) cell line expressing a gene encoding the rat apelin receptor fused to the enhanced green fluorescent protein, to investigate internalization and the pharmacological profile of the apelin receptor.",
    "REA01_FLUID": "Together, these results suggest that neuronal apelin plays an important role in the central control of body fluid homeostasis.",
    "REA01_AVP": "a decrease in vasopressin release following intracerebroventricular injection of K17F, or pE13F, but not R10F",
    # PMID:22810587 Scimia 2012 (full text)
    "SCI12_PERK": "Engineered cells stably expressing human APJ (APJ-HEK) responded to apelin by increasing the content of pERK",
    "SCI12_CAMP": "apelin addition decreased cAMP levels in the APJ-HEK cells",
    "SCI12_PTX": "This effect of apelin was partially inhibited by PTX, consistent with the involvement of Gαi",
    "SCI12_GI": "These data agree with previous reports21 and demonstrate that Gαi transduces the signal initiated by apelin binding to APJ.",
    "SCI12_ARRESTIN": "Using a β-arrestin/APJ complementation assay, apelin was found to induce a dose-dependent increase in β-arrestin signaling, as expected",
    "SCI12_IP1": "Stretch did not increase IP1 production whereas apelin did so in a dose-responsive manner",
    "SCI12_BP": "Apelin infusion significantly decreased systolic blood pressure in WT animals but not in APJ-KO mice",
    "SCI12_MEDIA": "the concentration of apelin in the media remained unchanged (approximately 5ng/ml) with or without stretch",
    "SCI12_BLOOD": "endogenous levels of apelin in blood increased after TAC from 1ng/ml to 2ng/ml",
    "SCI12_APJONLY": "In contrast, mice lacking apelin (the endogenous APJ ligand) remain sensitive, suggesting an apelin-independent function of APJ.",
    "SCI12_HYPERTROPHY": "Apelin does not induce hypertrophy, but instead blunts stretch-induced hypertrophic induction",
    # PMID:28137936 Yang 2017 (full text)
    "YAN17_PLASMA": "ELA and apelin were detectable in healthy human plasma at 0.34±0.03 nmol/L and 0.26±0.03 nmol/L, respectively",
    "YAN17_EIA": "Levels of ELA and apelin in healthy human plasma (n=25) were measured by using enzyme immunoassays",
    "YAN17_PARACRINE": "Both ELA and apelin were detectable in human plasma at subnanomolar levels, more indicative of peptides acting as locally released autocrine/paracrine mediators than as circulating hormones.",
    "YAN17_COMPETE": "ELA competed for binding of apelin in human heart with overlap for the 2 peptides indicated by in silico modeling.",
    "YAN17_LVHOMOG": "Experiments were conducted in homogenate of human ventricle or Chinese hamster ovary (CHO)-K1 cells expressing the human apelin receptor.",
    "YAN17_CAMP": "completely inhibited forskolin-induced cAMP production in a concentration-dependent manner",
    "YAN17_ARRESTIN": "stimulated β-arrestin recruitment in a concentration-dependent manner",
    "YAN17_INTERNALIZATION": "Potency (pD2) and Efficacy (EMAX) of ...apelin-13, ELA-32, ELA-21, and ELA-11 in cAMP Inhibition, β-Arrestin Recruitment, and Receptor Internalization Assays",
    "YAN17_INOTROPE": "In heart, apelin is reportedly the most potent inotrope in vitro",
    "YAN17_ERK": "apelin and ELA-32 increased levels of ERK1/2 phosphorylation, and in PAECs there was also a significant increase in phosphorylation of endothelial nitric oxide synthase",
    # PMID:38428423 Wang 2024 (abstract only)
    "WAN24_HORMONE": "Apelin is a key hormone in cardiovascular homeostasis that activates the apelin receptor (APLNR), which is regarded as a promising therapeutic target for cardiovascular disease.",
    "WAN24_CRYOEM": "we report cryoelectron microscopy (cryo-EM) structures of APLNR-Gi1 complexes bound to three agonists with divergent signaling profiles",
    "WAN24_ARRESTIN": "However, adverse effects through the β-arrestin pathway limit its pharmacological use.",
    "WAN24_BIAS": "in APLNR as key determinants for signaling bias, guiding the rational design of two exclusive G-protein-biased agonists WN353 and WN561",
    # PMID:23263626 Kim 2013 (full text)
    "KIM13_REPORTER": "We generated a putative miR-424/503 promoter based luciferase reporter construct, which was robustly induced by APLN overexpression in PAECs (Fig.",
    "KIM13_QPCR": "We confirmed via real-time quantitative PCR that both the pri-form and the mature form of miR-424 and miR-503 are significantly downregulated with APLN knockdown (Fig.",
    "KIM13_TRANSCRIPTION": "suggesting that the transcription of these miRNAs, rather than their post-transcriptional maturation, appears to be regulated by APLN signaling.",
    "KIM13_FGF": "Lastly, we found that APLN knockdown resulted in robust increases of FGF2 and FGFR1, that were abrogated with concurrent overexpression of miR-424 and miR-503 (Fig.",
    "KIM13_FGF2OE": "We confirmed this relationship by demonstrating a robust increase in FGF2 expression with APLN knockdown, and reciprocally decreased FGF2 levels with APLN overexpression (Fig.",
    "KIM13_CM": "we found that CM from normal PAECs subjected to APLN knockdown induced a significant increase in PASMC proliferation, which was reduced to baseline by concurrent overexpression of miR-424/503 in PAECs (Fig.",
    "KIM13_FGF2DEP": "Moreover, the hyperproliferative response of PASMCs to CM from PAEC subjected to APLN knockdown was abrogated by concurrent knockdown of FGF2 (Fig.",
    "KIM13_PROLIF": "We also found that whereas augmentation of APLN signaling in normal PAECs led to an increase in PAEC proliferation as previously described,9 augmentation of APLN signaling in PAH PAECs had a reverse effect of inhibiting proliferation (Supp.",
    "KIM13_REFUTED": "Nevertheless, these effects have been modest at best, and others have refuted such findings,23 suggesting a strong context-dependence for APLN’s effects on the endothelium.",
    "KIM13_QUIESCENT": "Rather, an emerging role of APLN signaling in mature vessels appears to be to preserve a differentiated, quiescent, and homeostatic endothelial layer.",
    # PMID:27492965 Pope 2016 (full text) - mechanism of agonist-driven APJ internalisation
    "POP16_CCV": "stimulation caused internalization of mAPJ via clathrin coated vesicles (CCVs) and also caused a rapid reduction in cell surface and whole cell HA-mAPJ",
    "POP16_GRK2": "Our data suggest that upon continuous agonist exposure GRK2-mediated phosphorylation targets APJ to CCVs that are internalized from the cell surface in a β-arrestin1-independent, EPS15- and dynamin-dependent manner.",
    # PMID:28890073 Sharma 2017 (full text) - mouse donor for GO:0060976
    "SHA17_NOPHENO": "but Apelin KO animals did not phenocopy the coronary defect seen in Apj KOs",
    "SHA17_OPPOSITE": "In fact, Apelin-deficient hearts displayed a phenotype opposite to that in Apj mutants with an increase in coronary growth so that the heart was fully covered at developmental time points earlier than wild-type controls",
    "SHA17_LIGANDS": "The opposing phenotypes in Apln and Ela KOs indicate that these two ligands may have opposing functions vis-a-vis APJ in the context of coronary vessel formation.",
    "SHA17_ELAAXIS": "We find that the ELABELA (ELA)-APJ signaling axis is only required for sinus venosus-derived progenitors.",
    # PMID:26611206 Perjes 2016 (abstract only) - rat donor for GO:0045823, GO:0031704
    "PER16_APELA": "just like the fellow receptor agonist apelin, apela increases cardiac contractility and induces coronary vasodilation already in the nanomolar level",
    "PER16_BINDS": "We also provide evidence that apela binds to apelin receptors in the heart.",
    # PMID:11384769 Tatemoto 2001 (abstract only)
    "TAT01_MAP": "mean arterial pressure after the administration of apelin-12, apelin-13, and apelin-36 at a dose of 10 nmol/kg in anaesthetized rats was reduced by 26+/-5, 11+/-4, and 5+/-4 mm Hg, respectively",
    "TAT01_NOS": "In the presence of a nitric oxide (NO) synthase inhibitor, the effect of apelin-12 on blood pressure was abolished.",
    "TAT01_ENDO": "We also detected apelin-like immunoreactivity localized within the endothelia of small arteries in various organs.",
    # PMID:17673668 Kuba 2007 (abstract only)
    "KUB07_AGED": "aged Apelin knockout mice developed progressive impairment of cardiac contractility associated with systolic dysfunction in the absence of histological abnormalities",
    "KUB07_CRUCIAL": "These genetic data show that the endogenous peptide Apelin is crucial to maintain cardiac contractility in pressure overload and aging.",
    "KUB07_VIABLE": "Apelin mutant mice are viable and fertile, appear healthy, and exhibit normal body weight, water and food intake, heart rates, and heart morphology.",
    # PMID:19767528 Charo 2009 (full text)
    "CHA09_NORMAL": "Apelin-deficient mice were viable, fertile, and showed normal development.",
    "CHA09_MODEST": "Under basal conditions, both apelin and APJ null mice that survived to adulthood manifested modest decrements in contractile function.",
    "CHA09_EXERCISE": "However, with exercise stress both mutant lines demonstrated consistent and striking decreases in exercise capacity.",
    "CHA09_UNDISCOVERED": "differences in the developmental phenotype between apelin and APJ null mice suggest the possibility of undiscovered APJ ligands or ligand-independent effects of APJ",
    # PMID:15231996 De Mota 2004 (full text)
    "DEM04_FORMS": "We first characterized the predominant molecular forms of endogenous hypothalamic and plasma apelin as corresponding to apelin 13 and, to a lesser extent, to apelin 17.",
    "DEM04_DIURESIS": "In lactating mice, intracerebroventricular administration of apelin 17 reduced plasma AVP levels and increased diuresis.",
    "DEM04_WATERDEP": "Moreover, water deprivation, which increases systemic AVP release and causes depletion of hypothalamic AVP stores, decreased plasma apelin concentrations and induced hypothalamic accumulation of the peptide, indicating that AVP and apelin are conversely regulated to facilitate systemic AVP release and suppress diuresis.",
    "DEM04_DIURETIC": "Altogether, these data demonstrate that apelin acts as a potent diuretic neuropeptide counteracting AVP actions through inhibition of AVP neuron activity and AVP release.",
    # PMID:11815627 Vickers 2002 (abstract only)
    "VIC02_CTERM": "in each case, the proteolytic activity resulted in removal of the C-terminal residue only",
    "VIC02_CONSENSUS": "An alignment of the ACE2 peptide substrates reveals a consensus sequence of: Pro-X((1-3 residues))-Pro-Hydrophobic, where hydrolysis occurs between proline and the hydrophobic amino acid.",
    # PMID:27217402 Wang 2016 (abstract only)
    "WAN16_DOMINANT": "We examined the ability of angiotensin-converting enzyme 2 (ACE2) to cleave and inactivate pyr-apelin 13 and apelin 17, the dominant apelin peptides.",
    "WAN16_ACE2KO": "In ACE2 knockout mice, hypotensive action of pyr-apelin 13 and apelin 17 was potentiated",
    "WAN16_NEGREG": "We conclude that ACE2 represents a major negative regulator of apelin action in the vasculature and heart.",
    # PMID:24251091 Shin 2013 (full text)
    "SHI13_FURIN": "We show direct cleavage of proapelin to apelin-13 by proprotein convertase subtilisin/kexin 3 (PCSK3, or furin) in vitro, with no production of longer isoforms.",
    "SHI13_PREPRO": "The peptide hormone apelin is translated as a 77-residue preproprotein, truncated to the 55-residue proapelin and, subsequently, to 13-36-residue bioactive isoforms named apelin-13 to -36.",
    # PMID:18617693 Eyries 2008 (abstract only)
    "EYR08_ANGIO": "This peptide exerts a variety of cardiovascular effects and particularly acts as an activator of angiogenesis.",
    "EYR08_KD": "microinterfering RNA-mediated apelin or APJ receptor knockdown inhibits both hypoxia-induced endothelial cell proliferation in vitro and hypoxia-induced vessel regeneration in the caudal fin regeneration of Fli-1 transgenic zebrafish",
    "EYR08_HIF": "Chromatin immunoprecipitation assay reveals that hypoxia-inducible factor-1alpha binds to the endogenous hypoxia-responsive element site of the apelin gene.",
    # PMID:19046574 Dray 2008 (abstract only)
    "DRA08_GLUCOSE": "in chow-fed mice, acute intravenous injection of apelin has a powerful glucose-lowering effect associated with enhanced glucose utilization in skeletal muscle and AT",
    # UniProt flat file (each must sit on ONE physical line of the record)
    "UP_SECRETED": "SUBCELLULAR LOCATION: Secreted",
    "UP_PTM": "Several active peptides may be produced by proteolytic processing",
    "UP_FAMILY": "Belongs to the apelin family.",
    # Affinage deep-research report - cited once, at core-function level, for its
    # synthesis-level summary only; every mechanistic claim is carried by a PMID.
    "AFF_SUMMARY": "Apelin (APLN) is a secreted peptide hormone, processed from a precursor into multiple bioactive forms (apelin-13, apelin-17, apelin-36), that acts as an endogenous agonist of the G-protein-coupled apelin receptor APJ/APLNR to coordinate cardiovascular, angiogenic, metabolic, and tissue-protective programs",
    # Local bioinformatics RESULTS.md
    "BIO_PEPTIDE": "A \"rat\" or \"bovine\" apelin-17 in a pharmacology paper is, residue for residue, the human gene product.",
    "BIO_DIVERGENCE": "Divergence is confined to apelin-36, i.e. to the part of the precursor that is trimmed away.",
    "BIO_MOTIF": "Across the family the motif is present in",
    "BIO_NODE": "Human is inside that clade, so the target inherits.",
    "BIO_DONORS": "so this row has **three** gene-level donors, not four",
}

PM = {k: v for k, v in Q.items()}

UNIPROT = "file:human/APLN/APLN-uniprot.txt"
BIOINF = "file:human/APLN/APLN-bioinformatics/RESULTS.md"
AFFINAGE = "file:human/APLN/APLN-deep-research-affinage.md"

# --------------------------------------------------------------------------------------
# Source-entity facts. These are resolutions, not opinions: each was produced by
# resolve_withfrom.py against a live database or the committed PAINT slice.
# --------------------------------------------------------------------------------------

SOURCE_LABELS = {
    "PANTHER:PTN001041490": "PTHR15953 (APELIN) IBD node PTN001041490, placed at taxon:32523 Tetrapoda",
    "RGD:620672": "Apln (rat) - resolves to exactly one entry, Q9R0R3 APEL_RAT",
    "UniProtKB:Q9R0R3": "Apln (rat, Swiss-Prot APEL_RAT)",
    "UniProtKB:Q9R0R4": "Apln (mouse, Swiss-Prot APEL_MOUSE)",
    "UniProtKB:Q9TUI9": "APLN (bovine, Swiss-Prot APEL_BOVIN)",
    "UniProtKB:Q9ULZ1": "APLN (human, the target itself)",
    "ensembl:ENSRNOP00000100018": "rat Apln protein - resolves to Q9R0R3, the same entity as the UniProtKB donor on this row",
    "ensembl:ENSMUSP00000046012": "mouse Apln protein - resolves to Q9R0R4, the same entity as the UniProtKB donor on this row",
    "InterPro:IPR026155": "InterPro family 'Apelin', 345 proteins",
    "UniProtKB-SubCell:SL-0112": "UniProt subcellular location 'Extracellular space'",
    "UniProtKB-SubCell:SL-0243": "UniProt subcellular location 'Secreted'",
}

# --------------------------------------------------------------------------------------
# Decisions, keyed by (go_id, evidence, reference, supporting_entities tuple)
# --------------------------------------------------------------------------------------

RAT_PAIR = ("UniProtKB:Q9R0R3", "ensembl:ENSRNOP00000100018")
MOUSE_PAIR = ("UniProtKB:Q9R0R4", "ensembl:ENSMUSP00000046012")

DECISIONS: dict[tuple, dict] = {}


def D(go_id, ev, ref, ents=(), **kw):
    DECISIONS[(go_id, ev, ref, tuple(ents))] = kw


# ---------- GO:0005102 signaling receptor binding (TAS x2) ----------
_sigrec_reason = (
    "GO:0031704 apelin receptor binding is a descendant of this term via GO:0001664 G "
    "protein-coupled receptor binding (QuickGO ancestors), and the gene already carries "
    "GO:0031704 from an IDA in native human left ventricle. The generic parent therefore "
    "adds nothing that the specific child does not say better, and 'signaling receptor "
    "binding' does not record which receptor. This is a granularity fix, not a "
    "disagreement with the curator: the cited paper is precisely about the apelin/APJ "
    "pairing."
)
D("GO:0005102", "TAS", "PMID:10525157",
  summary=("Legacy ProtInc statement that apelin binds a signalling receptor. True but "
           "uninformative: the receptor is known and named, and the specific term is "
           "already on the gene."),
  action="MODIFY",
  reason=_sigrec_reason,
  proposed_replacement_terms=[{"id": "GO:0031704", "label": "apelin receptor binding"}],
  supported_by=[("PMID:10525157", "HAB99_APJLIGAND"), ("PMID:9792798", "TAT98_LIGAND")])
D("GO:0005102", "TAS", "PMID:9792798",
  summary=("Legacy ProtInc statement from the paper that identified apelin as the APJ "
           "ligand. The paper names the receptor, so the annotation can be specific."),
  action="MODIFY",
  reason=_sigrec_reason + (" The cited paper is the deorphanisation of APJ itself, so "
                           "nothing about the receptor's identity is in doubt."),
  proposed_replacement_terms=[{"id": "GO:0031704", "label": "apelin receptor binding"}],
  supported_by=[("PMID:9792798", "TAT98_LIGAND"), ("PMID:9792798", "TAT98_ISOLATED")])

# ---------- GO:0005179 hormone activity ----------
D("GO:0005179", "IDA", "PMID:22810587",
  summary=("Apelin acting on human APJ expressed in HEK cells inhibits cAMP accumulation "
           "in a pertussis-toxin-sensitive manner, raises pERK and recruits beta-arrestin - "
           "receptor-ligand activity measured directly on the human receptor."),
  action="ACCEPT",
  reason=(
      "GO:0005179 is a child of GO:0048018 receptor ligand activity and its definition is "
      "explicitly permissive about route - 'carried (sometimes in the bloodstream) to "
      "another organ or group of cells' - so a peptide that acts mostly in an "
      "autocrine/paracrine mode still satisfies it. This is the core molecular function "
      "of the gene product and the assays here are on the human receptor. One caveat "
      "belongs on the record rather than on the action: the best human measurement of "
      "circulating apelin, in PMID:28137936, concludes the peptides look more like locally "
      "released mediators than circulating hormones, so 'hormone' should be read as "
      "'receptor agonist' rather than as a claim about endocrine delivery. The activity "
      "belongs to the cleaved peptides (apelin-13/-17), not to the 77-residue precursor, "
      "which UniProt records as PRO chains."),
  supported_by=[("PMID:22810587", "SCI12_CAMP"), ("PMID:22810587", "SCI12_PTX"),
                ("PMID:22810587", "SCI12_PERK"), ("PMID:22810587", "SCI12_GI"),
                (UNIPROT, "UP_PTM")],
  additional_reference_ids=["PMID:28137936", "PMID:24251091"])

D("GO:0005179", "IEA", "GO_REF:0000002", ents=("InterPro:IPR026155",),
  summary=("InterPro2GO from IPR026155 'Apelin', a family signature that matches this gene "
           "family and essentially nothing else. The mapping is exact."),
  action="ACCEPT",
  reason=(
      "IPR026155 resolves to InterPro family 'Apelin' with 345 member proteins, i.e. a "
      "one-family signature, and the whole family is peptide agonists of the apelin "
      "receptor. Unlike a fold-level signature, this one cannot leak the activity onto "
      "unrelated proteins. The propagation is sound and the term is at the right depth."),
  supported_by=[("PMID:9792798", "TAT98_LIGAND"), (UNIPROT, "UP_FAMILY")],
  prop=dict(root_cause="NO_FAILURE_CORE",
            status={"InterPro:IPR026155": "SUPPORTS_TRANSFER"},
            comments={"InterPro:IPR026155": (
                "Gene-family-level signature, not a fold or domain shared with other "
                "activities; every member is an apelin-receptor agonist precursor, so the "
                "hormone/receptor-ligand activity cannot be mis-assigned through it.")},
            residue_na=("The objection to a family-signature IEA would be that the "
                        "signature is broader than the activity; here signature and family "
                        "coincide, and no residue is at issue.")))

D("GO:0005179", "IMP", "PMID:28137936",
  summary=("Receptor-ligand activity of apelin measured alongside ELABELA in the same "
           "assays: competition binding in human left ventricle and full agonism in cells "
           "expressing the human apelin receptor."),
  action="ACCEPT",
  reason=(
      "The paper is titled for ELABELA/Toddler, but pyroglutamyl-apelin-13 is run as a "
      "head-to-head comparator in every assay, so there are genuine apelin measurements: "
      "competition binding in human left ventricle homogenate, complete inhibition of "
      "forskolin-stimulated cAMP, and concentration-dependent beta-arrestin recruitment. "
      "The biology is right and the annotation is not ELABELA's biology mis-filed under "
      "APLN. What does not fit is the evidence code: IMP implies a mutant phenotype and "
      "this paper contains no APLN mutant or knockdown - its apelin data are synthetic "
      "peptide pharmacology, which is IDA-grade. Flagged for UniProt rather than acted on, "
      "since the term itself is correct and already carried by an IDA row."),
  supported_by=[("PMID:28137936", "YAN17_COMPETE"), ("PMID:28137936", "YAN17_CAMP"),
                ("PMID:28137936", "YAN17_ARRESTIN"), ("PMID:28137936", "YAN17_LVHOMOG")])

# ---------- GO:0005576 extracellular region ----------
D("GO:0005576", "IBA", "GO_REF:0000033",
  ents=("PANTHER:PTN001041490", "RGD:620672", "UniProtKB:Q9TUI9", "UniProtKB:Q9ULZ1"),
  summary=("The single PAINT assertion for the whole apelin family: the ancestral node "
           "PTN001041490, placed at Tetrapoda, is active in the extracellular region. "
           "Human APLN is inside that clade and is itself one of the seeds."),
  action="ACCEPT",
  reason=(
      "The committed PAINT slice resolves this row completely: PTHR15953 carries exactly "
      "one node-level annotation, an IBD for GO:0005576 at node PTN001041490, not negated, "
      "at taxon:32523 (Tetrapoda per NCBI Taxonomy), seeded by rat Apln, bovine APLN and "
      "human APLN. Human is a tetrapod, so the target sits inside the inheriting clade. "
      "The seeds are experimentally grounded on two other species - rat Apln has an EXP "
      "GO:0005576 from PMID:10525157 and bovine APLN has experimental GO:0005576 from "
      "PMID:10525157 and PMID:9792798 - and the target's own accession appearing in the "
      "WITH/FROM is the expected, valid case: human APLN's own IDA rows are among the "
      "descendant evidences the PAINT curator used to place the node, which is a marker of "
      "experimental grounding on the target, not circularity. There is no IRD or IKR "
      "anywhere in the family slice and no reason to expect one: the protein has a signal "
      "peptide, no transmembrane segment, and is measured in plasma, colostrum and "
      "conditioned medium. Note also that this row has three gene-level donors, not four - "
      "PANTHER:PTN001041490 is the node, not a donor."),
  supported_by=[("PMID:28137936", "YAN17_PLASMA"), ("PMID:10525157", "HAB99_COLOSTRUM"),
                (UNIPROT, "UP_SECRETED"), (BIOINF, "BIO_NODE")],
  prop=dict(root_cause="NO_FAILURE_CORE",
            status={"PANTHER:PTN001041490": "SUPPORTS_TRANSFER",
                    "RGD:620672": "SUPPORTS_TRANSFER",
                    "UniProtKB:Q9TUI9": "SUPPORTS_TRANSFER",
                    "UniProtKB:Q9ULZ1": "SUPPORTS_TRANSFER"},
            comments={
                "PANTHER:PTN001041490": (
                    "The ancestral node and the source of the transfer. PTHR15953-paint.tsv: "
                    "IBD, GO:0005576, aspect C, negated=false, taxon:32523 (Tetrapoda), "
                    "seeds RGD:620672|UniProtKB:Q9TUI9|UniProtKB:Q9ULZ1. It is the only "
                    "node-level annotation in the entire family."),
                "RGD:620672": (
                    "One of three gene-level donors. Resolves to exactly one UniProt entry, "
                    "Q9R0R3 APEL_RAT, whose own GO:0005576 is EXP from PMID:10525157."),
                "UniProtKB:Q9TUI9": (
                    "Bovine APLN, the species apelin was first purified from; its own "
                    "GO:0005576 is experimental from PMID:10525157 and PMID:9792798."),
                "UniProtKB:Q9ULZ1": (
                    "The target's own accession. Expected and valid: human APLN's "
                    "experimental GO:0005576 annotations are among the descendant evidences "
                    "behind the IBD, so the gene legitimately appears among the node's "
                    "seeds.")},
            residue_na=("Secretion here follows from the signal peptide and from direct "
                        "measurement of the peptide in plasma, colostrum and conditioned "
                        "medium; no single residue carries the argument.")))

D("GO:0005576", "IDA", "PMID:22810587",
  summary="Apelin quantified in mouse blood and in cardiomyocyte conditioned medium.",
  action="ACCEPT",
  reason=("Direct measurement of the peptide outside cells: circulating apelin rose from "
          "1 to 2 ng/ml after transaortic constriction, and apelin in cardiomyocyte "
          "conditioned medium was measured at about 5 ng/ml. Extracellular location is "
          "where every apelin function is executed, so this is core."),
  supported_by=[("PMID:22810587", "SCI12_BLOOD"), ("PMID:22810587", "SCI12_MEDIA")])

D("GO:0005576", "IDA", "PMID:28137936",
  summary="Apelin measured in human plasma by enzyme immunoassay at 0.26 nmol/L.",
  action="ACCEPT",
  reason=("The most direct human evidence for the location: apelin in plasma from 25 "
          "healthy donors, quantified by immunoassay. The authors add that the "
          "subnanomolar concentration looks more like a locally released mediator than a "
          "circulating hormone - which bears on the choice of MF term, not on the "
          "cellular component, since either way the peptide is extracellular."),
  supported_by=[("PMID:28137936", "YAN17_EIA"), ("PMID:28137936", "YAN17_PLASMA"),
                ("PMID:28137936", "YAN17_PARACRINE")])

D("GO:0005576", "IDA", "PMID:38428423",
  summary=("Apelin-13 resolved as an extracellular ligand engaging the APLNR-Gi1 complex "
           "in cryo-EM structures."),
  action="ACCEPT",
  reason=("The structures place the peptide in the extracellular-facing orthosteric pocket "
          "of the receptor; UniProt records the modelled chains as residues 65-77 and "
          "66-77 of APLN in PDB 8XZG/8XZH/8XZJ. A ligand bound from outside the cell is "
          "extracellular by construction, and this is the same location the IBA and the "
          "immunoassay rows assert."),
  supported_by=[("PMID:38428423", "WAN24_CRYOEM"), ("PMID:38428423", "WAN24_HORMONE"),
                (UNIPROT, "UP_SECRETED")])

D("GO:0005576", "IEA", "GO_REF:0000044", ents=("UniProtKB-SubCell:SL-0112", "UniProtKB-SubCell:SL-0243"),
  summary=("Mapping of UniProt's own subcellular-location vocabulary ('Secreted', "
           "'Extracellular space') onto GO:0005576."),
  action="ACCEPT",
  reason=("Both source locations resolve to exactly the concept GO:0005576 names, and the "
          "UniProt record carries them with experimental evidence (ECO:0000269 from "
          "PMID:22810587 and PMID:38428423) as well as by similarity. A vocabulary mapping "
          "is only as good as its source term, and here the source terms are precise."),
  supported_by=[(UNIPROT, "UP_SECRETED"), ("PMID:28137936", "YAN17_PLASMA")],
  prop=dict(root_cause="NO_FAILURE_CORE",
            status={"UniProtKB-SubCell:SL-0112": "SUPPORTS_TRANSFER",
                    "UniProtKB-SubCell:SL-0243": "SUPPORTS_TRANSFER"},
            comments={
                "UniProtKB-SubCell:SL-0112": (
                    "Resolves to 'Extracellular space' (rest.uniprot.org/locations), a "
                    "child concept of GO:0005576 rather than a broader or unrelated one."),
                "UniProtKB-SubCell:SL-0243": (
                    "Resolves to 'Secreted'. The APLN record's SUBCELLULAR LOCATION line "
                    "carries ECO:0000269 from PMID:22810587 and PMID:38428423, so the "
                    "source assertion is experimentally backed, not inferred.")},
            residue_na=("The signal peptide SIGNAL 1..22 is a feature, not a point "
                        "residue, and nothing in this row turns on a substitution.")))

D("GO:0005576", "ISS", "GO_REF:0000024", ents=("UniProtKB:Q9TUI9",),
  summary=("Curator sequence-similarity transfer of secretion from bovine APLN, the "
           "species apelin was purified from."),
  action="ACCEPT",
  reason=("The donor is Swiss-Prot bovine APLN (Q9TUI9), whose own GO:0005576 is "
          "experimental from PMID:10525157 and PMID:9792798 - the papers that purified "
          "apelin from bovine stomach extract and measured it at 14-93 pmol/ml in bovine "
          "colostrum. Human and bovine precursors are both 77 residues and their apelin-13 "
          "and apelin-17 peptides are identical, so the transfer is about as safe as an "
          "ISS gets. The human gene also has three independent IDA rows for the same term, "
          "so this row adds provenance rather than new information."),
  supported_by=[("PMID:10525157", "HAB99_COLOSTRUM"), ("PMID:9792798", "TAT98_ISOLATED"),
                (BIOINF, "BIO_PEPTIDE")],
  prop=dict(root_cause="NO_FAILURE_CORE",
            status={"UniProtKB:Q9TUI9": "SUPPORTS_TRANSFER"},
            comments={"UniProtKB:Q9TUI9": (
                "Bovine APLN, Swiss-Prot, 77 aa. Its GO:0005576 is experimental from "
                "PMID:10525157 and PMID:9792798 (QuickGO). cterm_conservation.py shows "
                "bovine and human apelin-13 and apelin-17 are identical, with only two "
                "substitutions across the whole of apelin-36.")},
            residue_na=("The claim is about secretion of the whole peptide, not about any "
                        "single position.")))

_reactome_reason = (
    "Reactome's curated human reaction set places apelin in the extracellular compartment "
    "as the ligand of the apelin receptor, and exports one GO:0005576 row per reaction in "
    "the ligand-binding and Gi-activation cascade. The four rows are a single curatorial "
    "assertion projected across four reaction identifiers rather than four independent "
    "lines of evidence, but the assertion itself is correct and matches the IDA, IBA and "
    "ISS rows. Redundant, not wrong."
)
for _rid, _what in [("R-HSA-374337", "apelin binding to its receptor"),
                    ("R-HSA-380073", "the liganded receptor acting as a GEF for Gi"),
                    ("R-HSA-749454", "dissociation of the ligand:GPCR:Gi complex"),
                    ("R-HSA-749456", "the liganded receptor binding inactive Gi")]:
    D("GO:0005576", "TAS", f"Reactome:{_rid}",
      summary=f"Reactome places apelin extracellularly in its reaction for {_what}.",
      action="ACCEPT",
      reason=_reactome_reason,
      supported_by=[(UNIPROT, "UP_SECRETED"), ("PMID:28137936", "YAN17_PLASMA")])

# ---------- GO:0006955 immune response ----------
D("GO:0006955", "TAS", "PMID:10525157",
  summary=("Legacy ProtInc row resting on one ex vivo observation: apelin partially "
           "suppressed cytokine production by mouse spleen cells after TCR/CD3 "
           "cross-linking."),
  action="MODIFY",
  reason=(
      "GO:0006955 is 'any immune system process that functions in the calibrated response "
      "of an organism to a potential internal or invasive threat'. Apelin is not mounting "
      "a response here; the single experiment behind the row shows it damping cytokine "
      "output, which is the opposite direction and a different kind of process. "
      "GO:0001818 negative regulation of cytokine production says what was actually "
      "measured. The underlying evidence is weak - one ex vivo assay on mouse splenocytes, "
      "described as partial, with the authors' own conclusion hedged to 'might therefore "
      "modulate immune responses in neonates' - so the replacement should be read as the "
      "most this observation can support, not as a well-established role."),
  proposed_replacement_terms=[{"id": "GO:0001818", "label": "negative regulation of cytokine production"}],
  supported_by=[("PMID:10525157", "HAB99_CYTOKINE"), ("PMID:10525157", "HAB99_COLOSTRUM")])

# ---------- GO:0007165 signal transduction ----------
_sigtrans_reason = (
    "GO:0060183 apelin receptor signaling pathway exists, is exactly this gene's pathway, "
    "and is already on the record from three IDA rows and an IMP. Annotating the root-level "
    "GO:0007165 alongside it loses everything specific. This is a granularity fix."
)
D("GO:0007165", "IEA", "GO_REF:0000002", ents=("InterPro:IPR026155",),
  summary=("InterPro2GO maps the gene-family signature IPR026155 'Apelin' to the generic "
           "signal transduction term."),
  action="MODIFY",
  reason=(
      _sigtrans_reason + " The source signature makes the case stronger, not weaker: "
      "IPR026155 is a single-family signature covering 345 apelin precursors and nothing "
      "else, so it can safely carry the family-exact term. A fold-level signature would "
      "have to stay generic; this one need not."),
  proposed_replacement_terms=[{"id": "GO:0060183", "label": "apelin receptor signaling pathway"}],
  supported_by=[("PMID:9792798", "TAT98_LIGAND"), ("PMID:22810587", "SCI12_GI")],
  prop=dict(root_cause="TERM_SCOPING_PROBLEM",
            failure_modes=["GRANULARITY_MISMATCH"],
            status={"InterPro:IPR026155": "SUPPORTS_SOURCE_BUT_NOT_TARGET"},
            comments={"InterPro:IPR026155": (
                "The signature is right and family-exact ('Apelin', 345 proteins); it is "
                "the interpro2go target term that is too shallow. Every protein matching "
                "this signature signals through the apelin receptor, so the mapping could "
                "point at GO:0060183 without risk of over-reach.")},
            residue_na="The objection is to term depth, not to any sequence feature."))
D("GO:0007165", "TAS", "PMID:9792798",
  summary=("Legacy ProtInc row from the deorphanisation paper, recorded before the "
           "apelin-specific pathway term existed."),
  action="MODIFY",
  reason=(
      _sigtrans_reason + " The cited paper's content is specifically apelin-receptor "
      "signalling - synthetic C-terminal peptides raising the extracellular acidification "
      "rate of APJ-expressing cells at 0.1-100 nM - so the specific term is what the "
      "statement actually supports."),
  proposed_replacement_terms=[{"id": "GO:0060183", "label": "apelin receptor signaling pathway"}],
  supported_by=[("PMID:9792798", "TAT98_LIGAND"), ("PMID:9792798", "TAT98_PRECURSOR")])

# ---------- GO:0007595 lactation ----------
D("GO:0007595", "TAS", "PMID:10525157",
  summary=("Legacy ProtInc row inferred from apelin being abundant in mammary gland and "
           "secreted into colostrum and milk. That is expression and localisation, not "
           "participation in milk release."),
  action="REMOVE",
  reason=(
      "GO:0007595 is defined as 'the regulated release of milk from the mammary glands and "
      "the period of time that a mother lactates to feed her young'. What the cited paper "
      "reports is abundance: apelin mRNA highest in the mammary gland of pregnant rats, "
      "rising through pregnancy and lactation to a peak around parturition, and 14-93 "
      "pmol/ml of peptide in bovine colostrum. Apelin is therefore a constituent of milk - "
      "a localisation fact the gene already carries on ten other rows as GO:0005576 - and "
      "the paper contains no perturbation of apelin with a milk-release or milk-yield "
      "readout. Inferring a biological process from an expression profile is precisely the "
      "inference GO asks curators not to make, and nothing published since supplies the "
      "missing experiment: targeted PubMed searches pairing apelin with lactation, milk "
      "ejection and oxytocin return no study that perturbs apelin and measures milk "
      "release. The nearby real biology runs the other way - apelin acts centrally on "
      "vasopressin neurons and was studied in lactating rats for that reason "
      "(PMID:15231996) - which is a body-fluid role, not a lactation role, and is proposed "
      "separately here as GO:0050878."),
  supported_by=[("PMID:10525157", "HAB99_MAMMARY"), ("PMID:10525157", "HAB99_PARTURITION"),
                ("PMID:10525157", "HAB99_COLOSTRUM")],
  additional_reference_ids=["PMID:15231996"])

# ---------- GO:0010629 negative regulation of gene expression (IGI) ----------
D("GO:0010629", "IGI", "PMID:23263626",
  ents=("RNAcentral:URS00000F0F49_9606", "RNAcentral:URS00000F6E49_9606"),
  summary=("APLN knockdown in human pulmonary artery endothelial cells raises FGF2 and "
           "FGFR1; overexpressing miR-424 and miR-503 abolishes the rise. The two "
           "WITH/FROM identifiers resolve to exactly those miRNAs."),
  action="KEEP_AS_NON_CORE",
  reason=(
      "The experiment is sound and human: siRNA against APLN and lentiviral APLN "
      "overexpression in patient-derived and control PAECs, with both perturbation "
      "directions reported. The genetic-interaction partners are correctly identified - "
      "URS00000F0F49_9606 resolves to hsa-miR-424-5p and URS00000F6E49_9606 to "
      "hsa-miR-503-5p, which are the two miRNAs the paper is about. The term itself is "
      "near the top of the regulation hierarchy and says nothing about which gene, but it "
      "is not wrong and no obviously better child exists for 'reduces FGF2 and FGFR1 "
      "message'. Non-core: apelin is a secreted ligand, and this is a transcriptional "
      "consequence two steps downstream of receptor engagement, confined to pulmonary "
      "endothelium."),
  supported_by=[("PMID:23263626", "KIM13_FGF"), ("PMID:23263626", "KIM13_FGF2OE")])

# ---------- GO:0031704 apelin receptor binding ----------
D("GO:0031704", "IDA", "PMID:28137936",
  summary=("Radioligand competition binding in homogenates of human left ventricle and in "
           "CHO-K1 cells expressing the human apelin receptor."),
  action="ACCEPT",
  reason=(
      "This is the gene's most informative molecular-function annotation and it is measured "
      "in native human tissue rather than only in a heterologous system. The paper's "
      "subject is ELABELA, but apelin is the competitor the ELA peptides are measured "
      "against, so the apelin affinity is a real datum from this paper and not ELABELA's "
      "biology transferred onto APLN. Core function."),
  supported_by=[("PMID:28137936", "YAN17_COMPETE"), ("PMID:28137936", "YAN17_LVHOMOG"),
                ("PMID:38428423", "WAN24_CRYOEM")])

D("GO:0031704", "IEA", "GO_REF:0000120",
  ents=("UniProtKB:Q9R0R3", "ensembl:ENSRNOP00000100018", "InterPro:IPR026155"),
  summary=("Combined automatic pipeline: rat Apln ortholog plus the apelin family "
           "signature, both pointing at the same, correct, family-exact term."),
  action="ACCEPT",
  reason=(
      "Two independent supports converge. Rat Apln (Q9R0R3) carries GO:0031704 as an IDA "
      "from PMID:26611206, and IPR026155 is a single-family signature covering apelin "
      "precursors only. Human and rat apelin-13 and apelin-17 are identical residue for "
      "residue, so orthology transfer here is not an approximation. The human gene also "
      "has its own IDA in human left ventricle, so the row is redundant but correct, and it "
      "is the right depth."),
  supported_by=[("PMID:26611206", "PER16_BINDS"), ("PMID:26611206", "PER16_APELA"),
                ("PMID:28137936", "YAN17_COMPETE"), (BIOINF, "BIO_PEPTIDE")],
  prop=dict(root_cause="NO_FAILURE_CORE",
            status={"UniProtKB:Q9R0R3": "SUPPORTS_TRANSFER",
                    "ensembl:ENSRNOP00000100018": "SUPPORTS_TRANSFER",
                    "InterPro:IPR026155": "SUPPORTS_TRANSFER"},
            comments={
                "UniProtKB:Q9R0R3": (
                    "Rat Apln. Its own GO:0031704 is IDA from PMID:26611206, a paper whose "
                    "subject is apela/ELABELA but which reports apelin-receptor binding in "
                    "heart with apelin as the benchmark ligand. Cached abstract only, so "
                    "the apelin binding panel itself is not visible here; the curator read "
                    "the full text."),
                "ensembl:ENSRNOP00000100018": (
                    "Resolves to Q9R0R3, the same rat entity already listed on this row - "
                    "two identifiers, one donor."),
                "InterPro:IPR026155": (
                    "Independent of the ortholog arm: a family signature matching 345 "
                    "apelin precursors and nothing else.")},
            residue_na=("Binding is carried by the whole apelin-13 pharmacophore, whose "
                        "N-terminal RPRL motif and C-terminal Phe are both required "
                        "(PMID:11359874); the retention claim for that Phe is recorded on "
                        "the GO:0060183 IEA row rather than duplicated here.")))

# ---------- GO:0040037 negative regulation of FGFR signaling (IGI) ----------
D("GO:0040037", "IGI", "PMID:23263626",
  ents=("RNAcentral:URS00000F0F49_9606", "RNAcentral:URS00000F6E49_9606"),
  summary=("Loss of APLN in human pulmonary artery endothelial cells de-represses FGF2 and "
           "FGFR1 and increases downstream proliferation; restoring miR-424/miR-503 "
           "reverses it."),
  action="KEEP_AS_NON_CORE",
  reason=(
      "A well-formed IGI: the interacting entities really are hsa-miR-424-5p and "
      "hsa-miR-503-5p, and the epistasis runs in both directions (knockdown raises "
      "FGF2/FGFR1; miRNA overexpression abolishes the rise; FGF2 knockdown abolishes the "
      "downstream smooth-muscle phenotype). The term is more specific and more useful than "
      "its GO:0010629 sibling row. It remains non-core: apelin does not touch the FGF "
      "pathway directly - the chain is apelin, apelin receptor, miR-424/503 transcription, "
      "FGF2/FGFR1 message - and the whole axis is characterised only in pulmonary "
      "endothelium in the context of pulmonary arterial hypertension."),
  supported_by=[("PMID:23263626", "KIM13_FGF"), ("PMID:23263626", "KIM13_FGF2DEP"),
                ("PMID:23263626", "KIM13_QUIESCENT")])

# ---------- GO:0042756 drinking behavior ----------
_drink_summary = ("Central injection of pyroglutamyl-apelin-13 reduced water intake in "
                  "dehydrated rats; the human rows are ortholog transfers of that rat IMP.")
_drink_reason = (
    "The donor annotation is sound and the transfer is safe at the level of the ligand: rat "
    "Apln carries GO:0042756 as an IMP from PMID:11359874, whose abstract states that "
    "central pE13F significantly decreased water intake in dehydrated normotensive rats, "
    "and the rat and human apelin-13 and apelin-17 peptides are identical. The wider "
    "picture supports it - apelin inhibits vasopressin neuron activity and vasopressin "
    "release, and acts as a diuretic counteracting vasopressin (PMID:15231996). Two "
    "qualifications keep it out of core. It is an organismal behaviour several steps "
    "downstream of receptor activation, and the rat evidence is peptide infusion into the "
    "brain rather than a genetic loss of Apln, so 'IMP' overstates the perturbation: "
    "Apln-null mice have normal water intake (PMID:17673668)."
)
_drink_supp = [("PMID:11359874", "REA01_WATER"), ("PMID:11359874", "REA01_FLUID"),
               ("PMID:15231996", "DEM04_DIURETIC"), ("PMID:17673668", "KUB07_VIABLE")]
D("GO:0042756", "IEA", "GO_REF:0000107", ents=RAT_PAIR,
  summary=_drink_summary + " Automatic Ensembl Compara transfer.",
  action="KEEP_AS_NON_CORE", reason=_drink_reason, supported_by=_drink_supp,
  prop=dict(root_cause="NO_FAILURE_NON_CORE",
            status={k: "SUPPORTS_TRANSFER" for k in RAT_PAIR},
            comments={
                "UniProtKB:Q9R0R3": (
                    "Rat Apln, GO:0042756 IMP from PMID:11359874. The cited abstract does "
                    "support this term - it is the same sentence that fails to support the "
                    "rat blood-pressure annotation."),
                "ensembl:ENSRNOP00000100018": (
                    "Resolves to Q9R0R3: the same donor under a second identifier, so this "
                    "row has one gene-level donor, not two.")},
            residue_na=("A behavioural readout; no residue-level claim is involved, and the "
                        "peptide is identical between rat and human in any case.")))
D("GO:0042756", "ISS", "GO_REF:0000024", ents=("UniProtKB:Q9R0R3",),
  summary=_drink_summary + " Curator sequence-similarity transfer.",
  action="KEEP_AS_NON_CORE", reason=_drink_reason, supported_by=_drink_supp,
  prop=dict(root_cause="NO_FAILURE_NON_CORE",
            status={"UniProtKB:Q9R0R3": "SUPPORTS_TRANSFER"},
            comments={"UniProtKB:Q9R0R3": (
                "Rat Apln, GO:0042756 IMP from PMID:11359874. Sequence similarity is not an "
                "approximation here: rat and human apelin-13 and apelin-17 are identical, "
                "so the peptide injected into rat brain is the human gene product.")},
            residue_na="A behavioural readout; no residue-level claim is involved."))

# ---------- GO:0045776 negative regulation of blood pressure ----------
_bp_summary = ("Apelin is a vasodepressor. The human rows transfer a rat IMP whose cited "
               "paper reports no blood-pressure effect; the biology is nonetheless well "
               "established from other work.")
_bp_reason = (
    "Two things have to be separated here. The claim is true: apelin-12, -13 and -36 lower "
    "mean arterial pressure in anaesthetised rats in a nitric-oxide-dependent way "
    "(PMID:11384769), apelin infusion lowers systolic blood pressure in wild-type but not "
    "APJ-null mice (PMID:22810587), and ACE2 knockout potentiates the hypotensive action of "
    "the apelin peptides (PMID:27217402). The propagation chain, however, is weak: the only "
    "donor is rat Apln, whose GO:0045776 is an IMP citing PMID:11359874, and that paper's "
    "abstract reports the opposite result for its own blood-pressure readout - central "
    "pE13F decreased water intake but did not affect blood pressure. The cache is "
    "abstract-only so a peripheral-route experiment in the full text cannot be excluded, "
    "and the curator read what we cannot; but on the accessible record the cited evidence "
    "does not establish this term, and the same sentence is what legitimately supports the "
    "drinking-behaviour row. Kept, because the function is real and supported elsewhere, "
    "but non-core: it is an organismal haemodynamic readout of receptor activation, not a "
    "second activity of the gene product. Raised as a question for UniProt."
)
_bp_supp = [("PMID:11359874", "REA01_WATER"), ("PMID:11384769", "TAT01_MAP"),
            ("PMID:11384769", "TAT01_NOS"), ("PMID:22810587", "SCI12_BP"),
            ("PMID:27217402", "WAN16_ACE2KO")]
D("GO:0045776", "IEA", "GO_REF:0000107", ents=RAT_PAIR,
  summary=_bp_summary + " Automatic Ensembl Compara transfer.",
  action="KEEP_AS_NON_CORE", reason=_bp_reason, supported_by=_bp_supp,
  prop=dict(root_cause="SOURCE_WEAK_OR_INFERRED",
            failure_modes=["SOURCE_EVIDENCE_WEAK"],
            status={"UniProtKB:Q9R0R3": "SOURCE_WEAK_OR_INFERRED",
                    "ensembl:ENSRNOP00000100018": "SOURCE_WEAK_OR_INFERRED"},
            comments={
                "UniProtKB:Q9R0R3": (
                    "Rat Apln, GO:0045776 IMP from PMID:11359874 (verified on the rat "
                    "record via the GO API). That paper's abstract states central pE13F "
                    "'did not affect blood pressure'. The vasodepressor effect of apelin is "
                    "real but comes from PMID:11384769 and PMID:22810587, neither of which "
                    "is cited by the donor annotation."),
                "ensembl:ENSRNOP00000100018": (
                    "Resolves to Q9R0R3: one donor under two identifiers, so the weakness "
                    "is not offset by a second, independent source.")},
            residue_na=("The weakness is in the donor's citation, not in any sequence "
                        "feature of human apelin.")))
D("GO:0045776", "ISS", "GO_REF:0000024", ents=("UniProtKB:Q9R0R3",),
  summary=_bp_summary + " Curator sequence-similarity transfer.",
  action="KEEP_AS_NON_CORE", reason=_bp_reason, supported_by=_bp_supp,
  prop=dict(root_cause="SOURCE_WEAK_OR_INFERRED",
            failure_modes=["SOURCE_EVIDENCE_WEAK"],
            status={"UniProtKB:Q9R0R3": "SOURCE_WEAK_OR_INFERRED"},
            comments={"UniProtKB:Q9R0R3": (
                "The sole donor. Sequence similarity is not the problem - rat and human "
                "apelin-13/-17 are identical - the problem is that the donor's own IMP "
                "cites PMID:11359874, whose stated blood-pressure result is negative. A "
                "re-citation to PMID:11384769 on the rat record would repair the chain "
                "without changing any term.")},
            residue_na="The weakness is in the donor's citation, not in a sequence feature."))

# ---------- GO:0045823 positive regulation of heart contraction ----------
_inotrope_summary = ("Apelin is a potent positive inotrope. The human rows transfer a rat "
                     "IMP, with independent genetic support from Apln-null mice.")
_inotrope_reason = (
    "This is the best-supported of the organismal terms on the gene. Apelin is described as "
    "the most potent inotrope in the heart in vitro (PMID:28137936), and unlike the other "
    "physiological rows it has genuine loss-of-function backing: aged Apln-knockout mice "
    "develop progressive impairment of cardiac contractility and systolic dysfunction "
    "(PMID:17673668), and both apelin-null and APJ-null mice show basal contractile "
    "decrements and striking loss of exercise capacity (PMID:19767528). The donor chain is "
    "thinner than the biology: rat Apln's GO:0045823 is an IMP from PMID:26611206, a paper "
    "whose subject is apela/ELABELA and in which apelin appears as the comparator agonist, "
    "and which contains no Apln mutant. Kept as non-core because it is an organ-level "
    "readout of apelin receptor signalling rather than a second molecular function of the "
    "gene product."
)
_inotrope_supp = [("PMID:26611206", "PER16_APELA"), ("PMID:28137936", "YAN17_INOTROPE"),
                  ("PMID:17673668", "KUB07_AGED"), ("PMID:17673668", "KUB07_CRUCIAL"),
                  ("PMID:19767528", "CHA09_MODEST")]
D("GO:0045823", "IEA", "GO_REF:0000107", ents=RAT_PAIR,
  summary=_inotrope_summary + " Automatic Ensembl Compara transfer.",
  action="KEEP_AS_NON_CORE", reason=_inotrope_reason, supported_by=_inotrope_supp,
  prop=dict(root_cause="NO_FAILURE_NON_CORE",
            status={k: "SUPPORTS_TRANSFER" for k in RAT_PAIR},
            comments={
                "UniProtKB:Q9R0R3": (
                    "Rat Apln, GO:0045823 IMP from PMID:26611206. The paper is about apela, "
                    "with apelin as the benchmark agonist in isolated adult rat hearts; the "
                    "cache is abstract-only so the apelin inotropy panel is not visible "
                    "here. The term is independently supported by Apln-null mouse data "
                    "(PMID:17673668, PMID:19767528) that the donor does not cite."),
                "ensembl:ENSRNOP00000100018": (
                    "Resolves to Q9R0R3 - the same rat donor under a second identifier.")},
            residue_na=("An organ-level contractility readout; no residue claim applies.")))
D("GO:0045823", "ISS", "GO_REF:0000024", ents=("UniProtKB:Q9R0R3",),
  summary=_inotrope_summary + " Curator sequence-similarity transfer.",
  action="KEEP_AS_NON_CORE", reason=_inotrope_reason, supported_by=_inotrope_supp,
  prop=dict(root_cause="NO_FAILURE_NON_CORE",
            status={"UniProtKB:Q9R0R3": "SUPPORTS_TRANSFER"},
            comments={"UniProtKB:Q9R0R3": (
                "Rat Apln, GO:0045823 IMP from PMID:26611206. Sequence similarity is exact "
                "at the level of the mature peptide, so the transfer risk is in the "
                "physiology, not the ligand. Mouse Apln-null phenotypes make the same point "
                "genetically.")},
            residue_na="An organ-level contractility readout; no residue claim applies."))

# ---------- GO:0060183 apelin receptor signaling pathway ----------
D("GO:0060183", "IDA", "PMID:11359874",
  summary=("Apelin-17 and pyroglutamyl-apelin-13 inhibit forskolin-stimulated cAMP and "
           "drive receptor internalisation in cells expressing the apelin receptor; "
           "N-terminally truncated fragments are inactive."),
  action="ACCEPT",
  reason=(
      "A clean pharmacological demonstration of the pathway, with an internal specificity "
      "control: K17F and pE13F are active while R10F and G5F are not, so the response "
      "depends on the intact peptide and is not a non-specific effect. The receptor is rat "
      "and the cells are CHO, but the peptides are the human ones - human, rat, mouse and "
      "bovine apelin-13 and apelin-17 are identical residue for residue - so this is the "
      "human gene product engaging its receptor. Core function."),
  supported_by=[("PMID:11359874", "REA01_FRAGMENTS"), ("PMID:11359874", "REA01_INACTIVE"),
                ("PMID:11359874", "REA01_CHO"), (BIOINF, "BIO_PEPTIDE")])
D("GO:0060183", "IDA", "PMID:22810587",
  summary=("Apelin acting on human APJ inhibits adenylyl cyclase through Gi, raises pERK, "
           "generates inositol phosphates and recruits beta-arrestin."),
  action="ACCEPT",
  reason=(
      "The most complete single description of the pathway on the human receptor: cAMP "
      "inhibition that is pertussis-toxin sensitive, dose-dependent IP1 accumulation via "
      "the promiscuous Galpha16 reporter, ERK phosphorylation, and beta-arrestin "
      "recruitment. The paper's headline is that APJ also signals independently of apelin "
      "in response to stretch; that is a receptor property and is correctly not annotated "
      "to APLN. Core function."),
  supported_by=[("PMID:22810587", "SCI12_CAMP"), ("PMID:22810587", "SCI12_GI"),
                ("PMID:22810587", "SCI12_IP1"), ("PMID:22810587", "SCI12_ARRESTIN"),
                ("PMID:22810587", "SCI12_APJONLY")])
D("GO:0060183", "IDA", "PMID:38428423",
  summary=("Cryo-EM structures of apelin-bound APLNR-Gi1 complexes, with the residues "
           "controlling G-protein versus beta-arrestin bias identified."),
  action="ACCEPT",
  reason=(
      "Structural evidence for the pathway at its first step: the peptide occupies the "
      "orthosteric site of APLNR in complex with Gi1, and structure-guided redesign "
      "produced biased agonists, which only makes sense if the native ligand engages both "
      "arms. UniProt records two APLN residues from this work - SITE 75 and SITE 77, "
      "'Important for the balance between G(i) and beta-arrestin pathways induced by "
      "apelin-13-APLNR system' - so the paper assigns pathway-determining roles to "
      "positions in this gene product, not only to the receptor. Core function."),
  supported_by=[("PMID:38428423", "WAN24_CRYOEM"), ("PMID:38428423", "WAN24_BIAS"),
                ("PMID:38428423", "WAN24_ARRESTIN"), ("PMID:38428423", "WAN24_HORMONE")])
D("GO:0060183", "IEA", "GO_REF:0000120", ents=RAT_PAIR + MOUSE_PAIR,
  summary=("Combined automatic pipeline transferring the pathway from the rat and mouse "
           "orthologs, each of which carries it from PMID:11359874."),
  action="ACCEPT",
  reason=(
      "Both donors carry GO:0060183 as an IDA from PMID:11359874, and the human gene has "
      "three independent IDA rows of its own, so the propagation agrees with direct human "
      "evidence rather than substituting for it. The transfer is exact at the level of the "
      "ligand: cterm_conservation.py shows the C-terminal 12 residues R66-F77 are 97-98.5% "
      "invariant across all 333 UniProt members of PTHR15953, and rat, mouse, bovine and "
      "human apelin-13 and apelin-17 are identical. The terminal Phe77 that human apelin "
      "retains is both the determinant of signalling bias recorded by UniProt and the "
      "single residue ACE2 removes to terminate the signal, so retention of that residue "
      "is what makes the orthologs' pathway the target's pathway."),
  supported_by=[("PMID:11359874", "REA01_FRAGMENTS"), (BIOINF, "BIO_PEPTIDE"),
                ("PMID:11815627", "VIC02_CTERM"), ("PMID:11815627", "VIC02_CONSENSUS")],
  prop=dict(root_cause="NO_FAILURE_CORE",
            status={k: "SUPPORTS_TRANSFER" for k in RAT_PAIR + MOUSE_PAIR},
            comments={
                "UniProtKB:Q9R0R3": ("Rat Apln, GO:0060183 IDA from PMID:11359874 "
                                     "(cAMP inhibition and receptor internalisation)."),
                "ensembl:ENSRNOP00000100018": "Resolves to Q9R0R3; one donor, two identifiers.",
                "UniProtKB:Q9R0R4": ("Mouse Apln, GO:0060183 IDA from PMID:11359874, "
                                     "confirmed on the mouse record via the GO API."),
                "ensembl:ENSMUSP00000046012": "Resolves to Q9R0R4; one donor, two identifiers."},
            residue_claims=[dict(
                claim_type="RETAINED",
                anchor=dict(accession="UniProtKB:Q9R0R3", position=77, residue="F", sequence_version=1),
                target=dict(accession="UniProtKB:Q9ULZ1", position=77, residue="F", sequence_version=1),
                role=("C-terminal Phe of apelin-13/-17; required for receptor activation, "
                      "flagged by UniProt SITE 77 as a determinant of the G(i) versus "
                      "beta-arrestin balance, and the single residue removed by ACE2"),
                method="MSA",
                comment=(
                    "Computed in APLN-bioinformatics/cterm_conservation.py. The peptide is "
                    "released from the precursor's C-terminus, so the last n residues are an "
                    "exact alignment-free correspondence; both donor and target precursors "
                    "are 77 aa and their C-terminal 17 residues are identical. Across all "
                    "333 UniProt members of PTHR15953 the terminal residue is Phe in "
                    "328/333 (98.5%), and 328/333 match the ACE2 substrate consensus "
                    "Pro-X(1-3)-Pro-hydrophobic reported in PMID:11815627, which for human "
                    "apelin is P74-M75-P76-F77."))]))
D("GO:0060183", "IMP", "PMID:28137936",
  summary=("Apelin activating the human apelin receptor in cell-based assays, run "
           "alongside ELABELA: cAMP inhibition and beta-arrestin recruitment, both blocked "
           "by the antagonist ML221."),
  action="ACCEPT",
  reason=(
      "The pathway readouts for apelin in this paper are real and the antagonist control "
      "makes them receptor-dependent. As with the GO:0005179 row from the same paper, the "
      "evidence code is the questionable part: IMP implies a mutant phenotype, and the "
      "apelin arm of this study is synthetic peptide pharmacology in CHO-K1 cells "
      "expressing the human apelin receptor, which is IDA-grade. The term is correct, is "
      "already carried by three IDA rows, and is core."),
  supported_by=[("PMID:28137936", "YAN17_CAMP"), ("PMID:28137936", "YAN17_ARRESTIN"),
                ("PMID:28137936", "YAN17_LVHOMOG"), ("PMID:28137936", "YAN17_ERK")])

# ---------- GO:0060976 coronary vasculature development ----------
_cor_summary = ("Transferred from a mouse Apln IMP whose underlying paper reports that "
                "Apelin-null hearts have the opposite coronary phenotype to Apj-null "
                "hearts. The unsigned term survives; any directional reading does not.")
_cor_reason = (
    "Traced to its origin, this row means something different from what it looks like. The "
    "mouse donor's GO:0060976 is an IMP from PMID:28890073, a paper whose thesis is that "
    "the ELABELA-APJ axis, not apelin, is what sinus-venosus-derived coronary progenitors "
    "require. Its apelin data are a measured negative plus an opposite-sign phenotype: "
    "Apelin-knockout animals did not phenocopy the Apj-knockout coronary defect, and "
    "Apelin-deficient hearts showed increased coronary growth with earlier full coverage "
    "than wild type. Since GO:0060976 is an unsigned developmental process used with "
    "involved_in, an Apln-null with accelerated coronary coverage is still involvement, so "
    "the term itself transfers correctly and should not be removed. What does not transfer "
    "is the gloss UniProt places on the same evidence, 'Plays a role in early coronary "
    "blood vessels formation (By similarity)', which reads as a positive requirement. GO "
    "offers no regulation-of-coronary-vasculature-development child to move to, so the "
    "honest action is to keep the term as non-core with the direction recorded here. This "
    "is also the one row where the ELABELA/apelin confound genuinely reaches APLN, and the "
    "wider literature agrees the two ligands are separable: apelin-null mice develop "
    "normally while APJ-null mice do not (PMID:19767528, PMID:22810587)."
)
_cor_supp = [("PMID:28890073", "SHA17_NOPHENO"), ("PMID:28890073", "SHA17_OPPOSITE"),
             ("PMID:28890073", "SHA17_LIGANDS"), ("PMID:19767528", "CHA09_NORMAL"),
             ("PMID:19767528", "CHA09_UNDISCOVERED")]
D("GO:0060976", "IEA", "GO_REF:0000107", ents=MOUSE_PAIR,
  summary=_cor_summary + " Automatic Ensembl Compara transfer.",
  action="KEEP_AS_NON_CORE", reason=_cor_reason, supported_by=_cor_supp,
  prop=dict(root_cause="NO_FAILURE_NON_CORE",
            status={k: "SUPPORTS_TRANSFER" for k in MOUSE_PAIR},
            comments={
                "UniProtKB:Q9R0R4": (
                    "Mouse Apln, GO:0060976 IMP from PMID:28890073 (confirmed on the mouse "
                    "record via the GO API). The paper is an ELABELA/Apj study; its Apln "
                    "data are 'Apelin KO animals did not phenocopy the coronary defect seen "
                    "in Apj KOs' and an opposite-direction phenotype of increased coronary "
                    "growth. The unsigned term transfers; a positive reading of it does "
                    "not."),
                "ensembl:ENSMUSP00000046012": (
                    "Resolves to Q9R0R4 - the same mouse donor under a second identifier, "
                    "so there is one donor behind this row.")},
            residue_na=("A developmental-genetics phenotype in a knockout; the question is "
                        "the sign of the phenotype, not any sequence position.")))
D("GO:0060976", "ISS", "GO_REF:0000024", ents=("UniProtKB:Q9R0R4",),
  summary=_cor_summary + " Curator sequence-similarity transfer.",
  action="KEEP_AS_NON_CORE", reason=_cor_reason, supported_by=_cor_supp,
  prop=dict(root_cause="NO_FAILURE_NON_CORE",
            status={"UniProtKB:Q9R0R4": "SUPPORTS_TRANSFER"},
            comments={"UniProtKB:Q9R0R4": (
                "The sole donor. Mouse and human apelin-13/-17 are identical, so orthology "
                "is not in question; the issue is that the donor phenotype is an increase "
                "in coronary growth on loss of Apln, which an unsigned developmental term "
                "cannot express.")},
            residue_na="The question is the sign of a knockout phenotype, not a residue."))

# ---------- GO:1902895 positive regulation of miRNA transcription ----------
D("GO:1902895", "IDA", "PMID:23263626",
  summary=("APLN overexpression induces a miR-424/503 promoter-reporter in human pulmonary "
           "artery endothelial cells and APLN knockdown lowers both the primary and the "
           "mature miRNAs."),
  action="KEEP_AS_NON_CORE",
  reason=(
      "Both perturbation directions are present and the paper distinguishes transcription "
      "from processing, which is what the term requires: the pri- and mature forms fall "
      "together on knockdown, and a promoter-reporter responds to overexpression. Apelin "
      "is obviously not acting at the promoter - it is a secreted ligand and the effect is "
      "downstream of the apelin receptor - but 'involved_in' a regulation term tolerates "
      "that indirection. Non-core: this is one transcriptional output of apelin receptor "
      "signalling in one cell type, not an activity of the gene product. The evidence is "
      "also overexpression-and-knockdown, i.e. IMP-grade rather than IDA-grade, whatever "
      "the code says."),
  supported_by=[("PMID:23263626", "KIM13_REPORTER"), ("PMID:23263626", "KIM13_QPCR"),
                ("PMID:23263626", "KIM13_TRANSCRIPTION")])

# ---------- GO:1904022 positive regulation of GPCR internalization ----------
D("GO:1904022", "IDA", "PMID:11359874",
  summary=("Apelin-17 and pyroglutamyl-apelin-13 drive internalisation of a GFP-tagged "
           "apelin receptor; inactive fragments do not."),
  action="ACCEPT",
  reason=(
      "Agonist-driven receptor internalisation is part of what apelin does to its receptor, "
      "not a distant consequence: it is the desensitisation arm whose balance against Gi "
      "signalling is set by apelin residues 75 and 77 (UniProt SITE, from PMID:38428423) "
      "and whose over-activation is the adverse-effect problem that motivated the design of "
      "G-protein-biased agonists. The assay has its own specificity control in the inactive "
      "truncated fragments. One precision worth recording rather than glossing: apelin "
      "drives beta-arrestin recruitment and it drives internalisation, but these are not the "
      "same step - pyroglutamyl-apelin-13 internalises APJ through clathrin-coated vesicles "
      "in a GRK2-dependent, EPS15- and dynamin-dependent but beta-arrestin1-independent "
      "manner (PMID:27492965). Core."),
  supported_by=[("PMID:11359874", "REA01_FRAGMENTS"), ("PMID:11359874", "REA01_INACTIVE"),
                ("PMID:27492965", "POP16_CCV"), ("PMID:27492965", "POP16_GRK2"),
                ("PMID:38428423", "WAN24_ARRESTIN")],
  additional_reference_ids=["PMID:22810587"])
D("GO:1904022", "IEA", "GO_REF:0000120", ents=RAT_PAIR + MOUSE_PAIR,
  summary=("Combined automatic pipeline transferring receptor internalisation from the rat "
           "and mouse orthologs, both of which carry it from PMID:11359874."),
  action="ACCEPT",
  reason=(
      "Both donors hold GO:1904022 as an IDA from the same paper the human IDA row cites, "
      "and the human gene already carries the term directly, so this is a redundant but "
      "correct restatement. Transfer risk is negligible because the peptides are identical "
      "across the three species; the receptor in the donors' experiment is rat, but "
      "pyroglutamyl-apelin-13 was subsequently run in a receptor-internalisation assay "
      "against the human apelin receptor in CHO-K1 cells (PMID:28137936), and the mechanism "
      "- clathrin-coated vesicles, GRK2-, EPS15- and dynamin-dependent, beta-arrestin1-"
      "independent - has been worked out separately (PMID:27492965)."),
  supported_by=[("PMID:11359874", "REA01_FRAGMENTS"),
                ("PMID:28137936", "YAN17_INTERNALIZATION"),
                ("PMID:28137936", "YAN17_LVHOMOG"), ("PMID:27492965", "POP16_GRK2"),
                (BIOINF, "BIO_PEPTIDE")],
  prop=dict(root_cause="NO_FAILURE_CORE",
            status={k: "SUPPORTS_TRANSFER" for k in RAT_PAIR + MOUSE_PAIR},
            comments={
                "UniProtKB:Q9R0R3": "Rat Apln, GO:1904022 IDA from PMID:11359874.",
                "ensembl:ENSRNOP00000100018": "Resolves to Q9R0R3; one donor, two identifiers.",
                "UniProtKB:Q9R0R4": ("Mouse Apln, GO:1904022 IDA from PMID:11359874, "
                                     "confirmed on the mouse record via the GO API."),
                "ensembl:ENSMUSP00000046012": "Resolves to Q9R0R4; one donor, two identifiers."},
            residue_na=("Internalisation is driven by the intact peptide; the residue-level "
                        "argument for peptide identity is recorded once, on the GO:0060183 "
                        "IEA row, rather than repeated here.")))

# ---------- GO:1904706 neg. reg. of vascular smooth muscle cell proliferation ----------
D("GO:1904706", "IMP", "PMID:23263626",
  summary=("Conditioned medium from APLN-knockdown endothelial cells makes pulmonary artery "
           "smooth muscle cells proliferate; restoring miR-424/503 in the endothelium, or "
           "knocking down FGF2, abolishes the effect."),
  action="KEEP_AS_NON_CORE",
  reason=(
      "The perturbation is of APLN and the phenotype is a genuine increase in smooth muscle "
      "proliferation, so the annotation is well founded. It is doubly indirect, however: "
      "apelin acts on the endothelial cell, changes miR-424/503 and hence FGF2, and the "
      "smooth muscle cell responds to secreted FGF2 - the paper demonstrates exactly this "
      "chain by abolishing the phenotype with FGF2 knockdown. That places the term well "
      "downstream of anything the gene product does, and confines it to the pulmonary "
      "circulation in a disease model. Non-core."),
  supported_by=[("PMID:23263626", "KIM13_CM"), ("PMID:23263626", "KIM13_FGF2DEP")])

# ---------- GO:1905564 pos. reg. of vascular endothelial cell proliferation ----------
D("GO:1905564", "IDA", "PMID:23263626",
  summary=("Augmenting APLN signalling increases proliferation of control pulmonary artery "
           "endothelial cells - but has the reverse effect in cells from patients with "
           "pulmonary arterial hypertension, and the authors flag the effect as small and "
           "contested."),
  action="KEEP_AS_NON_CORE",
  reason=(
      "The positive direction is observed in the paper and independently: knockdown of "
      "apelin blocks hypoxia-induced endothelial proliferation (PMID:18617693). But the "
      "sign is context-dependent in the very same experiment - augmenting APLN signalling "
      "inhibited proliferation in PAH-derived endothelial cells - and the authors "
      "explicitly discount the literature the term rests on, calling the effects modest at "
      "best and noting that others have refuted them. Their own conclusion is that apelin's "
      "role in mature vessels is to preserve a quiescent, homeostatic endothelium, which is "
      "not a proliferative role. Kept, because the measurement in control cells is real, "
      "but firmly non-core and with the context-dependence recorded rather than smoothed "
      "over."),
  supported_by=[("PMID:23263626", "KIM13_PROLIF"), ("PMID:23263626", "KIM13_REFUTED"),
                ("PMID:23263626", "KIM13_QUIESCENT"), ("PMID:18617693", "EYR08_KD")])

# --------------------------------------------------------------------------------------
# NEW rows
# --------------------------------------------------------------------------------------

NEW_ROWS = [
    dict(
        term={"id": "GO:0007193",
              "label": "adenylate cyclase-inhibiting G protein-coupled receptor signaling pathway"},
        evidence_type="IDA",
        original_reference_id="PMID:22810587",
        summary=("Apelin engaging the human apelin receptor inhibits adenylyl cyclase "
                 "through Gi and lowers intracellular cAMP - the mechanistic identity of "
                 "the apelin receptor signalling pathway, which the record currently "
                 "states only in the ligand-specific term."),
        action="NEW",
        reason=(
            "GO:0060183 says which ligand starts the pathway; it does not say how the "
            "signal is transduced. Every primary description of apelin action reports the "
            "same mechanism - inhibition of adenylyl cyclase and a fall in cAMP through a "
            "pertussis-toxin-sensitive Gi protein - and this is measured directly on the "
            "human receptor: apelin lowers isoproterenol-stimulated cAMP in HEK cells "
            "stably expressing human APJ, an effect PTX inhibits and which is absent in "
            "untransfected controls, and apelin completely inhibits forskolin-stimulated "
            "cAMP in CHO-K1 cells expressing the human apelin receptor. The cryo-EM "
            "structures of APLNR-Gi1 complexes with apelin bound make the coupling "
            "explicit. GO:0007193 is the mechanism-level sibling of GO:0060183 and both "
            "belong on a Gi-coupled receptor's ligand; adding it is what makes the "
            "record say that apelin is an inhibitory-Gi agonist rather than merely that it "
            "has its own named pathway."),
        supported_by=[("PMID:22810587", "SCI12_CAMP"), ("PMID:22810587", "SCI12_PTX"),
                      ("PMID:22810587", "SCI12_GI"), ("PMID:28137936", "YAN17_CAMP"),
                      ("PMID:38428423", "WAN24_CRYOEM")],
    ),
    dict(
        term={"id": "GO:0090278", "label": "negative regulation of peptide hormone secretion"},
        evidence_type="ISS",
        original_reference_id="PMID:15231996",
        supporting_entities=["UniProtKB:Q9R0R3"],
        summary=("Apelin is a diuretic neuropeptide that opposes vasopressin: it inhibits "
                 "vasopressin neuron activity, lowers plasma vasopressin and increases "
                 "diuresis. The human record captures only the drinking half of this "
                 "biology."),
        action="NEW",
        reason=(
            "GO:0042756 drinking behavior is already annotated by ISS from rat, and it "
            "records the intake side of apelin's role in fluid balance. The output side is "
            "at least as well documented and is missing entirely. Apelin is co-localised "
            "with vasopressin in magnocellular supraoptic neurons, inhibits their phasic "
            "electrical activity, reduces plasma vasopressin and increases diuresis in "
            "vivo; water deprivation moves apelin and vasopressin in opposite directions, "
            "which is the signature of a counter-regulatory pair rather than a "
            "pharmacological artefact. The same laboratory's earlier work, which is the "
            "source of the existing drinking-behaviour annotation, already reported "
            "decreased vasopressin release after central apelin injection. Vasopressin is "
            "a peptide hormone, so GO:0090278 applies directly and is more informative "
            "than its broad alternative GO:0050878 regulation of body fluid levels; the "
            "ideal term, negative regulation of vasopressin secretion, does not exist, "
            "although ten sibling peptide hormones have one, and is proposed separately. "
            "Coded ISS rather than IMP because the perturbations are in rat and mouse; the "
            "transfer is unusually safe because rat and human apelin-13 and apelin-17 are "
            "identical residue for residue, so the peptide injected is the human gene "
            "product. Non-core, like the other organismal terms on this gene."),
        supported_by=[("PMID:15231996", "DEM04_DIURETIC"), ("PMID:15231996", "DEM04_DIURESIS"),
                      ("PMID:15231996", "DEM04_WATERDEP"), ("PMID:11359874", "REA01_AVP"),
                      ("PMID:11359874", "REA01_FLUID"), (BIOINF, "BIO_PEPTIDE")],
        prop=dict(root_cause="NO_FAILURE_NON_CORE",
                  status={"UniProtKB:Q9R0R3": "SUPPORTS_TRANSFER"},
                  comments={"UniProtKB:Q9R0R3": (
                      "Rat Apln. The rat and mouse experiments in PMID:15231996 are the "
                      "primary evidence; rat Apln already carries the sibling term "
                      "GO:0042756 as an IMP from the companion study PMID:11359874. Rat and "
                      "human apelin-13/-17 are identical, so sequence similarity is exact "
                      "at the level of the active peptide.")},
                  residue_na=("A physiological counter-regulation of vasopressin; no "
                              "residue-level claim is involved.")),
    ),
]
