"""Build the reviewed APPL2-ai-review.yaml from the seeded file plus a decision table.

The seeded rows come from the deterministic GOA loader. This script never edits a
seeded field: it reads `existing_annotations`, attaches a `review` block to each row
from DECISIONS (keyed by row index and cross-checked against the row's
term/evidence/reference/supporting_entities so the table cannot silently drift), and
derives every `propagation_review.source_entities` list *from the row's own
`supporting_entities`* rather than by hand.

Run from the repo root:  uv run python genes/human/APPL2/APPL2-bioinformatics/build_review.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from ruamel.yaml import YAML

REPO = Path(__file__).resolve().parents[4]
REVIEW = REPO / "genes" / "human" / "APPL2" / "APPL2-ai-review.yaml"

# ---------------------------------------------------------------------------
# Quote bank. Every string here is a verbatim substring of the cited cache file.
# ---------------------------------------------------------------------------
Q: dict[str, tuple[str, str]] = {
    # PMID:15016378 - Miaczynska 2004, Cell (abstract-only cache)
    "rab5_effectors": ("PMID:15016378", "This pathway operates via APPL1 and APPL2, two Rab5\neffectors, which reside on a subpopulation of endosomes."),
    "appl_proliferation": ("PMID:15016378", "Both APPL1 and APPL2 are essential for cell proliferation and their\nfunction requires Rab5 binding."),
    "endosome_intermediate": ("PMID:15016378", "Our findings identify an endosomal compartment\nbearing Rab5 and APPL proteins as an intermediate in signaling between the\nplasma membrane and the nucleus."),
    "nurd": ("PMID:15016378", "APPL1 translocates from the membranes to the nucleus where it\ninteracts with the nucleosome remodeling and histone deacetylase multiprotein\ncomplex NuRD/MeCP1"),
    "rab5_signal": ("PMID:15016378", "We report the identification of a pathway directly linking the small GTPase Rab5, a\nkey regulator of endocytosis, to signal transduction and mitogenesis."),
    # PMID:18034774 - Chial 2008, Traffic (full text)
    "ps_binding": ("PMID:18034774", "APPL isolated PTB domains also bound to membrane-immobilized phosphatidylserine (PS, spot 15)."),
    "pi_binding": ("PMID:18034774", "APPL1 and APPL2 full-length proteins, isolated PH domains and isolated PTB domains all bound to membrane-immobilized PtdIns(3)P, PtdIns(4)P, PtdIns(5)P, PtdIns(3,4)P 2 and PtdIns(3,5)P 2"),
    "bar_dimer": ("PMID:18034774", "the APPL minimal BAR domains were necessary and sufficient for mediating APPL1-APPL1, APPL2-APPL2 and APPL1-APPL2 interactions in the yeast two-hybrid system"),
    "appl2_self_coip": ("PMID:18034774", "APPL2-V5-His specifically coimmunoprecipitated with APPL2-YFP and vice versa"),
    "appl1_appl2_coip": ("PMID:18034774", "APPL2-V5-His specifically coimmunoprecipitated with APPL1-YFP and vice versa"),
    "ph_plasma_membrane": ("PMID:18034774", "We found that APPL1 and APPL2 isolated PH domains localized to the plasma membrane, cytosolic vesicles and distinct nuclear and perinuclear structures"),
    "dynamic_membranes": ("PMID:18034774", "Both APPL1-YFP and APPL2-YFP showed dynamic associations with cytosolic membrane structures that underwent movement, fusion and fission events"),
    "appl2_rab5_colocal": ("PMID:18034774", "APPL2-YFP colocalized strongly with RAB5 to smaller cytosolic vesicular structures"),
    "ps_caveat": ("PMID:18034774", "It is possible that APPL-APPL interactions and/or the overall conformation of the full-length proteins may inhibit PTB domain-mediated PS binding."),
    "appl_nuclear": ("PMID:18034774", "moderate overexpression did not disrupt APPL localization to cytosolic membranes and the nucleus"),
    # PMID:21645192 - Urbanska 2011, Traffic (full text)
    "appl_endosomes": ("PMID:21645192", "APPL endosomes are a recently identified subpopulation of early endosomes\ncharacterized by the presence of two homologous Rab5 effector proteins APPL1 and\nAPPL2."),
    "limited_eea1": ("PMID:21645192", "They exhibit only limited colocalization with EEA1, another Rab5 effector\nand a marker of the canonical early endosomes."),
    "anxa2_solubilize": ("PMID:21645192", "silencing of its\nexpression causes solubilization of APPL2 from endosomes"),
    "anxa2_required": ("PMID:21645192", "Annexin A2 is essential for targeting APPL2 to endosomes and can compensate for Rab5 deficiency in mediating APPL membrane recruitment"),
    "anxa2_interacts": ("PMID:21645192", "identified Annexin A2 as an interacting partner of both APPL1 and APPL2"),
    # PMID:23055524 - King 2012, JBC (full text)
    "rab_screen": ("PMID:23055524", "For APPL2, the yeast two-hybrid screen revealed interactions with Rabs 5, 22a, 24, and 31"),
    "rab31_stoich": ("PMID:23055524", "two Rab31 molecules bind one hAPPL2 BARPH dimer"),
    "rab31_22": ("PMID:23055524", "we conclude the stoichiometry of the complex is 2:2."),
    "xlink_dimer": ("PMID:23055524", "hAPPL2 BARPH is predominantly a dimer in solution"),
    "asu_two_dimers": ("PMID:23055524", "hAPPL2 BARPH crystallized in the P 2 1 2 1 2 1 space group with two dimers in the asymmetric unit."),
    "malls_dimer": ("PMID:23055524", "95.1 kDa ± 2.0% for hAPPL2 BARPH (theoretical mass of 92.1 for dimer)"),
    "not_rab21": ("PMID:23055524", "APPL2 did not bind the APPL1 partners Rab21 and none of the novel APPL2-interacting Rabs were found to interact with APPL1."),
    "ph_residues": ("PMID:23055524", "hAPPL2 BARPH has Lys-289, Arg-287, and Trp-297"),
    "nls_motif": ("PMID:23055524", "a putative nuclear localization sequence has been identified in the APPL2 sequence 151 PKKKENE 157"),
    "bar_crescent": ("PMID:23055524", "Each dimer is crescent-shaped and formed by an anti-parallel arrangement of the helical BAR domains of each hAPPL2 BARPH monomer."),
    "appl2_neg_adipo": ("PMID:23055524", "APPL2 is a negative regulator of adiponectin receptor signaling, whereas APPL1 has been reported to act as a positive regulator of adiponectin action"),
    # PMID:24879834 - Cheng 2014, Diabetes (abstract-only cache)
    "glut4_bidirectional": ("PMID:24879834", "insulin-evoked plasma membrane recruitment of GLUT4 and glucose uptake are impaired by APPL2 overexpression but\nenhanced by APPL2 knockdown."),
    "muscle_ko": ("PMID:24879834", "conditional deletion of APPL2 in skeletal\nmuscles enhances insulin sensitivity, leading to an improvement in glucose\ntolerance."),
    "tbc1d1_mech": ("PMID:24879834", "Insulin stimulates TBC1D1 phosphorylation on\nserine 235, leading to enhanced interaction with the BAR domain of APPL2, which\nin turn suppresses insulin-evoked TBC1D1 phosphorylation on threonine 596 in\ncultured myotubes and skeletal muscle."),
    "tbc1d1_partner": ("PMID:24879834", "We identified the Rab-GTPase-activating protein TBC1D1 as an\ninteracting partner of APPL2."),
    "finetune": ("PMID:24879834", "the APPL2-TBC1D1 interaction is a key step to fine tune\ninsulin-stimulated glucose uptake by regulating the membrane recruitment of\nGLUT4 in skeletal muscle."),
    # PMID:17030088 - Nechamen 2007 (abstract-only cache)
    "akt2_difference": ("PMID:17030088", "APPL1 associates with Akt2, whereas APPL2 does not. This is the first documented \ndifference in function between APPL1 and APPL2."),
    "fshr_appl2": ("PMID:17030088", "This report shows that, in addition to APPL1, \nFSHR interacts with FOXO1a and APPL2."),
    "appl1_appl2_bar": ("PMID:17030088", "APPL1 and APPL2 associate with \none another via the N-terminus of APPL1, presumably via the Bin-Amphiphysin-Rvs \n(BAR) domain."),
    # PMID:19433865 - Rashid 2009, JBC (full text)
    "reptin_direct": ("PMID:19433865", "Both APPL proteins interact directly with Reptin, a\ntranscriptional repressor binding to beta-catenin and HDAC1 (histone deacetylase\n1)"),
    "reptin_complex": ("PMID:19433865", "APPL proteins are present in an endogenous complex containing Reptin,\nbeta-catenin, HDAC1, and HDAC2."),
    "tcf_reporter": ("PMID:19433865", "overexpression of either APPL1 or APPL2 increased the levels of β-catenin-stimulated reporter activity in a dose-dependent manner"),
    "wnt3a_targets": ("PMID:19433865", "in cells treated with Wnt3a-conditioned medium, overexpression of either APPL1 or APPL2 proteins caused higher expression of the Wnt target genes"),
    "reptin_relief": ("PMID:19433865", "this repression was relieved in a dose-dependent manner by adding increasing amounts of APPL1 or APPL2"),
    "hdac_reduced": ("PMID:19433865", "overexpression of either APPL protein clearly reduced the levels of HDAC1 and HDAC2 associated with Reptin"),
    "appl2_undetectable": ("PMID:19433865", "Since APPL2 is practically undetectable in HEK293 cells, we could not test the effects of its knockdown on transcription."),
    "chip_promoters": ("PMID:19433865", "overexpression of either APPL protein caused an increased association of β-catenin with the cyclin D1 and Axin2 promoters with respect to mock-transfected cells"),
    # PMID:26583432 - Song 2016, Oncotarget (full text)
    "tgfb_required": ("PMID:26583432", "the endocytic\nadaptor molecules APPL1 and APPL2 are required for TGFβ-induced nuclear\ntranslocation of TβRI-ICD and for cancer cell invasiveness of human prostate and\nbreast cancer cell lines"),
    "tgfb_appl1_only": ("PMID:26583432", "we identify APPL1 as a TβRI- and PKCζ-associated protein and show that APPL1 and APPL2 are required for the nuclear translocation of TβRI-ICD"),
    "tgfb_nuclear_frac": ("PMID:26583432", "We observed that nuclear accumulation of endogenous TβRI-ICD decreased after siRNA-mediated silencing of APPL1 and APPL2"),
    "nls_untested": ("PMID:26583432", "A possible nuclear localization signal in APPL2 has recently been observed in silico"),
    "appl_nuclear_egf": ("PMID:26583432", "both APPL1 and APPL2 translocate into the nucleus from the cytosol in response to EGF stimulation, to regulate cell proliferation"),
    # PMID:19661063 - Wang 2009, JBC (full text)
    "yin_yang": ("PMID:19661063", "APPL2, an isoform\nof APPL1 that forms a dimer with APPL1, can interacts with both AdipoR1 and\nAdipoR2 and acts as a negative regulator of adiponectin signaling in muscle\ncells."),
    "appl2_rnai": ("PMID:19661063", "suppressing APPL2 expression by RNAi significantly enhances\nadiponectin-stimulated glucose uptake and fatty acid oxidation."),
    "sequestration": ("PMID:19661063", "APPL2\nalso suppresses adiponectin and insulin signaling by sequestrating APPL1 from\nthese two pathways."),
    "appl2_overexp_adipo": ("PMID:19661063", "Overexpression of APPL2 inhibits the interaction between APPL1 and\nAdipoR1, leading to down-regulation of adiponectin signaling in C2C12 myotubes."),
    # PMID:25568335 - Yeo 2015, MBoC (full text)
    "phago_sirna": ("PMID:25568335", "siRNA depletion of either Rab31 or APPL2\nreduces FcγR-mediated phagocytosis."),
    "appl2_ruffles": ("PMID:25568335", "APPL2 was immunolabeled in the cytoplasm, on cell surface ruffles, and on early, actin-rich phagosomes"),
    "rab31_gtp": ("PMID:25568335", "APPL2 showed a preference for binding to GTP-loaded Rab31 compared with its GDP-bound form"),
    "akt_p38": ("PMID:25568335", "APPL2\ndepletion also reduced PI3K/Akt signaling and enhanced p38 signaling from FcγR."),
    "absent_endosomes": ("PMID:25568335", "This contrasts with the predominant and stronger labeling of mCherry-APPL2 on phagosomes and its general absence from endosomes"),
    "cup_closure": ("PMID:25568335", "Mechanistically, this corresponds with a\ndelay in the transition to PI(3,4,5)P3 and phagocytic cup closure."),
    "rab31_direct": ("PMID:25568335", "Using purified APPL2 after cleavage of GST, together with GST-Rab31, we show direct binding of these two proteins."),
    "rab31_recruits": ("PMID:25568335", "During early phagocytosis, we find that Rab31\nrecruits the signaling adaptor APPL2."),
    "first_phagosome": ("PMID:25568335", "This is the first evidence that APPL2 is associated with early phagosomes."),
    "pi3k_unknown": ("PMID:25568335", "It is not known whether these or any other PI3K subunits are recruited or regulated by APPL2, and this remains to be elucidated in future studies."),
    # PMID:25328665 - Mao 2014, Cell Biosci (full text)
    "endotoxin_ko": ("PMID:25328665", "When challenged with\nlipopolysaccharides (LPS), Appl2 KO mice exhibited more severe symptoms of\nendotoxin shock, accompanied by increased production of proinflammatory\ncytokines."),
    "cytokine_up": ("PMID:25328665", "deletion of Appl2 led to\nhigher levels of TNF-α and IL-1β in primary macrophages"),
    "innate_negreg": ("PMID:25328665", "Appl2 is a critical negative regulator of innate immune response via\ninhibition of PI3K/Akt/NF-κB signaling pathway by forming a complex with Appl1\nand PI3K."),
    "akt_enhanced": ("PMID:25328665", "phosphorylation of Akt and its downstream effector NF-κB was significantly\nenhanced."),
    # PMID:27219021 - Yeo 2016, Traffic (abstract-only cache)
    "tlr4_constrain": ("PMID:27219021", "APPL2 has a\ndominant role in nuclear translocation of NF-KB p65 and it serves to constrain\nthe secretion of pro- and anti-inflammatory cytokines."),
    "tlr4_separate": ("PMID:27219021", "By\ndepleting cells of each adaptor respectively we show separate and opposing\nfunctions for APPL1 and 2 in Akt and MAPK signaling."),
    "tlr4_membranes": ("PMID:27219021", "APPL1 and 2\nare differentially localized to distinct signaling-competent membrane domains on\nthe surface and in endocytic compartments of LPS-activated macrophages."),
    # PMID:29467283 - Wang 2018, EMBO Rep (full text)
    "beiging_ko": ("PMID:29467283", "Genetic ablation of APPL2 in RIP-Cre neurons diminishes beiging in sWAT\nwithout affecting BAT, leading to cold intolerance and obesity in mice."),
    "ampk_axis": ("PMID:29467283", "Hypothalamic APPL2 enhances neuronal activation in VMH RIP-Cre neurons and raphe\npallidus, thereby eliciting SNS outflow to sWAT and subsequent beiging."),
    # PMID:26445298 - Tan 2016, J Cell Physiol (full text)
    "hgf_single_ko": ("PMID:26445298", "Appl1 KO, Appl2 KO, and especially Appl1/2 DKO MEFs showed consistently decreased Akt activation upon stimulation with HGF"),
    "hgf_migration": ("PMID:26445298", "Appl1/2-null mouse embryonic fibroblasts\nexhibited defects in HGF-induced Akt activation, migration, and invasion."),
    "appl_expendable": ("PMID:26445298", "ubiquitous Appl2 knockout (Appl2-/-) mice, much like Appl1-/- mice,\nare viable and grow normally to adulthood"),
    # PMID:28965332 / PMID:32468397 - neurogenesis (abstract-only / full text)
    "neuro_tg": ("PMID:28965332", "APPL2 Tg mice had decreased\nhippocampal neurogenesis that was reversed by GR antagonist RU486."),
    "neuro_gr": ("PMID:28965332", "APPL2 overexpression could blunt the activation of\nglucocorticoid receptor when undergoing environmental stress."),
    "nsc_switch": ("PMID:32468397", "APPL2 overexpression resulted in NSCs switching from neuronal differentiation to gliogenesis while APPL2 knockdown promoted neurogenesis."),
    "nsc_invivo": ("PMID:32468397", "APPL2 Tg mice had a higher population of glial cells and dampened neuronal production in the olfactory system"),
    # PMID:19056867 - urinary exosome proteomics
    "exosome_lcms": ("PMID:19056867", "we used LC-MS/MS to profile the proteome of human urinary exosomes"),
    "exosome_1132": ("PMID:19056867", "the\nanalysis identified 1132 proteins unambiguously"),
    # high-throughput interaction screens
    "ht_rual": ("PMID:16189514", "Using a stringent, high-throughput \nyeast two-hybrid system, we tested pairwise interactions"),
    "ht_lgmd": ("PMID:23414517", "We undertook a large-scale study using two-hybrid screens and a human \nskeletal-muscle cDNA library to establish a proteome-scale map of \nprotein-protein interactions centered on proteins involved in limb-girdle \nmuscular dystrophies (LGMD)."),
    "ht_y2hseq": ("PMID:23455924", "we developed a yeast two-hybrid \ninteraction screening approach involving short-read second-generation sequencing \n(Y2H-seq) with improved sensitivity and a quantitative scoring readout allowing \nrapid interaction validation"),
    "ht_rolland": ("PMID:25416956", "Here, we describe a systematic map of ?14,000 high-quality human \nbinary protein-protein interactions."),
    "ht_py": ("PMID:25814554", "We extended an established yeast two-hybrid system \nemploying human protein kinases for the analyses of phospho-tyrosine \n(pY)-dependent PPIs in a direct experimental, large-scale approach."),
    "ht_bioplex2": ("PMID:28514442", "Here we present BioPlex 2.0 \n(Biophysical Interactions of ORFeome-derived complexes), which uses robust \naffinity purification-mass spectrometry methodology to elucidate protein \ninteraction networks and co-complexes nucleated by more than"),
    "ht_variants": ("PMID:31515488", "Each human genome carries tens of thousands of coding variants."),
    "ht_huri": ("PMID:32296183", "Here we present a human 'all-by-all' \nreference interactome map of human binary protein interactions, or 'HuRI'."),
    "ht_bioplex3": ("PMID:33961781", "Through affinity-purification \nmass spectrometry, we have created two proteome-scale, cell-line-specific \ninteraction networks."),
    "ht_opencell": ("PMID:35271311", "We combined genome engineering, confocal live-cell imaging, \nmass spectrometry, and data science to systematically map the localization and \ninteractions of human proteins."),
    # local files
    "bioinf_identity": ("file:human/APPL2/APPL2-bioinformatics/RESULTS.md", "Human and mouse APPL2 are 92.7% identical over a full-length global alignment"),
    "bioinf_paralog": ("file:human/APPL2/APPL2-bioinformatics/RESULTS.md", "The paralog identity, 53.9%, reproduces the 52% that King et al. report by ClustalW"),
    "bioinf_residues": ("file:human/APPL2/APPL2-bioinformatics/RESULTS.md", "The patch is intact in human APPL2 and conserved in mouse Appl2"),
    "bioinf_nls": ("file:human/APPL2/APPL2-bioinformatics/RESULTS.md", "also present verbatim, sits inside the BAR domain (loop 2), and is conserved in\nmouse Appl2"),
    "uniprot_subunit": ("file:human/APPL2/APPL2-uniprot.txt", "CC   -!- SUBUNIT: Homodimer (PubMed:18034774, PubMed:23055524). Homotetramer"),
    "uniprot_nurd": ("file:human/APPL2/APPL2-uniprot.txt", "CC       subunits of the NuRD/MeCP1 complex (PubMed:15016378). Interacts with"),
    "uniprot_absent_macrophage": ("file:human/APPL2/APPL2-uniprot.txt", "CC       (PubMed:18034774). Absent of endosome in macrophage. Colocalized with RAB31"),
    "uniprot_domains": ("file:human/APPL2/APPL2-uniprot.txt", "CC   -!- DOMAIN: The BAR domain is necessary and sufficient for mediating homotypic"),
}


def sup(*names: str) -> list[dict]:
    out = []
    for n in names:
        ref, text = Q[n]
        out.append({"reference_id": ref, "supporting_text": text})
    return out


# ---------------------------------------------------------------------------
# Per-entity boilerplate used to build source_entities from supporting_entities.
# ---------------------------------------------------------------------------
MOUSE_NOTE = (
    "Mouse Appl2, the 1:1 ortholog of the target and the only gene-level donor on this "
    "row; human and mouse APPL2 are 92.7% identical over a full-length global alignment "
    "(APPL2-bioinformatics/RESULTS.md), so the transfer itself is safe."
)
ENSEMBL_NOTE = (
    "Ensembl protein accession for the same mouse Appl2 entry (it resolves to "
    "UniProtKB:Q8K3G9), so this row carries one donor under two identifiers, not two "
    "independent donors."
)
SUBCELL = {
    "UniProtKB-SubCell:SL-0300": "Ruffle",
    "UniProtKB-SubCell:SL-0301": "Ruffle membrane",
    "UniProtKB-SubCell:SL-0191": "Nucleus",
    "UniProtKB-SubCell:SL-0086": "Cytoplasm",
    "UniProtKB-SubCell:SL-0039": "Cell membrane",
    "UniProtKB-SubCell:SL-0100": "Endosome membrane",
    "UniProtKB-SubCell:SL-0093": "Early endosome membrane",
    "UniProtKB-SubCell:SL-0205": "Phagosome membrane",
    "UniProtKB-SubCell:SL-0206": "Phagosome",
}
ARBA_NOTE = {
    "ARBA:ARBA00089669": "ARBA rule for phosphatidylserine binding; 5 condition sets over FunFam signatures in primates and fungi. Narrow, and it reproduces a conclusion the IDA row already carries.",
    "ARBA:ARBA00028627": "ARBA rule for protein import into nucleus; 14 condition sets over FunFam/InterPro signatures in metazoa and fungi. Narrow, and it reproduces the IDA row's claim.",
    "ARBA:ARBA00085361": "ARBA rule for TGF-beta receptor signalling; 14 condition sets, metazoan. Narrow, and it reproduces the IMP row's claim.",
    "ARBA:ARBA00027526": "ARBA rule for homeostatic process; 135 condition sets spanning bacteria, plants, fungi and metazoa. A rule this broad attached to a term this general carries no information about APPL2.",
    "ARBA:ARBA00033889": "ARBA rule for regulation of the G1/S transition; 7 condition sets over primates, rodents and yeast. Narrow, and it reproduces the IDA row's claim.",
    "ARBA:ARBA00028568": "ARBA rule for endosome; 97 condition sets across eukaryotes. Broad, but the compartment is independently established for APPL2 by IDA.",
    "ARBA:ARBA00026540": "ARBA rule for cytoplasmic vesicle membrane; 72 condition sets across eukaryotes. Broad, and the term is a generic parent of the compartments APPL2 is actually on.",
    "ARBA:ARBA00027281": "ARBA rule for bounding membrane of organelle; 171 condition sets spanning bacteria to plants. Too broad and too generic to say anything about APPL2.",
    "ARBA:ARBA00026346": "ARBA rule for phosphatidylinositol binding; 7 condition sets across eukaryotes. Narrow, and it reproduces the IDA row's claim.",
    "ARBA:ARBA00027801": "ARBA rule for plasma membrane; 686 condition sets spanning bacteria, plants, fungi and metazoa. This is the most promiscuous rule on the gene and it is what drives the plasma-membrane call.",
    "ARBA:ARBA00093152": "ARBA rule for negative regulation of D-glucose import; only 4 condition sets. Narrow, and it agrees with the IMP row.",
}
IBA_NODE_LABEL = (
    "PTHR46415 Bilateria (taxon 33213) IBD node ancestral to both APPL1 (subfamily SF3) "
    "and APPL2 (SF1)"
)


def source_entity(eid: str, row_note: str, status: str = "SUPPORTS_TRANSFER",
                  overrides: dict[str, tuple[str, str, str]] | None = None) -> dict:
    """Build one source_entities entry for `eid`, given the row-specific note."""
    if overrides and eid in overrides:
        label, st, comment = overrides[eid]
        entry = {"source_id": eid}
        if label:
            entry["source_label"] = label
        entry["source_status"] = st
        entry["comment"] = comment
        return entry
    if eid == "UniProtKB:Q8K3G9":
        return {"source_id": eid, "source_label": "Appl2 (Mus musculus)",
                "source_status": status, "comment": f"{MOUSE_NOTE} {row_note}"}
    if eid == "ensembl:ENSMUSP00000020500":
        return {"source_id": eid, "source_label": "Appl2 (Mus musculus), Ensembl protein",
                "source_status": status, "comment": ENSEMBL_NOTE}
    if eid in SUBCELL:
        return {"source_id": eid, "source_label": f"UniProt subcellular-location keyword: {SUBCELL[eid]}",
                "source_status": status,
                "comment": ("Projection of UniProt's own curated subcellular-location keyword, so "
                            "this row re-states the Swiss-Prot annotation rather than adding "
                            f"independent evidence. {row_note}")}
    if eid in ARBA_NOTE:
        return {"source_id": eid, "source_label": f"ARBA rule {eid.split(':')[1]}",
                "source_status": status, "comment": ARBA_NOTE[eid]}
    if eid == "InterPro:IPR004148":
        return {"source_id": eid, "source_label": "InterPro BAR domain signature (IPR004148)",
                "source_status": status,
                "comment": ("A domain-presence signature. APPL2 does carry a BAR domain "
                            "(UniProt FT DOMAIN 3..268), but domain presence is not evidence "
                            "about where the protein is.")}
    raise KeyError(f"no boilerplate for source entity {eid!r}")


# ---------------------------------------------------------------------------
# Decision table. Key = seeded row index; `k` = (term, evidence, reference) guard.
# `prop` = (root_cause, failure_modes, row_note[, overrides]) for propagation_review.
# ---------------------------------------------------------------------------
MOUSE_ISS_REASON = (
    "The donor is mouse Appl2 (Q8K3G9), a 1:1 ortholog 92.7% identical to the human "
    "protein, so the orthology transfer carries no ortholog-assignment risk."
)

D: dict[int, dict] = {}


def add(idx, key, action, summary, reason, supported, prop=None, repl=None):
    D[idx] = {"k": key, "action": action, "summary": summary, "reason": reason,
              "supported": supported, "prop": prop, "repl": repl}


# ---- ruffle / ruffle membrane (mouse macrophage evidence) -----------------
for idx, key, term in [
    (0, ("GO:0001726", "IEA", "GO_REF:0000120"), "ruffle"),
    (1, ("GO:0001726", "ISS", "GO_REF:0000024"), "ruffle"),
    (76, ("GO:0032587", "IEA", "GO_REF:0000120"), "ruffle membrane"),
    (77, ("GO:0032587", "ISS", "GO_REF:0000024"), "ruffle membrane"),
]:
    add(idx, key, "KEEP_AS_NON_CORE",
        f"APPL2 is on cell-surface ruffles in macrophages; the {term} call is transferred from mouse Appl2.",
        ("Endogenous and GFP-tagged APPL2 were immunolabelled on cell-surface ruffles in mouse primary "
         "macrophages and RAW264.7 cells (PMID:25568335), which is the observation behind the mouse "
         f"annotation. {MOUSE_ISS_REASON} It is kept as non-core because it is a macrophage-specific "
         "membrane domain seen during phagocytosis, not where APPL2 sits in the cell types where its "
         "signalling functions were characterised."),
        sup("appl2_ruffles", "bioinf_identity"),
        prop=("NO_FAILURE_NON_CORE", None,
              "The mouse observation is immunofluorescence of endogenous and tagged APPL2 on macrophage "
              "surface ruffles (PMID:25568335); it transfers, but only as a cell-type-specific location."))

# ---- phosphatidylserine binding ------------------------------------------
add(2, ("GO:0001786", "IDA", "PMID:18034774"), "KEEP_AS_NON_CORE",
    "Phosphatidylserine binding was seen only for the isolated PTB domain on a lipid strip, not for full-length APPL2.",
    ("On PIP Strips the isolated APPL PTB domains bound phosphatidylserine, but the full-length proteins "
     "did not, and the authors explicitly flag the discrepancy. This is a real property of the domain in "
     "vitro and it is consistent with the PTB domain's role in membrane targeting, but it has not been "
     "shown for the intact protein and no cellular consequence has been attached to it. Kept, not "
     "removed, and marked non-core: the phosphoinositide binding of the full-length protein "
     "(GO:0035091) is the better-supported lipid-binding claim."),
    sup("ps_binding", "ps_caveat"))

add(3, ("GO:0001786", "IEA", "GO_REF:0000117"), "KEEP_AS_NON_CORE",
    "ARBA rule reproducing the isolated-domain phosphatidylserine-binding result.",
    ("ARBA00089669 is a narrow rule (5 condition sets over FunFam signatures in primates and fungi) that "
     "assigns the same term the IDA row carries. It adds no evidence beyond the IDA, and inherits the "
     "same caveat: the binding was demonstrated for the isolated PTB domain, not full-length APPL2."),
    sup("ps_binding"),
    prop=("NO_FAILURE_NON_CORE", None, ""))

# ---- thermogenesis (mouse VMH neurons) ------------------------------------
for idx, key, term in [
    (4, ("GO:0002024", "IEA", "GO_REF:0000107"), "diet induced thermogenesis"),
    (5, ("GO:0002024", "ISS", "GO_REF:0000024"), "diet induced thermogenesis"),
    (58, ("GO:0009631", "IEA", "GO_REF:0000107"), "cold acclimation"),
    (59, ("GO:0009631", "ISS", "GO_REF:0000024"), "cold acclimation"),
    (110, ("GO:0120162", "IEA", "GO_REF:0000107"), "positive regulation of cold-induced thermogenesis"),
    (111, ("GO:0120162", "ISS", "GO_REF:0000024"), "positive regulation of cold-induced thermogenesis"),
]:
    add(idx, key, "KEEP_AS_NON_CORE",
        f"{term} rests on a neuron-restricted Appl2 knockout in mouse hypothalamus.",
        ("Deleting APPL2 in ventromedial-hypothalamic RIP-Cre neurons reduced beiging of subcutaneous "
         "white adipose tissue and produced cold intolerance and obesity, acting through AMPK and "
         f"sympathetic outflow (PMID:29467283). The perturbation is APPL2-specific and conditional. "
         f"{MOUSE_ISS_REASON} This is nonetheless an organism-level physiological outcome of APPL2 "
         "acting in one neuronal population, several steps removed from what the protein does "
         "molecularly, so it is peripheral rather than core."),
        sup("beiging_ko", "ampk_axis"),
        prop=("NO_FAILURE_NON_CORE", None,
              "The mouse evidence is a conditional, neuron-restricted APPL2 knockout with a whole-animal "
              "thermogenic phenotype (PMID:29467283) - APPL2-specific, but organismal."))

# ---- GO:0005515 protein binding: Rab partners -> small GTPase binding -----
RAB_NAMES = {"UniProtKB:P20339": "RAB5A", "UniProtKB:P51148": "RAB5C",
             "UniProtKB:Q9UL26": "RAB22A", "UniProtKB:Q13636": "RAB31"}
RAB_ROWS = [
    (6, "PMID:15016378", "UniProtKB:P20339", ("rab5_effectors", "appl_proliferation")),
    (9, "PMID:16189514", "UniProtKB:Q9UL26", ("rab_screen", "ht_rual")),
    (16, "PMID:23055524", "UniProtKB:Q13636", ("rab31_direct", "rab31_stoich")),
    (22, "PMID:25416956", "UniProtKB:P51148", ("rab_screen", "ht_rolland")),
    (26, "PMID:25416956", "UniProtKB:Q9UL26", ("rab_screen", "ht_rolland")),
    (29, "PMID:31515488", "UniProtKB:P51148", ("rab_screen", "ht_variants")),
    (33, "PMID:31515488", "UniProtKB:Q9UL26", ("rab_screen", "ht_variants")),
    (35, "PMID:32296183", "UniProtKB:P51148", ("rab_screen", "ht_huri")),
    (40, "PMID:32296183", "UniProtKB:Q9UL26", ("rab_screen", "ht_huri")),
]
for idx, ref, partner, quotes in RAB_ROWS:
    name = RAB_NAMES[partner]
    add(idx, ("GO:0005515", "IPI", ref), "MODIFY",
        f"Bare protein binding for a Rab GTPase partner ({name}); the informative term is small GTPase binding.",
        ("APPL2 is a Rab effector: it binds GTP-loaded Rab5, Rab22A, Rab24 and Rab31 in a screen against "
         "46 Rabs, binds purified Rab31 directly with a preference for the GTP form, and the APPL2 "
         "BAR-PH dimer binds two Rab31 molecules. 'Protein binding' says none of this. GO:0031267 small "
         "GTPase binding is the current term for it - the former GO:0017137 'Rab GTPase binding' is "
         "listed among GO:0031267's secondary ids, i.e. it was merged into small GTPase binding rather "
         "than obsoleted, so GO:0031267 is the id to use."),
        sup(*quotes),
        repl=[{"id": "GO:0031267", "label": "small GTPase binding"}])

# ---- GO:0005515: APPL1 partner -> heterodimerization ----------------------
# The third element, when present, is an extra sentence appended to the shared reason.
AP_MS_NOTE = (
    " One caveat specific to this row: its own reference is an affinity-purification "
    "mass-spectrometry screen, which establishes co-complex membership rather than a 1:1 "
    "dimer. The stoichiometry that justifies GO:0046982 comes from PMID:18034774 - yeast "
    "two-hybrid with the minimal BAR domains plus reciprocal coimmunoprecipitation - not from "
    "the AP-MS experiment itself. The re-term is still the right call here, because the partner "
    "is identified and the nature of the APPL1-APPL2 interaction is independently established; "
    "that is what distinguishes this row from the other partners in the same screens, which have "
    "no such follow-up and are marked over-annotated."
)
APPL1_ROWS = {
    7: ("PMID:15016378", ("bar_dimer", "appl1_appl2_coip", "rab5_effectors")),
    8: ("PMID:16189514", ("bar_dimer", "ht_rual")),
    11: ("PMID:17030088", ("appl1_appl2_bar", "akt2_difference")),
    12: ("PMID:18034774", ("bar_dimer", "appl1_appl2_coip")),
    17: ("PMID:23414517", ("bar_dimer", "ht_lgmd")),
    21: ("PMID:24879834", ("tbc1d1_partner", "bar_dimer")),
    25: ("PMID:25416956", ("bar_dimer", "ht_rolland")),
    28: ("PMID:28514442", ("bar_dimer", "ht_bioplex2"), AP_MS_NOTE),
    32: ("PMID:31515488", ("bar_dimer", "ht_variants")),
    39: ("PMID:32296183", ("bar_dimer", "ht_huri")),
    41: ("PMID:33961781", ("bar_dimer", "ht_bioplex3"), AP_MS_NOTE),
    42: ("PMID:35271311", ("bar_dimer", "ht_opencell"), AP_MS_NOTE),
}
for idx, spec in APPL1_ROWS.items():
    ref, quotes = spec[0], spec[1]
    extra = spec[2] if len(spec) > 2 else ""
    add(idx, ("GO:0005515", "IPI", ref), "MODIFY",
        "Bare protein binding for the APPL1 partner; the interaction is a defined BAR-domain heterodimer.",
        ("APPL1 is by far the most frequently reported APPL2 partner in this GOA record, and the "
         "interaction is not a generic one: the minimal BAR domains are necessary and sufficient for "
         "APPL1-APPL2 heterodimerisation in yeast two-hybrid and the proteins reciprocally "
         "coimmunoprecipitate. GO:0046982 protein heterodimerization activity states that, where "
         "'protein binding' does not. The heterodimer is also the mechanistic substrate of the "
         "adiponectin antagonism, in which APPL2 sequesters APPL1." + extra),
        sup(*quotes),
        repl=[{"id": "GO:0046982", "label": "protein heterodimerization activity"}])

# ---- GO:0005515: mechanistically characterised non-Rab partners -----------
add(10, ("GO:0005515", "IPI", "PMID:17030088"), "KEEP_AS_NON_CORE",
    "Interaction with the FSH receptor, reported alongside APPL1 in a receptor-proximal complex.",
    ("FSHR was shown to interact with APPL2 as well as APPL1, independently of FSH stimulation, in a "
     "putative FSHR signalling complex. The same paper reports the one clean functional distinction "
     "between the paralogs - APPL1 binds Akt2 and APPL2 does not - which is why this reference matters "
     "beyond the interaction itself. No APPL2-specific functional consequence of the FSHR interaction "
     "has been established, and GO has no more informative molecular-function term for it, so the row is "
     "kept as a peripheral protein-binding record rather than re-termed."),
    sup("fshr_appl2", "akt2_difference"))

add(13, ("GO:0005515", "IPI", "PMID:19433865"),
    "KEEP_AS_NON_CORE",
    "Membership of an endogenous Reptin/beta-catenin/HDAC1/HDAC2 complex together with APPL1.",
    ("This row's WITH/FROM is the set CTNNB1, HDAC1, HDAC2 and APPL1 - it records co-membership of a "
     "nuclear repressive complex rather than a pairwise interaction. The complex is endogenous and the "
     "functional consequence is real: overexpressing APPL2 reduces the HDAC1/HDAC2 and beta-catenin "
     "associated with Reptin. It is non-core because the APPL2 evidence in this paper is entirely "
     "overexpression-based - APPL2 is practically undetectable in the HEK293 cells used, so no "
     "loss-of-function control was possible."),
    sup("reptin_complex", "hdac_reduced", "appl2_undetectable"))

add(14, ("GO:0005515", "IPI", "PMID:19433865"), "KEEP_AS_NON_CORE",
    "Direct interaction with RUVBL2/Reptin, the mechanistic basis of APPL2's effect on beta-catenin/TCF transcription.",
    ("Both APPL proteins bind Reptin directly, shown by in vitro binding of purified recombinant "
     "proteins as well as coimmunoprecipitation and GST pull-down, and the interaction relieves "
     "Reptin-mediated repression of beta-catenin/TCF transcription. This is one of the few APPL2 "
     "protein-binding rows with a mapped downstream consequence. It stays as protein binding because GO "
     "offers no molecular-function term for 'binds a transcriptional corepressor and displaces its "
     "partners'; the functional content is captured instead by the NEW GO:0090263 row."),
    sup("reptin_direct", "reptin_relief", "chip_promoters"))

add(15, ("GO:0005515", "IPI", "PMID:21645192"), "KEEP_AS_NON_CORE",
    "Interaction with annexin A2, which is required to keep APPL2 on endosomal membranes.",
    ("Annexin A2 was identified as an APPL1 and APPL2 partner by in vivo biotinylation and confirmed by "
     "GST pull-down, and silencing it solubilises APPL2 from endosomes and can substitute for Rab5 in "
     "recruiting APPL proteins to membranes. The interaction is therefore functionally consequential - "
     "it is part of how APPL2 gets to the compartment - but the annotation itself is a binding record, "
     "and the compartment claim is carried by the GO:0005768 and GO:0010008 rows from the same paper."),
    sup("anxa2_interacts", "anxa2_solubilize", "anxa2_required"))

for idx, ref, note in [(19, "PMID:24879834", "mouse Tbc1d1 (Q60949)"), (20, "PMID:24879834", "human TBC1D1 (Q86TI0)")]:
    add(idx, ("GO:0005515", "IPI", ref), "KEEP_AS_NON_CORE",
        f"Phospho-dependent interaction with {note}, the mechanism behind APPL2's inhibition of insulin-stimulated glucose uptake.",
        ("TBC1D1 was identified as an APPL2 partner and the interaction was mapped: insulin-driven "
         "phosphorylation of TBC1D1 Ser-235 enhances binding to the APPL2 BAR domain, and that binding "
         "suppresses TBC1D1 Thr-596 phosphorylation, blocking GLUT4 translocation. This is the "
         "best-characterised APPL2 interaction of all. It is kept rather than re-termed because the "
         "functional content is already carried, at the right level, by the GO:0046325 IMP and "
         "GO:0042593 IMP rows; 'protein binding' here is the interaction record underneath them."),
        sup("tbc1d1_partner", "tbc1d1_mech", "finetune"))

# ---- GO:0005515: high-throughput-only partners ---------------------------
HT_ROWS = {
    18: ("PMID:23455924", "SUV39H2", "ht_y2hseq"),
    23: ("PMID:25416956", "CRADD", "ht_rolland"),
    24: ("PMID:25416956", "SUV39H2", "ht_rolland"),
    27: ("PMID:25814554", "MAPRE3", "ht_py"),
    30: ("PMID:31515488", "CRADD", "ht_variants"),
    31: ("PMID:31515488", "SUV39H2", "ht_variants"),
    34: ("PMID:32296183", "PRR35", "ht_huri"),
    36: ("PMID:32296183", "EPM2AIP1", "ht_huri"),
    37: ("PMID:32296183", "KIFC3 (isoform 5)", "ht_huri"),
    38: ("PMID:32296183", "SUV39H2 (isoform 2)", "ht_huri"),
}
for idx, (ref, partner, quote) in HT_ROWS.items():
    add(idx, ("GO:0005515", "IPI", ref), "MARK_AS_OVER_ANNOTATED",
        f"Systematic-screen interaction with {partner}, with no functional follow-up for APPL2.",
        (f"This row comes from a proteome-scale screen. The {partner} interaction has never been "
         "followed up for APPL2: there is no localisation, no mapped binding surface, no perturbation "
         "and no pathway placement connecting it to anything APPL2 is known to do. Bare GO:0005515 rows "
         "of this kind are reproducible observations rather than statements about function, and marking "
         "them over-annotated is the accurate call - it does not dispute that the screen detected the "
         "pair. Note also that IntAct's experiment counts for APPL2 pool replicate experiments from the "
         "same studies and are not counts of independent publications."),
        sup(quote))

# ---- GO:0005634 nucleus ---------------------------------------------------
add(43, ("GO:0005634", "IDA", "PMID:15016378"), "ACCEPT",
    "APPL2 shuttles from endosomal membranes to the nucleus.",
    ("The paper that defined APPL endosomes also established the nuclear pool of APPL proteins and the "
     "stimulus-dependent translocation that links the two, and UniProt records Nucleus for Q8NEU8 with "
     "experimental evidence from this paper. A nuclear APPL2 pool is corroborated independently: both "
     "APPL1 and APPL2 translocate to the nucleus on EGF stimulation, APPL2 carries a BAR-loop basic "
     "motif absent from APPL1, and the Reptin/HDAC work places APPL2 in a nuclear complex."),
    sup("nurd", "endosome_intermediate", "appl_nuclear_egf"))

add(44, ("GO:0005634", "IDA", "PMID:18034774"), "ACCEPT",
    "Imaging of APPL2 fusion proteins shows a nuclear pool alongside the membrane pool.",
    ("Coexpressed full-length APPL fusion proteins localised to cytosolic membranes and the nucleus, "
     "and the isolated PH domains reached distinct nuclear and perinuclear structures. This is "
     "tagged-protein imaging rather than endogenous staining, so it is weaker than the compartment rows, "
     "but the nuclear pool is independently supported by the Rab5/NuRD and Reptin literature and by the "
     "APPL2-specific basic motif at 151-157, so the annotation stands."),
    sup("appl_nuclear", "ph_plasma_membrane", "bioinf_nls"))

add(45, ("GO:0005634", "IEA", "GO_REF:0000044"), "ACCEPT",
    "Projection of UniProt's curated Nucleus location keyword.",
    ("This row restates UniProt's own Nucleus annotation for Q8NEU8, which is itself supported by two "
     "experimental papers. It is redundant with the two IDA rows rather than independent of them, but it "
     "is correct."),
    sup("nurd", "appl_nuclear"),
    prop=("NO_FAILURE_CORE", None, ""))

# ---- GO:0005737 cytoplasm -------------------------------------------------
for idx, key in [(46, ("GO:0005737", "IEA", "GO_REF:0000120")), (47, ("GO:0005737", "ISS", "GO_REF:0000024"))]:
    add(idx, key, "KEEP_AS_NON_CORE",
        "A cytosolic pool exists, but 'cytoplasm' is too general to be informative for a peripheral membrane adaptor.",
        ("APPL2 is a peripheral membrane protein with a genuine soluble pool - it was immunolabelled in "
         "the cytoplasm of macrophages, and annexin A2 knockdown solubilises it from endosomes, which "
         "only makes sense if a cytosolic pool exists. So the term is not wrong. It is non-core because "
         "the informative statements about where APPL2 acts are the endosome, early-endosome-membrane "
         "and phagosome rows; 'cytoplasm' is their uninformative parent. "
         f"{MOUSE_ISS_REASON}"),
        sup("appl2_ruffles", "anxa2_solubilize"),
        prop=("NO_FAILURE_NON_CORE", None,
              "The mouse annotation reflects cytoplasmic immunolabelling of endogenous APPL2 in "
              "macrophages (PMID:25568335). True, but generic."))

# ---- GO:0005768 endosome --------------------------------------------------
add(48, ("GO:0005768", "IDA", "PMID:21645192"), "ACCEPT",
    "Endogenous APPL2 marks a biochemically distinct subpopulation of early endosomes.",
    ("APPL endosomes were characterised here by membrane fractionation and by imaging of endogenous "
     "APPL2 in human fibroblasts, and they behave as a discriminable compartment: a distinct migration "
     "pattern in continuous density gradients and only limited colocalisation with EEA1. This is core - "
     "membrane recruitment through Rab and annexin A2 binding is what APPL2 is for. GO has no 'APPL "
     "endosome' term, which is recorded under proposed_new_terms; GO:0005768 and the more specific "
     "GO:0031901 are the available and correct approximations."),
    sup("appl_endosomes", "limited_eea1", "anxa2_required"))

add(49, ("GO:0005768", "IEA", "GO_REF:0000117"), "ACCEPT",
    "ARBA rule reaching the same compartment the IDA row establishes.",
    ("ARBA00028568 is a broad rule (97 condition sets across eukaryotes), so on its own it would be weak "
     "evidence; here it happens to agree with a well-supported IDA row from endogenous-protein "
     "fractionation and imaging, so the annotation is correct even though the rule is not what "
     "establishes it."),
    sup("appl_endosomes"),
    prop=("NO_FAILURE_CORE", None, ""))

# ---- GO:0005886 plasma membrane -------------------------------------------
add(50, ("GO:0005886", "IDA", "PMID:18034774"), "KEEP_AS_NON_CORE",
    "The plasma-membrane signal comes from overexpressed isolated PH domains, not the intact protein.",
    ("The plasma-membrane observation in this paper is of isolated APPL PH domains expressed as CFP "
     "fusions; the full-length APPL2 fusion protein localised to cytosolic membrane structures, not the "
     "plasma membrane. An ectopically expressed fragment reaching the plasma membrane is a statement "
     "about the domain's lipid affinity rather than about where APPL2 resides. There is a defensible "
     "membrane-proximal pool - APPL endosomes accumulate beneath the plasma membrane and APPL2 is on "
     "surface ruffles in macrophages - so the term is kept, but as non-core."),
    sup("ph_plasma_membrane", "dynamic_membranes", "appl2_ruffles"))

add(51, ("GO:0005886", "IEA", "GO_REF:0000120"), "KEEP_AS_NON_CORE",
    "Driven by the most promiscuous ARBA rule on the gene, combined with a mouse keyword projection.",
    ("This row combines ARBA00027801 with the mouse ortholog and a Cell membrane keyword. ARBA00027801 "
     "has 686 condition sets spanning bacteria, plants, fungi and metazoa - a rule that broad firing on "
     "APPL2 conveys no information about APPL2, so none of this row's confidence should come from the "
     "rule. The term is nonetheless true: APPL2 sits on surface ruffles and phagocytic cups in "
     "macrophages, APPL endosomes accumulate beneath the plasma membrane, and UniProt records Cell "
     "membrane for Q8NEU8 with experimental evidence. Kept as non-core, consistent with the IDA and ISS "
     "rows for the same term, because ruffle, ruffle membrane and early phagosome state the same "
     "localisation far more precisely."),
    sup("appl2_ruffles", "absent_endosomes"),
    prop=("NO_FAILURE_NON_CORE", None,
          "The mouse donor's plasma-membrane association is really the ruffle and phagocytic-cup pool, "
          "which the ruffle, ruffle-membrane and early-phagosome rows already state more precisely."))

add(52, ("GO:0005886", "ISS", "GO_REF:0000024"), "KEEP_AS_NON_CORE",
    "Orthology transfer of the mouse Cell membrane location.",
    ("Mouse Appl2 is annotated to the cell membrane on the strength of its ruffle and phagocytic-cup "
     f"localisation in macrophages (PMID:25568335). {MOUSE_ISS_REASON} The transfer is sound, but the "
     "term is a generic parent of the ruffle and ruffle-membrane rows that carry the same observation "
     "more precisely."),
    sup("appl2_ruffles"),
    prop=("NO_FAILURE_NON_CORE", None,
          "The mouse cell-membrane call reflects ruffle and phagocytic-cup localisation in macrophages "
          "(PMID:25568335), already stated more precisely by the ruffle rows."))

# ---- GO:0006606 protein import into nucleus -------------------------------
add(53, ("GO:0006606", "IDA", "PMID:26583432"), "KEEP_AS_NON_CORE",
    "APPL proteins are required for nuclear delivery of the TGF-beta receptor intracellular domain - but only a double knockdown was done.",
    ("Silencing APPL1 and APPL2 abolished nuclear accumulation of endogenous and tagged TbetaRI-ICD "
     "after TGF-beta stimulation, so the gene product is genuinely required for this import event and "
     "the annotation is not wrong. Every functional experiment in the paper, however, silences both "
     "adaptors simultaneously, and the physical association with TbetaRI and PKCzeta was mapped to "
     "APPL1 alone - so APPL2's individual contribution is unresolved. Given 54% paralog identity, a "
     "double knockdown cannot be read as evidence about either gene singly. Kept as a real but "
     "peripheral role rather than removed, since curators reading the full text had the same design "
     "available to them and the requirement itself is not in doubt. Note the cargo imported is "
     "TbetaRI-ICD, not APPL2."),
    sup("tgfb_required", "tgfb_appl1_only", "tgfb_nuclear_frac", "bioinf_paralog"))

add(54, ("GO:0006606", "IEA", "GO_REF:0000117"), "KEEP_AS_NON_CORE",
    "Narrow ARBA rule reproducing the same claim as the IDA row.",
    ("ARBA00028627 has 14 condition sets over FunFam and InterPro signatures in metazoa and fungi. It "
     "reaches the same term the IDA row carries and inherits the same caveat - the only perturbation "
     "behind that term is a simultaneous knockdown of APPL1 and APPL2."),
    sup("tgfb_appl1_only"),
    prop=("NO_FAILURE_NON_CORE", None, ""))

# ---- GO:0007165 signal transduction (TAS) ---------------------------------
add(55, ("GO:0007165", "TAS", "PMID:15016378"), "KEEP_AS_NON_CORE",
    "A true but uninformative parent term, taken as an author statement from the paper that defined APPL endosomes.",
    ("APPL2 does act in signal transduction - the founding paper links Rab5 to signalling and mitogenesis "
     "through an endosomal intermediate carrying APPL1 and APPL2. But GO:0007165 is a high-level parent "
     "with no discriminating content, and APPL2's specific signalling roles are stated far better by the "
     "adiponectin, TLR4, Fc-gamma-receptor and insulin rows. A projection check confirms this reference "
     "is not a bulk source (20 annotations over 4 gene products in QuickGO), so the row is a genuine "
     "author statement, just a general one."),
    sup("rab5_signal", "endosome_intermediate"))

# ---- GO:0007179 TGF-beta receptor signaling -------------------------------
add(56, ("GO:0007179", "IEA", "GO_REF:0000117"), "KEEP_AS_NON_CORE",
    "Narrow ARBA rule agreeing with the IMP row.",
    ("ARBA00085361 has 14 metazoan condition sets and assigns the same term as the IMP row. It "
     "reproduces rather than corroborates that row, and inherits its double-knockdown caveat."),
    sup("tgfb_required"),
    prop=("NO_FAILURE_NON_CORE", None, ""))

add(57, ("GO:0007179", "IMP", "PMID:26583432"), "KEEP_AS_NON_CORE",
    "APPL1/APPL2 depletion impairs TGF-beta-driven TbetaRI-ICD transport, invasion and MMP transcription.",
    ("The functional readouts are real and multiple - loss of nuclear TbetaRI-ICD, reduced TGF-beta-induced "
     "invasion of prostate and breast cancer lines, and reduced MMP2/MMP9 transcription. The design, "
     "though, is a combined APPL1 + APPL2 knockdown throughout, with the receptor interaction mapped to "
     "APPL1. So APPL2 is required in combination, which justifies keeping the annotation, but the "
     "evidence does not make TGF-beta signalling a core APPL2 function, and it was obtained in cancer "
     "cell lines."),
    sup("tgfb_required", "tgfb_appl1_only", "bioinf_paralog"))

# ---- GO:0010008 endosome membrane (incl. the IBA) -------------------------
add(60, ("GO:0010008", "IBA", "GO_REF:0000033"), "ACCEPT",
    "Family-level endosomal-membrane inference placed at the Bilateria node ancestral to both APPL paralogs; correct and core for APPL2.",
    ("The IBD behind this IBA sits on PTN000572460 at taxon 33213 (Bilateria), above the APPL1/APPL2 "
     "duplication, and was seeded by mouse Appl1, human APPL1 and human APPL2 itself. Membrane "
     "recruitment through Rab binding is the defining property of both paralogs, so placing it at their "
     "last common ancestor is the right depth, and APPL2 sits squarely inside the inheriting clade "
     "(PANTHER subfamily PTHR46415:SF1). The target's own accession in the WITH/FROM is expected: APPL2 "
     "carries two independent IDA rows for this exact term plus an EXP row for the more specific early "
     "endosome membrane, and those descendant evidences are part of what the curator used to place the "
     "node. There is no evidence of loss or divergence - APPL2 binds four Rabs, is recruited by annexin "
     "A2, and is solubilised from endosomes when that recruitment fails."),
    sup("appl_endosomes", "rab5_effectors", "anxa2_required"),
    prop=("NO_FAILURE_CORE", None, "",
          {"PANTHER:PTN000572460": (IBA_NODE_LABEL, "SUPPORTS_TRANSFER",
            "Bilateria-level IBD node of PTHR46415, seeded by mouse Appl1, human APPL1 and human APPL2. "
            "The family has only two nodes and five reviewed members, and this node is ancestral to both "
            "subfamilies (SF1 = APPL2, SF3 = APPL1), so endosomal-membrane localisation is asserted for "
            "the whole family. APPL2 is inside the inheriting clade."),
           "MGI:MGI:1920243": ("Appl1 (Mus musculus)", "SUPPORTS_TRANSFER",
            "Mouse Appl1, resolved to UniProtKB:Q8K3H0. A Rab5 effector on the same APPL endosome "
            "compartment; the localisation is correct for it and transfers correctly to APPL2, which "
            "was shown on the same structures in the original characterisation."),
           "UniProtKB:Q9UKG1": ("APPL1 (Homo sapiens)", "SUPPORTS_TRANSFER",
            "Human APPL1, the paralog. APPL1 and APPL2 were identified together as the two Rab5 "
            "effectors defining APPL endosomes, so its endosomal-membrane evidence is directly "
            "applicable to the node."),
           "UniProtKB:Q8NEU8": ("APPL2 (Homo sapiens), the target", "SUPPORTS_TRANSFER",
            "The target's own accession, which is correct and expected here rather than circular: APPL2 "
            "has two IDA rows for GO:0010008 (PMID:15016378, PMID:21645192) and an EXP row for early "
            "endosome membrane, and those are among the descendant evidences the PAINT curator used to "
            "place the IBD. Their presence means the IBA adds a claim of inheritance on top of "
            "experimental grounding that already exists on the target.")}))

add(61, ("GO:0010008", "IDA", "PMID:15016378"), "ACCEPT",
    "APPL2 is a Rab5 effector on endosomal membranes - the founding observation for this compartment.",
    ("APPL1 and APPL2 were identified as the two Rab5 effectors residing on a distinct endosome "
     "subpopulation, with Rab5 binding required for their membrane recruitment and their role in "
     "proliferation. UniProt records Early endosome membrane and Peripheral membrane protein for Q8NEU8 "
     "from this paper. This is core."),
    sup("rab5_effectors", "appl_proliferation", "endosome_intermediate"))

add(62, ("GO:0010008", "IDA", "PMID:21645192"), "ACCEPT",
    "Endogenous APPL2 on endosomal membranes, with the recruitment mechanism demonstrated.",
    ("Membrane fractionation plus imaging of endogenous APPL2 places it on a discriminable subpopulation "
     "of early endosomes, and knocking down annexin A2 solubilises APPL2 from those membranes - a "
     "loss-of-function control on the localisation itself, which few compartment annotations have. Core."),
    sup("appl_endosomes", "anxa2_solubilize", "anxa2_required"))

add(63, ("GO:0010008", "IEA", "GO_REF:0000044"), "ACCEPT",
    "Projection of UniProt's Endosome membrane keyword.",
    ("Restates UniProt's curated location, which derives from the same experimental papers as the two "
     "IDA rows. Redundant with them, and correct."),
    sup("appl_endosomes"),
    prop=("NO_FAILURE_CORE", None, ""))

# ---- GO:0010762 / GO:0035729 HGF and fibroblast migration -----------------
for idx, key, term in [
    (64, ("GO:0010762", "IEA", "GO_REF:0000107"), "regulation of fibroblast migration"),
    (65, ("GO:0010762", "ISS", "GO_REF:0000024"), "regulation of fibroblast migration"),
    (84, ("GO:0035729", "IEA", "GO_REF:0000107"), "cellular response to hepatocyte growth factor stimulus"),
    (85, ("GO:0035729", "ISS", "GO_REF:0000024"), "cellular response to hepatocyte growth factor stimulus"),
]:
    add(idx, key, "KEEP_AS_NON_CORE",
        f"{term}, from mouse embryonic fibroblasts where a single Appl2 knockout has the phenotype.",
        ("The title of the source paper reads as a double-knockout result, and I checked whether it is: "
         "it is not. Single Appl1 KO, single Appl2 KO and the double KO all showed decreased HGF-induced "
         "Akt activation, so there is an APPL2-specific loss-of-function anchor here and the rows do not "
         "suffer the paralog conflation that the TGF-beta rows do. The migration and invasion defects "
         "are reported for Appl-deficient MEFs collectively, so the migration row is slightly weaker "
         f"than the HGF-response row. {MOUSE_ISS_REASON} Non-core because the effect is "
         "growth-factor-selective - EGF, insulin and serum activate Akt normally - and Appl2-null mice "
         "are viable and grow normally."),
        sup("hgf_single_ko", "hgf_migration", "appl_expendable"),
        prop=("NO_FAILURE_NON_CORE", None,
              "The mouse annotation has a single-Appl2-knockout anchor (decreased HGF-induced Akt "
              "activation in Appl2 KO MEFs), not only the double knockout the title implies."))

# ---- GO:0016020 membrane --------------------------------------------------
add(66, ("GO:0016020", "IDA", "PMID:18034774"), "KEEP_AS_NON_CORE",
    "Live-cell imaging of APPL2 on dynamic cytosolic membrane structures; the term is the root of the compartment branch.",
    ("Full-length APPL2-YFP associated with cytosolic membrane structures that moved, fused and "
     "underwent fission, and recruited endogenous RAB5. The observation is sound and it is the direct "
     "basis for calling APPL2 a peripheral membrane protein, but 'membrane' is the least specific term "
     "available and the same paper's cytoplasmic-vesicle row plus the endosome rows state it properly."),
    sup("dynamic_membranes", "appl2_rab5_colocal"))

# ---- GO:0023052 signaling (IBA) ------------------------------------------
add(67, ("GO:0023052", "IBA", "GO_REF:0000033"), "KEEP_AS_NON_CORE",
    "A deliberately generic family-level term: the node's seeds are APPL1 and APPL2, whose signalling roles are opposite in sign.",
    ("The IBD sits on PTN000572460 at Bilateria, seeded by mouse Appl2, human APPL1 and human APPL2. "
     "The instinct is to call such a high-level term a granularity mismatch, and that would be wrong "
     "here. The two seeds disagree in sign: APPL1 potentiates adiponectin and Akt signalling while "
     "APPL2 antagonises it, competing for AdipoR1/R2 and sequestering APPL1; and in the same macrophage "
     "system APPL1 and APPL2 have 'separate and opposing functions' in Akt and MAPK signalling. Any "
     "child term specific enough to be informative would be false for one seed, so the uninformative "
     "parent is the honest least common ancestor and there is no propagation failure. It is non-core "
     "only in the sense that the term conveys nothing; the underlying claim - that APPL2 is a "
     "signalling adaptor - is correct and is stated properly by the pathway-specific rows."),
    sup("yin_yang", "tlr4_separate", "sequestration"),
    prop=("NO_FAILURE_NON_CORE", None, "",
          {"PANTHER:PTN000572460": (IBA_NODE_LABEL, "SUPPORTS_TRANSFER",
            "Bilateria-level IBD node of PTHR46415, seeded by mouse Appl2, human APPL1 and human APPL2. "
            "Because the node is ancestral to both paralogs and the paralogs' signalling roles are "
            "opposite in sign, GO:0023052 is the correct least common ancestor rather than an "
            "under-specified choice. The same curator placed the AKT-binding and insulin-receptor "
            "-signalling IBDs one node down, at PTN008708200 (Tetrapoda, APPL1 subfamily only), where "
            "APPL2 does not inherit them - which is corroborated by direct human evidence that APPL1 "
            "binds Akt2 and APPL2 does not."),
           "MGI:MGI:2384914": ("Appl2 (Mus musculus)", "SUPPORTS_TRANSFER",
            "Mouse Appl2, resolved to UniProtKB:Q8K3G9 - the target's own 1:1 ortholog, 92.7% identical. "
            "Its signalling annotations come from Appl2 knockout mice and Appl2-specific knockdowns."),
           "UniProtKB:Q9UKG1": ("APPL1 (Homo sapiens)", "SUPPORTS_TRANSFER",
            "Human APPL1, the paralog. It supports the generic parent term; it would not support a "
            "signed child, since its effect on adiponectin/Akt signalling is the opposite of APPL2's."),
           "UniProtKB:Q8NEU8": ("APPL2 (Homo sapiens), the target", "SUPPORTS_TRANSFER",
            "The target's own accession among the seeds, which is expected rather than circular: APPL2 "
            "has its own experimental signalling annotations (the TAS row from PMID:15016378 and the IMP "
            "rows from PMID:24879834 and PMID:26583432), and those descendant evidences are part of what "
            "the PAINT curator used to place the node.")}))

# ---- generic ARBA-only compartment rows -----------------------------------
add(68, ("GO:0030659", "IEA", "GO_REF:0000117"), "KEEP_AS_NON_CORE",
    "Broad ARBA rule giving a generic parent of the vesicle compartments APPL2 actually occupies.",
    ("ARBA00026540 has 72 condition sets across eukaryotes. The term is true - APPL2 is on endosomal, "
     "phagosomal and macropinosomal membranes - but it is the uninformative parent of rows that already "
     "say which vesicle. Kept rather than marked over-annotated because, unlike the plasma-membrane and "
     "bounding-membrane rules, this one lands on a compartment class APPL2 genuinely belongs to."),
    sup("appl_endosomes", "appl2_ruffles"),
    prop=("NO_FAILURE_NON_CORE", None, ""))

add(109, ("GO:0098588", "IEA", "GO_REF:0000117"), "MARK_AS_OVER_ANNOTATED",
    "Very broad ARBA rule assigning a term with no discriminating content.",
    ("ARBA00027281 has 171 condition sets spanning bacteria, plants, fungi and metazoa. 'Bounding "
     "membrane of organelle' is a structural-class term that applies to any peripheral membrane protein "
     "on any organelle; combined with a rule that broad it conveys nothing about APPL2 that the "
     "endosome-membrane and phagosome-membrane rows do not say better."),
    sup("appl_endosomes"),
    prop=("TERM_SCOPING_PROBLEM", ["GRANULARITY_MISMATCH"],
          "The rule assigns a structural-class parent of the compartments APPL2 is already annotated to "
          "more precisely."))

add(88, ("GO:0042592", "IEA", "GO_REF:0000117"), "MARK_AS_OVER_ANNOTATED",
    "'Homeostatic process' is a content-free term reached by a rule spanning bacteria to plants.",
    ("ARBA00027526 has 135 condition sets covering bacteria, fungi, plants and metazoa. APPL2 does act "
     "in homeostasis - glucose homeostasis and adaptive thermogenesis are both annotated - but those "
     "specific rows are what carry the claim. A rule this promiscuous attached to a term this general "
     "is the clearest over-annotation in the record."),
    sup("muscle_ko", "beiging_ko"),
    prop=("TERM_SCOPING_PROBLEM", ["GRANULARITY_MISMATCH"],
          "The specific homeostatic roles are already annotated (GO:0042593 glucose homeostasis, "
          "GO:0002024 diet induced thermogenesis); this rule adds only their uninformative parent."))

# ---- phagosome / phagocytic vesicle keyword projections -------------------
add(69, ("GO:0030670", "IEA", "GO_REF:0000044"), "KEEP_AS_NON_CORE",
    "Phagosome membrane keyword projection, ultimately from mouse macrophage imaging.",
    ("UniProt's Phagosome membrane keyword for APPL2 is a by-similarity annotation from mouse Appl2, "
     "which was imaged on early, actin-rich phagosomes in primary macrophages and RAW264.7 cells, "
     "recruited there by GTP-Rab31. The location is real but macrophage-specific and, in macrophages, "
     "APPL2 is notably absent from endosomes - so this is a distinct cellular context rather than an "
     "extension of the endosomal pool."),
    sup("appl2_ruffles", "first_phagosome", "absent_endosomes"),
    prop=("NO_FAILURE_NON_CORE", None,
          "The underlying observation is APPL2 on early phagosomes in mouse macrophages "
          "(PMID:25568335), recruited by GTP-Rab31."))

add(97, ("GO:0045335", "IEA", "GO_REF:0000044"), "KEEP_AS_NON_CORE",
    "Phagocytic vesicle keyword projection, same macrophage origin as the phagosome-membrane row.",
    ("Restates UniProt's Phagosome keyword, whose experimental basis is APPL2 on early phagosomes in "
     "mouse macrophages. Correct, cell-type-specific, and redundant with GO:0032009 early phagosome, "
     "which is the more precise term for the same observation."),
    sup("first_phagosome", "rab31_recruits"),
    prop=("NO_FAILURE_NON_CORE", None,
          "Same source as the phagosome-membrane keyword row; GO:0032009 early phagosome states it "
          "more precisely."))

# ---- cytoplasmic vesicle / vesicle ---------------------------------------
add(70, ("GO:0031410", "IDA", "PMID:18034774"), "KEEP_AS_NON_CORE",
    "APPL2 fusion proteins on dynamic cytosolic vesicles.",
    ("Live imaging showed APPL2-YFP on cytosolic membrane structures undergoing movement, fusion and "
     "fission and recruiting endogenous RAB5 - the vesicles are the APPL endosomes. The term is correct "
     "but is the generic parent of the endosome rows that identify the vesicle."),
    sup("dynamic_membranes", "appl2_rab5_colocal"))

add(73, ("GO:0031982", "IDA", "PMID:21645192"), "KEEP_AS_NON_CORE",
    "Generic vesicle term from the APPL-endosome fractionation study.",
    ("The same study that established the endosome and endosome-membrane rows. 'Vesicle' is the "
     "top-level parent and adds nothing to them, but it is not wrong."),
    sup("appl_endosomes", "limited_eea1"))

# ---- early endosome membrane ---------------------------------------------
add(71, ("GO:0031901", "EXP", "PMID:15016378"), "ACCEPT",
    "The most specific correct compartment term for APPL2, from the founding characterisation.",
    ("APPL endosomes are, by the authors' own definition, a subpopulation of early endosomes that shows "
     "only limited colocalisation with EEA1. UniProt records Early endosome membrane with experimental "
     "evidence from this paper. Since GO has no 'APPL endosome' term, this is the most specific true "
     "statement available and it is core."),
    sup("rab5_effectors", "appl_endosomes", "limited_eea1"))

add(72, ("GO:0031901", "IEA", "GO_REF:0000044"), "ACCEPT",
    "Projection of UniProt's Early endosome membrane keyword.",
    ("Restates the curated UniProt location behind the EXP row. Redundant, correct."),
    sup("appl_endosomes"),
    prop=("NO_FAILURE_CORE", None, ""))

# ---- early phagosome / macropinosome / phagocytosis (mouse macrophage) ----
for idx, key, term, quotes, note in [
    (74, ("GO:0032009", "IEA", "GO_REF:0000107"), "early phagosome", ("first_phagosome", "rab31_recruits"), "early phagosomes"),
    (75, ("GO:0032009", "ISS", "GO_REF:0000024"), "early phagosome", ("first_phagosome", "rab31_recruits"), "early phagosomes"),
    (86, ("GO:0036186", "IEA", "GO_REF:0000107"), "early phagosome membrane", ("first_phagosome", "appl2_ruffles"), "early phagosome membranes"),
    (87, ("GO:0036186", "ISS", "GO_REF:0000024"), "early phagosome membrane", ("first_phagosome", "appl2_ruffles"), "early phagosome membranes"),
]:
    add(idx, key, "ACCEPT",
        f"APPL2 on {note} in macrophages, transferred from mouse.",
        ("Rab31-GTP recruits APPL2 to early-stage phagosomes in mouse macrophages, where the two "
         "colocalise around the phagosome circumference; the authors call this the first evidence that "
         f"APPL2 is associated with early phagosomes. {MOUSE_ISS_REASON} Accepted as core rather than "
         "peripheral: this is precisely where APPL2 performs the phagocytic-cup-closure and "
         "Fc-gamma-receptor signalling functions that are themselves accepted as core, and a location is "
         "not made peripheral by being cell-type-restricted when the activity carried out there is "
         "central. Note that in macrophages this pool replaces rather than supplements the endosomal "
         "one - APPL2 is largely absent from endosomes in that cell type."),
        sup(*quotes),
        prop=("NO_FAILURE_NON_CORE", None,
              "The mouse observation is GTP-Rab31-dependent recruitment of APPL2 to early phagosomes in "
              "primary macrophages and RAW264.7 cells (PMID:25568335)."))

for idx, key in [(92, ("GO:0044354", "IEA", "GO_REF:0000107")), (93, ("GO:0044354", "ISS", "GO_REF:0000024"))]:
    add(idx, key, "KEEP_AS_NON_CORE",
        "Macropinosome localisation in LPS-activated mouse macrophages.",
        ("APPL1 and APPL2 are differentially localised to distinct signalling-competent membrane domains "
         "on the surface and in endocytic compartments of LPS-activated macrophages, which is the basis "
         f"for the mouse macropinosome annotation. {MOUSE_ISS_REASON} Non-core: it is one membrane "
         "domain in one activated cell type."),
        sup("tlr4_membranes", "appl2_ruffles"),
        prop=("NO_FAILURE_NON_CORE", None,
              "The mouse annotation rests on differential localisation of APPL1 and APPL2 to distinct "
              "membrane domains in LPS-activated macrophages (PMID:27219021)."))

for idx, key in [(116, ("GO:1905303", "IEA", "GO_REF:0000107")), (117, ("GO:1905303", "ISS", "GO_REF:0000024"))]:
    add(idx, key, "KEEP_AS_NON_CORE",
        "Positive regulation of macropinocytosis, from mouse macrophage work.",
        ("APPL2 is recruited to surface ruffles and then to macropinosomes in LPS-activated macrophages, "
         "and the adaptors were depleted individually in that study, so this is an APPL2-specific "
         f"observation rather than a paralog-pooled one. {MOUSE_ISS_REASON} It is non-core because it is "
         "restricted to activated macrophages and because the closely related phagocytosis rows are "
         "better supported - there the depletion phenotype was measured directly."),
        sup("tlr4_membranes", "appl2_ruffles"),
        prop=("NO_FAILURE_NON_CORE", None,
              "Mouse macrophage evidence (PMID:27219021) in which each adaptor was depleted separately."))

for idx, key in [(106, ("GO:0060100", "IEA", "GO_REF:0000107")), (107, ("GO:0060100", "ISS", "GO_REF:0000024"))]:
    add(idx, key, "ACCEPT",
        "APPL2 depletion reduces Fc-gamma-receptor-mediated phagocytosis and delays phagocytic cup closure.",
        ("This is one of the better-evidenced APPL2-specific functions: siRNA against APPL2 alone reduced "
         "internalisation of IgG-coated particles, delayed the PI(3,4,5)P3 transition and delayed "
         "phagocytic cup closure, with APPL2 physically on the closing cup and bound to GTP-Rab31 there. "
         f"{MOUSE_ISS_REASON} Accepted as a core function - promoting phagosome closure is a direct "
         "membrane-remodelling role for a BAR-domain Rab effector, not a downstream physiological effect."),
        sup("phago_sirna", "cup_closure", "rab31_recruits"),
        prop=("NO_FAILURE_CORE", None,
              "The mouse evidence is an APPL2-only siRNA depletion with a quantified phagocytosis defect "
              "and a live-imaging cup-closure delay (PMID:25568335)."))

for idx, key in [(118, ("GO:1905451", "IEA", "GO_REF:0000107")), (119, ("GO:1905451", "ISS", "GO_REF:0000024"))]:
    add(idx, key, "ACCEPT",
        "APPL2 promotes PI3K/Akt signalling downstream of the Fc-gamma receptor during phagocytosis.",
        ("APPL2 depletion reduced PI3K/Akt signalling and enhanced p38 signalling from the Fc-gamma "
         "receptor, and reduced recruitment of Akt to phagosomal membranes. The sign is positive for the "
         f"Akt arm, which is what this term asserts. {MOUSE_ISS_REASON} Accepted as core, with one "
         "caveat recorded in the notes: in the same cell type but downstream of TLR4 rather than FcgammaR, "
         "APPL2 restrains Akt signalling - the sign of APPL2's effect on this kinase is "
         "receptor-dependent, and no single annotation can express that."),
        sup("akt_p38", "phago_sirna", "akt_enhanced"),
        prop=("NO_FAILURE_CORE", None,
              "Mouse macrophage evidence from an APPL2-only depletion (PMID:25568335); the opposite-sign "
              "TLR4 result (PMID:25328665) is a different receptor, not a contradiction of this term."))

# ---- adiponectin ----------------------------------------------------------
for idx, key in [(78, ("GO:0033211", "IEA", "GO_REF:0000107")), (79, ("GO:0033211", "ISS", "GO_REF:0000024"))]:
    add(idx, key, "ACCEPT",
        "APPL2 acts in the adiponectin-receptor pathway as APPL1's antagonist; the GO term is sign-neutral and therefore correct.",
        ("APPL2 binds AdipoR1 and AdipoR2 through its BAR domain, competes with APPL1 for the receptors "
         "and sequesters APPL1 away from the pathway; knocking APPL2 down enhances adiponectin-stimulated "
         "glucose uptake and fatty acid oxidation, and overexpressing it does the reverse. This is a "
         "core function. The sign-inversion risk here is real but does not bite: GO:0033211 is defined "
         "purely as the series of signals initiated by adiponectin binding its receptor, with no "
         "direction, so involvement is all that is asserted and involvement is exactly what the mouse "
         "data show. A QuickGO search finds no signed child of this term - there is no 'negative "
         "regulation of adiponectin-activated signaling pathway' - which is recorded under "
         f"proposed_new_terms. {MOUSE_ISS_REASON}"),
        sup("yin_yang", "appl2_rnai", "sequestration"),
        prop=("NO_FAILURE_CORE", None,
              "The mouse evidence (PMID:19661063) is APPL2-specific in both directions (RNAi and "
              "overexpression in C2C12 myotubes) and the transferred term carries no regulatory sign, so "
              "the negative direction of APPL2's effect cannot be inverted by this transfer."))

# ---- TLR4 / innate immunity ----------------------------------------------
for idx, key in [(80, ("GO:0034143", "IEA", "GO_REF:0000107")), (81, ("GO:0034143", "ISS", "GO_REF:0000024"))]:
    add(idx, key, "ACCEPT",
        "APPL2 regulates TLR4 signalling in macrophages, with each adaptor depleted separately.",
        ("Depleting APPL1 and APPL2 individually revealed separate and opposing functions in Akt and MAPK "
         "signalling downstream of LPS/TLR4, with APPL2 dominant in NF-kappaB p65 nuclear translocation "
         "and in constraining cytokine secretion. Crucially the adaptors were depleted 'respectively', "
         "so this is an APPL2-specific result, not a pooled one. Reinforced by the Appl2 knockout mouse, "
         f"which is hypersensitive to LPS. {MOUSE_ISS_REASON} Core."),
        sup("tlr4_separate", "tlr4_constrain", "endotoxin_ko"),
        prop=("NO_FAILURE_CORE", None,
              "Mouse macrophage evidence with each adaptor depleted separately (PMID:27219021), plus an "
              "Appl2 knockout mouse phenotype (PMID:25328665)."))

for idx, key in [(95, ("GO:0045088", "IEA", "GO_REF:0000107")), (96, ("GO:0045088", "ISS", "GO_REF:0000024"))]:
    add(idx, key, "ACCEPT",
        "Appl2 knockout mice are hypersensitive to endotoxin; APPL2 restrains the innate immune response.",
        ("A whole-animal Appl2 knockout gave more severe endotoxin shock with increased proinflammatory "
         "cytokines, and Appl2-null primary macrophages produced more TNF-alpha and IL-1beta with "
         "enhanced Akt and NF-kappaB phosphorylation; the authors trace this to an Appl2-Appl1-p85alpha "
         f"complex restraining PI3K/Akt. Clean, APPL2-specific loss of function. {MOUSE_ISS_REASON} Core."),
        sup("endotoxin_ko", "cytokine_up", "innate_negreg"),
        prop=("NO_FAILURE_CORE", None,
              "The donor annotation rests on an Appl2 knockout mouse and Appl2-null primary macrophages "
              "(PMID:25328665) - an APPL2-specific loss of function, not a paralog-pooled one."))

for idx, key in [(112, ("GO:1900016", "IEA", "GO_REF:0000107")), (113, ("GO:1900016", "ISS", "GO_REF:0000024"))]:
    add(idx, key, "ACCEPT",
        "APPL2 constrains cytokine secretion in the immune response; the negative sign is the one the data support.",
        ("Two independent mouse studies agree on the direction: Appl2 deletion raised TNF-alpha and "
         "IL-1beta from primary macrophages, and APPL2 depletion in macrophages showed it 'serves to "
         "constrain the secretion of pro- and anti-inflammatory cytokines'. The signed term is therefore "
         f"correctly signed, which is the thing to check on a transfer like this. {MOUSE_ISS_REASON}"),
        sup("cytokine_up", "tlr4_constrain", "endotoxin_ko"),
        prop=("NO_FAILURE_CORE", None,
              "Two independent APPL2-specific mouse perturbations (PMID:25328665 knockout, PMID:27219021 "
              "depletion) agree on the negative direction, so the signed term transfers safely."))

# ---- phosphatidylinositol binding ----------------------------------------
add(82, ("GO:0035091", "IDA", "PMID:18034774"), "ACCEPT",
    "Full-length APPL2 and its isolated PH and PTB domains bind phosphoinositides in vitro.",
    ("Lipid-strip overlays with affinity-purified protein show binding of full-length APPL2 - not just "
     "isolated domains - to PtdIns(3)P, PtdIns(4)P, PtdIns(5)P, PtdIns(3,4)P2 and PtdIns(3,5)P2, and "
     "UniProt records that the PH and PID domains mediate phosphoinositide binding. The structural work "
     "nominates a PH-domain contact surface, and I verified that those residues are present at the "
     "stated positions in Q8NEU8 (R287, K289, W297, all inside the PH span 277-375) and conserved in "
     "mouse Appl2. Core: lipid binding together with Rab binding is what puts APPL2 on membranes."),
    sup("pi_binding", "ph_residues", "bioinf_residues"))

add(83, ("GO:0035091", "IEA", "GO_REF:0000117"), "ACCEPT",
    "Narrow ARBA rule agreeing with the IDA row.",
    ("ARBA00026346 has only 7 condition sets and assigns the term the IDA row already establishes for "
     "full-length protein. Redundant but correct."),
    sup("pi_binding"),
    prop=("NO_FAILURE_CORE", None, ""))

# ---- glucose ---------------------------------------------------------------
add(89, ("GO:0042593", "IMP", "PMID:24879834"), "ACCEPT",
    "Muscle-specific APPL2 deletion improves glucose tolerance in mice.",
    ("Conditional deletion of APPL2 in skeletal muscle enhanced insulin sensitivity and improved glucose "
     "tolerance, and the cellular phenotype runs in both directions - overexpression impairs and "
     "knockdown enhances insulin-evoked GLUT4 recruitment and glucose uptake. The mechanism is mapped to "
     "a phospho-Ser235-dependent TBC1D1 interaction. This is the best-evidenced APPL2 function in the "
     "record and is core."),
    sup("muscle_ko", "glut4_bidirectional", "tbc1d1_mech"))

for idx, key, ev in [(100, ("GO:0046325", "IEA", "GO_REF:0000120"), "IEA"),
                     (102, ("GO:0046325", "ISS", "GO_REF:0000024"), "ISS")]:
    add(idx, key, "ACCEPT",
        "Negative regulation of glucose import, agreeing with the human/mouse IMP row from the same study.",
        ("APPL2 suppresses insulin-evoked GLUT4 translocation to the plasma membrane and glucose uptake, "
         "shown by overexpression, knockdown and a muscle-specific knockout. The signed term is correctly "
         f"signed. {MOUSE_ISS_REASON} Core, and not merely redundant with the IMP row: it is the same "
         "conclusion reached through the ortholog."),
        sup("glut4_bidirectional", "muscle_ko", "finetune"),
        prop=("NO_FAILURE_CORE", None,
              "The mouse donor annotation comes from the same study as the human IMP row, with "
              "bidirectional APPL2 perturbation and a muscle-specific knockout."))

add(101, ("GO:0046325", "IMP", "PMID:24879834"), "ACCEPT",
    "APPL2 overexpression impairs and knockdown enhances insulin-stimulated glucose uptake and GLUT4 recruitment.",
    ("Both perturbation directions were done, in cultured myotubes and in vivo, and the mechanism is "
     "mapped to the BAR-domain interaction with phospho-Ser235 TBC1D1 that blocks TBC1D1 Thr-596 "
     "phosphorylation. Core function."),
    sup("glut4_bidirectional", "tbc1d1_mech", "muscle_ko"))

for idx, key in [(114, ("GO:1900077", "IEA", "GO_REF:0000107")), (115, ("GO:1900077", "ISS", "GO_REF:0000024"))]:
    add(idx, key, "ACCEPT",
        "APPL2 negatively regulates the cellular insulin response, by sequestering APPL1 and by acting on TBC1D1.",
        ("Two independent mechanisms converge on the same sign: APPL2 sequesters APPL1 away from the "
         "insulin pathway in muscle cells, and it binds phospho-TBC1D1 to block GLUT4 translocation. The "
         f"signed term matches both. {MOUSE_ISS_REASON} Core."),
        sup("sequestration", "glut4_bidirectional", "yin_yang"),
        prop=("NO_FAILURE_CORE", None,
              "Two independent APPL2-specific mouse mechanisms (PMID:19661063 sequestration, "
              "PMID:24879834 TBC1D1) agree on the negative sign."))

for idx, key in [(98, ("GO:0046322", "IEA", "GO_REF:0000107")), (99, ("GO:0046322", "ISS", "GO_REF:0000024"))]:
    add(idx, key, "ACCEPT",
        "APPL2 restrains adiponectin-stimulated fatty acid oxidation in muscle cells.",
        ("Suppressing APPL2 by RNAi significantly enhanced adiponectin-stimulated fatty acid oxidation, "
         "which is the loss-of-function direction that establishes the negative sign; overexpression "
         f"produced the converse effect on adiponectin signalling. {MOUSE_ISS_REASON} Core, as part of "
         "the adiponectin antagonism."),
        sup("appl2_rnai", "yin_yang", "appl2_overexp_adipo"),
        prop=("NO_FAILURE_CORE", None,
              "APPL2-specific RNAi in C2C12 myotubes gives the loss-of-function direction "
              "(PMID:19661063), so the negative sign is established rather than assumed."))

# ---- identical protein binding / homodimerization -------------------------
add(90, ("GO:0042802", "IPI", "PMID:18034774"), "ACCEPT",
    "APPL2 self-association, demonstrated by reciprocal coimmunoprecipitation of differently tagged APPL2.",
    ("Differently tagged APPL2 constructs reciprocally coimmunoprecipitated, and yeast two-hybrid mapped "
     "the requirement to the minimal BAR domain. The WITH/FROM is APPL2's own accession, which is what "
     "an identical-protein-binding row should carry. The BAR dimer is the structural unit of the protein "
     "- the crystal structure shows the crescent-shaped antiparallel BAR dimer and solution methods "
     "agree - so this is core."),
    sup("appl2_self_coip", "bar_dimer", "bar_crescent"))

add(91, ("GO:0042803", "IDA", "PMID:18034774"), "ACCEPT",
    "BAR-domain-mediated homodimerization is the structural basis of APPL2 function.",
    ("The minimal BAR domains are necessary and sufficient for APPL2-APPL2 interaction, the crystal "
     "structure shows a crescent-shaped antiparallel BAR dimer, and independent solution measurements - "
     "chemical cross-linking and multi-angle light scattering - both give a dimer. The dimer is also the "
     "functional unit for Rab binding, since two Rab31 molecules bind one APPL2 BAR-PH dimer. Core."),
    sup("bar_dimer", "bar_crescent", "xlink_dimer"))

# ---- protein-containing complex binding -----------------------------------
add(94, ("GO:0044877", "IPI", "PMID:15016378"), "ACCEPT",
    "Binding to the MBD2/NuRD nucleosome remodelling and deacetylase complex (ComplexPortal CPX-880).",
    ("The WITH/FROM resolves to CPX-880, the MBD2/NuRD complex, and UniProt records that APPL2 binds "
     "subunits of the NuRD/MeCP1 complex with experimental evidence from this paper on the Q8NEU8 entry. "
     "The cached record for this reference is abstract-only and the abstract foregrounds APPL1's nuclear "
     "translocation, but the curator and the UniProt annotator read the full text, and the nuclear "
     "APPL2 pool is independently supported. Unlike a bare protein-binding row this one names a defined "
     "complex, which makes it informative, and it connects the endosomal and nuclear halves of APPL2 "
     "biology."),
    sup("nurd", "uniprot_nurd", "appl_nuclear_egf"))

# ---- neurogenesis ---------------------------------------------------------
for idx, key, term in [
    (103, ("GO:0050768", "IEA", "GO_REF:0000107"), "negative regulation of neurogenesis"),
    (104, ("GO:0050768", "ISS", "GO_REF:0000024"), "negative regulation of neurogenesis"),
    (122, ("GO:2000178", "IEA", "GO_REF:0000107"), "negative regulation of neural precursor cell proliferation"),
    (123, ("GO:2000178", "ISS", "GO_REF:0000024"), "negative regulation of neural precursor cell proliferation"),
]:
    add(idx, key, "KEEP_AS_NON_CORE",
        f"{term}, driven mainly by APPL2 transgenic overexpression in mouse.",
        ("The in vivo evidence is an APPL2 transgenic mouse: APPL2 Tg animals have reduced hippocampal "
         "and olfactory neurogenesis and a higher glial fraction, reversible by a glucocorticoid-receptor "
         "antagonist. A matching loss-of-function exists only in cultured neural stem cells, where APPL2 "
         "knockdown promoted neurogenesis. So both directions exist and the negative sign is right, but "
         "the animal-level claim rests on gain of function, where an overexpressed adaptor can titrate "
         f"partners non-physiologically. {MOUSE_ISS_REASON} Non-core: this is a tissue-specific "
         "developmental consequence of APPL2 tuning glucocorticoid-receptor sensitivity, several steps "
         "from the molecular function."),
        sup("neuro_tg", "nsc_switch", "nsc_invivo"),
        prop=("NO_FAILURE_NON_CORE", None,
              "The donor evidence is chiefly an APPL2 transgenic overexpression mouse (PMID:28965332, "
              "PMID:32468397), with the loss-of-function direction shown only in vitro."))

# ---- homotetramerization --------------------------------------------------
add(105, ("GO:0051289", "IDA", "PMID:23055524"), "MODIFY",
    "The cited paper reports a dimer by every solution method; the tetramer is a reading of the crystallographic asymmetric unit.",
    ("The word 'tetramer' does not occur anywhere in the full text of this paper. What it reports is that "
     "the APPL2 BAR-PH construct crystallised with two dimers in the asymmetric unit - four chains, which "
     "is a statement about crystal packing, not about the assembly state in solution. Every solution "
     "measurement in the same paper gives a dimer: chemical cross-linking, and multi-angle light "
     "scattering returning 95.1 kDa against a theoretical dimer mass of 92.1 kDa. The only tetramer "
     "described is a heterotetramer with the Rab (an APPL2 BAR-PH dimer plus two Rab31 monomers), which "
     "is not homotetramerization either. UniProt's 'Homotetramer (PubMed:23055524)' appears to rest on "
     "the same misreading. I propose GO:0051260 protein homooligomerization rather than deletion: the "
     "BAR domain does self-associate, and the defined oligomer the paper supports is the dimer, already "
     "annotated as GO:0042803 and GO:0042802. I am overruling a curator here only because the cached "
     "full text is complete and the decisive sentences are quotable verbatim."),
    sup("asu_two_dimers", "xlink_dimer", "malls_dimer", "rab31_22"),
    repl=[{"id": "GO:0051260", "label": "protein homooligomerization"}])

# ---- extracellular exosome ------------------------------------------------
add(108, ("GO:0070062", "HDA", "PMID:19056867"), "MARK_AS_OVER_ANNOTATED",
    "A whole-fraction urinary-exosome proteomics inventory projected onto every protein it detected.",
    ("I ran the reference-projection test against QuickGO: this single reference carries 1016 GO "
     "annotations over 1016 distinct gene products, all of them GO:0070062 - one per protein in the "
     "dataset. That is an inventory of what was in the fraction, not a claim that APPL2 functions in "
     "extracellular exosomes. By contrast the gene-specific references on this record project onto only "
     "2-6 entities each. APPL2 is a peripheral membrane protein on endosomal membranes, so detection in "
     "a multivesicular-body-derived fraction is unsurprising and carries no functional content. Marked "
     "over-annotated rather than removed: the protein was genuinely detected."),
    sup("exosome_lcms", "exosome_1132"))

# ---- G1/S transition ------------------------------------------------------
add(120, ("GO:2000045", "IDA", "PMID:15016378"), "KEEP_AS_NON_CORE",
    "APPL2 is required for cell proliferation in a Rab5-binding-dependent manner.",
    ("Both APPL1 and APPL2 are essential for cell proliferation and the requirement depends on Rab5 "
     "binding, which is the observation behind the cell-cycle term; the pathway is proposed to run from "
     "the APPL endosome to the nucleus and the NuRD/MeCP1 complex. It is kept as non-core because the "
     "specific G1/S claim is a downstream consequence of the signalling adaptor role rather than "
     "something APPL2 does directly, and because no APPL2-specific cell-cycle mechanism has been mapped "
     "since."),
    sup("appl_proliferation", "endosome_intermediate", "nurd"))

add(121, ("GO:2000045", "IEA", "GO_REF:0000117"), "KEEP_AS_NON_CORE",
    "Narrow ARBA rule reaching the same cell-cycle term as the IDA row.",
    ("ARBA00033889 has 7 condition sets over primates, rodents and yeast. It restates the IDA row's "
     "claim; the yeast condition set is irrelevant to APPL2 but does not make the human call wrong."),
    sup("appl_proliferation"),
    prop=("NO_FAILURE_NON_CORE", None, ""))


# ---------------------------------------------------------------------------
# NEW rows
# ---------------------------------------------------------------------------
NEW_ROWS = [
    {
        "term": {"id": "GO:0090263", "label": "positive regulation of canonical Wnt signaling pathway"},
        "evidence_type": "IMP",
        "original_reference_id": "PMID:19433865",
        "review": {
            "summary": ("APPL2 relieves Reptin-mediated repression of beta-catenin/TCF-dependent "
                        "transcription in human cells, a function with no corresponding GOA row."),
            "action": "NEW",
            "reason": (
                "GOA carries the APPL2-RUVBL2/Reptin and APPL2-CTNNB1/HDAC1/HDAC2 interactions as bare "
                "protein-binding rows but no biological-process row for what those interactions do. "
                "In human HEK293 cells, APPL2 overexpression increased beta-catenin-stimulated "
                "SuperTOPflash activity dose-dependently with no effect on the mutated-site control "
                "reporter, increased Wnt3a-induced expression of endogenous Wnt target genes, relieved "
                "Reptin-mediated repression, reduced HDAC1/HDAC2 and beta-catenin bound to Reptin, and "
                "increased beta-catenin occupancy at the cyclin D1 and Axin2 promoters while reducing "
                "Reptin and HDAC1 there. UniProt annotates the same role on Q8NEU8 with experimental "
                "evidence from this paper. Coded IMP rather than IDA because the perturbation is "
                "overexpression; the caveat that this is a gain-of-function assay is genuine - APPL2 is "
                "practically undetectable in HEK293 cells, so no knockdown control was possible, and "
                "APPL2's effect was consistently smaller than APPL1's."),
            "supported_by": sup("tcf_reporter", "wnt3a_targets", "reptin_relief", "hdac_reduced", "appl2_undetectable"),
        },
    },
    {
        "term": {"id": "GO:0140311", "label": "protein sequestering activity"},
        "evidence_type": "ISS",
        "original_reference_id": "PMID:19661063",
        "supporting_entities": ["UniProtKB:Q8K3G9"],
        "review": {
            "summary": ("APPL2 sequesters APPL1 away from the adiponectin and insulin pathways - the "
                        "mechanism behind its antagonism, and a molecular function GOA does not record."),
            "action": "NEW",
            "reason": (
                "Every functional row on this gene describes what APPL2 does to a pathway; none names "
                "the molecular activity by which it does it. The mechanism is explicit in the source: "
                "APPL2 binds AdipoR1 and AdipoR2 through its BAR domain, competes with APPL1 for the "
                "receptors, and additionally suppresses both adiponectin and insulin signalling by "
                "sequestrating APPL1 from those pathways; adiponectin and metformin both trigger "
                "APPL1-APPL2 dissociation, so the sequestration is regulated rather than constitutive. "
                "GO:0140311 is defined as binding a protein to prevent it interacting with other "
                "partners or to inhibit its localisation to where it is active, which is exactly this. "
                "Coded ISS with mouse Appl2 (Q8K3G9) as the donor because the experiments are in C2C12 "
                "mouse myotubes; the human protein is 92.7% identical and the APPL1-APPL2 heterodimer "
                "that the activity depends on is established directly for the human proteins."),
            "supported_by": sup("sequestration", "yin_yang", "appl2_overexp_adipo", "bioinf_identity"),
            "propagation_review": {
                "root_cause": "NO_FAILURE_CORE",
                "source_entities": [{
                    "source_id": "UniProtKB:Q8K3G9",
                    "source_label": "Appl2 (Mus musculus)",
                    "source_status": "SUPPORTS_TRANSFER",
                    "comment": (
                        "Mouse Appl2, the 1:1 ortholog of the target (92.7% identity over a full-length "
                        "global alignment, APPL2-bioinformatics/RESULTS.md). The sequestration was shown "
                        "in mouse C2C12 myotubes by overexpression and RNAi, and the heterodimer it "
                        "depends on is independently established for the human proteins by yeast "
                        "two-hybrid and reciprocal coimmunoprecipitation, so the transfer is safe."),
                }],
                "residue_claims_not_applicable": (
                    "The activity is mediated by the BAR-domain heterodimer interface rather than by any "
                    "identified catalytic or binding residue, and no BAR-interface mutant has been "
                    "reported, so there is no residue-level claim to make."),
            },
        },
    },
]


# ---------------------------------------------------------------------------
# References: titles are read from the caches, never written from memory.
# ---------------------------------------------------------------------------
REF_REVIEWS: dict[str, tuple[str, str, str]] = {
    "GO_REF:0000024": ("HIGH", "VERIFIED",
        "UniProt manual ortholog-transfer pipeline; the source of all 24 ISS rows, every one of them "
        "from mouse Appl2 (Q8K3G9). Verified by inspecting the WITH/FROM of each row."),
    "GO_REF:0000033": ("HIGH", "VERIFIED",
        "PAINT phylogenetic annotation; the source of both IBA rows. Verified against the family's own "
        "PAINT slice (interpro/panther/PTHR46415/PTHR46415-paint.tsv), which shows the two IBD nodes, "
        "their taxon levels and their seeds."),
    "GO_REF:0000044": ("MEDIUM", "VERIFIED",
        "UniProt subcellular-location keyword projection; five CC rows. Each keyword id was resolved "
        "against the UniProt locations API (SL-0191 Nucleus, SL-0100 Endosome membrane, SL-0093 Early "
        "endosome membrane, SL-0205 Phagosome membrane, SL-0206 Phagosome). These restate UniProt's own "
        "curated locations rather than adding evidence."),
    "GO_REF:0000107": ("HIGH", "VERIFIED",
        "Ensembl Compara orthology projection; 19 rows, all with WITH/FROM "
        "UniProtKB:Q8K3G9|ensembl:ENSMUSP00000020500. I confirmed via UniProt that ENSMUSP00000020500 "
        "maps to Q8K3G9, so these are one donor under two identifiers, not two."),
    "GO_REF:0000117": ("MEDIUM", "VERIFIED",
        "ARBA machine-learned rules. Each cited rule was fetched from rest.uniprot.org/arba and its "
        "condition sets counted; they range from 4 (ARBA00093152) to 171 (ARBA00027281), and that span "
        "is what separates the rules I kept from the ones I marked over-annotated."),
    "GO_REF:0000120": ("MEDIUM", "VERIFIED",
        "Combined multi-method IEA pipeline; the rows mix an ARBA rule, the mouse ortholog and a "
        "subcellular-location keyword in a single WITH/FROM. For GO:0005886 the ARBA component "
        "(ARBA00027801, 686 condition sets) is what drives the call."),
    "PMID:15016378": ("HIGH", "VERIFIED",
        "The founding characterisation of APPL endosomes and of APPL1/APPL2 as Rab5 effectors; source "
        "of the EXP, TAS and two IDA rows plus a complex-binding row. The cache is abstract-only "
        "(full_text_available: false), and the abstract foregrounds APPL1's nuclear translocation, so "
        "the APPL2-specific details behind the NuRD row were read by the curator in the full text, not "
        "by me. QuickGO projection test: 20 annotations over 4 gene products, so this is not a bulk "
        "reference."),
    "PMID:16189514": ("LOW", "VERIFIED",
        "Proteome-scale yeast two-hybrid map (Rual et al.). Two rows, partners APPL1 and RAB22A. "
        "Systematic-screen evidence with no APPL2-specific follow-up."),
    "PMID:17030088": ("HIGH", "VERIFIED",
        "FSHR complex study. Beyond the two interaction rows, this is the source of the single cleanest "
        "functional distinction between the paralogs - APPL1 binds Akt2, APPL2 does not - which is what "
        "corroborates PAINT's decision to place the protein-kinase-B-binding IBD at the APPL1-only node. "
        "Cache is abstract-only but the relevant statement is in the abstract."),
    "PMID:18034774": ("HIGH", "VERIFIED",
        "Domain-level membrane-targeting and oligomerisation study; the source of most MF and several CC "
        "rows. Full text cached. Note the record lists an erratum (Traffic 2008;9(4):623-4) whose "
        "content is not in the cache, so quotes are taken from main-text sections only. The paper's own "
        "distinction between full-length protein and isolated domains is what separates the "
        "phosphatidylinositol row (accepted) from the phosphatidylserine and plasma-membrane rows "
        "(non-core)."),
    "PMID:19056867": ("LOW", "VERIFIED",
        "Urinary exosome proteomics. Correctly cited and methodologically fine, but a whole-fraction "
        "inventory: the QuickGO projection test returns 1016 annotations over 1016 distinct gene "
        "products, all GO:0070062. Relevance to APPL2 function is nil."),
    "PMID:19433865": ("HIGH", "VERIFIED",
        "APPL proteins as activators of beta-catenin/TCF transcription via Reptin; full text cached. "
        "Source of two IPI rows and of the NEW GO:0090263 row. The APPL2 evidence is entirely "
        "gain-of-function because APPL2 is practically undetectable in the HEK293 cells used, which the "
        "paper states plainly - that limitation is recorded wherever the paper is used."),
    "PMID:19661063": ("HIGH", "VERIFIED",
        "The Yin-Yang adiponectin paper: APPL2 as a negative regulator of adiponectin signalling, with "
        "both RNAi and overexpression directions in C2C12 myotubes. Not in the GOA reference list - it "
        "is the experimental basis of the mouse annotations that the ISS/IEA rows transfer. Retrieved "
        "and read for this review."),
    "PMID:21645192": ("HIGH", "VERIFIED",
        "Biochemical characterisation of APPL endosomes and of annexin A2 as the recruitment factor; "
        "full text cached. Source of endosome, endosome-membrane and vesicle IDA rows, and the one "
        "paper providing a loss-of-function control on APPL2's own localisation."),
    "PMID:23055524": ("HIGH", "VERIFIED",
        "Crystal and solution structures of the APPL2 BAR-PH module plus the Rab-binding screen and "
        "Rab31 thermodynamics; full text cached. Correctly cited for the Rab31 interaction. It is "
        "MISCITED nowhere, but it does not support the homotetramerization row attributed to it - the "
        "word tetramer does not appear in the paper and all its solution data give a dimer. Recorded "
        "as VERIFIED because the citation resolves to the intended, supporting paper; the problem is "
        "with what one annotation claims it says, which is argued in that row's review."),
    "PMID:23414517": ("LOW", "VERIFIED",
        "Skeletal-muscle LGMD yeast two-hybrid interactome. One row, partner APPL1. Systematic screen."),
    "PMID:23455924": ("LOW", "VERIFIED",
        "Y2H-seq protein-methyltransferase interactome. One row, partner SUV39H2, no follow-up."),
    "PMID:24879834": ("HIGH", "VERIFIED",
        "APPL2-TBC1D1 and insulin-stimulated glucose uptake; the best-evidenced APPL2 function, with "
        "overexpression, knockdown and a muscle-specific conditional knockout. Cache is abstract-only, "
        "but the abstract states every result the annotations rest on."),
    "PMID:25328665": ("HIGH", "VERIFIED",
        "Appl2 knockout mice in endotoxin shock; the loss-of-function basis for the innate-immune and "
        "cytokine rows. Not in the GOA reference list; retrieved for this review."),
    "PMID:25416956": ("LOW", "VERIFIED",
        "Proteome-scale binary interactome map. Five rows; the two Rab partners are informative, the "
        "rest are unfollowed screen hits."),
    "PMID:25568335": ("HIGH", "VERIFIED",
        "Rab31/APPL2 in FcgammaR-mediated phagocytosis; the experimental basis for the phagosome, "
        "ruffle, cytoplasm, phagocytosis and FcgammaR-signalling annotations that reach human APPL2 by "
        "orthology. Uses APPL2-only siRNA. Not in the GOA reference list; retrieved for this review."),
    "PMID:25814554": ("LOW", "VERIFIED",
        "Phospho-tyrosine-dependent interaction screen. One row, partner MAPRE3, no follow-up."),
    "PMID:26445298": ("MEDIUM", "VERIFIED",
        "Appl1/Appl2 knockout mice and MEFs. Important as a control on a paralog-conflation suspicion: "
        "the title reads as a double-knockout result, but single Appl2 KO MEFs also show the HGF-induced "
        "Akt defect. Not in the GOA reference list; retrieved for this review."),
    "PMID:26583432": ("MEDIUM", "VERIFIED",
        "APPL proteins in TGF-beta-induced nuclear transport of TbetaRI-ICD; full text cached. Correctly "
        "cited, but every functional experiment is a simultaneous APPL1+APPL2 knockdown and the receptor "
        "interaction is mapped to APPL1 alone, so it cannot establish an APPL2-specific role. Recorded as "
        "VERIFIED rather than MISCITED because the paper does support the claim that the gene product is "
        "required - the limitation is one of attribution, argued in the affected rows."),
    "PMID:27219021": ("HIGH", "VERIFIED",
        "TLR4 signalling in macrophages with APPL1 and APPL2 depleted separately; the basis for the "
        "TLR4, cytokine and macropinosome annotations. Cache is abstract-only but the abstract states "
        "the separate-depletion design explicitly. Not in the GOA reference list; retrieved for this "
        "review."),
    "PMID:28514442": ("LOW", "VERIFIED",
        "BioPlex 2.0 affinity-purification mass spectrometry. One row, partner APPL1."),
    "PMID:28965332": ("MEDIUM", "VERIFIED",
        "APPL2 transgenic mice, glucocorticoid-receptor sensitivity and hippocampal neurogenesis; the "
        "basis for the neurogenesis rows. Gain-of-function in vivo. Abstract-only cache. Not in the GOA "
        "reference list; retrieved for this review."),
    "PMID:29467283": ("MEDIUM", "VERIFIED",
        "Conditional APPL2 ablation in VMH RIP-Cre neurons and beiging of white adipose tissue; the "
        "basis for the thermogenesis and cold-acclimation rows. Not in the GOA reference list; retrieved "
        "for this review."),
    "PMID:31515488": ("LOW", "VERIFIED",
        "Interaction disruption by coding variants. Five rows; two Rab partners plus unfollowed hits."),
    "PMID:32296183": ("LOW", "VERIFIED",
        "HuRI reference binary interactome. Seven rows, the largest single block of unfollowed "
        "screen hits on this gene."),
    "PMID:32468397": ("MEDIUM", "VERIFIED",
        "APPL2 and olfactory neurogenesis via Notch1; supplies the in vitro knockdown direction that "
        "the transgenic-mouse work lacks. Not in the GOA reference list; retrieved for this review."),
    "PMID:33961781": ("LOW", "VERIFIED",
        "BioPlex 3.0 dual proteome-scale networks. One row, partner APPL1."),
    "PMID:35271311": ("LOW", "VERIFIED",
        "OpenCell endogenous tagging. One row, partner APPL1. Endogenous tagging makes this a better "
        "class of screen than overexpression Y2H, but there is still no APPL2-specific follow-up."),
    "file:human/APPL2/APPL2-uniprot.txt": ("HIGH", "VERIFIED",
        "The UniProt Swiss-Prot record for Q8NEU8 (DP13B_HUMAN, 664 aa), fetched by the pipeline. "
        "Accession checked against the review's own id before use - this matters here because the "
        "Affinage service returned Q06481 (APLP2) for the symbol 'APPL2'."),
    "file:human/APPL2/APPL2-bioinformatics/RESULTS.md": ("HIGH", "VERIFIED",
        "Sequence analysis written for this review: live UniProt fetches with asserted lengths, pairwise "
        "global identities, and residue-level checks of the positions the structural paper names. "
        "Reproducible via appl_orthology.py."),
}

NO_AFFINAGE_NOTE = (
    "No affinage deep-research record exists for APPL2 and none is cited. The affinage prefetch "
    "refused to write one because its wrong-protein trust gate tripped: the record returned by the "
    "service was built on UniProt accession Q06481, which is APLP2 (amyloid-beta precursor-like "
    "protein 2), a different gene that carries 'APPL2' as a legacy alias, rather than Q8NEU8. This "
    "review therefore rests entirely on UniProt, GOA, the PANTHER PAINT slice and primary literature "
    "retrieved directly. The same symbol collision was filtered out of every literature search."
)


DESCRIPTION = (
    "APPL2 (DCC-interacting protein 13-beta, DIP13B) is a 664-residue cytoplasmic adaptor protein "
    "built from an N-terminal BAR domain, a central pleckstrin-homology domain and a C-terminal "
    "phosphotyrosine-binding domain, with no catalytic activity of its own. The BAR domain drives "
    "self-association into crescent-shaped dimers and also heterodimerisation with its paralog APPL1, "
    "while the PH and PTB domains bind phosphoinositides; together these give the protein a "
    "curvature-sensing, lipid-binding scaffold. APPL2 is an effector of small GTPases of the Rab5 "
    "branch, binding GTP-loaded Rab5, Rab22A, Rab24 and Rab31 - the last being the only one whose "
    "affinity has been measured, a dissociation constant of 140 nM - and this is what "
    "recruits it to membranes. On a peripheral subpopulation of early endosomes, called APPL "
    "endosomes for the two adaptors that mark them, APPL2 acts together with Rab5 and annexin A2 as "
    "part of a signalling platform that links internalised receptors to the nucleus; a pool of the "
    "protein shuttles into the nucleus and associates with the NuRD/MeCP1 chromatin-remodelling "
    "complex and with a Reptin-beta-catenin-HDAC repressive complex, where it promotes "
    "beta-catenin/TCF-dependent transcription. In muscle, APPL2 is a brake on metabolic signalling: "
    "it binds the adiponectin receptors AdipoR1 and AdipoR2 in competition with APPL1 and sequesters "
    "APPL1 away from the adiponectin and insulin pathways, and it binds phosphorylated TBC1D1 to block "
    "insulin-evoked GLUT4 translocation and glucose uptake, so losing APPL2 improves insulin "
    "sensitivity and glucose tolerance. In macrophages the protein instead occupies surface ruffles, "
    "macropinosomes and early phagosomes, where Rab31 recruits it to promote phagocytic cup closure "
    "and Fc-gamma-receptor-driven PI3K/Akt signalling, while downstream of TLR4 it restrains Akt and "
    "NF-kappaB activation and limits cytokine secretion. Further roles have been described in "
    "hypothalamic control of adipose beiging and cold tolerance, in hepatocyte-growth-factor-dependent "
    "fibroblast migration, and in tuning glucocorticoid-receptor sensitivity during adult "
    "neurogenesis. Across these settings APPL2 repeatedly behaves as the counterweight to APPL1 rather "
    "than its duplicate: the two proteins are only about 54% identical, bind different Rabs, and have "
    "opposite effects on adiponectin signalling and on Akt activation downstream of several receptors."
)

CORE_FUNCTIONS = [
    {
        "description": ("Effector of Rab5-branch small GTPases that recruits the protein to endosomal "
                        "and phagosomal membranes"),
        "molecular_function": {"id": "GO:0031267", "label": "small GTPase binding"},
        "locations": [
            {"id": "GO:0010008", "label": "endosome membrane"},
            {"id": "GO:0031901", "label": "early endosome membrane"},
            {"id": "GO:0032009", "label": "early phagosome"},
        ],
        "supported_by": sup("rab5_effectors", "rab_screen", "rab31_direct"),
    },
    {
        "description": ("BAR-domain scaffold that homodimerises and heterodimerises with APPL1, and "
                        "binds phosphoinositides through its PH and PTB domains"),
        "molecular_function": {"id": "GO:0042803", "label": "protein homodimerization activity"},
        "locations": [{"id": "GO:0010008", "label": "endosome membrane"}],
        "supported_by": sup("bar_dimer", "bar_crescent", "pi_binding"),
    },
    {
        "description": ("Phosphoinositide binding by the PH and PTB domains, which together with Rab "
                        "binding targets APPL2 to membranes"),
        "molecular_function": {"id": "GO:0035091", "label": "phosphatidylinositol binding"},
        "locations": [{"id": "GO:0010008", "label": "endosome membrane"}],
        "supported_by": sup("pi_binding", "ph_residues"),
    },
    {
        "description": ("Sequesters APPL1 and competes with it for the adiponectin receptors, acting as "
                        "the negative arm of adiponectin and insulin signalling in muscle"),
        "molecular_function": {"id": "GO:0140311", "label": "protein sequestering activity"},
        "directly_involved_in": [
            {"id": "GO:0033211", "label": "adiponectin-activated signaling pathway"},
            {"id": "GO:1900077", "label": "negative regulation of cellular response to insulin stimulus"},
        ],
        "supported_by": sup("yin_yang", "sequestration", "appl2_rnai"),
    },
    {
        "description": ("Binds phospho-Ser235 TBC1D1 through its BAR domain, holding it away from the "
                        "kinase that would otherwise phosphorylate its Thr-596 site, and so restrains "
                        "insulin-stimulated GLUT4 translocation and glucose uptake. The sequestering "
                        "here is of TBC1D1 from its upstream kinase rather than of APPL1 from a "
                        "receptor, which is the same activity applied to a different partner; what the "
                        "protein contributes is the same phospho-dependent occupancy in both cases."),
        "molecular_function": {"id": "GO:0140311", "label": "protein sequestering activity"},
        "directly_involved_in": [
            {"id": "GO:0046325", "label": "negative regulation of D-glucose import across plasma membrane"},
            {"id": "GO:0042593", "label": "glucose homeostasis"},
        ],
        "supported_by": sup("tbc1d1_mech", "glut4_bidirectional", "muscle_ko"),
    },
    {
        "description": ("Rab31-recruited adaptor on early phagosomes that promotes phagocytic cup "
                        "closure and Fc-gamma-receptor-driven PI3K/Akt signalling in macrophages"),
        "molecular_function": {"id": "GO:0031267", "label": "small GTPase binding"},
        "locations": [
            {"id": "GO:0032009", "label": "early phagosome"},
            {"id": "GO:0036186", "label": "early phagosome membrane"},
        ],
        "supported_by": sup("rab31_recruits", "phago_sirna", "akt_p38"),
    },
]

PROPOSED_NEW_TERMS = [
    {
        "proposed_name": "negative regulation of adiponectin-activated signaling pathway",
        "proposed_definition": ("A process that stops, prevents or reduces the frequency, rate or extent of the "
                        "adiponectin-activated signaling pathway. GO currently has GO:0033211 "
                        "adiponectin-activated signaling pathway but no signed children: a QuickGO "
                        "ontology search for 'regulation of adiponectin' returns only the secretion "
                        "branch (GO:0070163, GO:0070164, GO:0070165) and GO:0055100 adiponectin "
                        "binding. APPL2's best-characterised metabolic role is specifically to "
                        "antagonise this pathway - it competes with APPL1 for AdipoR1/AdipoR2 and "
                        "sequesters APPL1 - and that direction currently cannot be expressed, so the "
                        "annotation has to fall back on the neutral parent."),
        "justification": ("Without a signed child, an adiponectin antagonist and an adiponectin "
                      "potentiator receive the same GO term. APPL1 and APPL2 are exactly that pair, "
                      "and both are annotated to GO:0033211."),
        "supported_by": sup("yin_yang", "appl2_rnai"),
    },
    {
        "proposed_name": "APPL endosome",
        "proposed_definition": ("A subpopulation of early endosomes marked by the Rab5 effectors APPL1 and "
                        "APPL2, distinguishable from canonical EEA1-positive early endosomes by "
                        "limited EEA1 colocalisation, a distinct migration pattern in continuous "
                        "density gradients, a peripheral distribution beneath the plasma membrane, and "
                        "dependence on annexin A2 as well as Rab5 for membrane recruitment. Would be a "
                        "child of GO:0005769 early endosome."),
        "justification": ("The compartment has been defined biochemically and by imaging since 2004 and is "
                      "referred to by name throughout the field, but the most specific GO term "
                      "available for APPL2 is GO:0031901 early endosome membrane, which does not "
                      "distinguish it from the EEA1-positive population the authors explicitly "
                      "separate it from."),
        "supported_by": sup("appl_endosomes", "limited_eea1", "anxa2_required"),
    },
]

KNOWLEDGE_GAPS = [
    {
        "gap_statement": ("It is not known what determines the sign of APPL2's effect on PI3K/Akt "
                          "signalling: in macrophages APPL2 restrains Akt downstream of TLR4 but "
                          "promotes it downstream of the Fc-gamma receptor."),
        "boundary": ("Known: Appl2 knockout raises Akt and NF-kappaB phosphorylation after LPS, while "
                     "APPL2 depletion reduces Akt recruitment and phosphorylation during FcgammaR-mediated "
                     "phagocytosis, both in macrophages. Unknown: whether the reversal is set by the "
                     "recruiting Rab, the membrane domain, or a different PI3K at each site."),
        "gap_kind": ["BIOLOGY"],
        "status": "OPEN",
        "significance": ("Two GO annotations on this gene assert opposite directions of Akt-pathway "
                         "regulation, and both are correct in context. No single annotation can express "
                         "a receptor-dependent sign reversal, so the ontology forces an apparent "
                         "contradiction onto a real biological phenomenon."),
        "provenance": sup("akt_enhanced", "akt_p38"),
    },
    {
        "gap_statement": ("Whether APPL2 recruits or regulates a PI3K directly has never been tested, "
                          "even though the proposed mechanism for its role in phagocytosis depends on it."),
        "boundary": ("Known: APPL2 depletion delays the PI(4,5)P2-to-PI(3,4,5)P3 transition at the "
                     "phagocytic cup, and mouse Appl2 is found in a complex with the PI3K regulatory "
                     "subunit p85alpha together with Appl1. Unknown: whether APPL2 binds any PI3K "
                     "subunit directly, and whether that binding is what produces the phosphoinositide "
                     "phenotype."),
        "gap_kind": ["BIOLOGY"],
        "status": "OPEN",
        "significance": ("It is the difference between APPL2 being a lipid-kinase-recruiting adaptor and "
                         "being a passive curvature sensor whose loss perturbs the membrane indirectly."),
        "provenance": sup("pi3k_unknown", "innate_negreg"),
    },
    {
        "gap_statement": ("How the nuclear pool of APPL2 is generated is unknown: the proposed nuclear "
                          "localisation signal at residues 151-157 has never been mutated."),
        "boundary": ("Known: the motif PKKKENE is present verbatim at 151-157 of Q8NEU8, lies inside the "
                     "BAR domain, is conserved in mouse Appl2 and diverges in APPL1 (SKKREND), and the "
                     "crystal structure places it on a face masked by the PH domain. A nuclear APPL2 pool "
                     "is well documented. Unknown: whether this motif is the signal, and whether "
                     "PH-domain rotation gates it."),
        "gap_kind": ["BIOLOGY"],
        "status": "OPEN",
        "significance": ("The nucleus rows and the NuRD and Reptin complex-binding rows all rest on a "
                         "nuclear pool whose import mechanism is unexplained. It is also one of the very "
                         "few sequence features that distinguishes APPL2 from APPL1."),
        "provenance": sup("nls_motif", "nls_untested", "bioinf_nls"),
    },
    {
        "gap_statement": ("APPL2's individual contribution to TGF-beta-driven TbetaRI-ICD nuclear "
                          "transport is unresolved because only simultaneous APPL1 + APPL2 knockdowns "
                          "were performed."),
        "boundary": ("Known: depleting both adaptors abolishes nuclear TbetaRI-ICD accumulation and "
                     "reduces TGF-beta-induced invasion and MMP2/MMP9 transcription. Unknown: whether "
                     "APPL2 alone is required; the TbetaRI and PKCzeta associations were mapped to APPL1 "
                     "only."),
        "gap_kind": ["CURATION"],
        "status": "OPEN",
        "significance": ("Two GOA rows (GO:0007179 IMP and GO:0006606 IDA) rest entirely on this design. "
                         "At ~54% paralog identity and with documented opposite-sign behaviour elsewhere, "
                         "a double knockdown is not evidence about either gene singly."),
        "provenance": sup("tgfb_appl1_only", "bioinf_paralog"),
    },
    {
        "gap_statement": ("The assembly state of full-length APPL2 is unestablished; all structural work "
                          "is on the BAR-PH fragment and the PTB domain's contribution is unknown."),
        "boundary": ("Known: the BAR-PH module (residues 1-384, PDB 4H8S and 5C5B) forms a crescent-shaped "
                     "dimer, and cross-linking and light scattering both give a dimer in solution. "
                     "Unknown: whether the full-length protein behaves the same way; no full-length "
                     "structure and no APPL2-Rab complex structure exists."),
        "gap_kind": ["BIOLOGY"],
        "status": "OPEN",
        "significance": ("A GOA row asserts protein homotetramerization on the strength of two dimers in "
                         "a crystallographic asymmetric unit. Settling the solution assembly state of the "
                         "intact protein would close that question directly."),
        "provenance": sup("asu_two_dimers", "malls_dimer"),
    },
    {
        "gap_statement": ("Most of what is annotated for human APPL2 - adiponectin antagonism, endotoxin "
                          "hypersensitivity, phagocytosis, adipose beiging, neurogenesis - has only been "
                          "demonstrated in mouse."),
        "boundary": ("Known: human and mouse APPL2 are 92.7% identical over a full-length alignment, so "
                     "the orthology transfer is as safe as such transfers get. Unknown: whether the human "
                     "protein reproduces these phenotypes; the only human-cell functional data are the "
                     "glucose-uptake, Wnt-reporter and TGF-beta experiments."),
        "gap_kind": ["CURATION"],
        "status": "OPEN",
        "significance": ("Forty-three of the 124 rows on this gene (24 ISS plus 19 orthology-based IEA) "
                         "come from the single mouse donor Q8K3G9."),
        "provenance": sup("bioinf_identity", "yin_yang"),
    },
]

SUGGESTED_QUESTIONS = [
    {"question": ("Is the receptor-dependent sign of APPL2's effect on Akt - restraining after TLR4, "
                  "promoting after Fc-gamma receptor engagement - set by which Rab recruits it (Rab31 on "
                  "phagosomes versus the macropinosomal pool), or by which PI3K is available at each "
                  "membrane domain?")},
    {"question": ("Is sequestration the molecular activity of APPL2 rather than a side effect of "
                  "scaffolding? Everything mapped so far is competitive occupancy - of AdipoR1/R2 against "
                  "APPL1, of phospho-Ser235 TBC1D1, of Reptin.")},
    {"question": ("Given that APPL2 and APPL1 heterodimerise through their BAR domains yet oppose each "
                  "other functionally, is the APPL1-APPL2 heterodimer an inactive reservoir, or does it "
                  "have activities neither homodimer has?")},
    {"question": ("GO cannot currently express negative regulation of the adiponectin-activated signaling "
                  "pathway. Should such a term be created, and should APPL1 and APPL2 then be "
                  "re-annotated to the corresponding positive and negative children?")},
    {"question": ("Should GO represent the APPL endosome as a distinct compartment, given that it is "
                  "separable from EEA1-positive early endosomes biochemically, by density-gradient "
                  "migration, by peripheral distribution and by its dependence on annexin A2?")},
    {"question": ("Does the homotetramer recorded for APPL2 in UniProt and GOA have any experimental "
                  "basis beyond two dimers in a crystallographic asymmetric unit?")},
]

SUGGESTED_EXPERIMENTS = [
    {
        "hypothesis": ("APPL2 contributes to TbetaRI-ICD nuclear transport independently of APPL1, rather "
                       "than only as the redundant half of a pair."),
        "description": ("Rescue APPL1/APPL2 double-knockdown cells with APPL2 alone, APPL1 alone, or a "
                        "BAR-interface mutant that cannot heterodimerise, and score TbetaRI-ICD nuclear "
                        "accumulation and TGF-beta-induced invasion. This is the control the existing "
                        "literature lacks and is what would convert the GO:0007179 and GO:0006606 rows "
                        "from a paralog-pooled result into an APPL2-specific one."),
        "experiment_type": "genetic rescue / single-adaptor complementation",
    },
    {
        "hypothesis": ("The basic cluster at residues 151-157 (PKKKENE) is a functional nuclear "
                       "localisation signal that the PH domain masks."),
        "description": ("Mutate 151-157 to alanine and ask whether the nuclear pool of APPL2 is lost and "
                        "whether the Reptin/HDAC association and the beta-catenin/TCF reporter response "
                        "go with it; in parallel test whether a PH-domain-deletion construct, which "
                        "should unmask the motif, shows increased nuclear accumulation. The motif is "
                        "APPL2-specific - the aligned span in APPL1 is SKKREND - so a positive result "
                        "would also explain a paralog difference."),
        "experiment_type": "site-directed mutagenesis with imaging and biochemical readouts",
    },
    {
        "hypothesis": ("Full-length APPL2 is a dimer in solution, and the homotetramer in the current "
                       "annotations is a crystal-packing artefact."),
        "description": ("Measure the oligomeric state of full-length recombinant APPL2 by mass photometry "
                        "and SEC-MALS, and compare with the BAR-PH fragment; attempt a structure or "
                        "prediction of the full-length protein to determine whether the PTB domain "
                        "supports higher-order assembly."),
        "experiment_type": "biophysical characterisation",
    },
    {
        "hypothesis": ("The sign of APPL2's effect on Akt tracks the Rab that recruits it to the membrane."),
        "description": ("Compare Akt phosphorylation, PI(3,4,5)P3 kinetics and PI3K-subunit recruitment "
                        "side by side in APPL2-depleted macrophages stimulated through TLR4 versus the "
                        "Fc-gamma receptor, with Rab31 and Rab5 co-depletion arms, using live probes for "
                        "the phosphoinositide transitions."),
        "experiment_type": "comparative perturbation with live-cell imaging",
    },
    {
        "hypothesis": ("APPL2 antagonises adiponectin signalling by two separable mechanisms - receptor "
                       "competition and APPL1 sequestration - either of which is sufficient."),
        "description": ("Express in Appl2-null myotubes an APPL2 mutant that binds AdipoR1 but not APPL1 "
                        "and one that binds APPL1 but not AdipoR1, and measure adiponectin-stimulated "
                        "glucose uptake and fatty acid oxidation for each. The result would also "
                        "determine whether GO:0140311 protein sequestering activity is the right "
                        "molecular function or only part of it."),
        "experiment_type": "separation-of-function mutants in a null background",
    },
]

PROPOSED_NEW_TERMS[1]["proposed_parent"] = {"id": "GO:0005769", "label": "early endosome"}
PROPOSED_NEW_TERMS[0]["proposed_parent"] = {"id": "GO:0033211",
                                            "label": "adiponectin-activated signaling pathway"}


def cache_title(pmid: str) -> str:
    """Read the title from the cached publication. Never write a title from memory."""
    path = REPO / "publications" / f"PMID_{pmid.split(':', 1)[1]}.md"
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"{path} has no YAML front matter")
    front = text.split("\n---\n", 1)[0][4:]
    doc = YAML(typ="safe").load(front)
    title = doc.get("title")
    if not title:
        raise ValueError(f"{path} has no title")
    return " ".join(str(title).split())


def build_propagation(row: dict, spec) -> dict:
    """Derive source_entities from the row's OWN supporting_entities."""
    root_cause, failure_modes, row_note = spec[0], spec[1], spec[2]
    overrides = spec[3] if len(spec) > 3 else None
    entities = row.get("supporting_entities") or []
    if not entities:
        raise ValueError(f"propagation_review requested for a row with no supporting_entities: {row['term']}")
    block: dict = {"root_cause": root_cause}
    if failure_modes:
        block["failure_modes"] = list(failure_modes)
    block["source_entities"] = [source_entity(e, row_note, overrides=overrides) for e in entities]
    return block


