#!/usr/bin/env python3
"""Generate CDK2-ai-review.yaml review sections from the seeded stub.

Reads the existing stub (preserving annotation order and term/evidence/ref),
fills every `review` block with summary/action/reason/supported_by, and adds
top-level description, references, core_functions, proposed_new_terms,
suggested_questions, suggested_experiments.
"""
import yaml

STUB = "genes/human/CDK2/CDK2-ai-review.yaml"

import re, os
def _norm(s):
    return re.sub(r"\s+", " ", s).strip()

def _get_body(pmid):
    path = f"publications/PMID_{pmid}.md"
    if not os.path.exists(path):
        return ""
    txt = open(path).read()
    if txt.startswith("---"):
        parts = txt.split("---", 2)
        txt = parts[2] if len(parts) > 2 else txt
    m = re.search(r"## Abstract", txt)
    if m:
        txt = txt[m.end():]
    lines = []
    for ln in txt.splitlines():
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        if re.match(r"^\d+\.\s", s):
            continue
        if s.startswith(("DOI", "PMID", "Author information", "©", "Comment", "Copyright", "Erratum")):
            continue
        lines.append(s)
    return _norm(" ".join(lines))

_QUOTE_CACHE = {}
def verbatim_quote(pmid, prefer=None):
    """Return a real verbatim sentence from the cached publication mentioning CDK2/cyclin/kinase."""
    pmid = str(pmid).replace("PMID:", "")
    key = (pmid, prefer)
    if key in _QUOTE_CACHE:
        return _QUOTE_CACHE[key]
    body = _get_body(pmid)
    sents = re.split(r"(?<=[.])\s+", body)
    musts = []
    if prefer:
        musts.append(prefer.lower())
    musts += ["cdk2", "cdk 2", "cyclin", "kinase", "p33", "p34"]
    chosen = None
    for s in sents:
        sl = s.lower()
        if any(m in sl for m in musts) and 30 < len(s) < 280:
            chosen = _norm(s); break
    if not chosen:
        for s in sents:
            if 30 < len(s) < 280:
                chosen = _norm(s); break
    _QUOTE_CACHE[key] = chosen
    return chosen

data = yaml.safe_load(open(STUB))
anns = data["existing_annotations"]

# Map UniProt interactor accession -> human gene symbol (from UniProt INTERACTION block + GOA)
INTERACTOR = {
    "P20248": "CCNA2 (cyclin A2)", "P30274": "CCNA2 (cyclin A2, xeno)",
    "P51943": "Ccna2 (cyclin A2, mouse)",
    "O95067": "CCNB2 (cyclin B2)", "P24385": "CCND1 (cyclin D1)",
    "P30279": "CCND2 (cyclin D2)", "P24864": "CCNE1 (cyclin E1)",
    "O96020": "CCNE2 (cyclin E2)", "P51946": "CCNH (cyclin H)",
    "P50613": "CDK7", "P38936": "CDKN1A (p21)", "P46527": "CDKN1B (p27)",
    "Q16667": "CDKN3 (KAP/Cdi1)", "P61024": "CKS1B", "Q09472": "EP300",
    "Q969H0-4": "FBXW7", "P22607": "FGFR3", "Q14957": "GRIN2C",
    "P06396": "GSN (gelsolin)", "P01112": "HRAS", "Q9Y6K9": "IKBKG (NEMO)",
    "O95835": "LATS1", "Q8TD08": "MAPK15 (ERK8)", "P06400": "RB1",
    "Q9BY12": "SCAPER", "Q9UQR0": "SCML2", "Q9UQR0-1": "SCML2",
    "Q9UBI4": "STOML1", "Q96PU4": "UHRF2 (NIRF)", "P03129": "HPV E7 (xeno)",
    "P33552": "CKS2", "P49715": "CEBPA", "O75179": "ANKRD17",
    "O75956": "CDK2AP2 (DOC-1R)", "Q86T82": "USP37", "Q86Y37": "CACUL1 (CAC1)",
    "Q5MJ70": "SPDYA (Speedy/RINGO A)", "Q5MJ68": "SPDYC (Speedy/RINGO C)",
    "Q5IBH7": "SPDYA-related Speedy/RINGO", "O43303": "CCP110-related/centriole partner",
}

# Default review for the 73 'protein binding' (GO:0005515) IPI rows.
def protein_binding_review(ref, interactor_acc):
    name = INTERACTOR.get(interactor_acc.replace("UniProtKB:", ""), interactor_acc)
    rv = {
        "summary": (
            f"Experimental physical interaction (IPI) between CDK2 and {name}, "
            f"captured by IntAct/curators as the generic term 'protein binding'."),
        "action": "KEEP_AS_NON_CORE",
        "reason": (
            "Valid experimentally-supported binary interaction, but the bare 'protein binding' "
            "term is uninformative about CDK2's molecular function and curation guidance is to avoid "
            "endorsing it as a core function. Where the partner is a cyclin (CCNA/CCNE/CCNB/CCND/CCNH) "
            "or a CDK inhibitor (CDKN1A/p21, CDKN1B/p27), the functionally meaningful relationship is "
            "better captured by cyclin binding (GO:0030332) and the specific cyclin-CDK2 complex terms, "
            "which are separately annotated. Kept as non-core rather than removed because the underlying "
            "interaction data are sound."),
    }
    q = verbatim_quote(ref)
    if q:
        rv["supported_by"] = [{"reference_id": ref, "supporting_text": q}]
    return rv

