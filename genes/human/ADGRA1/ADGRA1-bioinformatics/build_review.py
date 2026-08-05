#!/usr/bin/env python3
"""Generate `ADGRA1-ai-review.yaml` from the GOA TSV plus the verdicts recorded here.

Why generate rather than hand-edit: the 22 `GO:0005515` rows differ only in the
WITH/FROM partner, and the campaign has repeatedly seen hand-maintained
`source_entities` lists drift from the GOA field they claim to mirror. Every row
here is emitted from the parsed TSV, with assertions that:

  * one `existing_annotations` entry exists per GOA data line (plus the NEW rows,
    counted separately and stated);
  * `supporting_entities` on IBA rows equals the row's WITH/FROM tokens exactly;
  * a verdict exists for every row (an unmatched row is an error, not a default);
  * PyYAML emits no anchors/aliases, so raw-text counts over the file are
    meaningful and no two rows can silently share one object.

Usage:  uv run python build_review.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE = HERE.parent
GOA = GENE / "ADGRA1-goa.tsv"
OUT = GENE / "ADGRA1-ai-review.yaml"
UNIPROT_FILE = "file:human/ADGRA1/ADGRA1-uniprot.txt"
RESULTS_FILE = "file:human/ADGRA1/ADGRA1-bioinformatics/RESULTS.md"


class NoAliasDumper(yaml.SafeDumper):
    """Forbid anchors/aliases: an alias silently multiplies one object across N
    rows, and every validator in this repo walks the parsed tree, so it would
    verify the same quote N times and report N successes."""

    def ignore_aliases(self, data):  # noqa: D102
        return True


def q(ref: str, text: str) -> dict:
    return {"reference_id": ref, "supporting_text": text}


# ---------------------------------------------------------------- verdict table
# Keyed on (GO term, evidence code, reference) -- stable entities, never on the
# wording of a conclusion, because the conclusion is what gets reworded.

PDZ_MECHANISM = (
    "ADGRA1's cytoplasmic C-terminus ends in ETTV, a class I PDZ-binding motif "
    "(consensus X-[ST]-X-[VIL]), on a 255-residue cytoplasmic tail (UniProt "
    "TOPO_DOM 306..560). Both references behind this gene's GO:0005515 rows are "
    "PDZ-specific assays by construction, all 21 partners carry annotated PDZ "
    "domains (2-13 each, all reviewed Swiss-Prot at canonical length), and IntAct "
    "curates the ADGRA1 side of every record as feature 'PDZ-binding motif' "
    "(sufficient to bind) against a partner 'PDZ domain'. 'protein binding' "
    "discards all of that; GO:0030165 states the mechanism."
)

GPCR_REASON = (
    "The G-protein-activating half of GO:0004930 is now demonstrated: TRUPATH "
    "BRET2 across all 14 Galphabetagamma sensors shows activation of Galpha13, "
    "Galpha11 and Galpha15 with a plasmid copy-number dependence and an "
    "unresponsive GalphaoB control (PMID:41961591). The assay used the MOUSE "
    "ortholog (Q8C4G9) overexpressed in HEK293T, so the appropriate evidence for "
    "the human gene is ISS with UniProtKB:Q8C4G9 as the supporting entity; GOA is "
    "asked to attach that evidence line to the existing term (see "
    "suggested_questions), since all four current lines cite references with no "
    "functional content. The term is therefore ACCEPTed and the reference problem "
    "recorded in reference_review rather than converted into a GO action. Caveat "
    "retained rather than smoothed over: the receptor is an orphan and the "
    "activation is agonist-independent, so the definition's first conjunct "
    "('combining with an extracellular signal') is unestablished; that is raised "
    "as an ontology question, not acted on."
)

MEMBRANE_REASON = (
    "GO:0016020 is the ontology root for membrane and says nothing this gene's "
    "record does not already say better. ADGRA1 is a 7-TM receptor whose PAINT "
    "ortholog node places it at the postsynaptic density and glutamatergic synapse "
    "by transfer from mouse Adgra1 IDA, and surface-labelled HA-ADGRA1 forms puncta "
    "at the neuronal surface (PMID:41961591). GO:0005886 is supported and is the "
    "informative parent of those locations."
)

VERDICTS: dict[tuple[str, str, str], dict] = {
    # ---- IBA (PAINT) ----------------------------------------------------------
    ("GO:0005886", "IBA", "GO_REF:0000033"): {
        "action": "ACCEPT",
        "summary": (
            "Correct, but note the donor set is entirely paralogous: node "
            "PTN001738137 spans ADGRA1/2/3 and all five non-node WITH/FROM tokens "
            "are ADGRA2 or ADGRA3."
        ),
        "reason": (
            "Provenance and circularity are separate claims and only the second "
            "carries a verdict. Provenance: 5 of 5 protein donors on this row are "
            "ADGRA2/ADGRA3 (mouse Adgra2 Q91ZV8, mouse Adgra3 Q7TT36, human ADGRA2 "
            "Q96PE1, zebrafish adgra2, zebrafish adgra3); not one is an ADGRA1 "
            "ortholog. On its own that supports nothing. Circularity: the chain is "
            "not circular - the donors carry their own experimental plasma-membrane "
            "evidence (human ADGRA2 has GO:0005886 EXP x3 plus IDA; mouse Adgra2 has "
            "EXP and IDA), and ADGRA1's own ortholog node independently places it at "
            "the postsynaptic density, which is plasma membrane. The term is also "
            "directly supported for ADGRA1 by surface labelling of HA-ADGRA1 in "
            "primary hippocampal neurons (PMID:41961591). ACCEPT."
        ),
        "propagation": {
            "root_cause": "NO_FAILURE_CORE",
            "note": (
                "Recorded for provenance only. The donor set contains no ADGRA1 "
                "ortholog, which means no ortholog-strength inference is available "
                "on this row; the term survives on independent evidence, not on the "
                "transfer."
            ),
        },
        "supported": [
            q(
                "PMID:41961591",
                "Neurons sparsely receiving HA-ADGRA1 overexpression displayed surface HA signals along both MAP2-labeled dendrites and AnkG-labeled axon initial segments, suggesting subcellular localization to both pre- and postsynaptic sites",
            ),
            q(RESULTS_FILE, "**1 of 6** IBA donor tokens are ADGRA1 orthologs"),
        ],
    },
    ("GO:0007166", "IBA", "GO_REF:0000033"): {
        "action": "ACCEPT",
        "summary": (
            "The cautious parent, deliberately chosen by PAINT over GO:0007186, and "
            "supportable."
        ),
        "reason": (
            "Same node and same all-paralog donor set as the GO:0005886 row "
            "(PTN001738137; human ADGRA2 plus two zebrafish adgra2/adgra3). Worth "
            "recording that PAINT gave ADGRA1 this term and withheld GO:0007186 - "
            "i.e. it declined to commit the family node to G-protein coupling. That "
            "restraint was well judged at the time and is now vindicated in "
            "substance by PMID:41961591. ACCEPT; the term is true of a cell-surface "
            "7-TM receptor that activates heterotrimeric G proteins."
        ),
        "propagation": {
            "root_cause": "NO_FAILURE_NON_CORE",
            "note": (
                "All four non-node donors are ADGRA2/ADGRA3. Provenance note only; "
                "the term is generic enough that the paralog restriction does not "
                "threaten it."
            ),
        },
        "supported": [
            q(RESULTS_FILE, "| `PANTHER:PTN001738137` | ADGRA1, ADGRA2, ADGRA3 | GO:0005886, GO:0007166 |"),
        ],
    },
    ("GO:0014069", "IBA", "GO_REF:0000033"): {
        "action": "ACCEPT",
        "summary": (
            "Genuine ortholog transfer: the sole protein donor is mouse Adgra1, "
            "which holds this exact term by IDA."
        ),
        "reason": (
            "Node PTN002914505 reaches exactly ADGRA1 among human genes, and its "
            "only non-node WITH/FROM token is MGI:MGI:1277167 = mouse Adgra1 "
            "(Q8C4G9, Swiss-Prot). QuickGO shows that donor carries GO:0014069 by "
            "IDA (and EXP) from PMID:28935861, which combined brain sub-cellular "
            "fractionation with super-resolution microscopy. The ACRV1 precision "
            "check therefore comes back NEGATIVE here: the propagation lands on the "
            "same term as the donor's IDA, not several levels above it, so no "
            "downward MODIFY is warranted. Recorded because a null result from a "
            "check is a finding."
        ),
        "propagation": {
            "root_cause": "NO_FAILURE_CORE",
            "note": (
                "Single ortholog donor with its own IDA to the identical term; "
                "transfer is sound and maximally specific."
            ),
        },
        "supported": [
            q(
                "PMID:28935861",
                "Using super-resolution microscopy on primary neuronal culture we confirmed the postsynaptic localization of PLEKHA5 and ADGRA1.",
            ),
        ],
    },
    ("GO:0098978", "IBA", "GO_REF:0000033"): {
        "action": "ACCEPT",
        "summary": "Ortholog transfer from mouse Adgra1's SynGO IDA; same node as GO:0014069.",
        "reason": (
            "Node PTN002914505, donor MGI:MGI:1277167 = mouse Adgra1 (Q8C4G9), which "
            "holds GO:0098978 by IDA/EXP from PMID:28935861 curated by SynGO. "
            "Consistent with ADGRA1 being enriched in hippocampal PV interneurons, "
            "whose own excitatory inputs are glutamatergic, and with surface ADGRA1 "
            "puncta co-localising with pre- and postsynaptic markers. ACCEPT."
        ),
        "propagation": {
            "root_cause": "NO_FAILURE_CORE",
            "note": "Ortholog donor carrying the identical term by IDA. No precision loss.",
        },
        "supported": [
            q(
                "PMID:28935861",
                "Using super-resolution microscopy on primary neuronal culture we confirmed the postsynaptic localization of PLEKHA5 and ADGRA1.",
            ),
        ],
    },
    # ---- InterPro IEA ---------------------------------------------------------
    ("GO:0004888", "IEA", "GO_REF:0000002"): {
        "action": "MODIFY",
        "replacements": [("GO:0004930", "G protein-coupled receptor activity")],
        "summary": "Redundant ancestor of GO:0004930, which the gene holds and which is now supported.",
        "reason": (
            "IPR017981 is the family-2 (secretin-like) 7-TM signature, so the "
            "inference is sound as far as it goes, but GO:0004888 is the parent of "
            "GO:0004930 and adds nothing once the child is held. PMID:41961591 "
            "supplies direct evidence at the child's level (Galpha13/11/15 "
            "activation), so the specific term is the right one to keep. This is a "
            "redundancy MODIFY, not a correction."
        ),
        "supported": [
            q("PMID:41961591", "Full-length ADGRA1 activated several G proteins, most notably Gα13"),
        ],
    },
    ("GO:0004930", "IEA", "GO_REF:0000002"): {
        "action": "ACCEPT",
        "summary": "Fold-derived, but the activity is now independently demonstrated.",
        "reason": GPCR_REASON,
        "supported": [
            q("PMID:41961591", "Full-length ADGRA1 activated several G proteins, most notably Gα13"),
            q(
                "PMID:41961591",
                "Gα11, Gα15, and Gα13 all exhibited a plasmid copy-number-dependent change in BRET2, supporting the specificity of these measurements",
            ),
        ],
    },
    ("GO:0007166", "IEA", "GO_REF:0000002"): {
        "action": "ACCEPT",
        "summary": "Consistent with the IBA row for the same term; supported.",
        "reason": (
            "InterPro IPR017981 (family-2 7-TM) supports a cell-surface receptor "
            "signalling role, and PAINT independently assigns the same term. ACCEPT."
        ),
    },
    ("GO:0007186", "IEA", "GO_REF:0000002"): {
        "action": "ACCEPT",
        "summary": "Now supported downstream of the demonstrated G-protein activation.",
        "reason": (
            "GO:0007186 is defined as the series of molecular signals in which an "
            "activated receptor promotes GDP/GTP exchange on a heterotrimeric "
            "G-protein alpha subunit; PMID:41961591 demonstrates exactly that step "
            "for the mouse ortholog with three Galpha subtypes and a dose-response "
            "control. ACCEPT. Same caveat as GO:0004930: the definition's opening "
            "clause presumes a ligand, and ADGRA1 has none - raised as an ontology "
            "question rather than acted on."
        ),
        "supported": [
            q(
                "PMID:41961591",
                "Gα11, Gα15, and Gα13 all exhibited a plasmid copy-number-dependent change in BRET2, supporting the specificity of these measurements",
            ),
        ],
    },
    ("GO:0016020", "IEA", "GO_REF:0000120"): {
        "action": "MODIFY",
        "replacements": [("GO:0005886", "plasma membrane")],
        "summary": "Root-level membrane term; the specific compartment is known.",
        "reason": MEMBRANE_REASON
        + " This row derives from UniProtKB-SubCell:SL-0162, and UniProt's own "
        "SUBCELLULAR LOCATION for this entry is sequence-predicted "
        "(ECO:0000255) rather than observed, so nothing is lost by refining it.",
        "supported": [
            q(UNIPROT_FILE, "-!- SUBCELLULAR LOCATION: Membrane {ECO:0000255}; Multi-pass membrane"),
        ],
    },
    # ---- legacy NAS / TAS -----------------------------------------------------
    ("GO:0004930", "NAS", "PMID:12565841"): {
        "action": "ACCEPT",
        "summary": (
            "Term correct; the cited reference is a genome-mining paper with no "
            "functional data (flagged MISCITED)."
        ),
        "reason": GPCR_REASON
        + " This particular reference is a database search that in fact singles "
        "ADGRA1 out as the family member LACKING the GPS domain, so it is the "
        "weakest possible basis for a receptor-activity call. NAS is nonetheless "
        "the correct evidence code for an author statement of this kind, so there "
        "is nothing malformed to fix.",
        "supported": [
            q(
                "PMID:12565841",
                "All the novel receptors have a GPS domain in their N-terminus, except GPR123, as well as long Ser/Thr rich regions forming mucin-like stalks.",
            ),
        ],
    },
    ("GO:0004930", "NAS", "PMID:17212699"): {
        "action": "ACCEPT",
        "summary": (
            "Term correct; the cited reference is an expression-mapping paper whose "
            "functional claim is explicitly a speculation (flagged MISCITED)."
        ),
        "reason": GPCR_REASON
        + " The cited paper is an in-situ hybridisation and real-time PCR "
        "expression map; its only functional statement is hedged as what GPR123 "
        "'may' do.",
        "supported": [
            q(
                "PMID:17212699",
                "The CNS specific expression, together with the high sequence conservation between the vertebrate sequences investigated, indicate that GPR123 may have an important role in the regulation of neuronal signal transduction.",
            ),
        ],
    },
    ("GO:0007165", "NAS", "PMID:17212699"): {
        "action": "MODIFY",
        "replacements": [("GO:0007166", "cell surface receptor signaling pathway")],
        "summary": "Redundant ancestor of a term the gene already holds by IBA and by IEA.",
        "reason": (
            "GO:0007165 signal transduction is an ancestor of GO:0007166, which "
            "ADGRA1 holds twice already (IBA from PAINT, IEA from InterPro). The "
            "cited paper offers it only as a prediction from expression pattern and "
            "sequence conservation, with no assay. MODIFY to the informative "
            "descendant rather than REMOVE, since the essence is sound."
        ),
        "supported": [
            q(
                "PMID:17212699",
                "The CNS specific expression, together with the high sequence conservation between the vertebrate sequences investigated, indicate that GPR123 may have an important role in the regulation of neuronal signal transduction.",
            ),
        ],
    },
    ("GO:0016020", "NAS", "PMID:12565841"): {
        "action": "MODIFY",
        "replacements": [("GO:0005886", "plasma membrane")],
        "summary": "Root-level membrane term; the specific compartment is known.",
        "reason": MEMBRANE_REASON,
    },
    ("GO:0016020", "NAS", "PMID:17212699"): {
        "action": "MODIFY",
        "replacements": [("GO:0005886", "plasma membrane")],
        "summary": "Root-level membrane term; the specific compartment is known.",
        "reason": MEMBRANE_REASON,
    },
    ("GO:0004930", "TAS", "PMID:15203201"): {
        "action": "ACCEPT",
        "summary": (
            "Term correct, but this row is one of 25 identical block annotations "
            "from a family-catalogue paper (flagged MISCITED)."
        ),
        "reason": GPCR_REASON
        + " Provenance finding worth separating from the verdict: querying QuickGO "
        "by reference rather than by gene, PMID:15203201 carries 78 annotations "
        "across 27 distinct entities - GO:0016020 on 27, GO:0007186 on 26, "
        "GO:0004930 on 25 - i.e. essentially the whole human adhesion-GPCR family, "
        "all TAS, all assigned by GDB, from a paper that performed no perturbation "
        "on any of them. That is a block projection of family membership into a "
        "molecular function. It entered through GDB TAS, a route the ~April 2026 "
        "retirement of Swiss-Prot-keyword annotations did not touch, which is why "
        "this error class is still visible in GOA here.",
        "supported": [
            q(
                "PMID:15203201",
                "EST expression charts for the entire repertoire of adhesion-GPCRs in human and mouse were established.",
            ),
            q(RESULTS_FILE, "`PMID:15203201` annotates **27 distinct entities** with identical evidence"),
        ],
    },
    ("GO:0007186", "TAS", "PMID:15203201"): {
        "action": "ACCEPT",
        "summary": "Term now supported; row is part of the same 26-entity family block.",
        "reason": (
            "The pathway step the term names - an activated receptor promoting "
            "GDP/GTP exchange on a Galpha subunit - is demonstrated for the mouse "
            "ortholog in PMID:41961591. ACCEPT. As with the GO:0004930 TAS row, the "
            "cited reference is a repertoire catalogue that carries this term on 26 "
            "adhesion GPCRs at once and contains no experiment; that is a "
            "provenance defect recorded in reference_review, not grounds to remove a "
            "term that is independently supported."
        ),
        "supported": [
            q("PMID:15203201", "Currently the total number of human adhesion-GPCRs is 33."),
        ],
    },
    ("GO:0016020", "TAS", "PMID:15203201"): {
        "action": "MODIFY",
        "replacements": [("GO:0005886", "plasma membrane")],
        "summary": "Root-level membrane term; the specific compartment is known.",
        "reason": MEMBRANE_REASON
        + " This row is one of 27 identical GO:0016020 TAS annotations that "
        "PMID:15203201 carries across the adhesion-GPCR family.",
    },
}

# Per-partner detail for the 22 GO:0005515 rows. Kd values in micromolar, read
# from IntAct (see RESULTS.md Q3); None means IntAct carries the kd:1(molar)
# placeholder, i.e. the affinity fell below the assay's quantification threshold.
PARTNERS = {
    "Q02410": ("APBA1", 2, None),
    "Q99767": ("APBA2", 2, None),
    "Q12959": ("DLG1", 3, 4.6),
    "Q15700": ("DLG2", 3, 7.9),
    "Q92796": ("DLG3", 3, 9.8),
    "P78352": ("DLG4", 3, 8.3),
    "Q68DX3": ("FRMPD2", 3, None),
    "A4D2P6": ("GRID2IP", 2, None),
    "Q9Y3R0": ("GRIP1", 7, None),
    "Q9C0E4": ("GRIP2", 7, None),
    "Q14005": ("IL16", 4, None),
    "Q8TBB1": ("LNX1", 4, None),
    "Q8N448": ("LNX2", 4, 11.7),
    "Q96QZ7": ("MAGI1", 6, 21.2),
    "Q86UL8": ("MAGI2", 6, 6.7),
    "O75970": ("MPDZ", 13, None),
    "Q8NI35": ("PATJ", 10, None),
    "Q5T2W1": ("PDZK1", 4, None),
    "Q14160": ("SCRIB", 4, 20.6),
    "Q07157": ("TJP1", 3, None),
    "Q9P202": ("WHRN", 3, None),
}


def binding_verdict(acc: str, ref: str) -> dict:
    gene, ndom, kd = PARTNERS[acc]
    if ref == "PMID:24550280":
        method = (
            f"Proteomic peptide-phage display: the ADGRA1 C-terminal peptide was "
            f"selected from a library of all human C-terminal peptides by a PDZ "
            f"domain of {gene}. The interactor on the ADGRA1 side is the peptide, "
            f"not the full-length receptor - a real caveat, but the peptide is "
            f"precisely the PDZ-binding motif at issue."
        )
        quotes = [
            q(
                "PMID:24550280",
                "With these libraries we screened the nine PSD-95/Dlg/ZO-1 (PDZ) domains of human Densin-180, Erbin, Scribble, and Disks large homolog 1 for peptide ligands.",
            )
        ]
    else:
        aff = (
            f"IntAct records a best dissociation constant of {kd} uM"
            if kd is not None
            else (
                "IntAct carries the kd:1(molar) placeholder for every record, i.e. "
                "the affinity fell below the assay's quantification threshold "
                "(~100-800 uM); the pair is nonetheless curated as a detected "
                "positive (negative flag False)"
            )
        )
        method = (
            f"Quantitative holdup assay against a panel of human PDZ domains. "
            f"{gene} contributes {ndom} annotated PDZ domains, and {aff}."
        )
        quotes = [
            q(
                "PMID:36115835",
                "we measure the affinities of 65,000 interactions involving PDZ domains and their target PDZ-binding motifs (PBM)",
            )
        ]
    return {
        "action": "MODIFY",
        "replacements": [("GO:0030165", "PDZ domain binding")],
        "summary": (
            f"Uninformative 'protein binding' for a mechanistically defined "
            f"interaction: ADGRA1's C-terminal class I PDZ-binding motif engaging a "
            f"PDZ domain of {gene}."
        ),
        "reason": PDZ_MECHANISM + " " + method,
        "supported": quotes
        + [
            q(RESULTS_FILE, "21/21 partners carry at least one annotated PDZ domain"),
        ],
    }


# ------------------------------------------------------------------------ build


def parse_rows() -> list[dict]:
    lines = GOA.read_text().rstrip("\n").split("\n")
    hdr = lines[0].split("\t")
    return [dict(zip(hdr, ln.split("\t"))) for ln in lines[1:]]


def build_annotation(r: dict) -> dict:
    term, ev, ref = r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"]
    wf = [t for t in r["WITH/FROM"].split("|") if t]

    if term == "GO:0005515":
        assert len(wf) == 1 and wf[0].startswith("UniProtKB:"), f"unexpected WITH/FROM {wf}"
        v = binding_verdict(wf[0].split(":", 1)[1], ref)
    else:
        v = VERDICTS.get((term, ev, ref))
        assert v is not None, f"NO VERDICT for {(term, ev, ref)} -- refusing to default"

    ann: dict = {
        "term": {"id": term, "label": r["GO NAME"]},
        "evidence_type": ev,
        "original_reference_id": ref,
    }
    if r["QUALIFIER"]:
        ann["qualifier"] = r["QUALIFIER"]
    if wf:
        ann["supporting_entities"] = list(wf)

    rev: dict = {"summary": v["summary"], "action": v["action"]}
    if v.get("reason"):
        rev["reason"] = v["reason"]
    if v.get("replacements"):
        rev["proposed_replacement_terms"] = [
            {"id": i, "label": lab} for i, lab in v["replacements"]
        ]
    if v.get("supported"):
        rev["supported_by"] = [dict(s) for s in v["supported"]]
    if v.get("propagation"):
        p = v["propagation"]
        rev["propagation_review"] = {
            "root_cause": p["root_cause"],
            "source_entities": [
                {
                    "source_id": t,
                    "source_status": (
                        "SUPPORTS_TRANSFER" if not t.startswith("PANTHER:") else "UNRESOLVED"
                    ),
                    "comment": (
                        "PANTHER internal tree node, not a protein"
                        if t.startswith("PANTHER:")
                        else p["note"]
                    ),
                }
                for t in wf
            ],
        }
    ann["review"] = rev
    return ann


# Only ONE NEW row. GO:0004930 is deliberately NOT proposed as NEW even though it
# needs a real evidence line: the term is already in GOA (four times), and the
# validator is right that NEW is for terms GOA lacks. The request to attach
# PMID:41961591 as an ISS evidence line to the existing term is made in
# suggested_questions and in each GO:0004930 row's reason instead.
NEW_ROWS = [
    {
        "term": {"id": "GO:0098982", "label": "GABA-ergic synapse"},
        "evidence_type": "ISS",
        "original_reference_id": "PMID:41961591",
        "qualifier": "is_active_in",
        "supporting_entities": ["UniProtKB:Q8C4G9"],
        "review": {
            "summary": (
                "Proposed: the cellular-component half of the same 2026 evidence that "
                "supports the GO:0032230 row - the receptor is at the inhibitory synapse."
            ),
            "action": "NEW",
            "reason": (
                "GOA places ADGRA1 only at the glutamatergic synapse and postsynaptic "
                "density, both by IBA from a 2017 sub-cellular proteomics survey. The "
                "2026 study localises it directly at the INHIBITORY synapse: HA-ADGRA1 "
                "delivered ex vivo to the dentate gyrus of PV-Cre and SST-Cre mice "
                "co-localises with vGAT, the vesicular GABA transporter. Without this "
                "term the review asserts a molecular function at the glutamatergic "
                "postsynapse while asserting positive regulation of GABAergic "
                "transmission as the process, and the compartment and the process do "
                "not line up. Same reference, same organism, same strength as the "
                "GO:0032230 row, so the same evidence code: ISS from mouse Adgra1 "
                "(Q8C4G9). This is additive - the existing GO:0098978 ACCEPT is left "
                "alone, deferring to the SynGO curator, and the two terms are not "
                "mutually exclusive for a receptor found at a subset of synapses of "
                "both kinds. GO:0098793 presynapse was considered and DECLINED: the "
                "only statement supporting it is hedged ('suggesting subcellular "
                "localization'), it rests entirely on overexpressed HA-tagged receptor "
                "because no reliable antibody exists, and the paper's own functional "
                "controls argue against the presynaptic release apparatus being where "
                "the receptor acts - paired-pulse ratio and coefficient of variation "
                "are unchanged and Syt2-labelled PV terminal density is unaltered. "
                "Recorded as a knowledge gap instead."
            ),
            "supported_by": [
                {
                    "reference_id": "PMID:41961591",
                    "supporting_text": "HA-ADGRA1 localized with inhibitory vGAT slightly higher in PV+ neurons than in SST+ neurons",
                },
                {
                    "reference_id": "PMID:41961591",
                    "supporting_text": "Surface ADGRA1 formed puncta that partially co-localized with both pre- and postsynaptic markers",
                },
            ],
        },
    },
    {
        "term": {
            "id": "GO:0032230",
            "label": "positive regulation of synaptic transmission, GABAergic",
        },
        "evidence_type": "ISS",
        "original_reference_id": "PMID:41961591",
        "qualifier": "involved_in",
        "supporting_entities": ["UniProtKB:Q8C4G9"],
        "review": {
            "summary": (
                "Proposed: ADGRA1 is required in PV interneurons for normal "
                "inhibitory synaptic strength onto dentate gyrus granule cells."
            ),
            "action": "NEW",
            "reason": (
                "Conditional deletion of Adgra1 in parvalbumin interneurons reduces "
                "inhibitory synaptic strength onto dentate gyrus granule cells and "
                "impairs PV intrinsic excitability, so the receptor positively "
                "regulates GABAergic synaptic transmission. The perturbation is in "
                "mouse, hence ISS for the human gene with UniProtKB:Q8C4G9 as the "
                "supporting entity. This is currently ADGRA1's only functional "
                "biological process supported by a perturbation of any kind, and it "
                "sits on the same mouse gene that seeds PAINT node PTN002914505 - so "
                "it is also the obvious candidate for PAINT to propagate."
            ),
            "supported_by": [
                {
                    "reference_id": "PMID:41961591",
                    "supporting_text": "ADGRA1 deletion in PV interneurons impairs intrinsic excitability and reduces inhibitory synaptic strength onto dentate gyrus granule cells.",
                },
            ],
        },
    },
]


def main() -> int:
    rows = parse_rows()
    anns = [build_annotation(r) for r in rows]

    # Invariant 1: one entry per GOA data line, plus the NEW rows, counted apart.
    assert len(anns) == len(rows), f"{len(anns)} entries for {len(rows)} GOA rows"

    # Invariant 2: supporting_entities mirrors WITH/FROM exactly, by construction.
    for a, r in zip(anns, rows):
        want = [t for t in r["WITH/FROM"].split("|") if t]
        got = a.get("supporting_entities", [])
        assert got == want, f"{a['term']['id']}: supporting_entities {got} != WITH/FROM {want}"

    doc = yaml.safe_load(OUT.read_text())
    doc["status"] = "COMPLETE"
    doc["description"] = DESCRIPTION
    doc["aliases"] = ["GPR123", "KIAA1828"]
    doc["references"] = REFERENCES
    doc["existing_annotations"] = anns + NEW_ROWS
    doc["core_functions"] = CORE_FUNCTIONS
    doc["knowledge_gaps"] = KNOWLEDGE_GAPS
    # Question and Experiment are objects in the schema, not bare strings.
    doc["suggested_questions"] = [
        {"question": q_, "experts": e_} for q_, e_ in SUGGESTED_QUESTIONS
    ]
    doc["suggested_experiments"] = [
        {"description": desc, "hypothesis": hyp} for hyp, desc in SUGGESTED_EXPERIMENTS
    ]

    text = yaml.dump(
        doc, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=100
    )
    # Invariant 3: no anchors survived, so raw-text counts over the file mean something.
    assert not re.search(r"&id\d+", text), "PyYAML emitted an anchor: rows are sharing an object"
    OUT.write_text(text)

    from collections import Counter

    acts = Counter(a["review"]["action"] for a in anns)
    print(f"GOA rows: {len(rows)}  entries: {len(anns)}  NEW: {len(NEW_ROWS)}")
    print("actions over GOA rows:", dict(acts))
    print(f"wrote {OUT}")
    return 0


DESCRIPTION = (
    "ADGRA1 (GPR123) is a brain-enriched seven-transmembrane receptor and the "
    "structural outlier of the adhesion G protein-coupled receptor family: unlike "
    "the other 32 human members it has no extracellular adhesion modules and no "
    "GAIN/GPS domain, its canonical isoform presenting only a 19-residue "
    "extracellular N-terminus ahead of the first transmembrane helix. Its bulk lies "
    "inside the cell, in a 255-residue cytoplasmic tail that terminates in a class I "
    "PDZ-binding motif (ETTV). Through that motif the receptor binds the PDZ domains "
    "of a wide set of membrane-associated scaffolds - the DLG/MAGUK proteins DLG1-4, "
    "MAGI1/2, SCRIB, MPDZ, PATJ, GRIP1/2, LNX1/2 and others - with micromolar "
    "affinities, placing it within postsynaptic scaffold networks. In the mammalian "
    "brain the receptor is enriched in thalamic nuclei, deep cortical layers, "
    "amygdala, hypothalamus and hippocampus, and localises to postsynaptic "
    "compartments and to a subset of synapses. In the hippocampus it is selectively "
    "enriched in parvalbumin-positive inhibitory interneurons, where it is required "
    "for their intrinsic excitability and for the strength of the inhibitory "
    "synapses they make onto dentate gyrus granule cells. No agonist is known, and "
    "the receptor activates heterotrimeric G proteins - most notably Galpha13, along "
    "with Galpha11 and Galpha15 - in an agonist-independent manner that does not "
    "require its short extracellular segment, suggesting it is regulated by "
    "localisation rather than by ligand binding. Loss of the receptor in mice also "
    "raises energy expenditure and thermogenesis and increases anxiety-like "
    "behaviour, and the human protein is required for maintenance of pluripotency in "
    "pluripotent stem cells."
)

REFERENCES = [
    # GO_REF entries: titles copied verbatim from the GO Consortium registry
    # (go-site/metadata/gorefs.yaml), never written from memory.
    {
        "id": "GO_REF:0000033",
        "title": "Annotation inferences using phylogenetic trees",
        "reference_review": {
            "relevance": "HIGH",
            "correctness": "VERIFIED",
            "review_notes": (
                "PAINT/PANTHER phylogenetic inference, behind all four IBA rows. The "
                "node structure it produced for this family is sound - see the "
                "GO:0005886 and GO:0014069 rows and the node-reach table in "
                "ADGRA1-bioinformatics/RESULTS.md."
            ),
        },
    },
    {
        "id": "GO_REF:0000002",
        "title": "Gene Ontology annotation through association of InterPro records with GO terms",
        "reference_review": {
            "relevance": "MEDIUM",
            "correctness": "VERIFIED",
            "review_notes": (
                "InterPro2GO, behind four IEA rows via IPR000832, IPR017981 and "
                "IPR017983. Fold-derived and therefore weak on its own, but the "
                "family-2 7-TM assignment is correct for this protein and the "
                "activity it implies is now independently demonstrated."
            ),
        },
    },
    {
        "id": "GO_REF:0000120",
        "title": "Combined Automated Annotation using Multiple IEA Methods",
        "reference_review": {
            "relevance": "LOW",
            "correctness": "VERIFIED",
            "review_notes": (
                "Behind the single GO:0016020 IEA row, sourced from "
                "UniProtKB-SubCell:SL-0162. Refined to GO:0005886 in this review."
            ),
        },
    },
    {
        "id": "file:human/ADGRA1/ADGRA1-deep-research-affinage.md",
        "title": "Affinage mechanistic annotation for ADGRA1 (human)",
        "reference_review": {
            "relevance": "LOW",
            "correctness": "LOW_QUALITY",
            "review_notes": (
                "Provider record, gates_passed: True, no bioRxiv-DOI pseudo-PMIDs in "
                "its citation list, and it surfaced the two most load-bearing "
                "references here (PMID:28935861, PMID:41961591). Two defects mean "
                "nothing in this review rests on it. First, it lists PMID:40766348 "
                "(2025 bioRxiv) and PMID:41961591 (2026 Cell Reports) as two separate "
                "dated findings; PubMed records UpdateIn: 41961591 on the former, so "
                "they are one study double-counted. Second, its headline claims track "
                "the preprint abstract (PV and SST interneurons, learning and memory "
                "deficits) where the published abstract is narrowed to PV. It also "
                "never mentions the PDZ interactome, which is the best-evidenced "
                "molecular fact about this protein."
            ),
        },
    },
    {
        "id": "PMID:41961591",
        "title": "The atypical adhesion GPCR ADGRA1 controls hippocampal inhibitory circuit function.",
        "reference_review": {
            "relevance": "HIGH",
            "correctness": "VERIFIED",
            "review_notes": (
                "The only functional characterisation of the receptor itself. "
                "PubMed-verified; full text cached. Establishes agonist-independent "
                "activation of Galpha13/11/15 by the mouse ortholog (Q8C4G9, stated "
                "in the Plasmids section) using the 14-sensor TRUPATH BRET2 panel "
                "with a dose-response control, and a PV-interneuron conditional "
                "knockout phenotype. No retraction, erratum or expression of "
                "concern; Crossref shows no update-to, only has-preprint."
            ),
        },
    },
    {
        "id": "PMID:40766348",
        "title": "The atypical adhesion GPCR ADGRA1 controls hippocampal inhibitory circuit function.",
        "publication_type": "PREPRINT",
        "reference_review": {
            "relevance": "LOW",
            "correctness": "VERIFIED",
            "review_notes": (
                "bioRxiv preprint of PMID:41961591 (PubMed records UpdateIn: "
                "41961591). Listed for transparency because the affinage report "
                "counts it as a separate dated finding, which double-counts one "
                "study. Nothing in this review rests on it uniquely; where the two "
                "versions differ - the preprint headline claims PV and SST, the "
                "published abstract is narrowed to PV - the published version is "
                "used."
            ),
        },
    },
    {
        "id": "PMID:36115835",
        "title": "Quantitative fragmentomics allow affinity mapping of interactomes.",
        "reference_review": {
            "relevance": "HIGH",
            "correctness": "VERIFIED",
            "review_notes": (
                "Source of 21 of the 22 GO:0005515 rows. Quantitative holdup assay "
                "over 266 human PDZ domains against 448 PDZ-binding motifs, so the "
                "partner set is PDZ-specific by construction. ADGRA1 itself is not "
                "named in the main text - its data are in Supplementary Data 1 - so "
                "no ADGRA1-specific sentence is quoted from it here; the "
                "per-partner numbers come from IntAct. Carries an Author Correction "
                "(PMID:36477203) which was read and is figure formatting only "
                "(missing PCC values, missing axis labels, panel order), affecting "
                "no data."
            ),
        },
    },
    {
        "id": "PMID:24550280",
        "title": "Large-scale interaction profiling of PDZ domains through proteomic peptide-phage display using human and viral phage peptidomes.",
        "reference_review": {
            "relevance": "HIGH",
            "correctness": "VERIFIED",
            "review_notes": (
                "Source of the DLG1 GO:0005515 row. ProP-PD against libraries of all "
                "human C-terminal peptides screened with nine PDZ domains including "
                "DLG1's; the ADGRA1 entity is its C-terminal peptide rather than the "
                "full-length protein, which is noted in the row. No corrections "
                "found by PubMed CommentsCorrections or by Crossref relation."
            ),
        },
    },
    {
        "id": "PMID:28935861",
        "title": "Correlation profiling of brain sub-cellular proteomes reveals co-assembly of synaptic proteins and subcellular distribution.",
        "reference_review": {
            "relevance": "HIGH",
            "correctness": "VERIFIED",
            "review_notes": (
                "The experimental basis for both IBA cellular-component rows: mouse "
                "Adgra1 (Q8C4G9) holds GO:0014069 and GO:0098978 by IDA/EXP from "
                "this paper, curated by SynGO, and is the sole protein donor at "
                "PANTHER node PTN002914505. Confirmed via QuickGO that the donor's "
                "own annotation is to the same terms that propagated, not to more "
                "specific ones."
            ),
        },
    },
    {
        "id": "PMID:17212699",
        "title": "The evolutionary history and tissue mapping of GPR123: specific CNS expression pattern predominantly in thalamic nuclei and regions containing large pyramidal cells.",
        "reference_review": {
            "relevance": "MEDIUM",
            "correctness": "MISCITED",
            "review_notes": (
                "Genuine, correctly identified paper, and its expression mapping and "
                "its prediction of a C-terminal PDZ-binding motif are used here as "
                "sound. MISCITED refers specifically to the two GOA rows that rest "
                "on it: GO:0004930 and GO:0007165 by NAS. The paper is an in-situ "
                "hybridisation and real-time PCR survey containing no functional or "
                "biochemical assay, and its only functional statement is hedged as "
                "what GPR123 'may' do."
            ),
        },
    },
    {
        "id": "PMID:12565841",
        "title": "There exist at least 30 human G-protein-coupled receptors with long Ser/Thr-rich N-termini.",
        "reference_review": {
            "relevance": "MEDIUM",
            "correctness": "MISCITED",
            "review_notes": (
                "Correctly identified, and the source of the durable structural fact "
                "that GPR123 alone in the family lacks a GPS domain. MISCITED for "
                "the GO:0004930 NAS row that cites it: the paper is a search of "
                "human genome databases followed by phylogenetic clustering, with no "
                "functional experiment on any of the six receptors it reports."
            ),
        },
    },
    {
        "id": "PMID:15203201",
        "title": "The human and mouse repertoire of the adhesion family of G-protein-coupled receptors.",
        "reference_review": {
            "relevance": "LOW",
            "correctness": "MISCITED",
            "review_notes": (
                "A repertoire catalogue with EST expression charts and no "
                "perturbation of any receptor. Querying QuickGO by reference shows "
                "it carries 78 annotations across 27 distinct entities - GO:0016020 "
                "on 27, GO:0007186 on 26, GO:0004930 on 25, all TAS, all assigned by "
                "GDB - i.e. it annotates essentially the entire human adhesion-GPCR "
                "family with the same three terms. The terms happen to be defensible "
                "for ADGRA1 on other evidence, but this reference does not support "
                "them for any individual gene."
            ),
        },
    },
    {
        "id": "PMID:33824276",
        "title": "ADGRA1 negatively regulates energy expenditure and thermogenesis through both sympathetic nervous system and hypothalamus-pituitary-thyroid axis in male mice.",
        "reference_review": {
            "relevance": "MEDIUM",
            "correctness": "VERIFIED",
            "review_notes": (
                "Constitutive mouse knockout; supports a non-core organismal role "
                "not currently represented in GOA. Sex-limited (male mice) and "
                "attributed to hypothalamic signalling rather than to a "
                "cell-autonomous receptor activity, so it is recorded as background "
                "rather than proposed as a term for the human gene."
            ),
        },
    },
    {
        "id": "PMID:36115515",
        "title": "Increased Anxiety-like Behaviors in Adgra1(-/-) Male But Not Female Mice are Attributable to Elevated Neuron Dendrite Density, Upregulated PSD95 Expression, and Abnormal Activation of the PI3K/AKT/GSK-3β and MEK/ERK Pathways.",
        "reference_review": {
            "relevance": "LOW",
            "correctness": "VERIFIED",
            "review_notes": (
                "Behavioural phenotype of the same constitutive knockout, again "
                "male-specific. Organism-level and several steps removed from a "
                "molecular function; not used to support any term."
            ),
        },
    },
    {
        "id": "PMID:36672239",
        "title": "Essential Role of Adhesion GPCR, GPR123, for Human Pluripotent Stem Cells and Reprogramming towards Pluripotency.",
        "reference_review": {
            "relevance": "MEDIUM",
            "correctness": "VERIFIED",
            "review_notes": (
                "The only functional study performed on the HUMAN protein, by RNAi "
                "in human pluripotent stem cells. Reported as a knowledge gap rather "
                "than as a proposed term: the readouts are pleiotropic (colony "
                "morphology, cell cycle, NANOG, E-cadherin) and no molecular "
                "function of the receptor is isolated."
            ),
        },
    },
    {
        "id": "PMID:25713288",
        "title": "International Union of Basic and Clinical Pharmacology. XCIV. Adhesion G protein-coupled receptors.",
        "publication_type": "REVIEW",
        "reference_review": {
            "relevance": "LOW",
            "correctness": "VERIFIED",
            "review_notes": (
                "IUPHAR nomenclature review; the source of the ADGRA1 name in "
                "UniProt (ECO:0000303|PubMed:25713288). Background only."
            ),
        },
    },
    {
        "id": UNIPROT_FILE,
        "title": "UniProtKB entry Q86SQ6 (AGRA1_HUMAN)",
        "reference_review": {
            "relevance": "HIGH",
            "correctness": "VERIFIED",
            "review_notes": (
                "Primary source for topology (TOPO_DOM 1..19 extracellular, "
                "TRANSMEM 20..40, TOPO_DOM 306..560 cytoplasmic), for the sequence "
                "whose C-terminus is ETTV, and for the CC INTERACTION block. "
                "Corrections to report upstream are listed in suggested_questions."
            ),
        },
    },
    {
        "id": RESULTS_FILE,
        "title": "ADGRA1 (Q86SQ6) — computed evidence for the GO review",
        "reference_review": {
            "relevance": "HIGH",
            "correctness": "VERIFIED",
            "review_notes": (
                "Reproducible analysis (analyze_adgra1.py) re-reading UniProt, "
                "IntAct and QuickGO at run time; no value is hardcoded. Carries a "
                "self-test that was break-tested in the direction each check exists "
                "to catch."
            ),
        },
    },
]

CORE_FUNCTIONS = [
    {
        "description": (
            "Binds the PDZ domains of postsynaptic and junctional scaffold proteins "
            "through a class I PDZ-binding motif (ETTV) at the end of its "
            "cytoplasmic tail, coupling the receptor into MAGUK and multi-PDZ "
            "scaffold networks. Affinities measured by holdup assay run from ~4.6 uM "
            "(DLG1) to ~116 uM (MAGI2), with DLG1-4, MAGI1/2 and SCRIB the "
            "best-quantified partners. The motif is not required for synaptic "
            "targeting, which depends on other features of the tail."
        ),
        "molecular_function": {"id": "GO:0030165", "label": "PDZ domain binding"},
        "locations": [
            {"id": "GO:0005886", "label": "plasma membrane"},
            {"id": "GO:0014069", "label": "postsynaptic density"},
            {"id": "GO:0098978", "label": "glutamatergic synapse"},
            {"id": "GO:0098982", "label": "GABA-ergic synapse"},
        ],
        "supported_by": [
            {
                "reference_id": "PMID:36115835",
                "supporting_text": "we measure the affinities of 65,000 interactions involving PDZ domains and their target PDZ-binding motifs (PBM)",
            },
            {
                "reference_id": "PMID:41961591",
                "supporting_text": "ADGRA1 exhibits a 7-transmembrane (7-TM) GPCR followed by a relatively large cytoplasmic tail",
            },
            {
                "reference_id": "PMID:41961591",
                "supporting_text": "ADGRA1-ΔPDZ localized to synapses comparable to the WT, suggesting that other sequence features are responsible for synaptic localization.",
            },
            {
                "reference_id": RESULTS_FILE,
                "supporting_text": "21/21 partners carry at least one annotated PDZ domain",
            },
        ],
    },
    {
        "description": (
            "Activates heterotrimeric G proteins - most notably Galpha13, and also "
            "Galpha11 and Galpha15 - as a seven-transmembrane receptor at the "
            "neuronal surface. Activation is agonist-independent: no ligand is "
            "known, and replacing the receptor's 19-residue extracellular segment "
            "with a glycine linker leaves the coupling profile unchanged, so the "
            "receptor appears to be regulated by localisation rather than by ligand "
            "binding. Demonstrated for the mouse ortholog (Q8C4G9) overexpressed in "
            "HEK293T cells. In hippocampal parvalbumin interneurons this pathway is "
            "required for intrinsic excitability and for the strength of the "
            "inhibitory synapses those interneurons make onto dentate gyrus granule "
            "cells."
        ),
        "molecular_function": {
            "id": "GO:0004930",
            "label": "G protein-coupled receptor activity",
        },
        "directly_involved_in": [
            {"id": "GO:0007186", "label": "G protein-coupled receptor signaling pathway"},
            {
                "id": "GO:0032230",
                "label": "positive regulation of synaptic transmission, GABAergic",
            },
        ],
        "locations": [
            {"id": "GO:0005886", "label": "plasma membrane"},
            {"id": "GO:0098982", "label": "GABA-ergic synapse"},
        ],
        "supported_by": [
            {
                "reference_id": "PMID:41961591",
                "supporting_text": "Full-length ADGRA1 activated several G proteins, most notably Gα13",
            },
            {
                "reference_id": "PMID:41961591",
                "supporting_text": "Gα11, Gα15, and Gα13 all exhibited a plasmid copy-number-dependent change in BRET2, supporting the specificity of these measurements",
            },
            {
                "reference_id": "PMID:41961591",
                "supporting_text": "The G protein coupling profile of ΔN-ADGRA1 was similar to full-length ADGRA1, suggesting that this extracellular sequence is not involved in basal G protein activation",
            },
            {
                "reference_id": "PMID:41961591",
                "supporting_text": "ADGRA1 deletion in PV interneurons impairs intrinsic excitability and reduces inhibitory synaptic strength onto dentate gyrus granule cells.",
            },
        ],
    },
]

KNOWLEDGE_GAPS = [
    {
        "gap_statement": (
            "Whether ADGRA1 sits on the presynaptic or the postsynaptic side of the "
            "inhibitory synapse is unresolved. Two distinct questions are involved and "
            "the evidence bears on them unequally. On LOCALISATION, the only positive "
            "statements are that tagged receptor appears on dendrites and on axon "
            "initial segments and co-localises with vGAT - and that sentence is hedged "
            "('suggesting subcellular localization'), rests entirely on overexpressed "
            "HA-tagged protein because no reliable antibody exists, and the rescue "
            "result establishes which CELL the receptor is needed in rather than which "
            "side of the synapse it occupies. Those are the grounds on which GO:0098793 "
            "presynapse was considered and not proposed. Separately, on FUNCTION, "
            "paired-pulse ratio, coefficient of variation and Syt2-labelled terminal "
            "density are all unaltered, so whatever the receptor does, it is not acting "
            "through presynaptic release probability or terminal number. That is a "
            "mechanistic gap in its own right and is not evidence about where the "
            "protein is."
        ),
        "boundary": (
            "Known: the receptor is at inhibitory synapses (vGAT co-localisation) and "
            "is required in PV cells for their inhibitory output. Unknown: which side "
            "of the synapse the protein occupies, and by what mechanism a receptor "
            "that does not change release probability reduces inhibitory strength. "
            "Every localisation result rests on overexpressed tagged protein, because "
            "no reliable antibody exists."
        ),
        "gap_kind": ["BIOLOGY"],
        "provenance": [
            {
                "reference_id": "PMID:41961591",
                "supporting_text": "Given the absence of reliable antibodies for ADGRA1, we expressed HA-tagged ADGRA1 in primary hippocampal cultures",
            },
            {
                "reference_id": "PMID:41961591",
                "supporting_text": "PV-cKO GCs displayed no changes in the PPR or coefficient of variation in eIPSCs, supporting that presynaptic release probability is preserved",
            },
            {
                "reference_id": "PMID:41961591",
                "supporting_text": "the overall density of PV terminals labeled with synaptotagmin-2 (Syt2) was unaltered throughout the hippocampus",
            },
        ],
    },
    {
        "gap_statement": (
            "No agonist is known for ADGRA1, and unlike every other adhesion GPCR it "
            "cannot use the tethered-agonist mechanism, because it has no GAIN "
            "domain and only a 19-residue extracellular N-terminus. The one "
            "experiment that tested whether that segment matters found it "
            "dispensable for basal G-protein activation, so how the receptor is "
            "switched on - or whether it is constitutively active and controlled "
            "only by where it is - is unresolved."
        ),
        "boundary": (
            "Known: the receptor activates Galpha13/11/15 when overexpressed, and "
            "deleting residues 1-22 does not change that. Unknown: whether any "
            "extracellular or membrane-embedded ligand exists, and whether coupling "
            "in neurons is regulated at all."
        ),
        "gap_kind": ["BIOLOGY"],
        "provenance": [
            {
                "reference_id": "PMID:41961591",
                "supporting_text": "The G protein coupling profile of ΔN-ADGRA1 was similar to full-length ADGRA1, suggesting that this extracellular sequence is not involved in basal G protein activation",
            },
            {
                "reference_id": UNIPROT_FILE,
                "supporting_text": "-!- FUNCTION: Orphan receptor.",
            },
        ],
    },
    {
        "gap_statement": (
            "The C-terminal PDZ-binding motif binds at least 21 scaffold proteins "
            "with measurable affinity, yet its cellular job is unidentified: "
            "deleting it changes neither synaptic localisation nor co-localisation "
            "with Galpha13. Which of the PDZ partners the receptor actually engages "
            "in a parvalbumin interneuron, and what that engagement does, is open."
        ),
        "boundary": (
            "Known: the motif exists, is conserved, and binds DLG1-4, MAGI1/2, SCRIB "
            "and others in vitro at 4.6-116 uM. Known negative: it is not required "
            "for synaptic targeting. Unknown: any in vivo consequence of the motif."
        ),
        "gap_kind": ["BIOLOGY"],
        "provenance": [
            {
                "reference_id": "PMID:41961591",
                "supporting_text": "ADGRA1-ΔPDZ localized to synapses comparable to the WT, suggesting that other sequence features are responsible for synaptic localization.",
            },
        ],
    },
    {
        "gap_statement": (
            "Almost every functional fact about ADGRA1 comes from mouse. The only "
            "experiments on the human protein are an RNAi study in pluripotent stem "
            "cells, whose readouts are pleiotropic and isolate no molecular "
            "function, and two in vitro PDZ-domain binding datasets. There is no "
            "human electrophysiology, no human G-protein coupling measurement and no "
            "antibody able to detect the endogenous protein in either species."
        ),
        "boundary": (
            "Known: human C-terminal peptide binds human PDZ domains; human protein "
            "is detected by mass spectrometry (UniProt PE 1). Unknown: whether human "
            "ADGRA1 couples to Galpha13, and where the endogenous protein is."
        ),
        "gap_kind": ["BIOLOGY", "CURATION"],
        "provenance": [
            {
                "reference_id": "PMID:36672239",
                "supporting_text": "Essential Role of Adhesion GPCR, GPR123, for Human Pluripotent Stem Cells and Reprogramming towards Pluripotency",
            },
        ],
    },
    {
        "gap_statement": (
            "PAINT gives ADGRA1 no molecular function and no functional biological "
            "process. Node PTN002914505, whose human reach is exactly ADGRA1, "
            "carries only two cellular-component terms, both traceable to a 2017 "
            "sub-cellular proteomics survey. The 2026 functional work on mouse "
            "Adgra1 - the very gene behind that node's only donor, MGI:MGI:1277167 - "
            "has not yet reached the tree."
        ),
        "boundary": (
            "Known: the node exists, is correctly scoped to ADGRA1 orthologs, and "
            "already uses mouse Adgra1 as its donor. Unknown to PAINT: that the same "
            "donor now carries G-protein coupling data and a conditional-knockout "
            "synaptic phenotype."
        ),
        "gap_kind": ["CURATION"],
        "provenance": [
            {
                "reference_id": RESULTS_FILE,
                "supporting_text": "| `PANTHER:PTN002914505` | ADGRA1 | GO:0014069, GO:0098978 |",
            },
        ],
    },
    {
        "gap_statement": (
            "GO:0004930 and GO:0007186 both presuppose a ligand in their definitions "
            "('combining with an extracellular signal'; 'initiated by a ligand "
            "binding to its receptor'), and GO offers no ligand-free sibling. Orphan "
            "and constitutively active receptors such as ADGRA1 are therefore "
            "annotated to terms whose first clause is unestablished for them."
        ),
        "boundary": (
            "Known: the GDP/GTP-exchange half of both definitions is demonstrated "
            "for ADGRA1. Unknown/absent: any GO term expressing receptor-driven "
            "G-protein activation without a ligand-reception step."
        ),
        "gap_kind": ["ONTOLOGY"],
        "provenance": [
            {
                "reference_id": "PMID:41961591",
                "supporting_text": "Full-length ADGRA1 activated several G proteins, most notably Gα13",
            },
        ],
    },
]

SUGGESTED_QUESTIONS = [
    (
        "For PAINT. Node PTN002914505 has a human reach of exactly ADGRA1 and gives "
        "it only GO:0014069 and GO:0098978, both from a 2017 proteomics survey; "
        "ADGRA1 consequently receives no molecular function and no functional "
        "biological process from the tree at all. Its sole donor, MGI:MGI:1277167 "
        "(mouse Adgra1), now carries direct G-protein coupling data and a "
        "parvalbumin-interneuron conditional-knockout phenotype from PMID:41961591. "
        "Would GO_Central consider adding GO:0004930 and a GABAergic "
        "synaptic-transmission term at that node? It would give ADGRA1 orthologs "
        "across vertebrates their first mechanism term in one edit.",
        ["GO_Central PAINT curators", "PANTHER"],
    ),
    (
        "For GOA. PMID:15203201, a catalogue of the human and mouse adhesion-GPCR "
        "repertoire with EST expression charts and no perturbation experiment, "
        "carries 78 TAS annotations from GDB across 27 distinct entities: GO:0016020 "
        "on 27, GO:0007186 on 26, GO:0004930 on 25 - essentially the whole family. "
        "This is the 'structural class became a molecular function' pattern that the "
        "retirement of Swiss-Prot-keyword annotations was expected to have removed "
        "from GO; it survives because it entered via GDB TAS rather than via "
        "UniProtKB-KW. The terms are defensible for ADGRA1 on independent 2026 "
        "evidence, but that will not be true of all 25 recipients. Is a review of "
        "this reference's block warranted?",
        ["GOA curators", "GO Consortium"],
    ),
    (
        "For UniProt (Q86SQ6). Four corrections, none of which has a GO row to act "
        "on. (1) CC FUNCTION reads only 'Orphan receptor'; the entry predates "
        "PMID:41961591 (Galpha13/11/15 coupling of the mouse ortholog) and "
        "PMID:36115835 (21 PDZ partners with measured affinities). (2) There is no "
        "FT MOTIF feature for the C-terminal class I PDZ-binding motif at residues "
        "557-560 (ETTV), even though the entry's own CC INTERACTION block lists 21 "
        "PDZ-domain proteins and the motif has been predicted in the literature "
        "since 2007. (3) CC SUBCELLULAR LOCATION is 'Membrane {ECO:0000255}', "
        "sequence-predicted, while SynGO holds IDA postsynaptic-density and "
        "glutamatergic-synapse annotations on the mouse ortholog. (4) NbExp in the "
        "INTERACTION block counts PDZ domains assayed within one holdup dataset, not "
        "independent experiments - it equals the IntAct record count for 21 of 21 "
        "partners.",
        ["UniProt curators"],
    ),
    (
        "For IntAct/GOA. The 21-partner GO:0005515 set for ADGRA1 is the subset of "
        "IntAct's 80 partners with two or more records, and because every record is "
        "one PDZ domain from the same holdup dataset, that filter selects "
        "multi-PDZ-domain scaffolds rather than strong binders. Thirteen of the 21 "
        "selected partners have no quantified affinity at all, while 23 partners "
        "with a measured Kd are excluded. The cleanest statement of the problem is a "
        "single pair: SNX27, at 3.7 uM the TIGHTEST binder measured anywhere in the "
        "dataset, is excluded, while DLG1 at 4.6 uM - the second tightest - is "
        "retained. Affinity is therefore not what separates them; PDZ-domain count "
        "is. Of the four tightest binders overall (SNX27 3.7, DLG1 4.6, MAST2 4.9, "
        "MAGI3 5.1 uM) three are excluded and only DLG1 is kept. Should an "
        "affinity-aware criterion be used "
        "where the source assay reports dissociation constants?",
        ["IntAct curators", "GOA curators"],
    ),
    (
        "Ontology question, raised rather than acted on. GO:0004930's definition "
        "requires 'combining with an extracellular signal and transmitting the "
        "signal across the membrane by activating an associated G-protein', and "
        "GO:0007186's begins 'initiated by a ligand binding to its receptor'. ADGRA1 "
        "satisfies the G-protein half and not the ligand half: it is an orphan, its "
        "activation is agonist-independent, and deleting its entire 19-residue "
        "ectodomain does not change the coupling profile. Is a definitional revision "
        "or a ligand-independent sibling term warranted for constitutively active "
        "and orphan receptors?",
        ["GO ontology editors"],
    ),
]

SUGGESTED_EXPERIMENTS = [
    (
        'Human ADGRA1 couples to Galpha13 as the mouse ortholog does, and the long Ser/Thr-rich isoform Q86SQ6-1 behaves differently from the canonical ectodomain-less isoform.',
        "Measure G-protein coupling of the HUMAN receptor. Every coupling "
        "measurement to date used mouse Adgra1 (Q8C4G9); running the same TRUPATH "
        "BRET2 panel on human ADGRA1, and on the two alternative isoforms - "
        "especially Q86SQ6-1, whose ~800-residue Ser/Thr-rich N-terminal extension "
        "gives the receptor an ectodomain the canonical isoform lacks - would show "
        "whether agonist-independent Galpha13 activation is a property of the "
        "protein or of the short isoform.",
    ),
    (
        'The agonist-independent G-protein activation reported for ADGRA1 is genuine constitutive activity rather than a consequence of receptor overexpression.',
        "Test whether coupling is truly constitutive rather than an overexpression "
        "artefact. Titrate receptor density against BRET2 response alongside a "
        "known constitutively active GPCR and a known ligand-gated one, and repeat "
        "in neurons at near-endogenous expression using a knock-in tag, since the "
        "current result comes from HEK293T overexpression scored against empty "
        "vector.",
    ),
    (
        'The C-terminal PDZ-binding motif has a function in inhibitory synaptic physiology even though it is dispensable for synaptic localisation.',
        "Give the PDZ motif a phenotype. Deleting it changes neither synaptic "
        "localisation nor Galpha13 co-localisation, so the informative experiment is "
        "a knock-in ETTV-to-ETTA mouse assayed for the published PV-interneuron "
        "readouts - intrinsic excitability and inhibitory synaptic strength onto "
        "dentate gyrus granule cells - rather than another localisation assay.",
    ),
    (
        'Only a subset of the PDZ-domain proteins that bind the ADGRA1 peptide in vitro engage the full-length receptor in parvalbumin interneurons.',
        "Identify which PDZ partners are engaged in vivo. Holdup measures affinity "
        "between isolated domains and a peptide; a proximity-labelling or "
        "co-immunoprecipitation experiment from parvalbumin interneurons would show "
        "which of DLG1-4, MAGI1/2, SCRIB, SNX27 and MAST2 the full-length receptor "
        "actually meets. SNX27 and MAST2 are worth including despite being absent "
        "from GOA, since they are the tightest binders measured.",
    ),
    (
        'Endogenous ADGRA1 can be localised directly, testing whether the tagged-overexpression and fractionation results reflect where the native protein is.',
        "Raise an antibody that detects endogenous ADGRA1. The 2026 study states it "
        "could not determine endogenous localisation for lack of one, so every "
        "localisation result for this protein rests either on tagged overexpression "
        "or on mass spectrometry of fractionated brain.",
    ),
]

if __name__ == "__main__":
    sys.exit(main())
