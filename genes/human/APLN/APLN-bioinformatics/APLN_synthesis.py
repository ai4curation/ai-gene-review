"""Top-level synthesis for the APLN review: description, core functions, gaps, questions,
experiments, proposed terms, and the per-reference review judgments.

Kept beside APLN_decisions.py so that build_review.py contains only mechanism.
"""

from __future__ import annotations

from APLN_decisions import AFFINAGE, BIOINF, UNIPROT

DESCRIPTION = (
    "Apelin is the endogenous peptide agonist of the apelin receptor APLNR (APJ), a "
    "Gi-coupled G-protein-coupled receptor. It is made as a 77-residue preproprotein: a "
    "cleaved signal peptide, a propeptide, and a C-terminal tail that is processed into a "
    "family of short bioactive peptides named for their length - apelin-36, -31, -28, -17 "
    "and -13, the last of which is frequently N-terminally cyclised to pyroglutamyl "
    "apelin-13. Furin cleaves the proprotein directly to apelin-13, and apelin-13 and "
    "apelin-17 are the predominant endogenous forms in plasma and hypothalamus. The active "
    "part of the molecule is extraordinarily conserved: the twelve C-terminal residues are "
    "essentially invariant across vertebrates, and human, rat, mouse and bovine apelin-13 "
    "and apelin-17 are identical, with divergence confined to the portion of the precursor "
    "that is trimmed away. Both ends of the peptide are required for activity - an "
    "N-terminal Arg-Pro-Arg-Leu motif for receptor recognition and the C-terminal "
    "phenylalanine for activation - and that terminal phenylalanine is also what sets the "
    "balance between the receptor's G-protein and beta-arrestin outputs.\n\n"
    "Binding of apelin to APLNR activates Gi, inhibiting adenylyl cyclase and lowering "
    "cAMP, while also activating ERK1/2 and recruiting beta-arrestin, which desensitises "
    "and internalises the receptor. Signalling is terminated proteolytically: "
    "angiotensin-converting enzyme 2 removes the single C-terminal phenylalanine, and the "
    "truncated peptides are much less active, making ACE2 a negative regulator of the "
    "whole axis. The peptide is secreted and acts largely in an autocrine or paracrine "
    "fashion; it circulates in human plasma only at subnanomolar concentrations, and it is "
    "also secreted in large amounts into colostrum and milk.\n\n"
    "Physiologically the apelin-APLNR axis is best characterised in the cardiovascular "
    "system and in fluid balance. Apelin is among the most potent positive inotropes known "
    "in the heart; it lowers blood pressure through a nitric-oxide-dependent vasodilator "
    "mechanism; and mice lacking apelin, although viable, fertile and outwardly normal, "
    "lose cardiac contractility with ageing and pressure overload and show markedly "
    "reduced exercise capacity. In the brain, apelin is co-expressed with vasopressin in "
    "magnocellular hypothalamic neurons, inhibits their activity, lowers circulating "
    "vasopressin and promotes diuresis, and reduces water intake in dehydrated animals - "
    "acting as a counter-regulator of vasopressin in body-fluid homeostasis. In the "
    "vasculature apelin is induced by hypoxia through HIF-1alpha, marks sprouting "
    "endothelium, and in pulmonary artery endothelial cells sustains transcription of "
    "miR-424 and miR-503, which restrain FGF2 and FGFR1 and thereby limit endothelial and "
    "smooth-muscle proliferation; this axis is lost in pulmonary arterial hypertension. "
    "Apelin also improves whole-body glucose utilisation in rodents. The receptor it acts "
    "through is shared with a second, structurally unrelated endogenous ligand, "
    "ELABELA/Toddler, and the two ligands are separable: apelin-null and APLNR-null animals "
    "have different, sometimes opposite, developmental phenotypes."
)

