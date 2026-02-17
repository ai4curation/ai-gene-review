#!/usr/bin/env python3
"""Generate SMAD3 annotation review by updating the YAML file."""

import yaml
import sys
import copy

# Load existing YAML
with open("/Users/cjm/repos/ai-gene-review/genes/human/SMAD3/SMAD3-ai-review.yaml") as f:
    data = yaml.safe_load(f)

# Update description
data["description"] = (
    "SMAD3 (Mothers against decapentaplegic homolog 3) is a receptor-regulated SMAD (R-SMAD) "
    "that serves as the principal intracellular signal transducer and transcriptional modulator "
    "in the TGF-beta/activin signaling pathway. Upon TGF-beta receptor activation, SMAD3 is "
    "phosphorylated at its C-terminal SSXS motif by TGF-beta type I receptor (ALK5/TGFBR1), "
    "forms heteromeric complexes with SMAD4 (co-SMAD), and translocates to the nucleus where "
    "it directly binds DNA at SMAD binding elements (SBE: GTCT/AGAC) and CAGA-box variants "
    "through its MH1 domain. SMAD3 cooperates with transcription factors such as c-Jun/c-Fos "
    "at composite AP-1/SMAD elements. It also participates in activin and nodal signaling. "
    "Key biological outcomes include regulation of cell proliferation, EMT, fibrosis, immune "
    "regulation, and cell differentiation. Germline mutations cause Loeys-Dietz syndrome type 3."
)
data["status"] = "IN_PROGRESS"

# Define review decisions for each annotation
# We process by building a lookup based on (GO_ID, evidence_type, reference)
# For annotations with identical keys, we process them in order

def make_review(summary, action, reason, supported_by=None, proposed_replacement_terms=None, additional_reference_ids=None):
    review = {
        "summary": summary,
        "action": action,
        "reason": reason,
    }
    if supported_by:
        review["supported_by"] = supported_by
    if proposed_replacement_terms:
        review["proposed_replacement_terms"] = proposed_replacement_terms
    if additional_reference_ids:
        review["additional_reference_ids"] = additional_reference_ids
    return review


# ---- Core function annotations (IBA) ----
IBA_CORE = {
    "GO:0000978": make_review(
        summary="SMAD3 directly binds DNA at SMAD binding elements (SBEs) in cis-regulatory regions of target genes, demonstrated by crystal structure (PMID:9741623), CASTing assays (Itoh et al. 2024), and ChIP-seq studies. IBA is well-supported across SMAD family.",
        action="ACCEPT",
        reason="Core molecular function of SMAD3. The MH1 domain directly binds SBE sequences (GTCT/AGAC) in promoter/enhancer regions, extensively validated by structural and functional studies.",
        supported_by=[
            {"reference_id": "PMID:9741623", "supporting_text": "Crystal structure of a Smad MH1 domain bound to DNA: insights on DNA binding in TGF-beta signaling"},
            {"reference_id": "PMID:9732876", "supporting_text": "Smad3 interacts directly with the TRE and that Smad3 and Smad4 can activate TGF-beta-inducible transcription from the TRE"},
        ],
    ),
    "GO:0000981": make_review(
        summary="SMAD3 is a sequence-specific DNA-binding transcription factor that activates and represses RNA polymerase II target genes in response to TGF-beta signaling. IBA supported across the SMAD family.",
        action="ACCEPT",
        reason="Core molecular function. SMAD3 directly binds DNA through its MH1 domain and recruits transcriptional coactivators (p300/CBP) or corepressors (Ski/SnoN, TGIF) to regulate Pol II transcription.",
        supported_by=[
            {"reference_id": "PMID:9732876", "supporting_text": "Smad3 and Smad4 cooperate with c-Jun/c-Fos to mediate TGF-beta-induced transcription"},
            {"reference_id": "PMID:21947082", "supporting_text": "USP15 is required for TGFbeta and BMP responses in mammalian cells"},
        ],
    ),
    "GO:0060395_iba": make_review(
        summary="SMAD3 is a core component of the SMAD protein signal transduction pathway. Upon TGF-beta receptor activation, SMAD3 is phosphorylated, complexes with SMAD4, and translocates to the nucleus. IBA well-supported.",
        action="ACCEPT",
        reason="Core biological process. SMAD3 is one of the principal R-SMADs mediating TGF-beta/activin signal transduction through the canonical SMAD pathway.",
        supported_by=[
            {"reference_id": "PMID:9311995", "supporting_text": "TGF-beta induces heteromeric complexes of Smads 2, 3 and 4, and their concomitant translocation to the nucleus, which is required for efficient TGF-beta signal transduction"},
            {"reference_id": "PMID:8774881", "supporting_text": "hMAD-3 but not hMAD-4 was phosphorylated and associated with the ligand-bound receptor complex"},
        ],
    ),
    "GO:0007179_iba": make_review(
        summary="SMAD3 is a key intracellular mediator of TGF-beta receptor signaling. Activated by TGFBR1/ALK5 phosphorylation. IBA well-supported.",
        action="ACCEPT",
        reason="Core biological process. SMAD3 is phosphorylated directly by the TGF-beta type I receptor and is essential for canonical TGF-beta signal transduction.",
        supported_by=[
            {"reference_id": "PMID:8774881", "supporting_text": "The activity of hMAD-3 and -4 was regulated by the TGF-beta receptors, and hMAD-3 but not hMAD-4 was phosphorylated and associated with the ligand-bound receptor complex"},
            {"reference_id": "PMID:9311995", "supporting_text": "Smad2 and Smad3 interacted with the kinase-deficient TGF-beta type I receptor"},
        ],
    ),
    "GO:0032924_iba": make_review(
        summary="SMAD3 also mediates activin receptor signaling, being phosphorylated by ACVR1B. IBA well-supported.",
        action="ACCEPT",
        reason="Core biological process. SMAD3 is activated by activin type I receptor (ACVR1B/ALK4) in addition to TGF-beta receptors. UniProt confirms interaction with ACVR1B (PMID:9892009).",
        supported_by=[
            {"reference_id": "PMID:9892009", "supporting_text": "Roles of pathway-specific and inhibitory Smads in activin receptor signaling"},
        ],
    ),
    "GO:0071144_iba": make_review(
        summary="SMAD3 forms heteromeric SMAD complexes with SMAD4 upon TGF-beta stimulation. IBA well-supported across species.",
        action="ACCEPT",
        reason="Core cellular component. The SMAD3/SMAD4 heteromeric complex is the functional unit of TGF-beta signaling. Crystal structure solved (PMID:15350224).",
        supported_by=[
            {"reference_id": "PMID:9311995", "supporting_text": "TGF-beta induces heteromeric complexes of Smads 2, 3 and 4"},
        ],
    ),
    "GO:0045944_iba": make_review(
        summary="SMAD3 positively regulates transcription by RNA polymerase II at TGF-beta target gene promoters. IBA supported.",
        action="ACCEPT",
        reason="Core biological process. SMAD3/SMAD4 complexes recruit p300/CBP coactivators to activate transcription of TGF-beta responsive genes.",
        supported_by=[
            {"reference_id": "PMID:9732876", "supporting_text": "Smad3 and Smad4 also act together with c-Jun and c-Fos to activate transcription in response to TGF-beta"},
        ],
    ),
    "GO:0070411": make_review(
        summary="SMAD3 binds inhibitory SMADs (SMAD6/SMAD7). IBA supported across the SMAD family.",
        action="ACCEPT",
        reason="Well-established interaction. Inhibitory SMADs compete with R-SMADs for receptor binding and recruit phosphatases/ubiquitin ligases. SMAD3 binds SMAD7 as part of pathway regulation.",
    ),
    "GO:0009653": make_review(
        summary="SMAD3 is involved in anatomical structure morphogenesis via TGF-beta signaling. IBA supported across species.",
        action="KEEP_AS_NON_CORE",
        reason="This is a broad downstream biological process. While SMAD3 contributes to morphogenesis through TGF-beta signaling, this is a pleiotropic outcome rather than a core function. IBA is valid at this level for SMAD family.",
    ),
    "GO:0030154": make_review(
        summary="SMAD3 is involved in cell differentiation through TGF-beta signaling. IBA supported.",
        action="KEEP_AS_NON_CORE",
        reason="Broad downstream process. TGF-beta/SMAD3 signaling regulates differentiation in many contexts (chondrocyte, osteoblast, T cell, etc.), but this is a pleiotropic outcome rather than core function.",
    ),
}

