"""Manual evidence-aware MYCTU review; immutable seed payloads checked on write."""

import json
import os
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
A = Path(__file__).resolve().parent
BASE = json.loads((A / "baseline.json").read_text())


def term(go, label):
    return {"id": "GO:" + go, "label": label}


NHEJ = term("0006303", "double-strand break repair via nonhomologous end joining")
DS = term("0003690", "double-stranded DNA binding")
SS = term("0003697", "single-stranded DNA binding")
LIG = term("0003910", "DNA ligase (ATP) activity")
DNA = term("0003887", "DNA-directed DNA polymerase activity")
RNA = term("0003899", "DNA-directed RNA polymerase activity")
EXO = term("0008310", "single-stranded DNA 3'-5' DNA exonuclease activity")
ACT = term("0008047", "enzyme activator activity")
MG = term("0000287", "magnesium ion binding")
MN = term("0030145", "manganese ion binding")
RIBO = term("0032553", "ribonucleotide binding")
DEOXY = term("0032552", "deoxyribonucleotide binding")


def supp(ref, quote):
    path = (
        ROOT / ("publications/PMID_" + ref[5:] + ".md")
        if ref.startswith("PMID:")
        else ROOT / "genes" / ref[5:]
    )
    assert re.sub(r"\s+", " ", quote) in re.sub(r"\s+", " ", path.read_text()), (
        ref,
        quote,
    )
    return {"reference_id": ref, "supporting_text": quote}


KU_RAW = "file:MYCTU/mku/mku-uniprot.txt"
LD_RAW = "file:MYCTU/ligD/ligD-uniprot.txt"
S = {
    "kuDNA": supp(
        KU_RAW,
        "Binds linear dsDNA with 5'- and 3'-overhangs but not closed\nCC       circular dsDNA nor ssDNA.",
    ),
    "kuLig": supp(
        "PMID:12215643",
        "bacterial Ku specifically recruits DNA ligase to DNA ends and stimulates DNA ligation.",
    ),
    "nhej": supp(
        "PMID:15499016",
        "These enzyme activities allow the Mt-Ku and Mt-Lig proteins to join incompatible DSB ends in vitro, as well as to reconstitute NHEJ in vivo in yeast.",
    ),
    "uvrd": supp(
        "PMID:17376770",
        "Ku stimulates UvrD1 to catalyze ATP-dependent unwinding of 3'-tailed DNAs. UvrD1, Ku, and DNA form a stable ternary complex in the absence of ATP.",
    ),
    "dimer": supp(
        "PMID:42953966",
        "all Ku mutants had retained proper secondary structure folding and a homodimeric state using CD Spectroscopy and SEC-MALS",
    ),
    "primase": supp(
        "PMID:16023671",
        "The polymerase domain demonstrated DNA-dependent RNA primase activity, catalysing the synthesis of unprimed oligoribonucleotides on single-stranded DNA templates.",
    ),
    "dnabind": supp(
        "PMID:16023671",
        "DNA-binding assays revealed that both the polymerase and ligase domains bind DNA in vitro, the latter with considerably higher affinity.",
    ),
    "poly": supp(
        "PMID:16023671",
        "The polymerase domain can also extend DNA in a template-dependent manner.",
    ),
    "lig": supp(
        "PMID:14985346",
        "LigC and LigD, which have ATP-specific adenylyltransferase activity, display weak nick joining activity and generate high levels of the DNA-adenylate intermediate.",
    ),
    "ligstruct": supp(
        "PMID:16476729",
        "captured as the covalent ligase-AMP intermediate with a divalent metal in the active site.",
    ),
    "native": supp(
        "PMID:14985346",
        "M. tuberculosis ligDDelta cells are defective in nonhomologous DNA end joining.",
    ),
    "nuc": supp(
        "PMID:15499016",
        "including gap-filling polymerase, terminal transferase, and primase, and is also a 3' to 5' exonuclease.",
    ),
    "ssnuc": supp(LD_RAW, "and 3'- to 5'-exonuclease on ssDNA (PubMed:15499016)."),
    "ribo": supp(
        "PMID:17174332",
        "ribonucleotide insertion appears to be a recurrent theme associated with NHEJ, maximised in this case by the deployment of a dedicated primase, although its in vivo relevance is unknown.",
    ),
    "nt": supp(
        "PMID:17174332",
        "crystal structures of the primase/polymerisation domain (PolDom) of Mycobacterium tuberculosis LigD, alone and complexed with nucleotides.",
    ),
    "mn": supp(
        LD_RAW,
        "Binds 4 Mn(2+); 2 Mn(2+) for polymerase/primase activity, 1 each\nCC       for 3-phosphoesterase and ligase.",
    ),
    "rnaseq": supp(
        LD_RAW, "DNA-directed DNA\nCC       or RNA polymerase on 5'-overhangs"
    ),
    "oldpositive": supp(
        "PMID:16023671",
        "Mt-Ku stimulated the primer extension activity of the polymerase domain",
    ),
    "newreg": supp(
        "PMID:42953966",
        "Ku stimulates LigD ligase activity through contacts with both polymerase and ligase domains, while Ku attenuates template-dependent polymerase activity",
    ),
    "construct": supp(
        "PMID:42953966",
        "Codon-optimized Ku (ID: P9WKD9) and LigD (ID: P9WNV2) sequences from M. tuberculosis were synthesized by Genewiz",
    ),
    "newMg": supp(
        "PMID:42953966",
        "polymerase buffer (50 mM HEPES pH 7.5, 5 mM MgCl2, and 5 mM DTT)",
    ),
    "synapse": supp(
        "PMID:17947582",
        "Biochemical and biophysical studies confirmed that polymerase-induced end synapsis also occurs in solution.",
    ),
    "metal": supp(
        "PMID:21255731",
        "Mycobacterium tuberculosis PolDom, consisting of a polymerase bound to a DNA end with a 3' overhang, two metal ions, and an incoming nucleotide",
    ),
    "anneal": supp(
        "PMID:24239356",
        "annealing the 3' overhanging strands from opposing breaks, forming a gapped intermediate that can be extended in trans.",
    ),
}