CORE_FUNCTIONS = [
    dict(
        description=(
            "Endogenous agonist of the apelin receptor APLNR. The peptides released from "
            "the precursor - predominantly apelin-13, pyroglutamyl-apelin-13 and apelin-17 "
            "- bind APLNR in the extracellular space and activate it, coupling it to Gi so "
            "that adenylyl cyclase is inhibited and cAMP falls, and activating ERK1/2. "
            "Agonism requires the intact peptide: fragments truncated past the N-terminal "
            "Arg-Pro-Arg-Leu motif are inactive, and removal of the single C-terminal "
            "phenylalanine by ACE2 inactivates the peptide. This is the molecular act from "
            "which every other apelin phenotype follows."),
        supported_by=[("PMID:9792798", "TAT98_LIGAND"), ("PMID:22810587", "SCI12_CAMP"),
                      ("PMID:22810587", "SCI12_GI"), ("PMID:11359874", "REA01_INACTIVE"),
                      ("PMID:11815627", "VIC02_CTERM"), (AFFINAGE, "AFF_SUMMARY")],
        molecular_function={"id": "GO:0005179", "label": "hormone activity"},
        directly_involved_in=[
            {"id": "GO:0060183", "label": "apelin receptor signaling pathway"},
            {"id": "GO:0007193",
             "label": "adenylate cyclase-inhibiting G protein-coupled receptor signaling pathway"},
        ],
        locations=[{"id": "GO:0005576", "label": "extracellular region"}],
    ),
    dict(
        description=(
            "Ligand-driven desensitisation of its own receptor. Apelin binding to APLNR "
            "recruits beta-arrestin and drives clathrin-dependent internalisation of the "
            "receptor, and the balance between this arm and the Gi arm is set by residues "
            "in the peptide itself - UniProt records positions 75 and 77 of APLN as "
            "determinants of that balance, from the cryo-EM structures of apelin-bound "
            "APLNR-Gi1 complexes. This is not a downstream consequence but part of what the "
            "ligand does to the receptor, and it is the arm whose over-activation "
            "motivated the design of G-protein-biased apelin analogues."),
        supported_by=[("PMID:11359874", "REA01_FRAGMENTS"), ("PMID:22810587", "SCI12_ARRESTIN"),
                      ("PMID:38428423", "WAN24_BIAS"), ("PMID:38428423", "WAN24_ARRESTIN")],
        molecular_function={"id": "GO:0031704", "label": "apelin receptor binding"},
        directly_involved_in=[
            {"id": "GO:1904022",
             "label": "positive regulation of G protein-coupled receptor internalization"},
        ],
        locations=[{"id": "GO:0005576", "label": "extracellular region"}],
    ),
]