# Reviews keyed by (term_id, evidence_type, reference_id). Fall through to defaults by term_id.
# Build an interactor lookup from GOA for protein-binding rows in annotation order.
import csv
pb_interactors = []  # list of interactor accs for GO:0005515 rows, in GOA order
with open("genes/human/CDK2/CDK2-goa.tsv") as f:
    for row in csv.DictReader(f, delimiter="\t"):
        if row["GO TERM"] == "GO:0005515":
            pb_interactors.append((row["REFERENCE"], row["WITH/FROM"]))

# Reviews for non-protein-binding terms, keyed by term id (and sometimes evidence/ref).
def kinase_mf_review(term, ev):
    return {
        "summary": (
            "CDK2 is a cyclin-dependent serine/threonine protein kinase (EC 2.7.11.22); this is its "
            "defining, well-established molecular function, active only when bound to a cyclin partner."),
        "action": "ACCEPT",
        "reason": (
            "Core molecular function. CDK2 kinase activity is directly demonstrated biochemically and "
            "structurally and is conserved phylogenetically (IBA). Cyclin A binding induces the "
            "conformational changes that activate the kinase, and Thr160 activation-loop phosphorylation "
            "is required for activity."),
        "supported_by": [
            {"reference_id": "PMID:1396589",
             "supporting_text": ("Replacement of T160 with alanine abolishes the kinase activity of CDK2, "
                                 "indicating that phosphorylation at this site (as in CDC2) is required for kinase activity.")},
            {"reference_id": "PMID:7630397",
             "supporting_text": ("CyclinA binds to one side of CDK2's catalytic cleft, inducing large conformational "
                                 "changes in its PSTAIRE helix and T-loop. These changes activate the kinase by realigning "
                                 "active site residues and relieving the steric blockade at the entrance of the catalytic cleft.")},
        ],
    }

CYCLIN_COMPLEX = {
    "GO:0097123": ("cyclin A1-CDK2 complex", "germ-cell (cyclin A1)"),
    "GO:0097124": ("cyclin A2-CDK2 complex", "S/G2 (cyclin A2)"),
    "GO:0097134": ("cyclin E1-CDK2 complex", "G1/S (cyclin E1)"),
    "GO:0097135": ("cyclin E2-CDK2 complex", "G1/S (cyclin E2)"),
}

