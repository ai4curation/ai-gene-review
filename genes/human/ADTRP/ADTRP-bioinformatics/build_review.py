#!/usr/bin/env python3
"""Build ``ADTRP-ai-review.yaml`` from the seeded GOA stub.

Why a builder rather than hand-editing:

* The stub **under-seeds**. ``GOAValidator.seed_missing_annotations`` keys entries on
  ``(GO id, evidence, reference, negated, qualifier)`` and omits WITH/FROM, so the two
  ``GO:0005515`` rows -- which differ *only* in the interaction partner -- collapse into one.
  This builder rebuilds ``existing_annotations`` **from the GOA TSV**, one entry per distinct
  TSV line, and asserts the count matches.
* Emitting through ``yaml.SafeDumper`` with ``ignore_aliases`` forced True guarantees every row
  is an independent object. A shared Python object would emit an ``&id001`` anchor and N
  aliases, and every quote checker walks the *parsed* tree, so it would verify one quote N
  times and report N successes.
* Every quote is asserted to be a whitespace-normalised substring of its cited source
  **before** the file is written, so a mistyped quote is an error rather than a silent defect.

Run:  uv run python build_review.py
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO = GENE_DIR.parents[2]
GOA = GENE_DIR / "ADTRP-goa.tsv"
OUT = GENE_DIR / "ADTRP-ai-review.yaml"

P_HYD = "PMID:27018888"
P_TFPI = "PMID:21868574"
P_CAD = "PMID:28341552"
P_HURI = "PMID:32296183"
P_MOUSE = "PMID:32152231"
P_POU = "PMID:32445923"
AFFINAGE = "file:human/ADTRP/ADTRP-deep-research-affinage.md"
RESULTS = "file:human/ADTRP/ADTRP-bioinformatics/RESULTS.md"


def norm(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip().lower()


def source_text(ref: str) -> str | None:
    if ref.startswith("PMID:"):
        p = REPO / "publications" / f"PMID_{ref.split(':', 1)[1]}.md"
    elif ref.startswith("file:"):
        rel = ref.split(":", 1)[1]
        p = REPO / "genes" / rel
        if not p.exists():
            p = REPO / rel
    else:
        return None
    return p.read_text() if p.exists() else ""


def q(ref: str, text: str) -> dict:
    """A supporting_text entry, verified verbatim at build time."""
    src = source_text(ref)
    if src is not None:
        assert norm(text) in norm(src), f"QUOTE NOT IN {ref}:\n  {text}"
    return {"reference_id": ref, "supporting_text": text}


# --------------------------------------------------------------------------- prose

FAHFA_MECHANISM = (
    "ADTRP is a six-pass integral membrane threonine hydrolase that cleaves the ester bond of "
    "fatty acid esters of hydroxy fatty acids (FAHFAs). Catalysis requires Thr47 and His131, "
    "both of which UniProt records as SITE features with experimental evidence from "
    "PubMed:27018888 and both of which lie inside predicted transmembrane helices."
)

# The MF and BP calls sit at one PANTHER node; the reason prose is shared but every
# action-specific clause is attached only to the row whose action it describes, so a later
# recalibration of one row cannot strand a sentence on the other.
NODE_FACTS = (
    "The IBD node PANTHER:PTN001659973 is scoped by PAINT to taxon:2759 (Eukaryota) and seeded "
    "by exactly two proteins, human ADTRP (Q96IZ2, the target itself) and human AIG1 (Q9NVV5). "
    "It reaches 86 gene products: 40 Vertebrata, 25 invertebrate Metazoa, 14 Fungi, "
    "5 Viridiplantae and 2 other Eukaryota. Only 7 of the 86 are Swiss-Prot reviewed, and two "
    "of those are uncharacterised UPF0641 fungal proteins (P38842 YHR140W, Q96WV4 "
    "SPBPJ4664.05). The character that is conserved across the node is the catalytic dyad: "
    "aligning all 85 other recipients to ADTRP and requiring the aligned column to land on "
    "ADTRP's own annotated SITE positions, 73 of 85 retain Thr47/His131, including 39/39 "
    "vertebrates and both Dictyostelium members (positive control: AIG1 scores dyad-intact at "
    "36.5% identity). All 14 fungal recipients fall below 25% identity, so their dyad status is "
    "undetermined rather than negative."
)


def check_quote_relevance(
    row_label: str, quotes: list[dict], keywords: list[str], forbidden: list[str] | None = None
) -> None:
    """Assert at least one of the row's quotes actually mentions the row's subject.

    The reference validator only checks that a ``supporting_text`` is a substring of the cited
    source. It cannot tell whether the quote is *about* the thing the row asserts, which is how
    one gene shipped nine verbatim quotes that discussed a different subject. So every row
    declares the keyword(s) that identify its subject, and at least one quote must contain one.

    On a MODIFY row the subject is the **proposed replacement** term, not the term being moved
    away from -- the quote has to support where the annotation is going.
    """
    if not quotes:
        return
    blob = norm(" || ".join(x["supporting_text"] for x in quotes))
    assert any(norm(k) in blob for k in keywords), (
        f"QUOTE RELEVANCE: no quote on {row_label} mentions any of {keywords}"
    )
    for bad in forbidden or []:
        assert norm(bad) not in blob, (
            f"QUOTE RELEVANCE: quote on {row_label} rests on the wrong subject {bad!r}"
        )


def annotation(term_id, label, evidence, ref, qualifier, action, summary, reason, **kw) -> dict:
    review = {"summary": summary, "action": action, "reason": reason}
    # Default subject keyword is the gene symbol; rows whose evidence is a computed table row
    # or a term-specific claim declare their own.
    keywords = kw.pop("subject_keywords", ["adtrp"])
    forbidden = kw.pop("forbidden_keywords", None)
    for k in ("supported_by", "proposed_replacement_terms", "propagation_review", "additional_reference_ids"):
        if k in kw:
            review[k] = kw.pop(k)
    check_quote_relevance(
        f"{term_id} {evidence} {ref} (action={action})",
        review.get("supported_by", []),
        keywords,
        forbidden,
    )
    row = {
        "term": {"id": term_id, "label": label},
        "evidence_type": evidence,
        "original_reference_id": ref,
    }
    if qualifier:
        row["qualifier"] = qualifier
    if "supporting_entities" in kw:
        row["supporting_entities"] = kw.pop("supporting_entities")
    if "extensions" in kw:
        row["extensions"] = kw.pop("extensions")
    assert not kw, f"unused kwargs {kw}"
    row["review"] = review
    return row


def build_annotations() -> list[dict]:
    A: list[dict] = []

    # ---------------------------------------------------------------- IBA rows
    A.append(
        annotation(
            "GO:0016787",
            "hydrolase activity",
            "IBA",
            "GO_REF:0000033",
            "enables",
            "KEEP_AS_NON_CORE",
            "Correct but maximally general: the root of the hydrolase branch, propagated from a "
            "pan-eukaryotic node whose only characterised members are ADTRP and AIG1. True of "
            "this gene, but subsumed by the experimentally grounded GO:0120573.",
            NODE_FACTS
            + " GO:0016787 is a verified is_a ancestor of GO:0120573 FAHFA hydrolase activity, "
            "which this gene already holds by IMP (mutagenesis of both catalytic residues) and "
            "by IEA from 11 RHEA reactions, so the IBA adds no information about ADTRP. It is "
            "kept rather than removed because at the node the general term is correctly scoped "
            "to the evidence: what is conserved family-wide is the Thr/His catalytic dyad, and a "
            "conserved dyad licenses a claim about catalytic MECHANISM but not about SUBSTRATE. "
            "GO:0016787 states mechanism only, so it is exactly what the residue conservation "
            "supports; the substrate is known only for the four characterised animal members. "
            "PAINT placed this term on 2026-05-28, ten weeks after GO:0120573 was created "
            "(2026-03-14), so the general term is a deliberate judgement and not a stale-term "
            "artefact. The action is KEEP_AS_NON_CORE rather than ACCEPT only because it should "
            "not be counted as this gene's core molecular function.",
            supporting_entities=[
                "PANTHER:PTN001659973",
                "UniProtKB:Q96IZ2",
                "UniProtKB:Q9NVV5",
            ],
            supported_by=[
                q(RESULTS, "| `PTN001659973` | taxon:2759 Eukaryota | GO:0016787, GO:0042758 | 86 |"),
                q(
                    P_HYD,
                    "We have discovered herein using ABPP that the poorly characterized multipass "
                    "transmembrane proteins AIG1 and ADTRP represent a new family of hydrolytic "
                    "enzymes that degrade the FAHFA class of signaling lipids.",
                ),
            ],
            propagation_review={
                "root_cause": "NO_FAILURE_NON_CORE",
                "failure_modes": [],
                "source_entities": [
                    {
                        "source_id": "PANTHER:PTN001659973",
                        "source_label": "PANTHER IBD node, taxon:2759 Eukaryota, 86 recipients",
                        "source_status": "SUPPORTS_TRANSFER",
                        "comment": "The conserved character across the node is the Thr/His "
                        "catalytic dyad (73/85 recipients), which supports a mechanism-level term "
                        "such as this one but not a substrate-level one.",
                    },
                    {
                        "source_id": "UniProtKB:Q96IZ2",
                        "source_label": "human ADTRP (the target itself)",
                        "source_status": "SUPPORTS_TRANSFER",
                        "comment": "Self-referential IBD seed: a PAINT curator judged the "
                        "hydrolase function to be a family-level character. Not circular.",
                    },
                    {
                        "source_id": "UniProtKB:Q9NVV5",
                        "source_label": "human AIG1, reviewed (Swiss-Prot), catalytic Thr43/His134",
                        "source_status": "SUPPORTS_TRANSFER",
                        "comment": "Genuine co-seed characterised in the same paper; carries its "
                        "own IMP to GO:0120573 and GO:0042758.",
                    },
                ],
            },
        )
    )

    A.append(
        annotation(
            "GO:0005901",
            "caveola",
            "IBA",
            "GO_REF:0000033",
            "is_active_in",
            "KEEP_AS_NON_CORE",
            "Propagated from a node whose reach is exactly the vertebrate ADTRP orthologue set "
            "and whose sole seed is this gene's own IDA. Taxon-consistent and not over-reaching, "
            "but the relation was upgraded from located_in to is_active_in without any assay "
            "placing the FAHFA hydrolase activity in caveolae.",
            "PANTHER:PTN002591065 is scoped taxon:117571 (Euteleostomi), seeded by "
            "UniProtKB:Q96IZ2 alone, and reaches 25 gene products which resolve to ADTRP "
            "orthologues in 25 vertebrate species and nothing else; the paralog AIG1 is "
            "correctly excluded. Caveolae are a vertebrate structure requiring caveolins, so the "
            "node's taxon scope and the term agree - this is the benign answer to the reciprocal "
            "'which node's reach is exactly my gene set' question. The reservation is the "
            "relation, not the compartment: the seeding evidence is a located_in IDA "
            "(colocalisation with TFPI and caveolin-1 in endothelial lipid rafts), whereas the "
            "IBA asserts is_active_in, i.e. that the molecular function executes there. ADTRP's "
            "catalytic activity was measured in bulk membrane lysates of transfected HEK293T "
            "cells, which carry no caveola-specific information, and the caveola observation "
            "comes from a TFPI-regulation study that did not assay hydrolase activity. Kept as "
            "non-core: the location is real and experimentally supported, but caveolar residence "
            "is a property of the endothelial TFPI role rather than a demonstrated requirement "
            "of FAHFA hydrolysis.",
            supporting_entities=["PANTHER:PTN002591065", "UniProtKB:Q96IZ2"],
            supported_by=[
                q(RESULTS, "| `PTN002591065` | taxon:117571 Euteleostomi | GO:0005901 | 25 | Vertebrata 25 | 3 |"),
                q(P_TFPI, "Imaging and Triton X-114-extraction confirm TFPI and ADTRP association with lipid rafts/caveolae."),
            ],
            subject_keywords=["caveola"],
            propagation_review={
                "root_cause": "NO_FAILURE_NON_CORE",
                "failure_modes": [],
                "source_entities": [
                    {
                        "source_id": "PANTHER:PTN002591065",
                        "source_label": "PANTHER IBD node, taxon:117571 Euteleostomi, 25 recipients, all ADTRP orthologues",
                        "source_status": "SUPPORTS_TRANSFER",
                        "comment": "Node reach matches the term's taxon requirement exactly; no "
                        "invertebrate or fungal recipient receives a caveola annotation.",
                    },
                    {
                        "source_id": "UniProtKB:Q96IZ2",
                        "source_label": "human ADTRP (the target itself)",
                        "source_status": "SUPPORTS_TRANSFER",
                        "comment": "Self-referential IBD seed backed by this gene's own IDA from "
                        "PMID:21868574. The seed's evidence is located_in; the propagation "
                        "states is_active_in.",
                    },
                ],
            },
        )
    )

    A.append(
        annotation(
            "GO:0042758",
            "long-chain fatty acid catabolic process",
            "IBA",
            "GO_REF:0000033",
            "involved_in",
            "ACCEPT",
            "True for human ADTRP, which holds the identical term by IMP from the same "
            "characterisation paper. Flagged upstream: the node placing it spans Eukaryota, so "
            "84 of its 86 recipients receive a specific lipid-catabolism claim with no "
            "supporting data.",
            "For this gene the term is right, and the substrate chemistry was checked rather "
            "than assumed: ChEBI classifies the substrate 9-PAHSA(1-) (CHEBI:83670) as a "
            "long-chain fatty acid anion, so hydrolysing a FAHFA is literally the breakdown of a "
            "long-chain fatty acid, and UniProt gives PhysiologicalDirection=left-to-right for "
            "all 12 catalytic-activity lines, i.e. the annotated direction is removal, not "
            "addition. The upstream concern does not change this gene's verdict but is recorded "
            "in suggested_questions: the same node that carries this four-step-deep biological "
            "process declines to give anything more specific than GO:0016787 for the molecular "
            "function. "
            + NODE_FACTS
            + " The asymmetry is a category distinction, not a curation lapse: the conserved "
            "dyad licenses the mechanism-level MF the node carries, whereas this BP asserts a "
            "SUBSTRATE, and the substrate is established only for the four characterised animal "
            "members. So the node propagates a substrate claim on evidence that can only support "
            "a mechanism claim. Note this corrects a first-pass reading of mine, which had argued "
            "from clade heterogeneity instead; measurement showed the dyad is broadly conserved, "
            "so heterogeneity is the wrong basis for the objection.",
            supporting_entities=[
                "PANTHER:PTN001659973",
                "UniProtKB:Q96IZ2",
                "UniProtKB:Q9NVV5",
            ],
            supported_by=[
                q(RESULTS, "| `CHEBI:83670` | 9-PAHSA(1-) | yes |"),
                q(
                    P_HYD,
                    "In contrast, both AIG1 and ADTRP-transfected cell membrane lysates robustly "
                    "hydrolyzed several fatty-acid esters of hydroxy-fatty acids (FAHFAs)",
                ),
            ],
            propagation_review={
                "root_cause": "NO_FAILURE_CORE",
                "failure_modes": [],
                "source_entities": [
                    {
                        "source_id": "PANTHER:PTN001659973",
                        "source_label": "PANTHER IBD node, taxon:2759 Eukaryota, 86 recipients",
                        "source_status": "SUPPORTS_TRANSFER",
                        "comment": "Supports the transfer to ADTRP, which has its own IMP, but "
                        "the node's taxon scope carries a substrate-level claim to 46 "
                        "non-vertebrate recipients whose substrate has never been determined; "
                        "their catalytic dyad is largely conserved, which supports mechanism but "
                        "not substrate.",
                    },
                    {
                        "source_id": "UniProtKB:Q96IZ2",
                        "source_label": "human ADTRP (the target itself)",
                        "source_status": "SUPPORTS_TRANSFER",
                        "comment": "Self-referential IBD seed; the target independently holds "
                        "this term by IMP from PMID:27018888.",
                    },
                    {
                        "source_id": "UniProtKB:Q9NVV5",
                        "source_label": "human AIG1, reviewed (Swiss-Prot)",
                        "source_status": "SUPPORTS_TRANSFER",
                        "comment": "Carries its own IMP to GO:0042758 from the same paper.",
                    },
                ],
            },
        )
    )

    # ---------------------------------------------------------------- automatic routes
    A.append(
        annotation(
            "GO:0005886",
            "plasma membrane",
            "IEA",
            "GO_REF:0000044",
            "located_in",
            "ACCEPT",
            "Swiss-Prot subcellular-location mapping of SL-0039 (Cell membrane), which UniProt "
            "asserts with experimental evidence. Consistent with the caveola and cell-surface "
            "IDAs from PMID:21868574.",
            "UniProt's SUBCELLULAR LOCATION line reads 'Cell membrane ... Multi-pass membrane "
            "protein', and the feature table gives six TRANSMEM helices with alternating "
            "cytoplasmic and extracellular topological domains, so a plasma-membrane call is "
            "well founded for this protein. The mapping route names its source explicitly "
            "(UniProtKB-SubCell:SL-0039) and is not an unattributed bulk import.",
            supporting_entities=["UniProtKB-SubCell:SL-0039"],
            supported_by=[
                q(P_TFPI, "Imaging and Triton X-114-extraction confirm TFPI and ADTRP association with lipid rafts/caveolae.")
            ],
        )
    )

    A.append(
        annotation(
            "GO:0016020",
            "membrane",
            "IEA",
            "GO_REF:0000002",
            "located_in",
            "ACCEPT",
            "InterPro2GO from IPR006838. The signature is family-specific (ADTRP/AIG1), not a "
            "bare fold, and it maps only to a cellular component - the predicted "
            "fold-to-activity error is absent here.",
            "IPR006838 'ADTRP/AIG1' covers 5788 proteins of which 8 are reviewed (Swiss-Prot): "
            "four ADTRP orthologues, two AIG1 orthologues and two uncharacterised UPF0641 fungal "
            "proteins. interpro2go maps the entry to GO:0016020 membrane and to nothing else - "
            "no molecular function, despite the family now being a characterised hydrolase "
            "family. That is the correct restraint: a quarter of its own reviewed members are "
            "curated as uncharacterised, and the entry spans thousands of unstudied proteins. "
            "The location claim it does make is independently confirmed by an IDA from "
            "PMID:27018888.",
            supporting_entities=["InterPro:IPR006838"],
            supported_by=[
                q(RESULTS, "interpro2go maps it to GO:0016020")
            ],
            subject_keywords=["interpro2go"],
        )
    )

    A.append(
        annotation(
            "GO:0120573",
            "FAHFA hydrolase activity",
            "IEA",
            "GO_REF:0000116",
            "enables",
            "ACCEPT",
            "Rhea mapping from the 11 FAHFA hydrolysis reactions UniProt curates for this "
            "protein with experimental evidence. This is the gene's core molecular function, "
            "anchored to explicit reaction identifiers.",
            "The term is RHEA-anchored on both sides: GO:0120573 carries 12 RHEA "
            "cross-references and this annotation's WITH/FROM lists 11 of them "
            "(RHEA:52048/52052/52056/52060/52064/52068/52072/52076/52080/52084/52096), each "
            "curated in UniProt as ECO:0000269|PubMed:27018888 with "
            "PhysiologicalDirection=left-to-right. The direction and the substrate identity are "
            "therefore both explicit and both correct: the enzyme removes an acyl group by "
            "hydrolysis rather than forming one. GO:0120573 is current (not obsolete, no "
            "secondary ids) and was created 2026-03-14.",
            supporting_entities=[
                "RHEA:52048", "RHEA:52052", "RHEA:52056", "RHEA:52060", "RHEA:52064",
                "RHEA:52068", "RHEA:52072", "RHEA:52076", "RHEA:52080", "RHEA:52084",
                "RHEA:52096",
            ],
            supported_by=[
                q(
                    P_HYD,
                    "Both AIG1 and ADTRP hydrolyze bioactive fatty acid esters of hydroxy fatty "
                    "acids (FAHFAs) but not other major classes of lipids.",
                )
            ],
        )
    )

    # ---------------------------------------------------------------- IPI rows (per partner)
    huri_reason = (
        "Both GO:0005515 rows come from the single HuRI binary interactome screen. IntAct "
        "returns 10 interactions for Q96IZ2; the two HuRI partners are each logged three times, "
        "as 'two hybrid array', 'two hybrid prey pooling approach' and 'validated two hybrid' - "
        "three sub-methods of one experiment, which is what UniProt's NbExp=3 is counting. All "
        "are yeast two-hybrid in Saccharomyces cerevisiae with an MI-score of 0.56, and there is "
        "no orthogonal assay and no follow-up anywhere in the ADTRP literature. ADTRP is a "
        "six-pass integral membrane protein whose extracellular and cytoplasmic loops are 13-22 "
        "residues long, which makes it a poor Y2H substrate. The partner accession itself is "
        "sound - it resolves to the reviewed canonical Swiss-Prot entry with matching length, so "
        "this is not an ORFeome-clone substitution - but a single unreplicated screen hit is not "
        "an informative molecular function. Marked over-annotated rather than removed: nothing "
        "refutes the interaction, it is simply unsupported beyond one screen."
    )
    for acc, sym, extra in (
        ("Q6PL24", "TMED8", "Q6PL24 is reviewed TMED8_HUMAN, 325 aa, matching the canonical entry."),
        ("Q96FZ5", "CMTM7", "Q96FZ5 is reviewed CKLF7_HUMAN, 175 aa, matching the canonical entry; it is itself a MARVEL-domain membrane protein."),
    ):
        A.append(
            annotation(
                "GO:0005515",
                "protein binding",
                "IPI",
                P_HURI,
                "enables",
                "MARK_AS_OVER_ANNOTATED",
                f"Uninformative bare protein-binding row for {sym} ({acc}), resting on one "
                f"yeast two-hybrid screen logged as three sub-methods.",
                huri_reason + " " + extra,
                supporting_entities=[f"UniProtKB:{acc}"],
                supported_by=[
                    q(
                        RESULTS,
                        f"| {sym} | two hybrid array, two hybrid prey pooling approach, "
                        f"validated two hybrid | 3 | 1 |",
                    )
                ],
                subject_keywords=[sym.lower()],
            )
        )

    # ---------------------------------------------------------------- experimental MF/BP
    A.append(
        annotation(
            "GO:0120573",
            "FAHFA hydrolase activity",
            "IMP",
            P_HYD,
            "enables",
            "ACCEPT",
            "The gene's core molecular function, established by loss-of-activity mutagenesis of "
            "both catalytic residues against a panel of non-FAHFA lipid controls.",
            FAHFA_MECHANISM
            + " The evidence is specific in both directions: transfected membrane lysates "
            "hydrolysed FAHFAs but showed negligible activity against (lyso)-phospholipids and "
            "mono-, di- and tri-glycerides, and both T47A and H131A abolished FAHFA hydrolysis. "
            "The term matches the measured reaction exactly and is anchored to RHEA, so no "
            "granularity question arises. IMP is the right code: the assignment rests on the "
            "mutant phenotype.",
            supported_by=[
                q(
                    P_HYD,
                    "The FAHFA hydrolase activities of AIG1 and ADTRP were abolished by mutating "
                    "their putative catalytic nucleophilic residues Thr-43 and Thr-47, respectively",
                ),
                q(
                    P_HYD,
                    "We also tested the H134A mutant of AIG1 and H131A mutant of ADTRP and found "
                    "that these proteins showed no detectable FAHFA hydrolase activity above a "
                    "mock-transfected control",
                ),
                q(
                    P_HYD,
                    "The membrane lysates of hAIG1- and hADTRP-transfected HEK293T cells showed "
                    "negligible hydrolytic activity above a mock-transfected control proteome "
                    "with the majority of tested lipid substrates, including common classes of "
                    "(lyso)-phospholipids and neutral lipids",
                ),
                q(
                    P_HYD,
                    "AIG1 and ADTRP displayed a preference for FAHFAs with branching distal from "
                    "the carboxylate head group of the lipids",
                ),
            ],
        )
    )

    A.append(
        annotation(
            "GO:0051897",
            "positive regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction",
            "IMP",
            P_CAD,
            "involved_in",
            "KEEP_AS_NON_CORE",
            "Downstream transcriptional consequence of ADTRP knockdown in endothelial cells, not "
            "a direct signalling activity of the protein.",
            "The mechanism reported is that ADTRP raises PIK3R3 transcript levels, which then "
            "activates AKT. ADTRP is a membrane lipid hydrolase with no kinase, adaptor or "
            "scaffold module, so its effect on PI3K/AKT is indirect and mediated by gene "
            "expression. involved_in is defensible for an siRNA phenotype and the IMP code is "
            "correct, but this is a pathway consequence rather than a core function. Note the "
            "cached record for this reference is abstract-only, so nothing here is asserted "
            "beyond what the abstract states.",
            supported_by=[
                q(
                    P_CAD,
                    "ADTRP positively regulates expression of PIK3R3 encoding the regulatory "
                    "subunit 3 of PI3K, which leads to activation of AKT, resulting in "
                    "up-regulation of MIA3/TANGO1.",
                )
            ],
        )
    )

    for ref in (P_TFPI, P_HYD):
        if ref == P_TFPI:
            summ = (
                "Plasma-membrane localisation supported by this paper's imaging and "
                "detergent-partitioning of ADTRP in endothelial lipid rafts."
            )
            reason = (
                "The abstract reports imaging plus Triton X-114 extraction placing ADTRP with "
                "TFPI in lipid rafts/caveolae of endothelial cells, and caveola is a verified "
                "descendant of plasma membrane, so the compartment is properly supported by this "
                "reference."
            )
            sup = [q(P_TFPI, "We confirm ADTRP expression and colocalization with TFPI and caveolin-1 in ECs.")]
        else:
            summ = (
                "Plasma-membrane localisation is correct for ADTRP and stands on PMID:21868574 "
                "and the SL-0039 mapping, so the term is accepted. Recorded caveat: this "
                "particular reference contains no localisation experiment and supports only "
                "GO:0016020 membrane, for which the same paper is separately cited - a UniProt "
                "evidence-attribution question, not a GO error."
            )
            reason = (
                "Accepted on the term, with a reference-attribution caveat rather than a GO "
                "action, because the plasma-membrane call stands independently on PMID:21868574 "
                "and on the SL-0039 mapping. The caveat: the cached full text of PMID:27018888 "
                "(full_text_available: true) contains no localisation experiment at all - zero "
                "occurrences of 'plasma membrane', 'cell surface', 'immunofluorescence', "
                "'confocal', 'localization' - against positive controls in the same file of "
                "'membrane lysates' 9, 'membrane fraction' 3, 'transmembrane' 29, 'HEK293T' 36 "
                "and 'FAHFA' 67, so the scan is working. What that paper shows is recovery of "
                "recombinant ADTRP in the membrane fraction of transfected HEK293T cells plus "
                "six topology predictors placing the catalytic residues in transmembrane "
                "helices; it supports 'membrane', not 'plasma membrane'. This row appears to "
                "descend from UniProt's SUBCELLULAR LOCATION line, which cites both PubMed:21868574 "
                "and PubMed:27018888 for 'Cell membrane'; GOA then split that into two EXP rows. "
                "Reported as a UniProt evidence-attribution question in suggested_questions. "
                "Supplementary figures are not in the cache, so the scan is scoped to the cached "
                "full text."
            )
            sup = [
                q(RESULTS, "no plasma-membrane or cell-surface localisation experiment in the cached full text"),
                q(
                    P_HYD,
                    "we next analyzed the protein sequences for both AIG1 and ADTRP using six "
                    "different transmembrane topology prediction programs (CCTOP, Phobius, PSORT "
                    "II, TMHMM, TMpred, and Uniprot) and found that these programs consistently "
                    "predicted that both the conserved Thr and His residues of AIG1 and ADTRP "
                    "were located within transmembrane domains of these proteins",
                ),
            ]
        A.append(
            annotation(
                "GO:0005886", "plasma membrane", "EXP", ref, "located_in", "ACCEPT", summ, reason,
                supported_by=sup,
            )
        )

    cad_common = (
        "One of nine biological-process rows curated by BHF-UCL from a single siRNA-knockdown "
        "study of ADTRP in endothelial cells. The cached record is abstract-only, so this review "
        "does not assert anything about the paper's figures. "
    )
    for term_id, label, summ, extra in (
        (
            "GO:0002042",
            "cell migration involved in sprouting angiogenesis",
            "Endothelial migration phenotype of ADTRP knockdown. Kept as non-core; note the "
            "abstract reports EC migration without using the words sprouting or angiogenesis.",
            "The abstract states that ADTRP knockdown 'inhibited EC proliferation and "
            "migration'. It does not mention sprouting or angiogenesis, and the full text is not "
            "cached, so the specific sprouting-angiogenesis context cannot be verified here; the "
            "BHF-UCL curator read the full text and the term is left in place. Either way this "
            "is a downstream cellular phenotype, not a core function of a lipid hydrolase.",
        ),
        (
            "GO:0002686",
            "negative regulation of leukocyte migration",
            "Monocyte transendothelial migration increases on ADTRP knockdown. Correct at the "
            "leukocyte level and the appropriate granularity for the data.",
            "Monocytes are leukocytes, so this term is satisfied by the reported phenotype and "
            "sits at a level the data supports. It is also the verified common ancestor covering "
            "the cell-type problem flagged on the GO:2000402 row below.",
        ),
        (
            "GO:0003332",
            "negative regulation of extracellular matrix constituent secretion",
            "ADTRP lowers collagen VII levels in endothelial and HepG2 cells. Indirect, via the "
            "MIA3/TANGO1 collagen-export pathway.",
            "Collagen VII is an extracellular matrix constituent and MIA3/TANGO1 is a collagen "
            "export factor, so the term matches the reported effect. The effect runs through "
            "ADTRP's regulation of MIA3/TANGO1 expression rather than any direct role in "
            "secretion.",
        ),
        (
            "GO:0050709",
            "negative regulation of protein secretion",
            "ADTRP lowers ApoB levels in endothelial and HepG2 cells; indirect, through the same "
            "MIA3/TANGO1 axis.",
            "Same evidence and same indirection as the extracellular-matrix row: ApoB is a "
            "secreted protein and MIA3/TANGO1 is the mediator. A regulatory consequence, not a "
            "core function.",
        ),
        (
            "GO:0140052",
            "cellular response to oxidised low-density lipoprotein particle stimulus",
            "The monocyte-adhesion phenotype was measured under oxidised-LDL stimulation.",
            "The abstract describes 'oxidized-LDL-mediated monocyte adhesion to ECs' being "
            "promoted by ADTRP knockdown, which places ADTRP within the cellular response to "
            "oxLDL. This is a context of the assay rather than a demonstrated ADTRP-dependent "
            "oxLDL-sensing step, so it is retained as non-core.",
        ),
        (
            "GO:1903038",
            "negative regulation of leukocyte cell-cell adhesion",
            "Monocyte adhesion to endothelial cells increases on ADTRP knockdown.",
            "Directly supported by the reported adhesion phenotype, and monocytes are leukocytes "
            "so the cell-type term is right here. Downstream of the PIK3R3/AKT/MIA3 axis rather "
            "than of hydrolase activity.",
        ),
    ):
        A.append(
            annotation(
                term_id, label, "IMP", P_CAD, "involved_in", "KEEP_AS_NON_CORE", summ,
                cad_common + extra,
                supported_by=[
                    q(
                        P_CAD,
                        "Knockdown of ADTRP expression by siRNA promoted oxidized-LDL-mediated "
                        "monocyte adhesion to ECs and transendothelial migration of monocytes, "
                        "inhibited EC proliferation and migration, and increased apoptosis",
                    )
                ],
            )
        )

    A.append(
        annotation(
            "GO:2000402",
            "negative regulation of lymphocyte migration",
            "IMP",
            P_CAD,
            "involved_in",
            "MODIFY",
            "Wrong leukocyte lineage, not merely imprecise. Every migration experiment described "
            "in the abstract used monocytes; lymphocyte and monocyte terms are disjoint siblings "
            "under negative regulation of leukocyte migration.",
            cad_common
            + "Cell-type words in the cached abstract: 'monocyte' 4, 'lymphocyte' 0, "
            "'leukocyte' 0. The phenotype is 'transendothelial migration of monocytes'. Both "
            "ancestor closures were fetched before calling this a granularity problem, and "
            "neither term contains the other: GO:2000402 (lymphocyte) is not an ancestor of "
            "GO:2000438 (monocyte extravasation) and GO:2000438 is not an ancestor of "
            "GO:2000402. Monocytes are myeloid mononuclear phagocytes and lymphocytes are "
            "lymphoid, so the annotated term names a different cell lineage from the one "
            "assayed - it is wrong rather than general. The proposed replacement GO:2000438 "
            "negative regulation of monocyte extravasation matches 'transendothelial migration "
            "of monocytes' precisely. If the uncached full text does contain a lymphocyte "
            "migration assay, the correct resolution is GO:0071676 negative regulation of "
            "mononuclear cell migration, a verified ancestor of both terms that would assert "
            "strictly less than either. Nothing is lost by the change in any case: the "
            "leukocyte-level claim is separately annotated from this same paper as GO:0002686.",
            proposed_replacement_terms=[
                {"id": "GO:2000438", "label": "negative regulation of monocyte extravasation"}
            ],
            supported_by=[
                q(
                    P_CAD,
                    "Knockdown of ADTRP expression by siRNA promoted oxidized-LDL-mediated "
                    "monocyte adhesion to ECs and transendothelial migration of monocytes, "
                    "inhibited EC proliferation and migration, and increased apoptosis",
                ),
                q(RESULTS, "**Neither closure contains the other**"),
            ],
            # On a MODIFY row the subject is the PROPOSED REPLACEMENT (monocyte extravasation),
            # not the term being moved away from. A quote about lymphocytes would support the
            # existing term, i.e. argue against this row's own action.
            subject_keywords=["monocyte"],
            forbidden_keywords=["lymphocyte"],
        )
    )

    A.append(
        annotation(
            "GO:0010628",
            "positive regulation of gene expression",
            "IMP",
            P_CAD,
            "involved_in",
            "KEEP_AS_NON_CORE",
            "ADTRP knockdown lowers PIK3R3 and MIA3/TANGO1 transcript levels. A real but very "
            "general and wholly indirect regulatory effect.",
            cad_common
            + "The term is the most general positive-regulation-of-expression node in GO and "
            "records nothing about which genes or by what mechanism. It is retained because the "
            "phenotype is real, but a membrane lipid hydrolase has no direct transcriptional "
            "activity and GO offers no target-specific child, so this cannot be a core function.",
            supported_by=[
                q(P_CAD, "We showed that knockdown of ADTRP expression markedly down-regulated expression of MIA3/TANGO1.")
            ],
        )
    )

    A.append(
        annotation(
            "GO:0016020", "membrane", "IDA", P_HYD, "located_in", "ACCEPT",
            "Recombinant ADTRP partitions into the membrane fraction, consistent with six "
            "predicted transmembrane helices. This is the compartment claim this paper actually "
            "supports.",
            "All ADTRP activity assays in this paper were run on membrane lysates of transfected "
            "HEK293T cells, and the protein's catalytic Thr47 and His131 are predicted by six "
            "independent topology programs to lie within transmembrane helices. GO:0016020 is "
            "the right granularity for that evidence; the more specific plasma-membrane claim "
            "rests on PMID:21868574 instead.",
            supported_by=[
                q(
                    P_HYD,
                    "we use activity-based profiling to discover that the poorly characterized "
                    "multipass transmembrane proteins AIG1 and ADTRP are atypical hydrolytic "
                    "enzymes that depend on conserved threonine and histidine residues for catalysis",
                )
            ],
        )
    )

    A.append(
        annotation(
            "GO:0042758", "long-chain fatty acid catabolic process", "IMP", P_HYD, "involved_in",
            "ACCEPT",
            "The biological-process expression of the gene's core activity. The substrate is "
            "itself a long-chain fatty acid by ChEBI, so the term names the right chemistry.",
            "9-PAHSA(1-) (CHEBI:83670) is classified in ChEBI as a long-chain fatty acid anion, "
            "and ADTRP cleaves it into palmitate and 9-hydroxystearate, so FAHFA hydrolysis is "
            "the breakdown of a long-chain fatty acid and the direction is degradative. The IMP "
            "rests on the catalytic-residue mutants. The term is nonetheless broader than the "
            "measured specificity - GO has no FAHFA-level biological process, only the "
            "molecular function GO:0120573 - which is filed under proposed_new_terms. For "
            "ADTRP specifically the in vivo demonstration is PMID:32152231, where Adtrp-knockout "
            "mouse tissues accumulate FAHFAs with unchanged levels of other lipid classes.",
            supported_by=[
                q(
                    P_MOUSE,
                    "Tissues from mice lacking ADTRP (Adtrp-KO), or both AIG1 and ADTRP (DKO) had "
                    "higher concentrations of FAHFAs particularly isomers with the ester bond at "
                    "the 9th carbon due to decreased FAHFA hydrolysis activity.",
                ),
                q(P_MOUSE, "The levels of other lipid classes were unaltered indicating that AIG1 and ADTRP specifically hydrolyze FAHFAs."),
            ],
        )
    )

    A.append(
        annotation(
            "GO:0005901", "caveola", "IDA", P_TFPI, "located_in", "KEEP_AS_NON_CORE",
            "Imaging plus Triton X-114 partitioning place ADTRP with TFPI and caveolin-1 in "
            "endothelial lipid rafts/caveolae. Solid evidence for a real location, kept as "
            "non-core because caveolar residence belongs to the endothelial TFPI role rather "
            "than to the catalytic function.",
            "Two independent methods in the same study support the compartment, and caveola is a "
            "verified descendant of plasma membrane so it is consistent with the other location "
            "rows. located_in is the right relation for a colocalisation result; see the "
            "GO:0005901 IBA row for why the is_active_in upgrade is treated more cautiously. "
            "Non-core rather than accepted-as-core so that this term matches the IBA row on the "
            "same term, and because the core_functions entry lists the plasma membrane and "
            "membrane as the locations of the FAHFA hydrolase activity: no assay has placed that "
            "activity in caveolae specifically, and the caveolar observation comes from a "
            "TFPI-regulation study in endothelial cells.",
            supported_by=[
                q(P_TFPI, "Imaging and Triton X-114-extraction confirm TFPI and ADTRP association with lipid rafts/caveolae."),
                q(P_TFPI, "We confirm ADTRP expression and colocalization with TFPI and caveolin-1 in ECs."),
            ],
        )
    )

    A.append(
        annotation(
            "GO:0009986", "cell surface", "IDA", P_TFPI, "located_in", "KEEP_AS_NON_CORE",
            "Retained on curator authority. Plausible for a polytopic plasma-membrane protein "
            "with three extracellular loops, though the cached abstract does not state it. "
            "Non-core: unlike GO:0016020, cell surface is not an ancestor of plasma membrane but "
            "an independent claim, and the catalytic residues sit inside the bilayer rather than "
            "on the external face.",
            "GO:0009986 sits in its own branch: closures were fetched and it is not a descendant "
            "of GO:0005886 plasma membrane or of GO:0016020 membrane, so it is a distinct claim "
            "rather than a coarser version of the other location rows. The cached record for "
            "this reference is abstract-only and the abstract does not use the phrase 'cell "
            "surface'; the study does measure cell-associated TFPI activity and FXa inhibition "
            "at the endothelial surface, and the UniProt curator worked from the full text. "
            "Retained with that limitation stated rather than marked undecided, because the "
            "topology makes an externally exposed surface pool unproblematic.",
            supported_by=[
                q(
                    P_TFPI,
                    "Dihydrotestosterone up-regulates TFPI and ADTRP expression, and increases FXa "
                    "inhibition by TFPI in an ADTRP- and caveolin-1-dependent manner.",
                )
            ],
        )
    )

    A.append(
        annotation(
            "GO:0010628", "positive regulation of gene expression", "IMP", P_TFPI, "involved_in",
            "KEEP_AS_NON_CORE",
            "ADTRP knockdown lowers and overexpression raises TFPI mRNA. Real, reproducible, and "
            "the origin of the gene's name - but an indirect effect and a very general term.",
            "This is the observation the gene was named for, and it is supported in both "
            "directions by shRNA and overexpression. It remains non-core for two reasons: the "
            "term says nothing about the target or the mechanism, and no direct transcriptional "
            "or promoter-binding activity of ADTRP has ever been shown. The mechanism was later "
            "resolved: the DNA-binding protein is the transcription factor POU1F1, which binds an "
            "ADTRP-response element 806 to 756 bp upstream of the TFPI start site, and deleting "
            "that site or knocking down POU1F1 abolishes ADTRP-mediated TFPI transcription. That "
            "places ADTRP upstream of a transcription factor rather than at the DNA, so an "
            "effect-on-expression process term is the correct aspect and no DNA-binding or "
            "transcription-factor molecular function should be inferred. 'Regulates the "
            "expression of TFPI' is a biological process, not a molecular function, and it is "
            "correctly annotated as one here.",
            supported_by=[
                q(P_TFPI, "ADTRP-shRNA reduces, while over-expression of ADTRP enhances, TFPI mRNA and activity and the colocalization of TF-FVIIa-FXa-TFPI with caveolin-1."),
                q(P_TFPI, "We demonstrate that this protein regulates both the native and androgen-enhanced TFPI expression and activity in cultured ECs, and we named it androgen-dependent TFPI-regulating protein (ADTRP)."),
                q(P_POU, "Deletion of POU1F1-binding site or knockdown of POU1F1 expression abolished ADTRP-mediated transcription of TFPI."),
                q(P_POU, "ChIP and EMSA demonstrated that POU1F1 binds to the ADTRP response element."),
                q(AFFINAGE, "ADTRP regulates TFPI transcription through transcription factor POU1F1"),
            ],
        )
    )

    A.append(
        annotation(
            "GO:0030195", "negative regulation of blood coagulation", "IMP", P_TFPI, "involved_in",
            "KEEP_AS_NON_CORE",
            "ADTRP raises TFPI-dependent FXa inhibition at the endothelial surface. An indirect, "
            "tissue-level consequence of regulating TFPI, not an activity of ADTRP.",
            "The anticoagulant readout is inhibition of factor Xa by TFPI, and the ADTRP "
            "dependence is on TFPI expression and its caveolar localisation. ADTRP is not itself "
            "a protease inhibitor or a coagulation factor, so this is a downstream physiological "
            "consequence. It is a genuine, experimentally supported process role and is retained, "
            "but it must not be read as evidence for any molecular function: the vascular and "
            "thrombosis associations of this locus, including its coronary-artery-disease GWAS "
            "signal, establish phenotype rather than activity.",
            supported_by=[
                q(P_TFPI, "the ADTRP-dependent up-regulation of TFPI expression and activity by androgen represents a novel mechanism of increasing the anticoagulant protection of the endothelium"),
            ],
        )
    )

    A.append(
        annotation(
            "GO:0071383", "cellular response to steroid hormone stimulus", "IEP", P_TFPI,
            "involved_in", "KEEP_AS_NON_CORE",
            "Dihydrotestosterone raises ADTRP expression. An expression-response annotation, "
            "correctly coded IEP.",
            "IEP is the right code for an expression-pattern inference and the term matches: "
            "dihydrotestosterone is a steroid hormone and ADTRP transcript rises in response. "
            "UniProt records the same fact as 'INDUCTION: By androgens'. This describes how the "
            "gene is regulated rather than what the protein does, so it is non-core by "
            "construction.",
            supported_by=[
                q(P_TFPI, "Dihydrotestosterone up-regulates TFPI and ADTRP expression, and increases FXa inhibition by TFPI in an ADTRP- and caveolin-1-dependent manner."),
            ],
        )
    )

    return A


def reconcile(annotations: list[dict]) -> None:
    """Assert one review entry per distinct GOA TSV line, keyed including WITH/FROM."""
    rows = list(csv.DictReader(GOA.open(), delimiter="\t"))
    keys = {
        (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], r["QUALIFIER"], r["WITH/FROM"])
        for r in rows
    }
    assert len(annotations) == len(keys), (
        f"row-count mismatch: {len(annotations)} review entries vs {len(keys)} distinct GOA rows"
    )
    got = {
        (a["term"]["id"], a["evidence_type"], a["original_reference_id"], a.get("qualifier", ""))
        for a in annotations
    }
    want = {(r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], r["QUALIFIER"]) for r in rows}
    assert got == want, f"key mismatch\n  only in review: {got - want}\n  only in GOA: {want - got}"
    assert all(a["review"]["action"] != "PENDING" for a in annotations), "PENDING left in review"


def _finalise_references(by_id: dict) -> list[dict]:
    """Emit the references list and assert its ids are unique.

    Kept as a separate function so the post-condition has a seam that can be exercised: a
    regression that rebuilds this list by appending (the original bug shape) is caught here.
    """
    refs = sorted(by_id.values(), key=lambda r: r["id"])
    ids = [r["id"] for r in refs]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    assert not dupes, f"duplicate reference ids in output: {dupes}"
    # Payload check, not just an id check. A de-duplication that rewrites the carrier will
    # silently drop whatever was attached to the duplicates: round 1 collapsed four
    # PMID:32152231 entries correctly and lost the reference_review blocks on two *other*
    # references, because the ids were all still right. Assert the payload survives.
    unreviewed = sorted(
        r["id"] for r in refs
        if not r.get("reference_review") and not r["id"].startswith("GO_REF:")
    )
    assert not unreviewed, (
        f"non-GO_REF references lacking reference_review (dedup payload loss?): {unreviewed}"
    )
    return refs


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # noqa: D102
        return True


def main() -> int:
    doc = yaml.safe_load(OUT.read_text())
    annotations = build_annotations()
    reconcile(annotations)

    doc["status"] = "COMPLETE"
    doc["description"] = (
        "ADTRP (androgen-dependent TFPI-regulating protein) is a six-pass integral membrane "
        "enzyme of the ADTRP/AIG1 family that hydrolyses fatty acid esters of hydroxy fatty "
        "acids (FAHFAs), a class of endogenous bioactive signalling lipids with "
        "anti-inflammatory and insulin-sensitising properties. It is an atypical hydrolase: it "
        "has no sequence or structural relationship to the classical serine-hydrolase folds, and "
        "instead uses a threonine nucleophile (Thr47) activated by a histidine general base "
        "(His131), both of which sit within transmembrane helices rather than in a soluble "
        "catalytic domain. Substitution of either residue abolishes FAHFA hydrolysis, and the "
        "enzyme is inactive against phospholipids, lysophospholipids and mono-, di- and "
        "triglycerides, preferring FAHFA isomers branched distal to the carboxylate head group. "
        "Together with its paralogue AIG1 it is one of the two principal FAHFA hydrolases in "
        "mammals; knockout mice accumulate FAHFAs, particularly the 9-position ester isomers, "
        "with other lipid classes unchanged. ADTRP is expressed in vascular endothelium and "
        "placenta, is transcriptionally induced by androgen, and localises to the plasma "
        "membrane, concentrating with tissue factor pathway inhibitor (TFPI) and caveolin-1 in "
        "lipid rafts and caveolae. In endothelial cells it raises TFPI expression and the "
        "cell-associated anticoagulant activity of TFPI against factor Xa, and its depletion "
        "increases monocyte adhesion and transendothelial migration through a PIK3R3-AKT-MIA3 "
        "axis. The gene lies at a coronary-artery-disease GWAS locus. How the lipid-hydrolase "
        "activity relates to the endothelial TFPI and vascular phenotypes is not established."
    )

    doc["existing_annotations"] = annotations

    doc["core_functions"] = [
        {
            "description": "Hydrolyses the ester bond of fatty acid esters of hydroxy fatty "
            "acids in the plasma membrane, releasing a free fatty acid and a hydroxy fatty acid "
            "and thereby terminating FAHFA signalling. Catalysis uses Thr47 as nucleophile and "
            "His131 as general base, both within transmembrane helices.",
            "molecular_function": {"id": "GO:0120573", "label": "FAHFA hydrolase activity"},
            "directly_involved_in": [
                {"id": "GO:0042758", "label": "long-chain fatty acid catabolic process"}
            ],
            "locations": [{"id": "GO:0005886", "label": "plasma membrane"}],
            "substrates": [
                {"id": "CHEBI:83670", "label": "9-PAHSA(1-)"},
                {"id": "CHEBI:83677", "label": "12-PAHSA(1-)"},
                {"id": "CHEBI:136282", "label": "9-[(9Z)-octadecenoyloxy]octadecanoate"},
            ],
            "supported_by": [
                q(
                    P_HYD,
                    "The FAHFA hydrolase activities of AIG1 and ADTRP were abolished by mutating "
                    "their putative catalytic nucleophilic residues Thr-43 and Thr-47, respectively",
                ),
                q(
                    P_HYD,
                    "Both AIG1 and ADTRP hydrolyze bioactive fatty acid esters of hydroxy fatty "
                    "acids (FAHFAs) but not other major classes of lipids.",
                ),
                q(
                    P_MOUSE,
                    "androgen-induced gene 1 (AIG1) and androgen-dependent TFPI-regulating "
                    "protein (ADTRP), two threonine hydrolases, control FAHFA levels in vivo in "
                    "both genetic and pharmacologic mouse models",
                ),
            ],
        }
    ]

    doc["proposed_new_terms"] = [
        {
            "proposed_name": "fatty acid ester of hydroxy fatty acid catabolic process",
            "proposed_definition": "The chemical reactions and pathways resulting in the "
            "breakdown of a fatty acid ester of a hydroxy fatty acid (FAHFA), a class of "
            "endogenous bioactive signalling lipids in which a fatty acid is esterified to a "
            "hydroxyl group on a second fatty acid backbone.",
            "proposed_parent": {
                "id": "GO:0042758",
                "label": "long-chain fatty acid catabolic process",
            },
            "justification": "GO gained the molecular function GO:0120573 FAHFA hydrolase "
            "activity on 2026-03-14 but has no biological-process counterpart; a QuickGO text "
            "search for 'FAHFA' returns GO:0120573 and nothing else. The nearest available "
            "process term, GO:0042758 long-chain fatty acid catabolic process, is chemically "
            "true for ADTRP because ChEBI classifies the substrate 9-PAHSA(1-) (CHEBI:83670) as "
            "a long-chain fatty acid anion, but it is far broader than the demonstrated "
            "specificity and it is the term PAINT is currently propagating from a "
            "pan-eukaryotic node to 86 gene products including 14 fungi and 5 plants. A "
            "FAHFA-level process term would let PAINT and manual curators state the specific "
            "claim where it is supported and withhold it where it is not. GO may reasonably "
            "decline this on the grounds that a single-step hydrolysis is adequately covered by "
            "the molecular function; that is recorded here as the counter-argument rather than "
            "suppressed.",
            "supported_by": [
                q(
                    P_MOUSE,
                    "The levels of other lipid classes were unaltered indicating that AIG1 and "
                    "ADTRP specifically hydrolyze FAHFAs.",
                )
            ],
        }
    ]

    doc["suggested_questions"] = [
        {
            "question": "PAINT recommendation for PTHR10989. At node PTN001659973, scoped "
            "taxon:2759 (Eukaryota) and seeded only by human ADTRP (Q96IZ2) and human AIG1 "
            "(Q9NVV5), the molecular function is held at GO:0016787 hydrolase activity - the "
            "root of the branch - while the biological process is the far more specific "
            "GO:0042758 long-chain fatty acid catabolic process. Both reach all 86 recipients, "
            "including 14 fungal, 5 plant and 2 other-eukaryote proteins, of which the only "
            "reviewed representatives are two uncharacterised UPF0641 proteins (P38842, "
            "Q96WV4). The character conserved across the node is the Thr/His catalytic dyad: "
            "73 of 85 recipients retain it when aligned onto ADTRP's own annotated SITE "
            "positions. A conserved dyad supports a claim about catalytic mechanism, which is "
            "what GO:0016787 states, but not a claim about substrate - and GO:0042758 is a "
            "substrate-level term whose substrate has been established only for the four "
            "characterised animal members. Should the process term therefore sit on the "
            "vertebrate or mammalian subclade where the IBD seeds actually are, as PTN002591065 "
            "already does for GO:0005901, leaving the mechanism-level MF at the Eukaryota node? "
            "Note the MF placement is recent and deliberate (2026-05-28, after GO:0120573 was "
            "created on 2026-03-14), so this is a question about the process term rather than a "
            "suggestion that the MF is stale.",
            "experts": ["GO Central / PAINT curators"],
        },
        {
            "question": "UniProt evidence attribution for Q96IZ2. The SUBCELLULAR LOCATION line "
            "cites both PubMed:21868574 and PubMed:27018888 as ECO:0000269 evidence for 'Cell "
            "membrane', and GOA has split this into two EXP rows for GO:0005886. The cached full "
            "text of PubMed:27018888 contains no localisation experiment - no "
            "immunofluorescence, confocal imaging or fractionation beyond bulk membrane lysates "
            "of transfected HEK293T cells, and no occurrence of the phrases 'plasma membrane' or "
            "'cell surface'. Should that reference be attached to 'Multi-pass membrane protein' "
            "only, leaving PubMed:21868574 as the evidence for the plasma-membrane compartment?",
            "experts": ["UniProt curators"],
        },
        {
            "question": "Is GO:2000402 negative regulation of lymphocyte migration correct for "
            "ADTRP from PMID:28341552? The abstract describes monocyte adhesion and monocyte "
            "transendothelial migration and never mentions lymphocytes. If the full text has no "
            "lymphocyte migration assay, GO:2000438 negative regulation of monocyte "
            "extravasation is the matching term; GO:0071676 negative regulation of mononuclear "
            "cell migration is a verified ancestor of both and would be the conservative choice.",
            "experts": ["BHF-UCL curators"],
        },
        {
            "question": "Does ADTRP's FAHFA hydrolase activity have anything to do with its "
            "effect on TFPI expression? The two literatures have never been joined: no study has "
            "asked whether the catalytically dead T47A or H131A mutant still supports TFPI "
            "up-regulation, nor whether FAHFA levels change in endothelial cells on ADTRP "
            "knockdown. Until that is done, the gene has two unconnected functional "
            "descriptions and GO records both without a causal link.",
            "experts": ["Lipid signalling", "Vascular biology"],
        },
        {
            "question": "Should human ADTRP carry a caveola annotation with the is_active_in "
            "relation? The seeding evidence is a located_in colocalisation IDA in endothelial "
            "cells, and no assay has placed FAHFA hydrolase activity in caveolae specifically.",
            "experts": ["GO Central / PAINT curators"],
        },
    ]

    doc["suggested_experiments"] = [
        {
            "hypothesis": "TFPI regulation by ADTRP requires its FAHFA hydrolase activity.",
            "description": "Reconstitute ADTRP knockdown endothelial cells with wild-type ADTRP, "
            "the T47A nucleophile mutant and the H131A general-base mutant, and measure TFPI "
            "mRNA, cell-associated TFPI anticoagulant activity against factor Xa, and cellular "
            "FAHFA levels by LC-MS in parallel. A catalytically dead mutant that still restores "
            "TFPI would separate the two functions; one that does not would unify them.",
            "experiment_type": "structure-function rescue",
        },
        {
            "hypothesis": "ADTRP hydrolyses FAHFAs within caveolae rather than across the plasma "
            "membrane generally.",
            "description": "Fractionate endothelial membranes into caveolar and non-caveolar "
            "pools by detergent-free density gradient, and assay FAHFA hydrolase activity in "
            "each with and without the ADTRP-active inhibitors KC01 and JJH260 alongside their "
            "inactive structural controls THL and ABC34. This would test the is_active_in "
            "caveola claim that PAINT currently propagates to 25 vertebrate orthologues.",
            "experiment_type": "subcellular fractionation and activity assay",
        },
        {
            "hypothesis": "The fungal ADTRP/AIG1 members that PAINT annotates as long-chain "
            "fatty acid catabolic enzymes are not FAHFA hydrolases.",
            "description": "Express the two reviewed uncharacterised family members, "
            "S. cerevisiae YHR140W (P38842) and S. pombe SPBPJ4664.05 (Q96WV4), and assay them "
            "against the same FAHFA and non-FAHFA lipid panel used for ADTRP and AIG1, checking "
            "fluorophosphonate probe reactivity and the conservation of the Thr/His pair. A "
            "negative result would justify restricting the node's process annotation to the "
            "clade where activity is demonstrated.",
            "experiment_type": "heterologous expression and substrate panel",
        },
    ]

    doc["knowledge_gaps"] = [
        {
            "gap_statement": "The physiological substrate-to-phenotype link for human ADTRP is "
            "unknown: no study connects its measured FAHFA hydrolase activity to any of the "
            "endothelial, coagulation or atherosclerosis phenotypes attributed to the gene.",
            "boundary": "Known: the enzyme hydrolyses FAHFAs in vitro and controls FAHFA levels "
            "in mouse tissues; and separately, its knockdown alters TFPI expression, monocyte "
            "adhesion and PIK3R3/AKT signalling in human endothelial cells. Unknown: whether "
            "either phenotype is downstream of the catalytic activity.",
            "gap_kind": ["BIOLOGY"],
            "dark_aspect": "RESIDUAL_SUBGAP",
            "status": "OPEN",
            "significance": "The gene has two independent functional literatures that GO records "
            "side by side without a causal relation. Any core-function statement that merges "
            "them would be asserting a link nobody has tested.",
            "provenance": [
                q(
                    P_HYD,
                    "If optimized inhibitors verify that AIG1 and/or ADTRP regulate FAHFA "
                    "metabolism in vivo, these enzymes could represent new targets for treating "
                    "metabolic disorders",
                ),
                q(
                    P_TFPI,
                    "We demonstrate that this protein regulates both the native and "
                    "androgen-enhanced TFPI expression and activity in cultured ECs, and we named "
                    "it androgen-dependent TFPI-regulating protein (ADTRP).",
                ),
            ],
        },
        {
            "gap_statement": "GO can express FAHFA hydrolysis as a molecular function but not as "
            "a biological process, so FAHFA catabolism has to be annotated with the much broader "
            "GO:0042758 long-chain fatty acid catabolic process.",
            "boundary": "Known: GO:0120573 FAHFA hydrolase activity exists and is RHEA-anchored. "
            "Unknown/absent: any FAHFA-level process term; a QuickGO search for 'FAHFA' returns "
            "exactly one term.",
            "gap_kind": ["ONTOLOGY"],
            "dark_aspect": "BP_DARK",
            "status": "OPEN",
            "significance": "The missing term is why a pan-eukaryotic PAINT node propagates a "
            "specific lipid-catabolism claim to 86 proteins: there is no way to state the "
            "narrower fact.",
            "provenance": [
                q(
                    P_MOUSE,
                    "these findings identify AIG1 and ADTRP as the first endogenous FAHFA "
                    "hydrolases identified",
                )
            ],
        },
        {
            "gap_statement": "The ADTRP/AIG1 family is pan-eukaryotic with 5788 members, but "
            "only four proteins have ever been characterised biochemically: human and mouse "
            "ADTRP and human and mouse AIG1. No substrate is known for any fungal, plant or "
            "invertebrate member.",
            "boundary": "Known: two human enzymes, their mouse orthologues, a mouse knockout "
            "phenotype, and that the Thr/His catalytic dyad is retained in 73 of 85 other "
            "members of the PANTHER node - so most of the family is very likely to be "
            "catalytically competent. Unknown: what any non-animal member hydrolyses, and "
            "whether FAHFAs exist as metabolites outside animals. Undetermined rather than "
            "negative for the 14 fungal members, whose alignments to ADTRP all fall below 25% "
            "identity.",
            "gap_kind": ["BIOLOGY", "CURATION"],
            "dark_aspect": "MF_DARK",
            "status": "OPEN",
            "significance": "Two of the eight reviewed members of the family signature IPR006838 "
            "are curated as uncharacterised UPF0641 proteins, yet PAINT gives all 86 recipients "
            "of PTN001659973 a long-chain fatty acid catabolic process annotation - a substrate "
            "claim, where the conserved evidence supports only a mechanism claim.",
            "provenance": [
                q(
                    P_HYD,
                    "The HHpred search results, however, uncovered a distinct set of "
                    "uncharacterized AIG1/ADTRP-like proteins that possess the conserved Thr and "
                    "His residues and are found in non-mammalian eukaryotic organisms (Panther "
                    "family PTHR12242; members in insects, plants, protozoa, and other "
                    "non-vertebrates)",
                )
            ],
        },
    ]

    # Reference metadata: titles are machine-sourced (stub / cached publication frontmatter),
    # reference_review is the manual judgement.
    reviews = {
        P_HYD: (
            "HIGH", "VERIFIED",
            "PubMed-verified; cached with full_text_available: true and read in full. This is "
            "the sole source of the gene's molecular function. No retraction, erratum or "
            "expression of concern on the PubMed record. Reference-projection test: it "
            "annotates 2 entities (ADTRP and AIG1) with 8 annotations - identical term sets, but "
            "the paper individually mutated and individually assayed both proteins, so this is "
            "parallel per-protein curation and not a projection.",
        ),
        P_TFPI: (
            "HIGH", "VERIFIED",
            "PubMed-verified; the paper that named the gene. Cached abstract-only "
            "(full_text_available: false), so this review restricts every claim from it to what "
            "the abstract states and defers to the UniProt curator on GO:0009986 cell surface. "
            "Projection test: 2 entities, ADTRP and TFPI (P10646), with different term sets.",
        ),
        P_CAD: (
            "MEDIUM", "VERIFIED",
            "PubMed-verified; source of nine BHF-UCL biological-process rows. Cached "
            "abstract-only. Projection test: 4 entities (ADTRP, AKT1, MIA3/TANGO1, PIK3R3) with "
            "22 annotations and a different term set per entity, so the network paper was curated "
            "per gene rather than projected. One cell-type problem is flagged on the GO:2000402 "
            "row: the abstract describes monocytes only.",
        ),
        P_HURI: (
            "LOW", "VERIFIED",
            "PubMed-verified. A systematic yeast two-hybrid interactome map, not an ADTRP study. "
            "It carries 85343 annotations across GOA, so the entity count is unavailable and the "
            "projection test was not run - recorded rather than approximated from a partial "
            "page. Both ADTRP rows trace to this one screen.",
        ),
        P_POU: (
            "MEDIUM", "VERIFIED",
            "PubMed-verified; cached abstract-only. Resolves the mechanism behind the GO:0010628 rows: POU1F1, not ADTRP, is the DNA-binding protein. Cited to keep the review from implying any transcriptional molecular function for ADTRP. Not present in GOA for this gene; surfaced by the affinage record and then read directly.",
        ),
        AFFINAGE: (
            "MEDIUM", "VERIFIED",
            "Machine-generated deep-research record, gates_passed: True, 12 citations. Recall was checked rather than assumed and it performed well on this gene: all 12 PMIDs are numeric (no bioRxiv ids in a PMID-shaped field), all 12 resolve to papers genuinely about ADTRP - there is no gene-symbol collision here - and none carries a retraction, erratum or expression of concern on its PubMed record. It also surfaced two papers absent from GOA that this review uses, PMID:32152231 (in vivo FAHFA control) and PMID:32445923 (POU1F1). Cited only as a lead and for claims independently anchored to a primary PMID; its own GO grounding block is wrong (it lists GO:0140098 catalytic activity, acting on RNA for a lipid hydrolase) and was not used.",
        ),
        P_MOUSE: (
            "HIGH", "VERIFIED",
            "PubMed-verified; the in vivo demonstration that ADTRP controls FAHFA levels, using "
            "Adtrp-knockout and AIG1/ADTRP double-knockout mice plus a dual inhibitor. Cited here "
            "for the core function and knowledge gaps. Not present in GOA for this gene and not "
            "returned by the affinage record as a GOA-linked source, so it is added by this "
            "review. Mouse data, so it is not used to assert a human-specific claim.",
        ),
    }
    # This builder loads its own previous output as the starting document, so appending
    # references unconditionally re-appends them on every re-run -- which is exactly how
    # PMID:32152231 reached four byte-identical entries. Merge by id instead of appending, so
    # the step is idempotent, then assert uniqueness. (`reference_id` citation counts cannot
    # catch this: they count citations, not uniqueness of the references list itself.)
    extra_refs = [
        {
            "id": P_POU,
            "title": "ADTRP regulates TFPI expression via transcription factor POU1F1 involved "
            "in coronary artery disease.",
            "findings": [],
        },
        {"id": AFFINAGE, "title": "Affinage mechanistic annotation for ADTRP (human)", "findings": []},
        {
            "id": P_MOUSE,
            "title": "AIG1 and ADTRP are endogenous hydrolases of fatty acid esters of hydroxy "
            "fatty acids (FAHFAs) in mice.",
            "findings": [],
        },
    ]
    # Detector: report duplicates present in the INPUT document. This is the check that would
    # have caught the shipped defect (four PMID:32152231 entries). It has to look at the loaded
    # list, because the merge below repairs them -- an assertion placed only after the merge is
    # vacuous, since dict values are unique by construction.
    loaded_ids = [r["id"] for r in doc["references"]]
    input_dupes = sorted({i for i in loaded_ids if loaded_ids.count(i) > 1})
    if input_dupes:
        print(f"  repaired duplicate reference ids present in input: {input_dupes}")

    # Take id/title/findings from the loaded document but DROP any inherited
    # ``reference_review``, so reviewer judgement can only come from the ``reviews`` dict below.
    # Round 1 lost two reference_review blocks precisely because they were inherited from the
    # previous output rather than declared here: the ids all stayed correct, so no id-level check
    # could see it, and the payload assertion could not fire either while the payload was being
    # silently carried over from disk. Rebuilding the field from a single source makes that class
    # of loss impossible by construction and makes the assertion load-bearing.
    by_id = {}
    for r in doc["references"]:
        stripped = {k: v for k, v in r.items() if k != "reference_review"}
        by_id[r["id"]] = stripped
    for r in extra_refs:
        by_id.setdefault(r["id"], r)
    for ref_id, (rel, corr, notes) in reviews.items():
        assert ref_id in by_id, f"reference {ref_id} not present to review"
        by_id[ref_id]["reference_review"] = {
            "relevance": rel,
            "correctness": corr,
            "review_notes": notes,
        }
    doc["references"] = _finalise_references(by_id)


    text = yaml.dump(doc, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=100)
    assert "&id" not in text and "*id" not in text, "YAML anchors emitted; rows are sharing objects"

    # Raw-vs-parsed reconciliation: a duplicate mapping key silently discards data on parse, and
    # every quote checker walks the parsed tree, so it cannot see what parsing removed.
    raw = len(re.findall(r"^\s*(?:-\s*)?reference_id:", text, re.M))
    parsed = count_quotes(yaml.safe_load(text))
    assert raw == parsed, f"raw/parsed reference_id mismatch: {raw} vs {parsed}"

    OUT.write_text(text)
    print(f"wrote {OUT} ({len(doc['existing_annotations'])} annotations, {parsed} quotes)")
    return 0


def count_quotes(node) -> int:
    if isinstance(node, dict):
        n = 1 if "reference_id" in node and "supporting_text" in node else 0
        return n + sum(count_quotes(v) for v in node.values())
    if isinstance(node, list):
        return sum(count_quotes(v) for v in node)
    return 0


if __name__ == "__main__":
    sys.exit(main())