KNOWLEDGE_GAPS = [
    dict(
        gap_statement=(
            "Which processed apelin peptide does what, in which tissue, is unresolved - and "
            "the gene record cannot express the difference, because every annotation is "
            "made against the 77-residue precursor rather than against the chains UniProt "
            "already defines."),
        boundary=(
            "Firmly established: the precursor yields apelin-36, -31, -28, -17 and -13; "
            "furin cleaves proapelin directly to apelin-13 with no longer intermediates; "
            "apelin-13 and, less abundantly, apelin-17 are the predominant endogenous forms "
            "in plasma and hypothalamus; the peptides differ in receptor residence time, in "
            "their G-protein versus beta-arrestin bias, and in susceptibility to ACE2; and "
            "UniProt carries PRO chain identifiers PRO_0000001760 to PRO_0000001763 for "
            "four of them. Equally established: not one GO annotation on this gene is made "
            "against a chain identifier."),
        gap_kind=["BIOLOGY", "CURATION"],
        dark_aspect="RESIDUAL_SUBGAP",
        status="OPEN",
        significance=(
            "Apelin analogues are being developed as cardiovascular drugs precisely because "
            "the forms differ in bias and stability. A record that treats them as one "
            "entity cannot support that distinction, and cannot say which form a given "
            "physiological claim rests on. It also makes the gene look like a protein with "
            "a dozen activities rather than a precursor for a small set of peptides."),
        resolution=(
            "Two separable steps. Biologically: measure the tissue distribution of each "
            "processed form with form-specific assays, and repeat the key physiological "
            "perturbations with each. Curationally: annotate against the existing PRO chain "
            "identifiers, as UniProt already does for the isoform-level GO:0005179 and "
            "GO:0005576 rows it carries on PRO_0000001763 in other species."),
        provenance=[("PMID:24251091", "SHI13_FURIN"), ("PMID:15231996", "DEM04_FORMS"),
                    ("PMID:27217402", "WAN16_DOMINANT"), (UNIPROT, "UP_PTM")],
    ),
    dict(
        gap_statement=(
            "Whether apelin should be treated as a hormone or as a locally released "
            "autocrine/paracrine mediator is unsettled, and the ontology forces a choice "
            "that the data do not support."),
        boundary=(
            "Established: apelin is detectable in human plasma, at 0.26 nmol/L, and the "
            "authors of that measurement conclude the concentration is more consistent with "
            "local release than with circulating hormone action. Also established: apelin is "
            "secreted in very large amounts into colostrum, at 14 to 93 pmol/ml, which is an "
            "exocrine route entirely. GO:0005179 hormone activity is defined permissively "
            "enough to cover both, because it says 'sometimes in the bloodstream', and its "
            "own comment points to GO:0048018 receptor agonist activity as an alternative."),
        gap_kind=["BIOLOGY", "ONTOLOGY"],
        dark_aspect="MF_DARK",
        status="OPEN",
        significance=(
            "The choice determines what a reader infers about where apelin acts and over "
            "what distance, and it propagates: three rows on this gene assert hormone "
            "activity, and the term is transferred to the rodent and bovine orthologs by "
            "ISS and IEA. If apelin is mostly paracrine, every one of those rows is "
            "conveying something slightly false about the route."),
        resolution=(
            "Biologically, a measurement of the arteriovenous gradient of each apelin form "
            "across a vascular bed, and of local interstitial concentration, would show "
            "whether circulating apelin is a signal or a spillover. Ontologically, the "
            "question is whether GO wants GO:0005179 to be about the route of delivery or "
            "only about the agonist relationship; if the former, apelin belongs under "
            "GO:0048018 instead."),
        provenance=[("PMID:28137936", "YAN17_PARACRINE"), ("PMID:28137936", "YAN17_PLASMA"),
                    ("PMID:10525157", "HAB99_COLOSTRUM")],
    ),
    dict(
        gap_statement=(
            "Apelin's role in angiogenesis is absent from the human GO record entirely, "
            "although it is one of the two things the protein is best known for."),
        boundary=(
            "Established: apelin is induced by hypoxia through HIF-1alpha binding an "
            "intronic hypoxia-responsive element, and knockdown of apelin blocks "
            "hypoxia-induced endothelial proliferation in vitro and vessel regeneration in "
            "vivo. Zebrafish apln carries GO:0002040 sprouting angiogenesis by IGI, and "
            "UniProt keeps 'Angiogenesis' as a keyword on the human entry. Equally "
            "established: the human GOA record contains no angiogenesis term of any kind. "
            "The closest rows, GO:1905564 and GO:1904706, are about proliferation of the "
            "two cell types, not about vessel formation."),
        gap_kind=["CURATION"],
        dark_aspect="BP_DARK",
        status="OPEN",
        significance=(
            "Angiogenesis is the context in which apelin is most often studied and targeted "
            "therapeutically, in tumours and in retinopathy. Its absence means a search of "
            "GO for angiogenic ligands does not return apelin, and it leaves the review "
            "unable to record the function without inventing an ISS donor that does not "
            "carry the term."),
        resolution=(
            "A curator with access to the mouse Apln-CreER sprouting-endothelium and "
            "retinal-angiogenesis literature could make a mouse experimental annotation, "
            "from which an ISS to human would follow. No NEW row is proposed here for "
            "exactly that reason: no rodent ortholog currently holds an angiogenesis term, "
            "so there is nothing to transfer from, and the human experiments in hand "
            "measure endothelial proliferation rather than vessel formation."),
        provenance=[("PMID:18617693", "EYR08_ANGIO"), ("PMID:18617693", "EYR08_KD"),
                    ("PMID:18617693", "EYR08_HIF")],
    ),
    dict(
        gap_statement=(
            "The phylogenetic annotation of the apelin family propagates a localisation and "
            "nothing else, although the family's function is known and conserved."),
        boundary=(
            "Established from the committed PAINT slice: PTHR15953 carries exactly one "
            "node-level annotation, an IBD for GO:0005576 at PTN001041490, and UniProt's "
            "own cross-reference records 'PAN-GO; Q9ULZ1; 1 GO annotation based on "
            "evolutionary models'. Equally established: apelin receptor binding and the "
            "apelin receptor signalling pathway are experimentally annotated in human, rat, "
            "mouse and zebrafish, and the C-terminal twelve residues of the peptide are 97 "
            "to 98.5 per cent invariant across all 333 UniProt members of the family."),
        gap_kind=["CURATION"],
        dark_aspect="RESIDUAL_SUBGAP",
        status="OPEN",
        significance=(
            "This is an IBA-incompleteness case of the cleanest possible kind: a small, "
            "single-function family with an invariant active site and experimental support "
            "in four species, whose evolutionary annotation says only that the product "
            "leaves the cell. Any downstream analysis that uses IBA as a proxy for "
            "conserved function will miss apelin's actual function completely."),
        resolution=(
            "IBD assertions for GO:0031704 and GO:0060183 at or near PTN001041490, seeded "
            "from the existing experimental annotations in human, rat, mouse and zebrafish."),
        provenance=[(BIOINF, "BIO_NODE"), (BIOINF, "BIO_PEPTIDE"),
                    ("PMID:11359874", "REA01_FRAGMENTS")],
    ),
    dict(
        gap_statement=(
            "Whether apelin regulates glucose metabolism in humans is unknown; the entire "
            "case rests on acute peptide infusion into rodents."),
        boundary=(
            "Established in mouse: intravenous apelin lowers blood glucose and increases "
            "glucose utilisation in skeletal muscle and adipose tissue, through eNOS, AMPK "
            "and Akt, and restores glucose tolerance in obese insulin-resistant animals. "
            "Not established: any human perturbation, any effect of losing endogenous "
            "apelin on glucose handling, and any GO annotation on any species' APLN for a "
            "metabolic process."),
        gap_kind=["BIOLOGY"],
        dark_aspect="BP_DARK",
        status="OPEN",
        significance=(
            "Apelin is repeatedly proposed as a target in insulin resistance on the "
            "strength of this work. The distinction between a pharmacological effect of an "
            "infused agonist and a physiological role for the endogenous peptide is exactly "
            "the distinction GO evidence codes are meant to preserve, and here it has not "
            "been tested."),
        resolution=(
            "Glucose tolerance and hyperinsulinaemic-euglycaemic clamp phenotyping of "
            "apelin-null mice, which have not been reported for this readout, and a "
            "controlled apelin infusion study with a clamp in humans."),
        provenance=[("PMID:19046574", "DRA08_GLUCOSE"), ("PMID:17673668", "KUB07_VIABLE")],
    ),
]