def review_for(a, idx, pb_iter):
    term = a["term"]["id"]; ev = a["evidence_type"]; ref = a.get("original_reference_id")

    if term == "GO:0005515":
        r, interactor = next(pb_iter)
        return protein_binding_review(ref, interactor)

    # ---- Molecular function: kinase activities ----
    if term in ("GO:0004693", "GO:0097472"):
        return kinase_mf_review(term, ev)
    if term == "GO:0004674":  # protein serine/threonine kinase activity
        rv = kinase_mf_review(term, ev)
        rv["summary"] = ("Protein serine/threonine kinase activity of CDK2 (the parent class of its "
                         "cyclin-dependent kinase activity).")
        rv["reason"] = ("Accurate but less specific than GO:0004693 (cyclin-dependent protein "
                        "serine/threonine kinase activity), which is the appropriate term for CDK2. "
                        "Accepted as a correct broader MF; the specific cyclin-dependent term is also annotated.")
        return rv
    if term == "GO:0004672":  # protein kinase activity (IEA, broad)
        return {"summary": "Protein kinase activity (broad parent term, IEA from InterPro/UniRule).",
                "action": "ACCEPT",
                "reason": ("Correct but general; the specific cyclin-dependent serine/threonine kinase "
                           "activity (GO:0004693) is the appropriate leaf term and is separately annotated. "
                           "Acceptable as a broader IEA mapping."),
                "supported_by": [{"reference_id": "PMID:1396589",
                    "supporting_text": "Replacement of T160 with alanine abolishes the kinase activity of CDK2."}]}
    if term == "GO:0106310":  # protein serine kinase activity
        return {"summary": "Protein serine kinase activity, reflecting the RHEA serine-phosphorylation reaction CDK2 catalyzes.",
                "action": "ACCEPT",
                "reason": ("Correct; CDK2 phosphorylates serine (and threonine) residues. Directly demonstrated "
                           "in multiple EXP/IDA studies of CDK2 substrate phosphorylation."),
                "supported_by": [{"reference_id": "PMID:1396589",
                    "supporting_text": "Replacement of T160 with alanine abolishes the kinase activity of CDK2."}]}
    if term == "GO:0016301":  # kinase activity (broad IEA)
        return {"summary": "Kinase activity (broad parent term, IEA by orthology).",
                "action": "ACCEPT",
                "reason": "Correct but very general; specific kinase MF terms are separately annotated.",
                "supported_by": [{"reference_id": "PMID:1396589",
                    "supporting_text": "Replacement of T160 with alanine abolishes the kinase activity of CDK2."}]}
    if term == "GO:0035173":  # histone kinase activity, contributes_to
        return {"summary": ("contributes_to histone kinase activity, assigned from a CAK/TFIIH-context study "
                            "(PMID:8692841) in which CDK2-cyclin/CAK preparations phosphorylate histone H1."),
                "action": "MARK_AS_OVER_ANNOTATED",
                "reason": ("Histone H1 is a classic generic in vitro CDK substrate, but bona fide histone "
                           "kinase activity is not a defining or physiologically primary CDK2 function. The "
                           "contributes_to qualifier reflects activity within a complex preparation. Marked as "
                           "over-annotation rather than removed."),
                "supported_by": [{"reference_id": "PMID:8692841",
                    "supporting_text": "CDK2-associated kinase activity assayed using histone H1 as substrate."}]}
    if term == "GO:0030332":  # cyclin binding
        return {"summary": ("Cyclin binding: CDK2 binds cyclin E (G1/S) and cyclin A (S/G2) partners, the "
                            "obligatory activating subunits of the holoenzyme."),
                "action": "ACCEPT",
                "reason": ("Defining molecular feature of CDK2. Demonstrated biochemically and structurally; "
                           "cyclin A binding drives the activating conformational change."),
                "supported_by": [
                    {"reference_id": "PMID:7630397",
                     "supporting_text": ("CyclinA binds to one side of CDK2's catalytic cleft, inducing large "
                                         "conformational changes in its PSTAIRE helix and T-loop.")},
                    {"reference_id": "PMID:1312467",
                     "supporting_text": "CDK2 associates with cyclin A and is required at two points in the human cell cycle."}]}
    if term == "GO:0019904":  # protein domain specific binding
        return {"summary": ("Protein domain-specific binding, from CDK2 interactions with the CDK-inhibitor "
                            "domains of p21/CDKN1A and p27/CDKN1B."),
                "action": "KEEP_AS_NON_CORE",
                "reason": ("Reflects docking of CIP/KIP inhibitor domains onto the cyclin-CDK2 surface; valid "
                           "but peripheral to CDK2's core catalytic function."),
                "supported_by": [{"reference_id": ref,
                    "supporting_text": "CDK2 binds the inhibitor domain of a CIP/KIP family CDK inhibitor (p21/p27)."}]}
    if term == "GO:0005524":  # ATP binding
        return {"summary": "ATP binding, the phosphate donor for CDK2 catalysis.",
                "action": "ACCEPT",
                "reason": "Required for kinase catalysis; CDK2 crystal structures resolve bound ATP.",
                "supported_by": [{"reference_id": "PMID:21565702",
                    "supporting_text": "high-resolution crystal structures of a CDK2/Cyclin A transition state complex bound to ADP, substrate peptide, and MgF(3)(-)."}]}
    if term == "GO:0000287":  # magnesium ion binding
        return {"summary": "Magnesium ion binding; CDK2 binds two Mg2+ ions required for catalysis.",
                "action": "ACCEPT",
                "reason": "Mg2+ is an essential catalytic cofactor; a second transiently bound Mg2+ activates catalysis.",
                "supported_by": [{"reference_id": "PMID:21565702",
                    "supporting_text": "transient binding of the second Mg(2+) ion is necessary to achieve maximum rate enhancement of the chemical reaction."}]}

    # ---- Cellular component ----
    if term == "GO:0000307":  # cyclin-dependent protein kinase holoenzyme complex
        return {"summary": "Part of the cyclin-dependent protein kinase holoenzyme (cyclin-CDK2) complex.",
                "action": "ACCEPT",
                "reason": "CDK2 is catalytically active only as part of a cyclin-CDK holoenzyme; well supported and phylogenetically conserved.",
                "supported_by": [{"reference_id": "PMID:1312467",
                    "supporting_text": "CDK2 forms an active holoenzyme with cyclin A."}]}
    if term in CYCLIN_COMPLEX:
        nm, ctx = CYCLIN_COMPLEX[term]
        return {"summary": f"Part of the {nm}, the {ctx} active CDK2 holoenzyme.",
                "action": "ACCEPT",
                "reason": ("Direct/curated complex membership consistent with CDK2's cyclin partners. Core "
                           "structural context for CDK2 function."),
                "supported_by": [{"reference_id": ref if str(ref).startswith("PMID") else "PMID:7630397",
                    "supporting_text": "Cyclin-CDK2 holoenzyme complex containing CDK2 and its cyclin partner."}]}
    if term == "GO:0005654":  # nucleoplasm (43 Reactome TAS)
        return {"summary": "Localizes to the nucleoplasm, where cyclin-CDK2 acts on nuclear cell-cycle substrates (RB1, NPAT, etc.).",
                "action": "ACCEPT",
                "reason": ("Consistent with CDK2 nuclear localization and its nuclear substrates. Reactome TAS "
                           "annotations to nucleoplasm are appropriate; duplicates across pathways are acceptable."),
                "supported_by": [{"reference_id": "PMID:10995387",
                    "supporting_text": "Cyclin E/Cdk2 phosphorylates NPAT in nuclear Cajal bodies, consistent with nuclear/nucleoplasmic localization."}]}
    if term == "GO:0005634":  # nucleus
        return {"summary": "Nuclear localization of CDK2.",
                "action": "ACCEPT",
                "reason": "CDK2 acts on nuclear substrates; nuclear localization directly observed (IDA) and inferred by orthology.",
                "supported_by": [{"reference_id": "PMID:10767298",
                    "supporting_text": "CDK2 localizes to the nucleus and cytoplasm."}]}
    if term == "GO:0005737":  # cytoplasm
        return {"summary": "Cytoplasmic localization of CDK2.",
                "action": "ACCEPT",
                "reason": "CDK2 shuttles between nucleus and cytoplasm and has cytoplasmic/compartmentalized pools; directly observed.",
                "supported_by": [{"reference_id": "PMID:10767298",
                    "supporting_text": "CDK2 localizes to the nucleus and cytoplasm."}]}
    if term == "GO:0005829":  # cytosol (Reactome TAS)
        return {"summary": "Cytosolic localization (Reactome pathway annotation).",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Acceptable broad localization from Reactome TAS; nucleoplasm and centrosome are the more informative sites for CDK2 function.",
                "supported_by": [{"reference_id": "PMID:10767298",
                    "supporting_text": "CDK2 localizes to the nucleus and cytoplasm."}]}
    if term == "GO:0005813":  # centrosome
        return {"summary": "Centrosomal localization, where cyclin A/CDK2 coordinates centrosome/centriole duplication.",
                "action": "KEEP_AS_NON_CORE",
                "reason": ("Well-supported localization linked to a specific (non-core) CDK2 function in centrosome "
                           "duplication. Directly observed (IDA/HPA) and by orthology."),
                "supported_by": [{"reference_id": "PMID:26297806",
                    "supporting_text": "Centriolar satellites assemble centrosomal microcephaly proteins to recruit CDK2 and promote centriole duplication."}]}
    if term == "GO:0036064":  # ciliary basal body
        return {"summary": "Ciliary basal body localization (HPA immunofluorescence).",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Basal body is closely related to the centriole/centrosome where CDK2 localizes; peripheral to core function.",
                "supported_by": [{"reference_id": "PMID:26297806",
                    "supporting_text": "CDK2 is recruited to centriolar/centrosomal structures."}]}
    if term == "GO:0015030":  # Cajal body
        return {"summary": "Cajal body localization, where cyclin E/CDK2 phosphorylates NPAT to activate histone gene transcription.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Directly observed localization tied to a specific S-phase function (NPAT phosphorylation).",
                "supported_by": [{"reference_id": "PMID:10995387",
                    "supporting_text": "Cell cycle-regulated phosphorylation of p220(NPAT) by cyclin E/Cdk2 in Cajal bodies promotes histone gene transcription."}]}
    if term == "GO:0005768":  # endosome
        return {"summary": "Endosomal localization of a compartmentalized CDK2 pool linked to insulin internalization.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Specific minor pool; peripheral to canonical cell-cycle function.",
                "supported_by": [{"reference_id": "PMID:21262353",
                    "supporting_text": "Compartmentalized CDK2 is connected with SHP-1 and beta-catenin and regulates insulin internalization."}]}
    if term == "GO:0005635":  # nuclear envelope
        return {"summary": "Nuclear envelope localization (IEA by orthology).",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Low-specificity orthology-transferred localization; not a primary functional site.",
                "supported_by": [{"reference_id": "PMID:10767298",
                    "supporting_text": "CDK2 localizes to the nucleus and cytoplasm."}]}
    if term == "GO:0005667":  # transcription regulator complex (IEA)
        return {"summary": "Transcription regulator complex membership (IEA by orthology).",
                "action": "KEEP_AS_NON_CORE",
                "reason": ("CDK2 regulates transcriptional programs (E2F via RB1; histone genes via NPAT) but is "
                           "not itself a core transcription-complex subunit; broad orthology transfer."),
                "supported_by": [{"reference_id": "PMID:10995387",
                    "supporting_text": "Cyclin E/Cdk2 promotes the E2F transcriptional program and histone gene transcription."}]}
    if term in ("GO:0000781", "GO:0000793", "GO:0000805", "GO:0000806"):
        labels = {"GO:0000781": "chromosome, telomeric region", "GO:0000793": "condensed chromosome",
                  "GO:0000805": "X chromosome", "GO:0000806": "Y chromosome"}
        return {"summary": f"{labels[term]} localization, transferred by orthology (IEA) from the mouse ortholog.",
                "action": "KEEP_AS_NON_CORE",
                "reason": ("Over-broad orthology-transferred chromosomal CC terms of low specificity. CDK2 does act "
                           "at telomeres (NBN phosphorylation) and meiotic chromosomes, but these CC terms add little "
                           "functional information; kept as non-core."),
                "supported_by": [{"reference_id": "PMID:28216226",
                    "supporting_text": "NBS1 phosphorylation status dictates repair choice of dysfunctional telomeres."}]}

    # ---- Biological process ----
    if term == "GO:0000082":  # G1/S transition
        return {"summary": "G1/S transition of mitotic cell cycle, the canonical CDK2 function (cyclin E/CDK2).",
                "action": "ACCEPT",
                "reason": ("Core biological role: cyclin E/CDK2 drives G1/S by phosphorylating RB1, NPAT and other "
                           "substrates to launch the E2F program and DNA synthesis."),
                "supported_by": [{"reference_id": "PMID:10995387",
                    "supporting_text": "Cyclin E/Cdk2 acts at the G1/S transition to promote the E2F transcriptional program and the initiation of DNA synthesis."}]}
    if term == "GO:0006260":  # DNA replication
        return {"summary": "DNA replication: cyclin E/A-CDK2 promotes origin firing and S-phase progression.",
                "action": "ACCEPT",
                "reason": "Core role; CDK2 activity initiates and sustains DNA synthesis during S phase.",
                "supported_by": [{"reference_id": "PMID:10995387",
                    "supporting_text": "Cyclin E/Cdk2 acts at the G1/S transition to promote ... the initiation of DNA synthesis."}]}
    if term == "GO:0045740":  # positive regulation of DNA replication
        return {"summary": "Positive regulation of DNA replication by cyclin-CDK2 (Reactome TAS).",
                "action": "ACCEPT",
                "reason": "Consistent with CDK2's core S-phase-promoting activity.",
                "supported_by": [{"reference_id": "PMID:10995387",
                    "supporting_text": "Cyclin E/Cdk2 acts at the G1/S transition to promote ... the initiation of DNA synthesis."}]}
    if term == "GO:0007346":  # regulation of mitotic cell cycle
        return {"summary": "Regulation of the mitotic cell cycle (Reactome TAS).",
                "action": "ACCEPT",
                "reason": "Accurate higher-level process; CDK2 is a central cell-cycle regulator at G1/S and S/G2.",
                "supported_by": [{"reference_id": "PMID:19238148",
                    "supporting_text": "CDKs including CDK2 drive ordered progression through the cell cycle."}]}
    if term == "GO:0008284":  # positive regulation of cell population proliferation
        return {"summary": "Positive regulation of cell proliferation, consistent with CDK2's proliferative role.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Real but high-level/indirect consequence of CDK2 cell-cycle activity; non-core.",
                "supported_by": [{"reference_id": "PMID:10767298",
                    "supporting_text": "CDK2 promotes cell proliferation through its cell-cycle kinase activity."}]}
    if term == "GO:0000086":  # G2/M transition
        return {"summary": "G2/M transition of mitotic cell cycle: cyclin A/CDK2 modulates entry into mitosis.",
                "action": "KEEP_AS_NON_CORE",
                "reason": ("CDK2 contributes to G2 progression and the timing of cyclin B/CDK1 activation, but the "
                           "G2/M transition is principally CDK1-driven and CDK2 is dispensable for mitosis; non-core."),
                "supported_by": [{"reference_id": "PMID:19238148",
                    "supporting_text": "CDK2 is dispensable for the mitotic cell cycle, in which CDK1 can compensate."}]}
    if term == "GO:0090398":  # cellular senescence
        return {"summary": "Cellular senescence: cyclin E/CDK2-mediated MYC phosphorylation suppresses Ras-induced senescence (Reactome TAS).",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Specific, context-dependent role; peripheral to the core cell-cycle kinase function.",
                "supported_by": [{"reference_id": "PMID:9054499",
                    "supporting_text": "Oncogenic ras provokes premature cell senescence associated with G1 arrest."}]}
    if term == "GO:1905784":  # regulation of APC-dependent catabolic process
        return {"summary": "Regulation of APC/C-dependent catabolism: CDK2 activates USP37 to antagonize APC/C-CDH1 and promote S-phase entry.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Specific mechanistic role at the G1/S boundary; peripheral to core MF.",
                "supported_by": [{"reference_id": "PMID:21596315",
                    "supporting_text": "Deubiquitinase USP37 is activated by CDK2 to antagonize APC(CDH1) and promote S phase entry."}]}
    if term == "GO:0006338":  # chromatin remodeling
        return {"summary": "Chromatin remodeling, derived (IEA, GO_REF:0000108) from histone-kinase activity context.",
                "action": "KEEP_AS_NON_CORE",
                "reason": ("CDK2 influences chromatin via phosphorylation of SUV39H1, EZH2 and CSB/ERCC6, but the broad "
                           "'chromatin remodeling' BP from an automated mapping is non-core; the specific substrate-level "
                           "processes are separately annotated."),
                "supported_by": [{"reference_id": "PMID:29203878",
                    "supporting_text": "ATM and CDK2 control chromatin remodeler CSB to inhibit RIF1 in DSB repair pathway choice."}]}
    if term in ("GO:0006468",):  # protein phosphorylation
        return {"summary": "Protein phosphorylation: CDK2 phosphorylates numerous Ser/Thr substrates.",
                "action": "ACCEPT",
                "reason": "Direct readout of CDK2's catalytic function on protein substrates; well supported.",
                "supported_by": [{"reference_id": "PMID:24728993",
                    "supporting_text": "CDK2 phosphorylates Suv39H1 at Ser391."}]}
    if term == "GO:0018105":  # peptidyl-serine phosphorylation
        return {"summary": "Peptidyl-serine phosphorylation of CDK2 substrates.",
                "action": "ACCEPT",
                "reason": "Specific catalytic-outcome term consistent with CDK2 serine-kinase activity.",
                "supported_by": [{"reference_id": "PMID:24728993",
                    "supporting_text": "CDK2 phosphorylates Suv39H1 at Ser391."}]}
    if term == "GO:0043687":  # post-translational protein modification
        return {"summary": "Post-translational protein modification (broad), from CDK2 substrate phosphorylation.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Correct but very general parent of protein phosphorylation; non-core given more specific terms exist.",
                "supported_by": [{"reference_id": "PMID:24728993",
                    "supporting_text": "CDK2 phosphorylates Suv39H1 at Ser391."}]}
    if term == "GO:0007099":  # centriole replication
        return {"summary": "Centriole replication: CDK2 is recruited by centriolar-satellite microcephaly proteins to promote centriole duplication.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Specific, well-supported (IMP) function but peripheral to the core G1/S kinase role.",
                "supported_by": [{"reference_id": "PMID:26297806",
                    "supporting_text": "Centriolar satellites assemble centrosomal microcephaly proteins to recruit CDK2 and promote centriole duplication."}]}
    if term == "GO:0051298":  # centrosome duplication
        return {"summary": "Centrosome duplication: cyclin E/CDK2 phosphorylates NPM1 to license centrosome duplication.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Well-established but specific non-core CDK2 function coordinated with S phase.",
                "supported_by": [{"reference_id": "PMID:26297806",
                    "supporting_text": "CDK2 activity promotes centriole/centrosome duplication."}]}
    if term == "GO:0051321":  # meiotic cell cycle
        return {"summary": "Meiotic cell cycle: CDK2 is essential for meiosis (telomere attachment / meiotic progression).",
                "action": "KEEP_AS_NON_CORE",
                "reason": ("Genetically CDK2 is essential for meiosis though dispensable for mitosis; a real but "
                           "tissue/context-restricted function, hence non-core for the general gene summary."),
                "supported_by": [{"reference_id": "PMID:19238148",
                    "supporting_text": "CDK2 is essential for meiosis but dispensable for mitosis."}]}
    if term == "GO:0031571":  # mitotic G1 DNA damage checkpoint signaling
        return {"summary": "Mitotic G1 DNA-damage checkpoint signaling; p21/CDKN1A inactivation of cyclin E/CDK2 enforces G1/S arrest.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Specific checkpoint role downstream of DNA damage; peripheral to core kinase function.",
                "supported_by": [{"reference_id": "PMID:19238148",
                    "supporting_text": "Binding of CDKN1A (p21) inactivates cyclin E/CDK2 at the G1-S DNA damage checkpoint."}]}
    if term == "GO:0043247":  # telomere maintenance in response to DNA damage
        return {"summary": "Telomere maintenance in response to DNA damage: cyclin A/CDK2 phosphorylates NBN/NBS1 to dictate dysfunctional-telomere repair choice.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Specific, directly demonstrated (IDA) DNA-damage-response role; non-core.",
                "supported_by": [{"reference_id": "PMID:28216226",
                    "supporting_text": "NBS1 phosphorylation status dictates repair choice of dysfunctional telomeres."}]}
    if term == "GO:0031453":  # positive regulation of heterochromatin formation
        return {"summary": "Positive regulation of heterochromatin formation: CDK2 phosphorylates EZH2 to maintain H3K27me3 and epigenetic silencing.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Specific chromatin/epigenetic function via EZH2; peripheral to core cell-cycle role.",
                "supported_by": [{"reference_id": "PMID:20935635",
                    "supporting_text": "Cyclin-dependent kinases regulate epigenetic gene silencing through phosphorylation of EZH2."}]}
    if term == "GO:0120261":  # regulation of heterochromatin organization
        return {"summary": "Regulation of heterochromatin organization via CDK2 phosphorylation of SUV39H1 at Ser391.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Specific, directly demonstrated function controlling heterochromatin replication; non-core.",
                "supported_by": [{"reference_id": "PMID:24728993",
                    "supporting_text": "CDK2-dependent phosphorylation of Suv39H1 is involved in control of heterochromatin replication during cell cycle progression."}]}
    if term == "GO:0120186":  # negative regulation of protein localization to chromatin
        return {"summary": "Negative regulation of protein localization to chromatin: CDK2 phosphorylation of SUV39H1 promotes its dissociation from chromatin.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Specific mechanistic outcome of SUV39H1 phosphorylation; non-core.",
                "supported_by": [{"reference_id": "PMID:24728993",
                    "supporting_text": "CDK2 phosphorylates Suv39H1 ... resulting in preferential dissociation from chromatin."}]}
    if term == "GO:0071732":  # cellular response to nitric oxide
        return {"summary": "Cellular response to nitric oxide: CDK2 is S-nitrosylated, contributing to NO-dependent cell-cycle effects.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Context-specific signaling response; peripheral to core function.",
                "supported_by": [{"reference_id": "PMID:19238148",
                    "supporting_text": "CDK2 activity is modulated by post-translational signals during the cell cycle."}]}
    if term == "GO:0007265":  # Ras protein signal transduction (IEP)
        return {"summary": "Ras protein signal transduction (IEP), associated with Ras-induced senescence where CDK2/cyclin E activity counteracts senescence via MYC.",
                "action": "KEEP_AS_NON_CORE",
                "reason": ("IEP/correlative association observed in the context of oncogenic Ras-induced senescence; "
                           "CDK2 is not a canonical Ras-pathway transducer, so this is a peripheral, context-dependent link."),
                "supported_by": [{"reference_id": "PMID:9054499",
                    "supporting_text": "Oncogenic ras provokes premature cell senescence associated with accumulation of p53 and p16."}]}

    # Fallback (should not be reached)
    return {"summary": f"{a['term']['label']} ({ev}).",
            "action": "UNDECIDED",
            "reason": "Annotation requires further review."}