# Build review for each annotation
for ann in data["existing_annotations"]:
    go_id = ann["term"]["id"]
    go_label = ann["term"]["label"]
    ev = ann["evidence_type"]
    ref = ann.get("original_reference_id", "")

    # ====================
    # IBA ANNOTATIONS
    # ====================
    if ev == "IBA":
        if go_id == "GO:0000978":
            ann["review"] = IBA_CORE["GO:0000978"]
        elif go_id == "GO:0000981":
            ann["review"] = IBA_CORE["GO:0000981"]
        elif go_id == "GO:0060395":
            ann["review"] = IBA_CORE["GO:0060395_iba"]
        elif go_id == "GO:0007179":
            ann["review"] = IBA_CORE["GO:0007179_iba"]
        elif go_id == "GO:0032924":
            ann["review"] = IBA_CORE["GO:0032924_iba"]
        elif go_id == "GO:0071144":
            ann["review"] = IBA_CORE["GO:0071144_iba"]
        elif go_id == "GO:0045944":
            ann["review"] = IBA_CORE["GO:0045944_iba"]
        elif go_id == "GO:0070411":
            ann["review"] = IBA_CORE["GO:0070411"]
        elif go_id == "GO:0009653":
            ann["review"] = IBA_CORE["GO:0009653"]
        elif go_id == "GO:0030154":
            ann["review"] = IBA_CORE["GO:0030154"]
        else:
            ann["review"] = make_review(
                summary=f"IBA annotation for {go_label} - unexpected IBA term for SMAD3.",
                action="UNDECIDED",
                reason="IBA annotation not matching expected SMAD family patterns.",
            )

    # ====================
    # PROTEIN BINDING (IPI) - always mark as uninformative
    # ====================
    elif go_id == "GO:0005515" and ev == "IPI":
        ann["review"] = make_review(
            summary=f"Protein binding annotation from high-throughput or targeted interaction study ({ref}). SMAD3 interacts with numerous proteins as a signaling hub.",
            action="REMOVE",
            reason="'Protein binding' (GO:0005515) is uninformative for a transcription factor and signaling hub like SMAD3. More specific binding terms (co-SMAD binding, R-SMAD binding, TF binding, ubiquitin ligase binding) are preferred and already present in the annotation set.",
        )

    # ====================
    # IEA ANNOTATIONS - broad electronic annotations
    # ====================
    elif ev == "IEA":
        if go_id == "GO:0003677":
            ann["review"] = make_review(
                summary="IEA for DNA binding. SMAD3 directly binds DNA through MH1 domain at SBE sequences.",
                action="ACCEPT",
                reason="Correct but overly broad. More specific DNA binding terms (GO:0000978, GO:0000987) are already annotated with experimental evidence. This IEA is acceptable as a general parent term.",
            )
        elif go_id == "GO:0005634":
            ann["review"] = make_review(
                summary="IEA for nucleus localization. SMAD3 translocates to nucleus upon TGF-beta stimulation.",
                action="ACCEPT",
                reason="Well-supported. SMAD3 is found in nucleus upon activation. Multiple IDA annotations also confirm this.",
            )
        elif go_id == "GO:0005667":
            ann["review"] = make_review(
                summary="IEA for transcription regulator complex. SMAD3 forms complexes with SMAD4 and other transcription factors.",
                action="ACCEPT",
                reason="Correct. SMAD3/SMAD4 complexes function as transcription regulator complexes. Also supported by IDA (PMID:21947082).",
            )
        elif go_id == "GO:0005737":
            ann["review"] = make_review(
                summary="IEA for cytoplasm localization. SMAD3 resides in cytoplasm when inactive.",
                action="ACCEPT",
                reason="Well-supported. SMAD3 shuttles between cytoplasm and nucleus, residing primarily in cytoplasm before TGF-beta stimulation.",
            )
        elif go_id == "GO:0006355" and ref == "GO_REF:0000120":
            ann["review"] = make_review(
                summary="IEA for regulation of DNA-templated transcription based on InterPro domain mapping.",
                action="ACCEPT",
                reason="Correct. SMAD3 is a transcription factor that regulates DNA-templated transcription. Consistent with experimental annotations.",
            )
        elif go_id == "GO:0032502":
            ann["review"] = make_review(
                summary="IEA for developmental process. Very broad term from ARBA prediction.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Excessively broad. While TGF-beta/SMAD3 signaling contributes to development, GO:0032502 is too general to be informative. More specific developmental processes are annotated elsewhere.",
            )
        elif go_id == "GO:0046872":
            ann["review"] = make_review(
                summary="IEA for metal ion binding from UniProt keyword mapping. SMAD3 MH1 domain coordinates a zinc ion essential for DNA binding.",
                action="MODIFY",
                reason="The annotation is correct in that SMAD3 binds metal ions, but the term is too broad. The MH1 domain contains a zinc-binding site essential for structural integrity and DNA binding (PMID:12686552). Should be zinc ion binding (GO:0008270) which is already annotated with IDA.",
                proposed_replacement_terms=[{"id": "GO:0008270", "label": "zinc ion binding"}],
            )
        elif go_id == "GO:0071363":
            ann["review"] = make_review(
                summary="IEA for cellular response to growth factor stimulus. SMAD3 mediates TGF-beta responses.",
                action="ACCEPT",
                reason="Correct but broad. SMAD3 mediates cellular responses to TGF-beta and activin, which are growth factors. More specific pathway terms are also annotated.",
            )
        elif go_id == "GO:0141091":
            ann["review"] = make_review(
                summary="IEA for TGF-beta receptor superfamily signaling pathway from ARBA.",
                action="ACCEPT",
                reason="Correct. SMAD3 is a core mediator of TGF-beta receptor superfamily signaling. More specific TGF-beta pathway terms are also present.",
            )
        # Ensembl IEA annotations (GO_REF:0000107)
        elif go_id == "GO:0000122":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for negative regulation of Pol II transcription. SMAD3 can also repress transcription at certain loci.",
                action="ACCEPT",
                reason="SMAD3 acts as both transcriptional activator and repressor depending on context and cofactors (Ski/SnoN, TGIF). Also supported by IDA (PMID:28467929).",
            )
        elif go_id == "GO:0000165":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for MAPK cascade.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="SMAD3 is not a core component of the MAPK cascade. While MAPK phosphorylates SMAD3 linker region, and SMAD3/AP-1 cooperate at promoters, SMAD3 does not directly participate in the MAPK cascade itself. Cross-talk annotation is misleading.",
            )
        elif go_id == "GO:0000977":
            ann["review"] = make_review(
                summary="IEA (Ensembl/UniProt) for RNA polymerase II transcription regulatory region sequence-specific DNA binding.",
                action="ACCEPT",
                reason="Correct. SMAD3 binds SBE sequences in Pol II regulatory regions. Also supported by IDA annotations.",
            )
        elif go_id == "GO:0001228" and ev == "IEA":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for DNA-binding transcription activator activity, Pol II-specific.",
                action="ACCEPT",
                reason="Correct. SMAD3 activates Pol II transcription at TGF-beta target genes. Also supported by multiple IDA annotations.",
            )
        elif go_id == "GO:0001649":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for osteoblast differentiation from mouse data.",
                action="KEEP_AS_NON_CORE",
                reason="Valid downstream effect. SMAD3 regulates osteoblast differentiation and chondrogenesis (UniProt confirms SMAD3 is a regulator of osteogenesis). Non-core pleiotropic process.",
            )
        elif go_id == "GO:0001657":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for ureteric bud development from mouse data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Very specific developmental process likely reflecting pleiotropic TGF-beta pathway effects in kidney development. No direct evidence for SMAD3-specific role in ureteric bud development in humans.",
            )
        elif go_id == "GO:0001836":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for release of cytochrome c from mitochondria from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Indirect downstream effect. TGF-beta/SMAD3 signaling can trigger apoptosis in some contexts, which may involve cytochrome c release, but this is not a direct function of SMAD3.",
            )
        elif go_id == "GO:0003682":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for chromatin binding from mouse data.",
                action="ACCEPT",
                reason="Correct. SMAD3 binds chromatin at enhancer/promoter regions. Also supported by IDA chromatin localization (PMID:21828274).",
            )
        elif go_id == "GO:0003690":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for double-stranded DNA binding from mouse data.",
                action="ACCEPT",
                reason="Correct. Crystal structure confirms SMAD3 MH1 domain binds dsDNA at SBE sequences (PMID:9741623, PMID:12686552).",
            )
        elif go_id == "GO:0003700" and ev == "IEA":
            ann["review"] = make_review(
                summary="IEA for DNA-binding transcription factor activity.",
                action="ACCEPT",
                reason="Correct. SMAD3 is a bona fide DNA-binding transcription factor. Also supported by multiple IDA annotations.",
            )
        elif go_id == "GO:0005518":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for collagen binding from mouse data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="SMAD3 regulates collagen gene expression as a transcription factor, but there is no evidence it directly binds collagen protein. This appears to be a misannotation or conflation of transcriptional regulation with physical binding.",
            )
        elif go_id == "GO:0005886":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for plasma membrane localization from mouse data.",
                action="KEEP_AS_NON_CORE",
                reason="SMAD3 can associate with TGF-beta receptors at the plasma membrane during initial activation, but its primary functional locations are cytoplasm and nucleus. Plasma membrane localization is transient.",
            )
        elif go_id in ("GO:0007179",) and ref == "GO_REF:0000107":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for TGF-beta receptor signaling pathway from rat orthologs.",
                action="ACCEPT",
                reason="Correct. Core biological process for SMAD3. Also supported by multiple IDA and IMP annotations.",
            )
        elif go_id == "GO:0007254":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for JNK cascade from mouse data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="SMAD3 is not a component of the JNK cascade. While TGF-beta can activate JNK through non-canonical signaling and SMAD3/JUN cooperate at AP-1 sites, SMAD3 does not participate directly in JNK signal transduction.",
            )
        elif go_id == "GO:0008013":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for beta-catenin binding from rat data.",
                action="UNDECIDED",
                reason="There are reports of TGF-beta/SMAD3 and Wnt/beta-catenin pathway crosstalk, but direct SMAD3-beta-catenin binding evidence in human is limited. Unable to verify without accessing primary reference.",
            )
        elif go_id == "GO:0008285" and ev == "IEA":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for negative regulation of cell population proliferation from rat data.",
                action="KEEP_AS_NON_CORE",
                reason="Valid downstream effect. TGF-beta/SMAD3 signaling inhibits cell proliferation through transcriptional regulation of CDK inhibitors (p15, p21). Also supported by IMP (PMID:14555988). Non-core pleiotropic process.",
            )
        elif go_id == "GO:0010332":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for response to gamma radiation from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Indirect response. While SMAD3 may be activated or its expression altered by gamma radiation in some cell types, this is not a direct or core function of SMAD3.",
            )
        elif go_id == "GO:0010467":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for gene expression from mouse data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Excessively broad. 'Gene expression' is too general. SMAD3 regulates transcription, which is a component of gene expression, but more specific terms are already annotated.",
            )
        elif go_id == "GO:0019899":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for enzyme binding from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="While SMAD3 binds kinases (TGFBR1, CDKs, PDPK1), phosphatases (PPM1A), and E3 ligases, 'enzyme binding' is too broad. More specific binding terms are already present.",
            )
        elif go_id == "GO:0023019":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for signal transduction involved in regulation of gene expression from rat data.",
                action="ACCEPT",
                reason="Correct description of SMAD3 core function: signal transduction (TGF-beta pathway) that directly regulates gene expression.",
            )
        elif go_id == "GO:0030325":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for adrenal gland development from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Very specific developmental process likely reflecting broad TGF-beta pathway pleiotropic effects. No direct evidence for SMAD3-specific role in human adrenal development.",
            )
        elif go_id == "GO:0030335":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for positive regulation of cell migration from rat data.",
                action="KEEP_AS_NON_CORE",
                reason="Valid downstream effect. TGF-beta/SMAD3 signaling promotes cell migration, particularly in EMT context. UniProt notes SMAD3 role in EMT. Non-core pleiotropic process.",
            )
        elif go_id == "GO:0030501":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for positive regulation of bone mineralization from rat data.",
                action="KEEP_AS_NON_CORE",
                reason="Valid downstream effect. UniProt notes SMAD3 is a regulator of osteogenesis. Non-core tissue-specific process.",
            )
        elif go_id == "GO:0031490":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for chromatin DNA binding from mouse data.",
                action="ACCEPT",
                reason="Correct. SMAD3 binds DNA within chromatin context at enhancers and promoters. Supported by ChIP studies.",
            )
        elif go_id == "GO:0032332":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for positive regulation of chondrocyte differentiation from mouse data.",
                action="KEEP_AS_NON_CORE",
                reason="Valid downstream effect. UniProt notes SMAD3 is a regulator of chondrogenesis. Non-core developmental process.",
            )
        elif go_id == "GO:0032731":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for positive regulation of IL-1 beta production from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Indirect downstream effect of TGF-beta signaling in immune regulation. Not a direct function of SMAD3 as a transcription factor.",
            )
        elif go_id == "GO:0032916":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for positive regulation of TGF-beta3 production from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="While SMAD3 could transcriptionally regulate TGF-beta3 expression as a feedback mechanism, this is a very specific downstream effect. Limited direct human evidence.",
            )
        elif go_id == "GO:0032993":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for protein-DNA complex from mouse data.",
                action="ACCEPT",
                reason="Correct. SMAD3 forms protein-DNA complexes at SBE-containing regulatory regions. Crystal structure of SMAD3 MH1-DNA complex solved (PMID:12686552).",
            )
        elif go_id == "GO:0033689":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for negative regulation of osteoblast proliferation from mouse data.",
                action="KEEP_AS_NON_CORE",
                reason="Valid downstream effect consistent with SMAD3 role in osteogenesis regulation. Non-core tissue-specific process.",
            )
        elif go_id == "GO:0036120":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for cellular response to PDGF stimulus from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Indirect. PDGF may modulate TGF-beta/SMAD signaling through MAPK crosstalk, but SMAD3 is not a direct mediator of PDGF responses.",
            )
        elif go_id == "GO:0042110":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for T cell activation from mouse data.",
                action="KEEP_AS_NON_CORE",
                reason="Valid downstream effect. TGF-beta/SMAD3 signaling is critical for T cell differentiation and immune regulation. SMAD3 knockout mice have T cell activation defects. Non-core immune process.",
            )
        elif go_id == "GO:0042177":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for negative regulation of protein catabolic process from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Indirect downstream effect. While TGF-beta signaling can affect protein stability, this is not a direct SMAD3 function.",
            )
        elif go_id == "GO:0042220":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for response to cocaine from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Highly specific environmental response likely from rat neurological studies. No evidence SMAD3 directly mediates cocaine responses. Over-annotation from ortholog transfer.",
            )
        elif go_id == "GO:0042802" and ev == "IEA":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for identical protein binding from mouse data.",
                action="ACCEPT",
                reason="Correct. SMAD3 forms homomeric complexes. SMAD3 homo-oligomerization is well-documented (PMID:9670020).",
            )
        elif go_id == "GO:0043066":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for negative regulation of apoptotic process from rat data.",
                action="KEEP_AS_NON_CORE",
                reason="Context-dependent downstream effect. TGF-beta/SMAD3 can both promote and inhibit apoptosis depending on cell type. Non-core pleiotropic process.",
            )
        elif go_id == "GO:0043565":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for sequence-specific DNA binding from rat data.",
                action="ACCEPT",
                reason="Correct. SMAD3 MH1 domain binds specific DNA sequences (SBE: GTCT/AGAC). Crystal structure confirms sequence-specific binding (PMID:9741623).",
            )
        elif go_id == "GO:0045429" and ev == "IEA":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for positive regulation of nitric oxide biosynthesis from rat data.",
                action="KEEP_AS_NON_CORE",
                reason="Context-dependent downstream effect. TGF-beta/SMAD3 can regulate iNOS expression in certain cell types. Also supported by IDA (PMID:27038547). Non-core process.",
            )
        elif go_id == "GO:0045944" and ev == "IEA":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for positive regulation of Pol II transcription from rat data.",
                action="ACCEPT",
                reason="Correct. SMAD3 activates Pol II transcription. Also supported by IBA and IMP annotations.",
            )
        elif go_id == "GO:0050728" and ev == "IEA":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for negative regulation of inflammatory response from mouse data.",
                action="KEEP_AS_NON_CORE",
                reason="Valid downstream effect. TGF-beta/SMAD3 is a key anti-inflammatory pathway. Also supported by NAS (ComplexPortal). Non-core immune process.",
            )
        elif go_id == "GO:0050776":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for regulation of immune response from mouse data.",
                action="KEEP_AS_NON_CORE",
                reason="Valid broad downstream effect. TGF-beta/SMAD3 is critical for immune regulation. Non-core pleiotropic process.",
            )
        elif go_id == "GO:0050821":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for protein stabilization from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Indirect effect. While SMAD3 can affect protein stability through transcriptional regulation of ubiquitin pathway components, protein stabilization is not a direct function.",
            )
        elif go_id == "GO:0050927":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for positive regulation of positive chemotaxis from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Indirect downstream effect of TGF-beta signaling. Not a direct SMAD3 function.",
            )
        elif go_id == "GO:0051496":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for positive regulation of stress fiber assembly from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Indirect downstream effect. TGF-beta can promote stress fiber formation through EMT-related cytoskeletal remodeling, but this is not a direct SMAD3 transcription factor function.",
            )
        elif go_id == "GO:0051881":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for regulation of mitochondrial membrane potential from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Indirect downstream effect. Not a direct function of SMAD3 as a transcription factor.",
            )
        elif go_id == "GO:0051894":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for positive regulation of focal adhesion assembly from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Indirect downstream effect of TGF-beta-mediated EMT or cytoskeletal changes. Not a direct SMAD3 function.",
            )
        elif go_id == "GO:0060290":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for transdifferentiation from rat data.",
                action="KEEP_AS_NON_CORE",
                reason="Valid downstream effect. TGF-beta/SMAD3 drives EMT (a form of transdifferentiation). Non-core pleiotropic process.",
            )
        elif go_id == "GO:0060395" and ev == "IEA":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for SMAD protein signal transduction from rat data.",
                action="ACCEPT",
                reason="Correct. Core biological process. Also supported by multiple IBA and IDA annotations.",
            )
        elif go_id == "GO:0061001":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for regulation of dendritic spine morphogenesis from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Very specific neuronal process. Likely indirect TGF-beta pathway effect. No direct evidence for SMAD3-specific role in dendritic spine morphogenesis in humans.",
            )
        elif go_id == "GO:0061045":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for negative regulation of wound healing from mouse data.",
                action="KEEP_AS_NON_CORE",
                reason="Valid downstream effect. UniProt notes SMAD3 has inhibitory effect on wound healing. Non-core tissue-specific process.",
            )
        elif go_id == "GO:0061629" and ev == "IEA":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for RNA polymerase II-specific DNA-binding TF binding from mouse data.",
                action="ACCEPT",
                reason="Correct. SMAD3 binds other Pol II TFs (c-Jun, c-Fos, FOXH1, etc.). Also supported by IPI annotations.",
            )
        elif go_id == "GO:0061767":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for negative regulation of lung blood pressure from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Very specific physiological process likely from rat cardiovascular studies. Indirect downstream effect of TGF-beta signaling.",
            )
        elif go_id == "GO:0071333":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for cellular response to glucose stimulus from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Indirect. TGF-beta/SMAD signaling may be modulated by metabolic conditions, but SMAD3 is not a direct glucose sensor.",
            )
        elif go_id == "GO:0071560" and ev == "IEA":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for cellular response to TGF-beta stimulus from rat data.",
                action="ACCEPT",
                reason="Correct. Core biological process. SMAD3 is a primary mediator of cellular responses to TGF-beta. Also supported by IDA (PMID:12902338).",
            )
        elif go_id == "GO:0090263":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for positive regulation of canonical Wnt signaling pathway from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="SMAD3 is not a direct component of the Wnt pathway. While there is TGF-beta/Wnt pathway crosstalk, annotating SMAD3 to Wnt pathway regulation is misleading.",
            )
        elif go_id == "GO:0097191" and ev == "IEA":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for extrinsic apoptotic signaling pathway from rat data.",
                action="KEEP_AS_NON_CORE",
                reason="Valid downstream effect. TGF-beta can trigger apoptosis through SMAD3-dependent transcriptional programs. Also supported by IMP (PMID:15334054). Non-core process.",
            )
        elif go_id == "GO:0097305":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for response to alcohol from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Likely from rat liver/fibrosis studies where alcohol induces TGF-beta signaling. Not a direct SMAD3 function.",
            )
        elif go_id == "GO:0098586":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for cellular response to virus from mouse data.",
                action="KEEP_AS_NON_CORE",
                reason="TGF-beta/SMAD3 signaling is involved in antiviral responses and immune regulation. SARS-CoV nucleoprotein interacts with SMAD3 (PMID:18055455). Non-core immune process.",
            )
        elif go_id == "GO:1903243":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for negative regulation of cardiac muscle hypertrophy from rat data.",
                action="MARK_AS_OVER_ANNOTATED",
                reason="Very specific cardiac process. Indirect TGF-beta pathway effect. Not a direct SMAD3 function.",
            )
        elif go_id == "GO:1990841":
            ann["review"] = make_review(
                summary="IEA (Ensembl orthologs) for promoter-specific chromatin binding from mouse data.",
                action="ACCEPT",
                reason="Correct. SMAD3 binds chromatin at specific promoters of TGF-beta target genes.",
            )
        else:
            # Catch-all for remaining IEA
            ann["review"] = make_review(
                summary=f"IEA annotation for {go_label}. Electronic annotation transferred from ortholog or domain mapping.",
                action="UNDECIDED",
                reason="IEA annotation requires further review to determine if the function is directly attributable to SMAD3 in humans.",
            )

    # ====================
    # IDENTICAL PROTEIN BINDING (IPI)
    # ====================
    elif go_id == "GO:0042802" and ev == "IPI":
        ann["review"] = make_review(
            summary="SMAD3 forms homo-oligomers. Confirmed by co-immunoprecipitation and structural studies.",
            action="ACCEPT",
            reason="SMAD3 homo-oligomerization is well-documented. Crystal structure shows SMAD3 trimeric assembly (PMID:11224571).",
            supported_by=[
                {"reference_id": "PMID:11224571", "supporting_text": "The L3 loop and C-terminal phosphorylation jointly define Smad protein trimerization"},
            ],
        )

    # ====================
    # SPECIFIC MF BINDING TERMS (IPI)
    # ====================
    elif go_id == "GO:0070410":
        ann["review"] = make_review(
            summary=f"co-SMAD binding confirmed. SMAD3 directly binds SMAD4 via MH2 domain to form the transcriptionally active heteromeric complex ({ref}).",
            action="ACCEPT",
            reason="Core molecular function. SMAD3-SMAD4 interaction is the central event in TGF-beta signal transduction.",
            supported_by=[
                {"reference_id": "PMID:9311995", "supporting_text": "Smads 2 and 3 interacted with Smad4 after TbetaR activation in transfected COS cells"},
            ],
        )
    elif go_id == "GO:0070412":
        ann["review"] = make_review(
            summary=f"R-SMAD binding confirmed. SMAD3 binds other R-SMADs (SMAD2) and itself ({ref}).",
            action="ACCEPT",
            reason="Well-supported interaction. SMAD3 interacts with SMAD2 as part of the TGF-beta signaling pathway.",
            supported_by=[
                {"reference_id": "PMID:9311995", "supporting_text": "we observed TbetaR-activation-dependent interaction between Smad2 and Smad3"},
            ],
        )
    elif go_id == "GO:0031625":
        ann["review"] = make_review(
            summary=f"Ubiquitin protein ligase binding confirmed. SMAD3 interacts with E3 ligases including SMURF2, NEDD4L, STUB1/CHIP ({ref}).",
            action="ACCEPT",
            reason="Well-supported. SMAD3 is a substrate of multiple E3 ubiquitin ligases that regulate its stability and function.",
        )
    elif go_id == "GO:0001222":
        ann["review"] = make_review(
            summary=f"Transcription corepressor binding confirmed. SMAD3 interacts with corepressors including Ski, SnoN, TGIF ({ref}).",
            action="ACCEPT",
            reason="Well-supported. SMAD3 recruits transcriptional corepressors at certain target genes.",
        )
    elif go_id == "GO:0001223":
        ann["review"] = make_review(
            summary=f"Transcription coactivator binding confirmed. SMAD3 interacts with coactivators including p300/CBP, ZMIZ1 ({ref}).",
            action="ACCEPT",
            reason="Well-supported. SMAD3 linker region and MH2 domain recruit p300/CBP coactivators.",
        )
    elif go_id == "GO:0017151":
        ann["review"] = make_review(
            summary=f"DEAD/H-box RNA helicase binding. SMAD3 interacts with DDX5 (p68) ({ref}).",
            action="ACCEPT",
            reason="Documented interaction. DDX5/p68 modulates SMAD3-dependent transcription.",
        )
    elif go_id == "GO:0016922":
        ann["review"] = make_review(
            summary=f"Nuclear receptor binding. SMAD3 binds PPARgamma ({ref}).",
            action="ACCEPT",
            reason="Well-documented interaction. SMAD3 interacts with nuclear receptors as part of transcriptional cross-talk.",
        )
    elif go_id == "GO:0061629" and ev == "IPI":
        ann["review"] = make_review(
            summary=f"SMAD3 binds Pol II-specific DNA-binding TFs including c-Jun, c-Fos, PAX6 ({ref}).",
            action="ACCEPT",
            reason="Core molecular function. SMAD3 cooperates with other TFs at composite promoter elements.",
            supported_by=[
                {"reference_id": "PMID:9732876", "supporting_text": "Smad3 and Smad4 also act together with c-Jun and c-Fos to activate transcription in response to TGF-beta, through a TGF-beta-inducible association of c-Jun with Smad3 and an interaction of Smad3 and c-Fos"},
            ],
        )
    elif go_id == "GO:0140297":
        ann["review"] = make_review(
            summary=f"DNA-binding transcription factor binding. SMAD3 binds FOXH1 ({ref}).",
            action="ACCEPT",
            reason="Well-supported. SMAD3 cooperates with multiple DNA-binding TFs.",
        )
    elif go_id == "GO:0043425":
        ann["review"] = make_review(
            summary=f"bHLH transcription factor binding. SMAD3 binds HEB/TCF12 ({ref}).",
            action="ACCEPT",
            reason="Documented interaction between SMAD3 and bHLH TFs at target gene promoters.",
        )
    elif go_id == "GO:0019901":
        ann["review"] = make_review(
            summary=f"Protein kinase binding. SMAD3 binds CDK8/CDK9 ({ref}).",
            action="ACCEPT",
            reason="SMAD3 interacts with kinases including CDK8/9 that phosphorylate its linker region.",
        )
    elif go_id == "GO:0019902":
        ann["review"] = make_review(
            summary=f"Phosphatase binding. SMAD3 binds PPM1A ({ref}).",
            action="ACCEPT",
            reason="Well-documented. PPM1A dephosphorylates SMAD3 C-terminal SSXS motif to terminate TGF-beta signaling (PMID:16751101).",
        )
    elif go_id == "GO:0043130":
        ann["review"] = make_review(
            summary=f"Ubiquitin binding confirmed ({ref}). SMAD3 is subject to monoubiquitination that regulates DNA binding.",
            action="ACCEPT",
            reason="Well-supported by PMID:18794808 and PMID:21947082. Monoubiquitination of SMAD3 prevents DNA binding; USP15 deubiquitination restores it.",
        )
    elif go_id == "GO:0032810":
        ann["review"] = make_review(
            summary=f"Sterol response element binding. SMAD3 binds SRE in IGI with TGF-beta1 ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Specialized binding activity at specific genomic loci. Non-core but documented.",
        )
    elif go_id == "GO:0031962":
        ann["review"] = make_review(
            summary=f"Nuclear mineralocorticoid receptor binding. SMAD3 interacts with NR3C2 ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Documented interaction representing transcriptional cross-talk between TGF-beta and mineralocorticoid signaling.",
        )
    elif go_id == "GO:0035259":
        ann["review"] = make_review(
            summary=f"Nuclear glucocorticoid receptor binding. SMAD3 interacts with NR3C1 ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Documented interaction representing transcriptional cross-talk between TGF-beta and glucocorticoid signaling.",
        )
    elif go_id == "GO:0008270":
        ann["review"] = make_review(
            summary=f"Zinc ion binding confirmed ({ref}). SMAD3 MH1 domain coordinates zinc via Cys and His residues.",
            action="ACCEPT",
            reason="Crystal structure confirms zinc coordination in MH1 domain essential for DNA binding (PMID:12686552).",
        )

    # ====================
    # DNA BINDING MF (IDA, IMP, ISA)
    # ====================
    elif go_id == "GO:0003700" and ev in ("IDA", "IMP"):
        ann["review"] = make_review(
            summary=f"DNA-binding transcription factor activity confirmed by experimental evidence ({ref}).",
            action="ACCEPT",
            reason="Core molecular function of SMAD3. Directly binds DNA and regulates transcription.",
        )
    elif go_id == "GO:0000978" and ev in ("IDA", "IMP"):
        ann["review"] = make_review(
            summary=f"RNA polymerase II cis-regulatory region sequence-specific DNA binding confirmed ({ref}).",
            action="ACCEPT",
            reason="Core molecular function. SMAD3 binds SBEs in Pol II-regulated cis-regulatory regions.",
        )
    elif go_id == "GO:0000987" and ev in ("IDA", "IMP", "IC"):
        ann["review"] = make_review(
            summary=f"Cis-regulatory region sequence-specific DNA binding confirmed ({ref}).",
            action="ACCEPT",
            reason="Core molecular function. SMAD3 binds SBE sequences in cis-regulatory regions.",
        )
    elif go_id == "GO:0001228" and ev in ("IDA", "IMP", "ISS"):
        ann["review"] = make_review(
            summary=f"DNA-binding transcription activator activity, Pol II-specific, confirmed ({ref}).",
            action="ACCEPT",
            reason="Core molecular function. SMAD3 activates transcription of TGF-beta target genes.",
        )
    elif go_id == "GO:0001217" and ev == "IDA":
        ann["review"] = make_review(
            summary=f"DNA-binding transcription repressor activity confirmed ({ref}). SMAD3 can also repress transcription at certain loci.",
            action="ACCEPT",
            reason="Valid. SMAD3 acts as both activator and repressor depending on cofactor context (Ski/SnoN, TGIF for repression).",
        )
    elif go_id == "GO:0003677" and ev == "IDA":
        ann["review"] = make_review(
            summary=f"DNA binding confirmed by direct assay ({ref}).",
            action="ACCEPT",
            reason="Core molecular function. SMAD3 MH1 domain directly binds DNA.",
        )

    # ====================
    # SMAD PROTEIN SIGNAL TRANSDUCTION (IDA, IMP)
    # ====================
    elif go_id == "GO:0060395" and ev in ("IDA", "IMP"):
        ann["review"] = make_review(
            summary=f"SMAD protein signal transduction confirmed by experimental evidence ({ref}).",
            action="ACCEPT",
            reason="Core biological process. SMAD3 is a principal mediator of SMAD signal transduction.",
        )
    elif go_id == "GO:0060391":
        ann["review"] = make_review(
            summary=f"Positive regulation of SMAD protein signal transduction ({ref}).",
            action="ACCEPT",
            reason="SMAD3 positively promotes SMAD signal transduction as an R-SMAD that forms complexes with SMAD4.",
        )

    # ====================
    # TGF-BETA RECEPTOR SIGNALING PATHWAY (IDA, IMP, NAS)
    # ====================
    elif go_id == "GO:0007179" and ev in ("IDA", "IMP", "NAS"):
        ann["review"] = make_review(
            summary=f"TGF-beta receptor signaling pathway confirmed ({ref}).",
            action="ACCEPT",
            reason="Core biological process. SMAD3 is phosphorylated by TGFBR1 and is essential for canonical TGF-beta signaling.",
        )

    # ====================
    # CELLULAR COMPONENT ANNOTATIONS
    # ====================
    elif go_id == "GO:0005634" and ev in ("IDA", "IPI", "IGI"):
        ann["review"] = make_review(
            summary=f"Nucleus localization confirmed ({ref}). SMAD3 translocates to nucleus upon TGF-beta activation.",
            action="ACCEPT",
            reason="Core cellular localization. SMAD3 accumulates in nucleus after TGF-beta-induced phosphorylation.",
        )
    elif go_id == "GO:0005737" and ev in ("IDA", "IPI"):
        ann["review"] = make_review(
            summary=f"Cytoplasm localization confirmed ({ref}). SMAD3 resides in cytoplasm before activation.",
            action="ACCEPT",
            reason="Core cellular localization. SMAD3 shuttles between cytoplasm and nucleus.",
        )
    elif go_id == "GO:0005654" and ev in ("IDA", "TAS"):
        ann["review"] = make_review(
            summary=f"Nucleoplasm localization ({ref}).",
            action="ACCEPT",
            reason="Correct. SMAD3 is found in nucleoplasm when in the nucleus. Multiple Reactome pathways confirm.",
        )
    elif go_id == "GO:0005829" and ev in ("TAS", "IGI"):
        ann["review"] = make_review(
            summary=f"Cytosol localization ({ref}).",
            action="ACCEPT",
            reason="Correct. SMAD3 is found in the cytosol before activation. Multiple Reactome pathways confirm.",
        )
    elif go_id == "GO:0005667" and ev == "IDA":
        ann["review"] = make_review(
            summary=f"Transcription regulator complex confirmed ({ref}). SMAD3 forms complexes with SMAD4 and cofactors.",
            action="ACCEPT",
            reason="Correct. SMAD3/SMAD4 heteromeric complexes function as transcription regulator complexes.",
        )
    elif go_id == "GO:0071144" and ev == "IDA":
        ann["review"] = make_review(
            summary=f"Heteromeric SMAD protein complex confirmed ({ref}).",
            action="ACCEPT",
            reason="Core cellular component. SMAD3/SMAD4 heterotrimer is the functional transcriptional complex.",
        )
    elif go_id == "GO:0071141" and ev == "IDA":
        ann["review"] = make_review(
            summary=f"SMAD protein complex confirmed ({ref}).",
            action="ACCEPT",
            reason="Correct. SMAD3 forms SMAD protein complexes including homo-oligomers and hetero-complexes with SMAD4.",
        )
    elif go_id == "GO:0000785" and ev in ("IDA", "ISA"):
        ann["review"] = make_review(
            summary=f"Chromatin localization ({ref}). SMAD3 is found at chromatin at TGF-beta target gene loci.",
            action="ACCEPT",
            reason="Correct. ChIP studies confirm SMAD3 binding to chromatin at enhancer/promoter regions.",
        )
    elif go_id == "GO:0005637":
        ann["review"] = make_review(
            summary=f"Nuclear inner membrane localization ({ref}). SMAD3 co-localizes with LEMD3/MAN1.",
            action="KEEP_AS_NON_CORE",
            reason="SMAD3 interacts with LEMD3/MAN1 at the nuclear inner membrane, which sequesters SMAD3 to antagonize signaling. Specialized localization.",
        )

    # ====================
    # BIOLOGICAL PROCESS - EXPERIMENTAL
    # ====================
    elif go_id == "GO:0032924" and ev in ("IMP", "NAS"):
        ann["review"] = make_review(
            summary=f"Activin receptor signaling pathway confirmed ({ref}).",
            action="ACCEPT",
            reason="Core biological process. SMAD3 mediates activin signaling through ACVR1B.",
        )
    elif go_id == "GO:0038092":
        ann["review"] = make_review(
            summary=f"Nodal signaling pathway ({ref}).",
            action="ACCEPT",
            reason="SMAD3 also mediates Nodal signaling, which uses the same R-SMAD pathway as activin/TGF-beta.",
        )
    elif go_id == "GO:0006355" and ev in ("IDA", "NAS"):
        ann["review"] = make_review(
            summary=f"Regulation of DNA-templated transcription confirmed ({ref}).",
            action="ACCEPT",
            reason="Core biological process. SMAD3 is a transcription factor that regulates gene expression.",
        )
    elif go_id == "GO:0006357":
        ann["review"] = make_review(
            summary=f"Regulation of transcription by RNA polymerase II confirmed ({ref}).",
            action="ACCEPT",
            reason="Core biological process. SMAD3 regulates Pol II transcription at target genes.",
        )
    elif go_id == "GO:0000122" and ev == "IDA":
        ann["review"] = make_review(
            summary=f"Negative regulation of transcription by Pol II confirmed ({ref}). SMAD3 can repress transcription.",
            action="ACCEPT",
            reason="Valid. SMAD3 acts as transcriptional repressor at certain loci with Ski/SnoN/TGIF cofactors.",
        )
    elif go_id == "GO:0045944" and ev in ("IDA", "IMP"):
        ann["review"] = make_review(
            summary=f"Positive regulation of Pol II transcription confirmed ({ref}).",
            action="ACCEPT",
            reason="Core biological process. SMAD3 activates transcription of TGF-beta responsive genes.",
        )
    elif go_id == "GO:0010628":
        ann["review"] = make_review(
            summary=f"Positive regulation of gene expression ({ref}).",
            action="ACCEPT",
            reason="Core biological process. SMAD3 activates expression of TGF-beta target genes.",
        )
    elif go_id == "GO:0010718":
        ann["review"] = make_review(
            summary=f"Positive regulation of EMT ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Valid downstream effect. TGF-beta/SMAD3 is a major driver of EMT. Non-core but well-documented process.",
        )
    elif go_id == "GO:0045216":
        ann["review"] = make_review(
            summary=f"Cell-cell junction organization ({ref}). Related to EMT.",
            action="KEEP_AS_NON_CORE",
            reason="Valid downstream effect related to TGF-beta-induced EMT. Non-core pleiotropic process.",
        )
    elif go_id == "GO:0008285" and ev == "IMP":
        ann["review"] = make_review(
            summary=f"Negative regulation of cell population proliferation confirmed ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Valid downstream effect. TGF-beta/SMAD3 mediates growth arrest through CDK inhibitor induction. Non-core but important pleiotropic process.",
        )
    elif go_id == "GO:0097190":
        ann["review"] = make_review(
            summary=f"Apoptotic signaling pathway ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Valid downstream effect. TGF-beta/SMAD3 can trigger apoptosis in certain contexts. Non-core pleiotropic process.",
        )
    elif go_id == "GO:0097191" and ev == "IMP":
        ann["review"] = make_review(
            summary=f"Extrinsic apoptotic signaling pathway ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Valid downstream effect. Non-core pleiotropic process.",
        )
    elif go_id == "GO:0030279":
        ann["review"] = make_review(
            summary=f"Negative regulation of ossification ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Valid downstream effect. UniProt notes SMAD3 inhibits early healing of bone fractures. Non-core tissue-specific process.",
        )
    elif go_id == "GO:0045596":
        ann["review"] = make_review(
            summary=f"Negative regulation of cell differentiation ({ref}). ISS from mouse ortholog.",
            action="KEEP_AS_NON_CORE",
            reason="Valid downstream effect. TGF-beta/SMAD3 can inhibit differentiation in certain contexts. Non-core pleiotropic process.",
        )
    elif go_id == "GO:0045599":
        ann["review"] = make_review(
            summary=f"Negative regulation of fat cell differentiation ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Valid downstream effect. TGF-beta/SMAD3 inhibits adipogenesis. Non-core tissue-specific process.",
        )
    elif go_id == "GO:0042307":
        ann["review"] = make_review(
            summary=f"Positive regulation of protein import into nucleus ({ref}).",
            action="ACCEPT",
            reason="SMAD3 promotes nuclear import of the SMAD2/3-SMAD4 complex. Part of core signaling mechanism.",
        )
    elif go_id == "GO:0071560" and ev in ("IDA",):
        ann["review"] = make_review(
            summary=f"Cellular response to TGF-beta stimulus confirmed ({ref}).",
            action="ACCEPT",
            reason="Core biological process. SMAD3 is a primary mediator of cellular TGF-beta responses.",
        )
    elif go_id == "GO:0045429" and ev == "IDA":
        ann["review"] = make_review(
            summary=f"Positive regulation of nitric oxide biosynthetic process ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Specific downstream effect in certain cell types. Non-core pleiotropic process.",
        )
    elif go_id == "GO:0051481":
        ann["review"] = make_review(
            summary=f"Negative regulation of cytosolic calcium ion concentration ({ref}).",
            action="MARK_AS_OVER_ANNOTATED",
            reason="Indirect downstream effect. SMAD3 as a transcription factor does not directly regulate calcium concentrations.",
        )
    elif go_id == "GO:1901203" and ev in ("IDA", "IMP"):
        ann["review"] = make_review(
            summary=f"Positive regulation of extracellular matrix assembly ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Valid downstream effect. TGF-beta/SMAD3 transcriptionally activates ECM genes (collagen, fibronectin). Non-core but well-documented in fibrosis context.",
        )
    elif go_id == "GO:1902895" and ev in ("IDA", "IMP"):
        ann["review"] = make_review(
            summary=f"Positive regulation of miRNA transcription ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Valid specific function. SMAD3 regulates miRNA transcription at specific loci. Non-core regulatory process.",
        )
    elif go_id == "GO:1902894":
        ann["review"] = make_review(
            summary=f"Negative regulation of miRNA transcription ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Valid specific function. SMAD3 can also repress miRNA transcription at certain loci. Non-core regulatory process.",
        )
    elif go_id == "GO:1902893":
        ann["review"] = make_review(
            summary=f"Regulation of miRNA transcription ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Valid. SMAD3 regulates miRNA transcription. Parent term of both positive and negative regulation annotations. Non-core.",
        )
    elif go_id == "GO:0061450":
        ann["review"] = make_review(
            summary=f"Trophoblast cell migration ({ref}).",
            action="KEEP_AS_NON_CORE",
            reason="Specific developmental process. TGF-beta/SMAD3 promotes trophoblast migration. Non-core tissue-specific process.",
        )
    elif go_id == "GO:0031665":
        ann["review"] = make_review(
            summary=f"Negative regulation of LPS-mediated signaling pathway ({ref}). NAS from ComplexPortal.",
            action="KEEP_AS_NON_CORE",
            reason="Valid downstream effect reflecting anti-inflammatory role of TGF-beta/SMAD3. Non-core immune process.",
        )
    elif go_id == "GO:0050728" and ev == "NAS":
        ann["review"] = make_review(
            summary=f"Negative regulation of inflammatory response ({ref}). NAS from ComplexPortal.",
            action="KEEP_AS_NON_CORE",
            reason="Valid downstream effect. TGF-beta/SMAD3 is a key anti-inflammatory pathway. Non-core immune process.",
        )
    elif go_id == "GO:0071635":
        ann["review"] = make_review(
            summary=f"Negative regulation of TGF-beta production ({ref}). NAS from ComplexPortal.",
            action="KEEP_AS_NON_CORE",
            reason="Valid feedback regulation. SMAD3 can modulate TGF-beta expression as part of signaling feedback. Non-core regulatory process.",
        )
    elif go_id == "GO:0010629":
        ann["review"] = make_review(
            summary=f"Negative regulation of gene expression ({ref}).",
            action="ACCEPT",
            reason="Valid. SMAD3 can repress gene expression at certain loci through corepressor recruitment.",
        )

    # ====================
    # ACTS_UPSTREAM_OF annotations
    # ====================
    elif go_id == "GO:1990776":
        ann["review"] = make_review(
            summary=f"Response to angiotensin ({ref}). Acts upstream of.",
            action="KEEP_AS_NON_CORE",
            reason="TGF-beta/SMAD3 signaling cross-talks with angiotensin pathways in cardiovascular/fibrotic contexts. Non-core.",
        )

    # ====================
    # ISA annotation
    # ====================
    elif go_id == "GO:0000981" and ev == "ISA":
        ann["review"] = make_review(
            summary="ISA from TFClass database for DNA-binding TF activity Pol II-specific.",
            action="ACCEPT",
            reason="Correct. SMAD3 is classified as a TF in TFClass. Also supported by IDA and IBA.",
        )

    # ====================
    # Catch remaining annotations that still have PENDING
    # ====================
    if ann["review"].get("action") == "PENDING" or ann["review"].get("summary", "").startswith("TODO"):
        # Default handling for anything not yet covered
        if go_id == "GO:0005515":
            ann["review"] = make_review(
                summary=f"Protein binding from interaction study ({ref}).",
                action="REMOVE",
                reason="'Protein binding' is uninformative. More specific binding terms should be used.",
            )
        elif ev == "TAS" and "Reactome" in ref:
            ann["review"] = make_review(
                summary=f"Reactome pathway annotation for {go_label} ({ref}).",
                action="ACCEPT",
                reason="Reactome localization annotation is consistent with known SMAD3 biology.",
            )
        else:
            ann["review"] = make_review(
                summary=f"Annotation for {go_label} ({ev}, {ref}).",
                action="UNDECIDED",
                reason=f"Requires further review. {ev} evidence for {go_label}.",
            )

# Write updated YAML
with open("/Users/cjm/repos/ai-gene-review/genes/human/SMAD3/SMAD3-ai-review.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, width=120, sort_keys=False)

print("Done! Review generated.")