PROPOSED_NEW_TERMS = [
    dict(
        proposed_name="negative regulation of vasopressin secretion",
        proposed_definition=(
            "Any process that decreases the rate, frequency or extent of the regulated "
            "release of vasopressin from a cell."),
        justification=(
            "GO:0030103 vasopressin secretion exists but has no regulation children, while "
            "its parent GO:0090278 negative regulation of peptide hormone secretion already "
            "has ten hormone-specific children - calcitonin, somatostatin, "
            "corticotropin-releasing hormone, corticotropin, growth hormone, glucagon, "
            "substance P, prolactin, thyroid-stimulating hormone and insulin. Vasopressin "
            "is conspicuously missing. Apelin is the clearest case needing it: it is "
            "co-localised with vasopressin in magnocellular hypothalamic neurons, inhibits "
            "their phasic activity, and lowers plasma vasopressin with a corresponding "
            "increase in diuresis, and this is its best-characterised central action. The "
            "term would also serve the several other neuropeptides and receptors known to "
            "modulate vasopressin release. Without it the biology has to be recorded "
            "against the generic parent, which loses the identity of the hormone."),
        proposed_parent={"id": "GO:0090278", "label": "negative regulation of peptide hormone secretion"},
        supported_by=[("PMID:15231996", "DEM04_DIURETIC"), ("PMID:15231996", "DEM04_DIURESIS"),
                      ("PMID:11359874", "REA01_AVP")],
    ),
]