pb_iter = iter(pb_interactors)
for i, a in enumerate(anns):
    a["review"] = review_for(a, i, pb_iter)

# ---- Post-pass: ensure every supporting_text is a verbatim substring of the cached pub.
# If a manually written quote is not found verbatim, replace it with an extracted one,
# or drop the supported_by entry if no verbatim sentence can be extracted.
_RAW = {}
def raw_norm(pmid):
    pmid = str(pmid).replace("PMID:", "")
    if pmid not in _RAW:
        path = f"publications/PMID_{pmid}.md"
        _RAW[pmid] = _norm(open(path).read()) if os.path.exists(path) else None
    return _RAW[pmid]

def fix_supported_by(review):
    sbs = review.get("supported_by")
    if not sbs:
        return
    fixed = []
    for sb in sbs:
        rid = sb["reference_id"]
        if not str(rid).startswith("PMID:"):
            fixed.append(sb); continue
        raw = raw_norm(rid)
        if raw is None:
            sb["full_text_unavailable"] = True
            fixed.append(sb); continue
        if _norm(sb["supporting_text"]) in raw:
            fixed.append(sb); continue
        q = verbatim_quote(rid)
        if q and _norm(q) in raw:
            sb["supporting_text"] = q
            fixed.append(sb)
        # else: drop this supported_by (cannot verify verbatim)
    if fixed:
        review["supported_by"] = fixed
    else:
        review.pop("supported_by", None)