def rev(action, summary, reason, keys, replacements=None):
    d = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": [S[k] for k in keys],
    }
    if replacements:
        d["proposed_replacement_terms"] = replacements
    return d


for gene in ("mku", "ligD"):
    path = ROOT / f"genes/MYCTU/{gene}/{gene}-ai-review.yaml"
    d = yaml.safe_load(path.read_text())
    seed = BASE["reviews"][str(path.relative_to(ROOT))]
    assert d["existing_annotations"] == seed["existing_annotations"]
    for ann in d["existing_annotations"]:
        go = ann["term"]["id"]
        original = ann["original_reference_id"]
        if go == "GO:0005515":
            key = "uvrd" if original == "PMID:17376770" else "kuLig"
            ann["review"] = rev(
                "REMOVE",
                "The physical interaction is real, but bare protein binding is uninformative.",
                "Apply the repository bare GO:0005515 policy. This removes the generic annotation, not the demonstrated Ku–LigD or Ku–UvrD1 interaction. Functional recruitment, ligase stimulation, and the helicase-complex context are retained independently where supported.",
                [key],
            )
        elif gene == "mku":
            if go == "GO:0003677":
                ann["review"] = rev(
                    "MODIFY",
                    "Ku recognizes exposed double-stranded DNA ends.",
                    "Refine the true DNA-binding genus to its supported double-stranded DNA-binding descendant. Curated primary-linked biochemical findings distinguish linear duplex ends from closed circular duplex and single-stranded DNA; no general single-stranded binding claim is inferred.",
                    ["kuDNA"],
                    [DS],
                )
            elif go == "GO:0003690":
                ann["review"] = rev(
                    "ACCEPT",
                    "Double-stranded DNA-end binding is the central Ku recognition function.",
                    "Direct target biochemical curation and native Ku architecture support the claim. For the IBA, the exact P9WKD9 leaf PTN002447586 descends from the cited IBD PTN002222140 in the retrieved family tree. Target P9WKD9 in the seed list is legitimate experimental grounding, not circularity. The local PAINT slice has no recorded loss row; a global loss-free lineage is not asserted.",
                    ["kuDNA"],
                )
            elif go in ("GO:0006281", "GO:0006974"):
                ann["review"] = rev(
                    "MODIFY",
                    "The supported repair response is nonhomologous end joining.",
                    "GO:0006303 is a verified descendant of both DNA repair and DNA damage response through the current is_a/part_of closure. Ku performs DNA-end recognition and recruitment in this process, rather than being merely a damage-sensitive substrate. This positive refinement does not add a new process row.",
                    ["nhej"],
                    [NHEJ],
                )
            elif go == "GO:0006303":
                ann["review"] = rev(
                    "ACCEPT",
                    "Ku and LigD directly reconstitute nonhomologous joining of incompatible DNA ends.",
                    "The original target biochemical study and heterologous yeast reconstitution establish participation. The paper is not recast as a native H37Rv survival experiment; the Bacillus radiation phenotype in PMID12215643 is also not transferred to H37Rv. The electronic row is supported by the same independently characterized Ku function.",
                    ["nhej"],
                )
            elif go == "GO:0033202":
                ann["review"] = rev(
                    "KEEP_AS_NON_CORE",
                    "Ku participates in a functional UvrD1–Ku–DNA helicase complex.",
                    "The term denotes a complex possessing helicase activity and does not assign autonomous helicase catalysis to Ku. The primary abstract explicitly reports the stable ternary complex and Ku-dependent unwinding. This is a secondary partner context relative to Ku–LigD end joining. The native deletion/radiation phenotypes in that paper are M. smegmatis, not H37Rv; unavailable full construct details are not grounds to reject the curated interaction.",
                    ["uvrd"],
                )
            elif go == "GO:0042803":
                ann["review"] = rev(
                    "ACCEPT",
                    "Ku functions as a homodimeric DNA-end recognition factor.",
                    "Retain the original IPI claim: identical-subunit association is intrinsic to the Ku assembly. Recent experiments explicitly use Ku accession P9WKD9 and check retained homodimeric state by SEC-MALS. This is not a claim that the synthetic tagged construct measures native cellular stoichiometry in situ.",
                    ["dimer", "construct"],
                )
            elif go == "GO:0051351":
                ann["review"] = rev(
                    "ACCEPT",
                    "Ku recruits LigD and increases ligation activity.",
                    "Direct ligation stimulation is supported by the original bacterial Ku study and later interaction assays. The recent construct pairs P9WKD9 Ku with CDC1551 LigD P9WNV2, not H37Rv LigD P9WNV3. Ligase stimulation remains distinct from assay-dependent polymerase modulation; it is not a universal activation claim for every LigD domain.",
                    ["kuLig", "newreg", "construct"],
                )
            else:
                raise AssertionError(go)
        elif go == "GO:0000166":
            ann["review"] = rev(
                "MODIFY",
                "LigD recognizes both ribonucleotide and deoxyribonucleotide substrates.",
                "The polymerase and ligase activities support both substrate classes, rather than ATP alone. Replace the generic nucleotide claim with both chemical classes. GO:0032553 is an ontology descendant; the current GO:0032552 snapshot lacks a path to GO:0000166 despite its deoxyribonucleotide definition, so the latter is an explicit semantic specificity correction, not a claimed ontology descendant.",
                ["nt", "poly", "ribo"],
                [RIBO, DEOXY],
            )
        elif go in ("GO:0000287", "GO:0030145"):
            metal = "magnesium" if go == "GO:0000287" else "manganese"
            ann["review"] = rev(
                "ACCEPT",
                f"{metal.capitalize()} is an experimentally assigned catalytic metal for LigD chemistry.",
                "Retain the original target IDA assignment, supported by metal-dependent polymerase/ligation chemistry and structural metal coordination. The primary-linked UniProt cofactor synthesis explicitly describes manganese sites. Exact site occupancy and physiological metal preference should not be inferred from an assay-buffer concentration; the recent magnesium-buffer experiment uses the one-residue-different CDC1551 LigD comparator. Several original papers are abstract-only here, so their curated positive metal evidence is not rejected from abstract silence.",
                ["metal", "mn"]
                if metal == "manganese"
                else ["metal", "newMg", "construct"],
            )
        elif go == "GO:0003677":
            ann["review"] = rev(
                "MODIFY",
                "LigD binds duplex break intermediates and single-stranded DNA templates.",
                "Both polymerase and ligase domains bind DNA. Refine to the two supported descendant classes: duplex binding in nicked/gapped/end-synaptic substrates and single-stranded binding required for the directly measured synthesis of RNA primers on unprimed ssDNA. The latter is substrate engagement inferred from the purified template-dependent reaction, not a separately claimed affinity constant. No sequence-specific transcription-factor function is implied.",
                ["dnabind", "primase", "anneal"],
                [DS, SS],
            )
        elif go == "GO:0003887":
            ann["review"] = rev(
                "ACCEPT",
                "The POL domain catalyzes DNA-template-directed nucleotide extension during end processing.",
                "Direct target polymerase assays support this molecular function. The exact target leaf PTN002448560 descends from IBD PTN001627042; target-seeded PAINT evidence is legitimate. Changes in Ku regulation do not abolish intrinsic polymerase activity. The 2026 inhibitory result is bounded to its CDC1551 LigD construct and DNA/metal conditions; the older target primary explicitly reports stimulation of primer extension.",
                ["poly", "oldpositive", "newreg", "construct"],
            )
        elif go == "GO:0003899":
            ann["review"] = rev(
                "ACCEPT",
                "LigD catalyzes DNA-dependent RNA synthesis in its repair polymerase/primase domain.",
                "The current term explicitly permits de novo initiation. Purified-domain RNA priming and the primary-linked curated rNTP extension activity support the MF without asserting a transcriptional RNA-polymerase role. Physiological deployment of the short RNA products remains less certain than the measured molecular activity.",
                ["primase", "rnaseq", "ribo"],
            )
        elif go == "GO:0003909":
            ann["review"] = rev(
                "MODIFY",
                "LigD uses ATP to seal DNA termini.",
                "Refine the valid generic DNA ligase activity to the verified ATP-dependent descendant GO:0003910. ATP-specific adenylation and phosphodiester sealing are directly supported; weak nick joining in one isolated assay does not negate the enzyme class.",
                ["lig", "ligstruct"],
                [LIG],
            )
        elif go == "GO:0003910":
            ann["review"] = rev(
                "ACCEPT",
                "ATP-dependent DNA ligation is the central strand-sealing activity of LigD.",
                "Target biochemical and structural evidence establishes ATP-dependent adenylation and sealing. The exact target leaf lies below PAINT IBD PTN001627042 and supplies one experimental seed, which is appropriate phylogenetic grounding. The reaction does not depend on transferring every feature of another LigD architecture.",
                ["lig", "ligstruct"],
            )
        elif go == "GO:0005524":
            ann["review"] = rev(
                "ACCEPT",
                "ATP is the substrate of LigD adenylation and ligation.",
                "ATP binding is independently supported by ATP-specific adenylyltransferase chemistry and structural capture of the covalent AMP intermediate. This is not ATPase activity, and the use of additional nucleotide substrates by POL does not contradict ATP recognition by the ligase domain.",
                ["lig", "ligstruct"],
            )
        elif go == "GO:0006269":
            ann["review"] = rev(
                "KEEP_AS_NON_CORE",
                "LigD has measured de novo primer-synthesis capability, with uncertain physiological deployment.",
                "The current definition includes short nucleotide-polymer synthesis on a DNA template and explicitly admits DNA-damage contexts. Purified H37Rv LigD POL synthesizes unprimed oligoribonucleotides on ssDNA. Retain the experimental claim and its consistent IBA with a peripheral biochemical interpretation, without asserting that LigD is the normal chromosomal replication primase or that the activity is used in vivo. The target lies below PTN001627042 and is the legitimate experimental seed; donor count is not a negative argument.",
                ["primase", "ribo"],
            )
        elif go in ("GO:0006281", "GO:0006302"):
            ann["review"] = rev(
                "MODIFY",
                "The experimentally supported repair mechanism is nonhomologous end joining.",
                "Refine the true repair/DSB-repair ancestor to GO:0006303, already supported by target biochemistry and genetics. LigD performs end synthesis and sealing rather than being merely required as a substrate. Native M. tuberculosis genetic evidence and heterologous reconstitution are distinguished; strain-specific fidelity results from incompletely inspected studies are not silently assigned to H37Rv.",
                ["nhej", "native"],
                [NHEJ],
            )
        elif go == "GO:0006303":
            ann["review"] = rev(
                "ACCEPT",
                "LigD catalyzes end processing and sealing in bacterial nonhomologous end joining.",
                "Direct biochemical reconstitution, target-specific domain studies and M. tuberculosis ligD deletion evidence converge on the repair role. Exact IBD PTN001627042 is ancestral to the target leaf; its target self-seed is expected. Polymerase-mediated synapsis and trans extension contribute to the mechanism. This does not assert that every conditional end-joining event absolutely requires every LigD domain.",
                ["nhej", "native", "anneal"],
            )
        elif go == "GO:0006310":
            ann["review"] = rev(
                "MODIFY",
                "The experimentally resolved DNA-joining role is NHEJ repair.",
                "The generic electronic recombination assignment is best expressed as the supported NHEJ mechanism. This is a lateral mechanistic correction: current GO:0006303 is not a descendant of GO:0006310. End-joining repair should not be presented as demonstrated homologous exchange or chromosome assortment, although joining can alter sequence outcomes.",
                ["nhej"],
                [NHEJ],
            )
        elif go == "GO:0008310":
            ann["review"] = rev(
                "ACCEPT",
                "Full-length Mt-Lig has reported single-stranded DNA 3'-to-5' exonuclease activity.",
                "The original experimental study and its curated target synthesis explicitly support this substrate-specific activity. The later failure of an isolated nuclease domain to act independently does not refute the full-length enzyme measurement. Retain the claim without conflating all phosphoesterase-domain chemistry with an autonomous DNA exonuclease or a universal activity of every LigD homolog.",
                ["nuc", "ssnuc"],
            )
        elif go == "GO:0032553":
            ann["review"] = rev(
                "ACCEPT",
                "Ribonucleotide recognition supports the POL/primase substrate repertoire.",
                "Direct RNA synthesis, ribonucleotide insertion and the nucleotide-bound POL structures support this class. The repertoire is not restricted to ATP, so refining this entire claim to ATP binding would discard other demonstrated substrates. Native physiological use of RNA priming remains distinct from measured substrate recognition.",
                ["nt", "ribo", "primase"],
            )
        elif go == "GO:0046872":
            ann["review"] = rev(
                "MODIFY",
                "LigD catalytic chemistry uses divalent metals, with magnesium and manganese assignments.",
                "Refine the generic metal-binding class to both supported specific classes already carried by this review. The original ligase structure captures a divalent metal but its abstract alone does not identify every physiological ion; independent target IDA assignments and curated cofactor evidence supply the specific classes. Assay-buffer magnesium in the recent CDC1551 comparator is corroborating chemistry, not H37Rv site-occupancy proof.",
                ["ligstruct", "mn", "metal"],
                [MG, MN],
            )
        elif go == "GO:0071897":
            ann["review"] = rev(
                "ACCEPT",
                "LigD performs DNA synthesis while remodeling broken termini.",
                "Template-dependent DNA polymerization directly performs DNA biosynthesis. Retain this chemical process at its warranted precision; it does not imply genome replication or RNA transcription. NHEJ separately identifies the mechanistic context, and no unsupported more specific DNA-biosynthesis subclass is substituted.",
                ["poly", "anneal"],
            )
        else:
            raise AssertionError(go)
    d["status"] = "COMPLETE"
    if gene == "mku":
        d["description"] = (
            "Mku is the homodimeric DNA-end recognition factor of the Mycobacterium tuberculosis H37Rv nonhomologous end-joining system. It binds exposed double-stranded DNA termini, recruits LigD and promotes ligation. Mku can also associate with UvrD1 in a DNA-unwinding complex without itself being the catalytic helicase. Ku regulation of LigD is activity- and assay-dependent: older mycobacterial experiments reported polymerase stimulation, whereas a recent study of H37Rv Ku with CDC1551 LigD observed ligase stimulation together with attenuation of template-dependent polymerization."
        )
        d["core_functions"] = [
            {
                "description": "Homodimeric binding to exposed double-stranded DNA ends recognizes and organizes substrates for LigD-mediated end joining.",
                "molecular_function": DS,
                "directly_involved_in": [NHEJ],
                "supported_by": [S["kuDNA"], S["nhej"]],
            },
            {
                "description": "Recruitment and stimulation of LigD ligation support NHEJ. This does not imply a common regulatory sign for every LigD catalytic domain or construct.",
                "molecular_function": ACT,
                "directly_involved_in": [NHEJ],
                "supported_by": [S["kuLig"], S["newreg"], S["construct"]],
            },
        ]
    else:
        d["description"] = (
            "LigD is a multifunctional DNA-break repair enzyme of Mycobacterium tuberculosis H37Rv. Its POL, phosphoesterase and ATP-dependent ligase modules support processing and sealing of DNA ends in cooperation with Ku. The polymerase recognizes broken-end intermediates, supports synapsis and trans extension, and can use deoxyribonucleotides or ribonucleotides; purified-domain RNA priming is demonstrated, although its physiological deployment is unresolved. Reported full-length exonuclease activity is distinct from autonomous activity of the isolated phosphoesterase domain. Ku-dependent regulation varies with the tested activity and construct; recent polymerase inhibition was measured with the one-residue-different CDC1551 LigD rather than this H37Rv sequence."
        )
        d["core_functions"] = [
            {
                "description": "ATP-dependent sealing of processed DNA ends completes the strand-joining reaction of NHEJ.",
                "molecular_function": LIG,
                "directly_involved_in": [NHEJ],
                "supported_by": [S["lig"], S["ligstruct"], S["native"]],
            },
            {
                "description": "DNA-template-directed extension, coupled to DNA-end synapsis, remodels incompatible breaks before sealing.",
                "molecular_function": DNA,
                "directly_involved_in": [NHEJ],
                "supported_by": [S["poly"], S["synapse"], S["anneal"]],
            },
            {
                "description": "DNA-dependent RNA synthesis supplies ribonucleotide incorporation by the repair POL/primase domain. De novo priming is measured biochemically; its native use is unresolved.",
                "molecular_function": RNA,
                "directly_involved_in": [NHEJ],
                "supported_by": [S["primase"], S["rnaseq"], S["ribo"]],
            },
            {
                "description": "Reported full-length single-stranded DNA 3'-to-5' exonuclease activity provides one end-processing capability. This is not a claim that the isolated PE domain alone performs this reaction.",
                "molecular_function": EXO,
                "directly_involved_in": [NHEJ],
                "supported_by": [S["nuc"], S["ssnuc"]],
            },
        ]
    refs = {r["id"]: r for r in d["references"]}
    needed = {
        s["reference_id"]
        for ann in d["existing_annotations"]
        for s in ann["review"].get("supported_by", [])
    }
    needed |= {
        s["reference_id"]
        for c in d["core_functions"]
        for s in c.get("supported_by", [])
    }
    for rid in sorted(needed):
        if rid not in refs:
            if rid.startswith("PMID:"):
                meta = yaml.safe_load(
                    (ROOT / f"publications/PMID_{rid[5:]}.md")
                    .read_text()
                    .split("---")[1]
                )
                title = meta["title"]
            else:
                title = "Frozen UniProt target record: curated experimental function and domain evidence"
            refs[rid] = {"id": rid, "title": title, "findings": []}
            d["references"].append(refs[rid])
    for key in (
        [
            "kuDNA",
            "kuLig",
            "nhej",
            "uvrd",
            "dimer",
            "newreg",
            "construct",
            "oldpositive",
        ]
        if gene == "mku"
        else [
            "primase",
            "dnabind",
            "poly",
            "lig",
            "native",
            "nuc",
            "nt",
            "mn",
            "anneal",
            "newreg",
            "construct",
            "oldpositive",
        ]
    ):
        item = S[key]
        rid = item["reference_id"]
        if rid not in refs:
            meta = yaml.safe_load(
                (ROOT / f"publications/PMID_{rid[5:]}.md").read_text().split("---")[1]
            )
            refs[rid] = {"id": rid, "title": meta["title"], "findings": []}
            d["references"].append(refs[rid])
        statement = {
            "newreg": "The recent Ku–LigD construct combination gives stimulation of ligation and attenuation of template-dependent polymerization; the LigD sequence is CDC1551 P9WNV2.",
            "construct": "Synthetic accession-defined Ku is the H37Rv target; LigD is a CDC1551 comparator differing from H37Rv at residue344.",
            "oldpositive": "The older mycobacterial study explicitly reports polymerase stimulation, so the direction is not collapsed into a universal species rule.",
            "primase": "Purified POL makes unprimed RNA on ssDNA; this establishes biochemical capability without normal chromosomal-replication assignment.",
            "uvrd": "Ku is a partner in an active UvrD1 complex; UvrD1 is the catalytic helicase and native deletion phenotypes are in M.smegmatis.",
            "native": "The abstract explicitly reports defective NHEJ in M.tuberculosis ligD deletion cells; it is not a claim of essential growth.",
        }.get(
            key,
            "The cited experimental or curated statement supports the corresponding binding, catalytic or repair capability, within the construct and assay limits described in the annotation reviews.",
        )
        refs[rid]["findings"].append(
            {"statement": statement, "supporting_text": item["supporting_text"]}
        )
    # Fill standard GO reference names using independent repository records, not invented literature titles.
    names = {
        "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
        "GO_REF:0000033": "Annotation inferences using phylogenetic trees",
        "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
        "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on on inter-ontology links",
        "GO_REF:0000117": "Electronic annotation based on ARBA machine learning models",
        "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
    }
    for r in d["references"]:
        if r["id"] in names:
            r["title"] = names[r["id"]]

    def payload(row):
        return {k: v for k, v in row.items() if k != "review"}

    assert [payload(a) for a in d["existing_annotations"]] == [
        payload(a) for a in seed["existing_annotations"]
    ]
    text = (
        "\n".join(
            line.rstrip()
            for line in yaml.safe_dump(
                d, sort_keys=False, allow_unicode=True, width=100
            ).splitlines()
        )
        + "\n"
    )
    tmp = path.with_suffix(".tmp")
    tmp.write_text(text)
    os.replace(tmp, path)
    note = ROOT / f"genes/MYCTU/{gene}/{gene}-notes.md"
    with note.open("a") as f:
        f.write(
            f"""\n## 2026-11-07 manual review\n\nReviewed all {len(d["existing_annotations"])} original annotations with ordered payloads/qualifiers intact; no NEW or retired rows. Full PMID42953966 and PMID24239356 were consulted alongside the original primary abstracts and curated experimental UniProt statements. Abstract-only sources were not portrayed as complete inspected methods, and experimental claims were not removed from abstract silence.\n\nConstruct boundary: 42953966 specifies P9WKD9 Ku and P9WNV2 LigD. Root's official sequence comparison shows CDC1551/P9WNV2 is R344 versus H37Rv/P9WNV3 C344 (759aa each); exact equality is false. Its Mg-buffer, defined-DNA, synthetic-protein assays demonstrate a particular dual regulatory effect, not native H37Rv regulatory signs. PMID16023671 explicitly reported stimulation of template-dependent primer extension; the two assay contexts remain distinct.\n\nBiology: DNA-end recognition, ATP-dependent ligation, DNA/RNA synthesis and measured processing are separate capabilities. Ku–UvrD1 association supports the helicase-complex CC claim without assigning helicase catalysis to Ku. LigD de novo RNA priming is retained as a bounded secondary biochemical capability; GO0006269 currently includes damage contexts, and native deployment remains unresolved. Binding/catalytic metals are not equated with physiological metal preference. Bare protein-binding removal follows repository policy and does not deny experimentally observed interactions.\n\nPAINT: exact target leaves and cited IBD ancestors were checked against root's official tree receipts and raw family assertions. Target self-seeds are legitimate. Local PAINT exports contain no loss assertions, but no global loss-free claim or whole-family activity grant is made. All LigD architecture/function conclusions remain target-specific.\n\nProvider provenance: root reports a real default Falcon authentication failure earlier in this session with no credential change; no retry or fabricated gene/provider output was produced. These are manual notes. The OpenScientist module report is discovery support, not independent biological evidence.\n\nGO definitions and ancestry snapshots are in myctu-review-20261107. Current GO0032552 lacks the expected nucleotide-binding ancestor path; the two-substrate-class refinement is therefore explicitly semantic for that branch, not falsely described as a descendant. DNA recombination to NHEJ is also a lateral mechanistic replacement. No new annotation was manufactured to eliminate core-coverage warnings.\n"""
        )
print("Curated both MYCTU genes; preserved 55 original source payloads.")