def main() -> int:
    yaml_rt = YAML()
    yaml_rt.preserve_quotes = True
    yaml_rt.width = 100
    doc = yaml_rt.load(REVIEW.read_text())

    rows = doc["existing_annotations"]
    if len(rows) != len(D):
        raise SystemExit(f"decision table covers {len(D)} rows but the file has {len(rows)}")

    used_refs: set[str] = set()

    def note_refs(items):
        for it in items:
            used_refs.add(it["reference_id"])

    for i, row in enumerate(rows):
        dec = D[i]
        got = (row["term"]["id"], row["evidence_type"], row["original_reference_id"])
        if got != dec["k"]:
            raise SystemExit(f"row {i} is {got} but the decision table expects {dec['k']}")
        review = {"summary": dec["summary"], "action": dec["action"], "reason": dec["reason"]}
        if dec["repl"]:
            review["proposed_replacement_terms"] = dec["repl"]
        review["supported_by"] = dec["supported"]
        note_refs(dec["supported"])
        if dec["prop"] is not None:
            review["propagation_review"] = build_propagation(row, dec["prop"])
        elif row["evidence_type"] in {"IBA", "ISS", "ISO", "IEA", "IC"} and row.get("supporting_entities"):
            raise SystemExit(f"row {i} ({got}) needs a propagation_review but the table has none")
        row["review"] = review

    for new in NEW_ROWS:
        note_refs(new["review"]["supported_by"])
        rows.append(new)

    for cf in CORE_FUNCTIONS:
        note_refs(cf["supported_by"])
    for pt in PROPOSED_NEW_TERMS:
        note_refs(pt["supported_by"])
    for kg in KNOWLEDGE_GAPS:
        note_refs(kg["provenance"])

    # ---- references -------------------------------------------------------
    existing = {r["id"]: r for r in doc["references"]}
    refs = []
    for rid in sorted(used_refs | set(existing)):
        if rid in existing:
            entry = existing[rid]
        elif rid.startswith("PMID:"):
            entry = {"id": rid, "title": cache_title(rid)}
        elif rid.startswith("file:"):
            entry = {"id": rid, "title": {
                "file:human/APPL2/APPL2-uniprot.txt":
                    "UniProtKB record Q8NEU8 (DP13B_HUMAN), DCC-interacting protein 13-beta",
                "file:human/APPL2/APPL2-bioinformatics/RESULTS.md":
                    "APPL2 (Q8NEU8) sequence checks: orthology, paralogy and residue-level verification",
            }[rid]}
        else:
            raise SystemExit(f"unknown reference id {rid}")
        if rid not in REF_REVIEWS:
            raise SystemExit(f"no reference_review written for {rid}")
        rel, corr, notes = REF_REVIEWS[rid]
        if rid == "file:human/APPL2/APPL2-uniprot.txt":
            notes = notes + " " + NO_AFFINAGE_NOTE
        entry["reference_review"] = {"relevance": rel, "correctness": corr, "review_notes": notes}
        refs.append(entry)
    # every reference we wrote a review for must actually be cited
    unused = set(REF_REVIEWS) - used_refs - set(existing)
    if unused:
        raise SystemExit(f"reference_review written for uncited references: {sorted(unused)}")
    doc["references"] = refs

    doc["status"] = "COMPLETE"
    doc["description"] = DESCRIPTION
    doc["core_functions"] = CORE_FUNCTIONS
    doc["proposed_new_terms"] = PROPOSED_NEW_TERMS
    doc["suggested_questions"] = SUGGESTED_QUESTIONS
    doc["suggested_experiments"] = SUGGESTED_EXPERIMENTS
    doc["knowledge_gaps"] = KNOWLEDGE_GAPS

    with REVIEW.open("w") as fh:
        yaml_rt.dump(doc, fh)

    n_prop = sum(1 for r in rows if "propagation_review" in (r.get("review") or {}))
    print(f"wrote {REVIEW}")
    print(f"  {len(rows)} annotation rows ({len(NEW_ROWS)} NEW), {n_prop} propagation_review blocks, "
          f"{len(refs)} references")
    return 0


if __name__ == "__main__":
    sys.exit(main())