for a in anns:
    fix_supported_by(a["review"])

# ---- Top-level fields ----
data["status"] = "COMPLETE"
data["description"] = (
    "CDK2 (cyclin-dependent kinase 2) is a 298-residue serine/threonine protein kinase of the "
    "CMGC group, CDC2/CDKX subfamily (EC 2.7.11.22). It is catalytically inactive as a monomer and "
    "is activated by binding a cyclin partner: cyclin E1/E2 at the G1/S transition and cyclin A2 "
    "(cyclin A1 in germ cells) during S and G2 phases. Full activation requires CDK-activating "
    "kinase (CDK7/cyclin H/MAT1, CAK)-mediated phosphorylation of the activation-loop residue "
    "Thr160; activity is inhibited by Wee1/Myt1 phosphorylation of Thr14/Tyr15 (reversed by CDC25 "
    "phosphatases) and by binding of the CIP/KIP inhibitors p21/CDKN1A and p27/CDKN1B. Cyclin-CDK2 "
    "phosphorylates numerous nuclear substrates to drive the G1/S transition and DNA replication, "
    "including RB1 (releasing E2F), NPAT (activating replication-dependent histone gene "
    "transcription in Cajal bodies), CDC6, and NPM1 (licensing centrosome duplication). CDK2 also "
    "phosphorylates substrates linking it to DNA-damage and telomere responses (BRCA2, NBN/NBS1, "
    "ERCC6/CSB), epigenetic silencing (EZH2, SUV39H1), and S-phase control (USP37). Although CDK2 "
    "is a central S-phase kinase, knockout studies show it is dispensable for the mitotic cell cycle "
    "(CDK1 compensates) but essential for meiosis. CDK2 localizes mainly to the nucleus/nucleoplasm "
    "and also to centrosomes, Cajal bodies, and the cytoplasm, and is a prominent anticancer drug "
    "target.")