SUGGESTED_QUESTIONS = [
    dict(question=(
        "For the PAINT curators of PTHR15953: the family carries exactly one node-level "
        "annotation, an IBD for GO:0005576 at PTN001041490. Apelin receptor binding "
        "(GO:0031704) and the apelin receptor signalling pathway (GO:0060183) are "
        "experimentally annotated in human, rat, mouse and zebrafish, and the peptide's "
        "C-terminal twelve residues are 97-98.5% invariant across all 333 members. Is "
        "there a reason these were not placed at the same node, or is this simply "
        "unfinished?")),
    dict(question=(
        "For UniProt: rat Apln carries GO:0045776 negative regulation of blood pressure as "
        "an IMP from PMID:11359874, and that paper's abstract reports that central "
        "pE13F 'did not affect blood pressure'. The same sentence is what supports the "
        "drinking-behaviour annotation from the same paper. Apelin's vasodepressor action "
        "is well established, but from PMID:11384769 and PMID:22810587. What supports the "
        "blood-pressure annotation as cited? This row reaches human APLN twice, by ISS and "
        "by Ensembl Compara IEA.")),
    dict(question=(
        "For UniProt: the mouse Apln GO:0060976 coronary vasculature development IMP cites "
        "PMID:28890073, which reports that Apelin-knockout animals did not phenocopy the "
        "Apj-knockout coronary defect and that Apelin-deficient hearts showed increased "
        "coronary growth - the opposite direction. The unsigned GO term still applies, but "
        "the FUNCTION line transferred to human APLN reads 'Plays a role in early coronary "
        "blood vessels formation', which implies the opposite sign. Should that comment be "
        "reworded?")),
    dict(question=(
        "For UniProt: four APLN rows cite PMID:28137936 and two of them are coded IMP "
        "(GO:0005179, GO:0060183). That paper contains no APLN mutant or knockdown; its "
        "apelin data are synthetic-peptide pharmacology run as a comparator to ELABELA. "
        "Should these be IDA? The same question applies to rat Apln GO:0045823 IMP from "
        "PMID:26611206, which is an apela paper.")),
    dict(question=(
        "For GOA and UniProt jointly: UniProt defines four PRO chain identifiers for this "
        "entry (PRO_0000001760 to PRO_0000001763) and almost every annotation on the gene "
        "is really about apelin-13 or apelin-17 rather than about the 77-residue "
        "precursor. Would annotations against those chain identifiers be accepted, as they "
        "already are for some orthologs?")),
    dict(question=(
        "For UniProt: apelin-17 has no PEPTIDE feature on this entry, although it is one "
        "of the two predominant endogenous forms (PMID:15231996), is the form used in most "
        "central work as K17F, and is one of the two peptides whose ACE2 cleavage was "
        "characterised (PMID:27217402). Should it be added alongside apelin-36, -31, -28 "
        "and -13?")),
    dict(question=(
        "For GO: apelin is annotated to GO:0005179 hormone activity three times, yet the "
        "best human measurement of the circulating peptide concludes it looks 'more "
        "indicative of peptides acting as locally released autocrine/paracrine mediators "
        "than as circulating hormones'. Does GO intend GO:0005179 to carry a claim about "
        "route of delivery, given its definition says 'sometimes in the bloodstream' and "
        "its comment points to GO:0048018?")),
]

SUGGESTED_EXPERIMENTS = [
    dict(
        hypothesis=(
            "The physiological roles currently attributed to apelin are carried by "
            "different processed forms in different tissues, and the precursor-level record "
            "conflates them."),
        description=(
            "Raise or commission form-specific immunoassays that discriminate apelin-36, "
            "apelin-17, apelin-13 and pyroglutamyl-apelin-13, validated against synthetic "
            "standards and against ACE2-cleaved products, and map their absolute "
            "concentrations across plasma, heart, hypothalamus, adipose tissue and "
            "colostrum. Then repeat the three defining physiological readouts - inotropy in "
            "an isolated heart, blood pressure in vivo, and central vasopressin release - "
            "with each form at matched receptor occupancy rather than matched mass dose. "
            "The prediction from the processing data is that apelin-13 dominates everywhere "
            "and that apelin-36's reported effects are largely a slow-off-rate artefact of "
            "high dosing."),
        experiment_type="quantitative peptidomics plus matched-occupancy pharmacology",
    ),
    dict(
        hypothesis=(
            "Apelin is a paracrine mediator rather than a circulating hormone, so its "
            "molecular-function annotation should be a receptor agonist term and not a "
            "hormone term."),
        description=(
            "Measure the arteriovenous gradient of each apelin form across a defined "
            "vascular bed in vivo, together with interstitial concentration by microdialysis "
            "in heart and skeletal muscle, and compare local concentration with the "
            "receptor's measured affinity in human tissue (pKi about 8.85 for "
            "pyroglutamyl-apelin-13 in human left ventricle). A hormone should reach "
            "receptor-saturating concentrations at the target from the circulation; a "
            "paracrine mediator should show local concentrations far above plasma and a "
            "net release gradient at the site of production."),
        experiment_type="in vivo arteriovenous sampling and microdialysis",
    ),
    dict(
        hypothesis=(
            "Loss of endogenous apelin, as opposed to infusion of exogenous peptide, does "
            "not impair glucose handling - meaning the metabolic literature describes "
            "pharmacology rather than physiology."),
        description=(
            "Phenotype apelin-null mice, which are viable, fertile and outwardly normal, "
            "with a hyperinsulinaemic-euglycaemic clamp and tissue-specific 2-deoxyglucose "
            "uptake on chow and on high-fat diet, alongside wild-type littermates and "
            "alongside wild-type animals receiving an ACE2-resistant apelin analogue. This "
            "is the loss-of-function control the field has never published, and it is the "
            "experiment that decides whether any metabolic GO annotation on this gene is "
            "warranted."),
        experiment_type="mouse metabolic phenotyping of a knockout",
    ),
    dict(
        hypothesis=(
            "The opposite coronary phenotypes of Apln-null and Apela-null mice reflect the "
            "two ligands driving different APLNR output arms rather than different amounts "
            "of the same signal."),
        description=(
            "In sinus-venosus-derived coronary progenitors, compare apelin and ELABELA "
            "head to head for Gi activation, beta-arrestin recruitment and receptor "
            "internalisation at matched occupancy, then test whether a G-protein-biased "
            "apelin analogue such as WN561 and a beta-arrestin-biased one reproduce the "
            "Apln-null and Apela-null coronary phenotypes respectively when delivered to "
            "the developing heart. A bias explanation predicts that the two knockouts can "
            "be phenocopied pharmacologically in wild-type embryos; a dosage explanation "
            "predicts they cannot."),
        experiment_type="biased-agonist pharmacology in a developmental model",
    ),
]