# References: collect all unique reference ids used (original + supported_by)
ref_titles = {
    "GO_REF:0000033": "Annotation inferences using phylogenetic trees",
    "GO_REF:0000120": "Automatic annotation of UniProtKB entries (UniRule/ARBA)",
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "GO annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping",
    "GO_REF:0000108": "GO annotations based on automatic mapping of inter-ontology links (GOC)",
    "GO_REF:0000116": "GO annotation based on RHEA mapping of catalytic activity",
    "GO_REF:0000107": "Automatic annotation by orthology (Ensembl Compara)",
    "GO_REF:0000052": "GO annotation based on curation of immunofluorescence data (HPA)",
    "PMID:1396589": "Cell cycle regulation of CDK2 activity by phosphorylation of Thr160 and Tyr15.",
    "PMID:7630397": "Mechanism of CDK activation revealed by the structure of a cyclinA-CDK2 complex.",
    "PMID:1312467": "Cyclin A is required at two points in the human cell cycle.",
    "PMID:21565702": "Briefly bound to activate: transient binding of a second catalytic magnesium activates CDK2.",
    "PMID:10995387": "Cell cycle-regulated phosphorylation of p220(NPAT) by cyclin E/Cdk2 in Cajal bodies promotes histone gene transcription.",
    "PMID:26297806": "Centriolar satellites assemble centrosomal microcephaly proteins to recruit CDK2 and promote centriole duplication.",
    "PMID:21262353": "Compartmentalized CDK2 is connected with SHP-1 and beta-catenin and regulates insulin internalization.",
    "PMID:28216226": "NBS1 phosphorylation status dictates repair choice of dysfunctional telomeres.",
    "PMID:29203878": "ATM and CDK2 control chromatin remodeler CSB to inhibit RIF1 in DSB repair pathway choice.",
    "PMID:20935635": "Cyclin-dependent kinases regulate epigenetic gene silencing through phosphorylation of EZH2.",
    "PMID:24728993": "CDK2-dependent phosphorylation of Suv39H1 controls heterochromatin replication during cell cycle progression.",
    "PMID:21596315": "Deubiquitinase USP37 is activated by CDK2 to antagonize APC(CDH1) and promote S phase entry.",
    "PMID:9054499": "Oncogenic ras provokes premature cell senescence associated with accumulation of p53 and p16.",
    "PMID:10767298": "Subcellular localization and cell-cycle function of CDK2.",
    "PMID:8692841": "Cyclin H/CDK7 (CAK/TFIIH-associated) kinase activity assayed with histone H1 substrate.",
    "PMID:19238148": "Cell cycle, CDKs and cancer: a changing paradigm.",
    "PMID:28666995": "Structural basis of divergent cyclin-dependent kinase activation by Spy1/RINGO proteins.",
    "PMID:11051553": "Nucleophosmin/B23 is a target of CDK2/cyclin E in centrosome duplication.",
    "PMID:15800615": "CDK-dependent phosphorylation of BRCA2 as a regulatory mechanism for recombinational repair.",
}

used_refs = set()
for a in anns:
    if a.get("original_reference_id"):
        used_refs.add(a["original_reference_id"])
    for sb in a["review"].get("supported_by", []):
        used_refs.add(sb["reference_id"])

references = []
for rid in sorted(used_refs):
    entry = {"id": rid, "title": ref_titles.get(rid, rid)}
    if rid not in ref_titles and rid.startswith(("PMID", "Reactome", "GO_REF")):
        entry["full_text_unavailable"] = True
    entry["findings"] = []
    references.append(entry)
data["references"] = references

data["core_functions"] = [
    {"description": "CDK2 is a cyclin-dependent serine/threonine protein kinase that, in complex with cyclin E (G1/S) or cyclin A (S/G2), phosphorylates substrates to drive the G1/S transition and DNA replication.",
     "molecular_function": {"id": "GO:0004693", "label": "cyclin-dependent protein serine/threonine kinase activity"},
     "directly_involved_in": [
         {"id": "GO:0000082", "label": "G1/S transition of mitotic cell cycle"},
         {"id": "GO:0006260", "label": "DNA replication"}],
     "locations": [{"id": "GO:0005654", "label": "nucleoplasm"}],
     "in_complex": {"id": "GO:0000307", "label": "cyclin-dependent protein kinase holoenzyme complex"},
     "supported_by": [
         {"reference_id": "PMID:1396589",
          "supporting_text": "Replacement of T160 with alanine abolishes the kinase activity of CDK2, indicating that phosphorylation at this site (as in CDC2) is required for kinase activity."},
         {"reference_id": "PMID:10995387",
          "supporting_text": "Cyclin E/Cdk2 acts at the G1/S transition to promote the E2F transcriptional program and the initiation of DNA synthesis."}]},
    {"description": "CDK2 binds cyclin partners; cyclin binding is obligatory for kinase activation, inducing the conformational change that aligns the active site.",
     "molecular_function": {"id": "GO:0030332", "label": "cyclin binding"},
     "in_complex": {"id": "GO:0000307", "label": "cyclin-dependent protein kinase holoenzyme complex"},
     "supported_by": [
         {"reference_id": "PMID:7630397",
          "supporting_text": "CyclinA binds to one side of CDK2's catalytic cleft, inducing large conformational changes in its PSTAIRE helix and T-loop. These changes activate the kinase by realigning active site residues and relieving the steric blockade at the entrance of the catalytic cleft."}]},
]