# Per-reference judgments. relevance / correctness / review_notes.
REFERENCE_REVIEWS = {
    "PMID:9792798": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "The deorphanisation of APJ and the paper that named apelin; source of the "
            "77-residue precursor architecture used throughout this review. Cached "
            "abstract only. Verified against the cache: the abstract itself states the "
            "precursor length, the C-terminal location of the peptide, and receptor "
            "activation by synthetic C-terminal peptides at 0.1-100 nM, which is what the "
            "two GO:0005102 and one GO:0007165 TAS rows rest on. Missed by affinage.")),
    "PMID:10525157": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Cited by four GOA rows and is the sole support for both legacy ProtInc "
            "process annotations. Cached abstract only. Verified: it supports secretion "
            "into colostrum and milk quantitatively, and it supports partial suppression "
            "of splenocyte cytokine production - but it reports only expression and "
            "abundance for the mammary gland, which is why the lactation row is removed "
            "here rather than kept. Missed by affinage.")),
    "PMID:11359874": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Source of two human IDA rows and, through rat Apln, of the drinking-behaviour "
            "and blood-pressure ISS/IEA rows. Cached abstract only. Verified: the abstract "
            "supports cAMP inhibition, receptor internalisation, the inactivity of "
            "truncated fragments, reduced vasopressin release and reduced water intake. It "
            "does NOT support a blood-pressure effect - it states the opposite - which is "
            "the donor-side defect recorded on the GO:0045776 rows. Missed by affinage.")),
    "PMID:11384769": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Fetched by this review. The primary demonstration that apelin lowers blood "
            "pressure and that the effect is nitric-oxide dependent; it is what actually "
            "supports the GO:0045776 rows, although no annotation cites it. Cached "
            "abstract only; quantities quoted are from the abstract. Missed by affinage.")),
    "PMID:11815627": dict(
        relevance="MEDIUM", correctness="VERIFIED",
        review_notes=(
            "Fetched by this review. Not about apelin primarily - a survey of 126 peptides "
            "against purified ACE2 - but it is where the single-residue C-terminal "
            "cleavage and the Pro-X(1-3)-Pro-hydrophobic consensus come from, which is "
            "what makes the Phe77 retention claim checkable. Cached abstract only. "
            "Affinage cited a 2005 review for ACE2 cleavage but not this primary source.")),
    "PMID:15231996": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Fetched by this review; full text cached. Establishes apelin-13 and apelin-17 "
            "as the predominant endogenous forms and apelin as a vasopressin "
            "counter-regulator; the basis for the NEW GO:0090278 row and for the proposed "
            "vasopressin-secretion term. Missed by affinage.")),
    "PMID:17673668": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Fetched by this review. The apelin-knockout mouse: viable and outwardly "
            "normal, with progressive loss of cardiac contractility on ageing and pressure "
            "overload. The genetic evidence the GO:0045823 chain lacks, and the control "
            "that shows apelin-null animals have normal water intake. Cached abstract "
            "only. Missed by affinage.")),
    "PMID:18617693": dict(
        relevance="MEDIUM", correctness="VERIFIED",
        review_notes=(
            "Fetched by this review. HIF-1alpha induction of apelin and the knockdown "
            "experiments behind the endothelial-proliferation and angiogenesis claims. "
            "Cached abstract only. Used here for the GO:1905564 row and for the "
            "angiogenesis knowledge gap; note the in vivo angiogenic readout is zebrafish, "
            "which is why no human angiogenesis row is proposed. Affinage cited it.")),
    "PMID:19046574": dict(
        relevance="MEDIUM", correctness="VERIFIED",
        review_notes=(
            "Fetched by this review. The glucose-utilisation work, cited here only in the "
            "metabolic knowledge gap: the perturbation is acute infusion of exogenous "
            "peptide into mice, so it is pharmacology, and no loss-of-function control "
            "exists. Cached abstract only. Missed by affinage.")),
    "PMID:19767528": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Fetched by this review; full text cached. Side-by-side apelin-null and "
            "APJ-null mice - the cleanest statement that ligand and receptor phenotypes "
            "differ, which is the crux of the ELABELA confound on this gene. Missed by "
            "affinage.")),
    "PMID:22810587": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Full text cached. Cited by three GOA rows. The most complete description of "
            "apelin signalling on the human receptor and the basis for the NEW GO:0007193 "
            "row. Its headline claim - that APJ also signals in response to stretch, "
            "independently of apelin - is a receptor property and is correctly not "
            "annotated to APLN anywhere. Missed by affinage.")),
    "PMID:23263626": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Full text cached. Cited by five GOA rows, all in human pulmonary artery "
            "endothelial cells with APLN knockdown and overexpression. Verified including "
            "the authors' own caveat that the endothelial proliferative effect is modest "
            "and contested, which is recorded on the GO:1905564 row rather than omitted. "
            "Missed by affinage.")),
    "PMID:24251091": dict(
        relevance="MEDIUM", correctness="VERIFIED",
        review_notes=(
            "Fetched by this review; full text cached. Direct furin cleavage of proapelin "
            "to apelin-13 with no longer intermediates - the only mechanistic account of "
            "how the annotated gene product becomes the assayed peptide, and the basis for "
            "the processing knowledge gap. Missed by affinage.")),
    "PMID:26611206": dict(
        relevance="MEDIUM", correctness="VERIFIED",
        review_notes=(
            "Fetched by this review as a donor-side source: rat Apln's GO:0045823 IMP and "
            "GO:0031704 IDA both cite it, and both reach human APLN. The paper's subject is "
            "apela/ELABELA, with apelin as the comparator agonist. Cached abstract only, so "
            "the apelin panel itself is not visible; the annotation is not second-guessed "
            "on that basis, but the IMP coding is queried since there is no Apln mutant. "
            "Missed by affinage.")),
    "PMID:27217402": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Fetched by this review. In vivo demonstration that ACE2 inactivates "
            "pyroglutamyl-apelin-13 and apelin-17 and that ACE2 loss potentiates their "
            "hypotensive action; also the source for those two being 'the dominant apelin "
            "peptides'. Cached abstract only. Missed by affinage, which cited a review "
            "instead.")),
    "PMID:28137936": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Full text cached. Cited by four GOA rows. The paper is titled and framed for "
            "ELABELA, which makes it a candidate for mis-attribution, but verification "
            "against the full text shows genuine apelin measurements in every assay it is "
            "cited for: human plasma immunoassay, competition binding in human left "
            "ventricle, cAMP inhibition and beta-arrestin recruitment. So the citations are "
            "right; only two evidence codes (IMP) are questionable. It is also the source "
            "of the paracrine-versus-hormone caveat. Missed by affinage.")),
    "PMID:28890073": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Fetched by this review as a donor-side source; full text cached. The mouse "
            "Apln GO:0060976 IMP cites it, and it reaches human APLN by ISS and IEA. "
            "Verified: the paper's Apln data are a measured negative plus an opposite-sign "
            "phenotype. The citation is correct for the unsigned GO term and incorrect for "
            "the directional wording UniProt derives from it. Missed by affinage.")),
    "PMID:38428423": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Cited by two GOA rows. Cryo-EM of apelin-bound APLNR-Gi1 complexes and the "
            "source of UniProt's SITE 75 and SITE 77 on this entry. Cached abstract only, "
            "so all quotes here are from the abstract. The cache records an erratum (Cell "
            "2026;189:5478); this is a correction, not a retraction, and nothing used here "
            "depends on a detail likely to be affected. The only GOA reference affinage "
            "also cited.")),
    "GO_REF:0000002": dict(
        relevance="MEDIUM", correctness="VERIFIED",
        review_notes=(
            "InterPro2GO. The signature involved, IPR026155 'Apelin', was resolved live to "
            "a 345-protein single-family entry, so the hormone-activity mapping is exact; "
            "the signal-transduction mapping is the one that loses granularity.")),
    "GO_REF:0000024": dict(
        relevance="MEDIUM", correctness="VERIFIED",
        review_notes=(
            "Curator sequence-similarity transfers. Five rows on this gene use it, from "
            "bovine, rat and mouse donors, all Swiss-Prot and all resolved. Sequence "
            "similarity is unusually strong here because the mature peptides are identical "
            "between the donor species and human.")),
    "GO_REF:0000033": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "PAINT. The single IBA row on this gene resolves fully against the committed "
            "PTHR15953 PAINT slice: node PTN001041490, IBD, GO:0005576, Tetrapoda, three "
            "gene-level seeds. The reference is used correctly; the criticism recorded here "
            "is of what PAINT has not yet asserted for this family, not of what it has.")),
    "GO_REF:0000044": dict(
        relevance="MEDIUM", correctness="VERIFIED",
        review_notes=(
            "UniProt subcellular-location vocabulary mapping. Both source terms were "
            "resolved live to 'Extracellular space' and 'Secreted', and the UniProt record "
            "carries them with experimental evidence, so the mapping is faithful.")),
    "GO_REF:0000107": dict(
        relevance="MEDIUM", correctness="VERIFIED",
        review_notes=(
            "Ensembl Compara orthology transfer. Four rows use it. Every donor was resolved "
            "and every donor's own annotation traced to its citation; note that each of "
            "these rows lists the same donor twice, once as a UniProt accession and once as "
            "an Ensembl protein, so the apparent donor count is double the real one.")),
    "GO_REF:0000120": dict(
        relevance="MEDIUM", correctness="VERIFIED",
        review_notes=(
            "Combined automatic annotation. Three rows use it, each combining an ortholog "
            "arm with the InterPro family signature. All three terms are independently "
            "supported by direct human evidence, so the pipeline is confirming rather than "
            "substituting.")),
    "Reactome:R-HSA-374337": dict(
        relevance="MEDIUM", correctness="VERIFIED",
        review_notes=(
            "The cached Reactome entry describes apelin as the endogenous ligand of APJ and "
            "notes the processed peptide forms, so the extracellular placement is sound. "
            "One of four Reactome reactions exporting the same GO:0005576 assertion.")),
    "Reactome:R-HSA-380073": dict(
        relevance="LOW", correctness="VERIFIED",
        review_notes=(
            "A generic Gi-activation reaction, not apelin-specific. The extracellular "
            "placement of the ligand is correct but carries no apelin-specific information; "
            "one of four rows projecting a single curatorial assertion.")),
    "Reactome:R-HSA-749454": dict(
        relevance="LOW", correctness="VERIFIED",
        review_notes=(
            "A generic ligand:GPCR:Gi dissociation reaction. Correct but uninformative "
            "about apelin specifically; one of four rows projecting a single assertion.")),
    "Reactome:R-HSA-749456": dict(
        relevance="LOW", correctness="VERIFIED",
        review_notes=(
            "A generic reaction for liganded Gi-activating GPCRs binding inactive Gi. "
            "Correct but uninformative about apelin specifically; one of four rows "
            "projecting a single assertion.")),
    UNIPROT: dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "The Swiss-Prot record for Q9ULZ1, entry version 169. Used for the precursor "
            "architecture, the PEPTIDE and SITE features, the subcellular location and the "
            "family assignment. Accession confirmed as APEL_HUMAN, 77 aa, not a merged "
            "accession. One caveat is recorded in the review: its FUNCTION line 'Plays a "
            "role in early coronary blood vessels formation (By similarity)' states the "
            "opposite sign to the mouse phenotype it is drawn from.")),
    BIOINF: dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Analyses written for this review. Live fetches from UniProt, InterPro and "
            "RNAcentral plus the committed PAINT slice; no result hardcoded, and the "
            "scripts assert the human precursor length before computing. Supplies the "
            "peptide-conservation numbers, the ACE2 motif count, the resolution of every "
            "WITH/FROM identifier and the GOA-to-YAML reconciliation.")),
    AFFINAGE: dict(
        relevance="MEDIUM", correctness="LOW_QUALITY",
        review_notes=(
            "Trust gates cleared (self_evaluation_pairwise: win, faith_pct 100) and the "
            "record describes the right protein - no symbol collision. Marked LOW_QUALITY "
            "not because it is wrong but because it is a lead list whose bibliography "
            "barely intersects the record under review: of the seven PMIDs cited by GOA "
            "rows on this gene it cites exactly one, and it omits the apelin knockouts, "
            "both donor-side papers behind the ISS chains, the primary ACE2 cleavage "
            "paper, and the fluid-homeostasis pair. Its year column is also unreliable "
            "(several entries dated against the wrong journal year). Used for leads only; "
            "every claim taken from it was re-verified against the PMID, and no GO "
            "grounding was imported from its mechanism profile.")),
}