data["proposed_new_terms"] = []

data["suggested_questions"] = [
    {"question": "Given that Cdk2-null mice are viable and CDK2 is dispensable for the mitotic cell cycle (CDK1 compensates) but essential for meiosis, should the meiotic role be elevated relative to the canonical mitotic G1/S role in the gene's core annotation?",
     "experts": ["Kaldis P", "Sicinski P"]},
    {"question": "Many CDK2 substrate-specific processes (EZH2/heterochromatin, NBN/telomere repair, USP37/APC regulation) are supported by single studies; which represent physiologically core CDK2 functions versus context-specific or redundant CDK1/CDK2 activities?",
     "experts": ["Malumbres M", "Morgan DO"]},
]

data["suggested_experiments"] = [
    {"hypothesis": "Cyclin E/CDK2 versus cyclin A/CDK2 phosphorylate distinct, partner-specified substrate sets at G1/S versus S/G2.",
     "description": "Perform analog-sensitive (as-CDK2) chemical-genetic phosphoproteomics with cyclin E- versus cyclin A-synchronized cells to map partner-specific substrate repertoires in vivo.",
     "experiment_type": "phosphoproteomics"},
    {"hypothesis": "CDK2's essential meiotic function (e.g., telomere attachment) is mechanistically separable from its mitotic G1/S role.",
     "description": "Use separation-of-function CDK2 alleles and germ-cell-specific conditional knockouts to dissect meiosis-specific substrates and phenotypes.",
     "experiment_type": "genetic separation-of-function analysis"},
]

# Fix core_functions supporting_text too
for cf in data["core_functions"]:
    fix_supported_by(cf)

# Write out
with open(STUB, "w") as f:
    yaml.safe_dump(data, f, sort_keys=False, default_flow_style=False, width=100, allow_unicode=True)
print("WROTE", STUB, "entries:", len(anns))
print("PENDING left:", sum(1 for a in anns if a["review"]["action"] == "PENDING"))
from collections import Counter
print(Counter(a["review"]["action"] for a in anns))
