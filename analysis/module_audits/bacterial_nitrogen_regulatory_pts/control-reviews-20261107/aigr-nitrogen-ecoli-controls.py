from pathlib import Path
import yaml
import json
import hashlib

w = Path("/private/tmp/aigr-nitrogen-pts-taxon-audit")
c = (
    w
    / "analysis/module_audits/bacterial_nitrogen_regulatory_pts/control-reviews-20261107"
)


def term(i, label):
    return {"id": i, "label": label}


def sup(ref, quote=None):
    d = {"reference_id": ref}
    if quote:
        d["supporting_text"] = quote
    return d


def review(action, summary, reason, refs, repl=None):
    d = {"action": action, "summary": summary, "reason": reason, "supported_by": refs}
    if repl:
        d["proposed_replacement_terms"] = repl
    return d


for gene in ["ptsI", "ptsH"]:
    p = w / f"genes/ECOLI/{gene}/{gene}-ai-review.yaml"
    d = yaml.safe_load(p.read_text())
    assert all(a["review"]["action"] == "PENDING" for a in d["existing_annotations"])
    (c / f"ECOLI-{gene}-seeded-baseline.yaml").write_bytes(p.read_bytes())
    original = [
        {k: v for k, v in a.items() if k != "review"} for a in d["existing_annotations"]
    ]
    u = f"file:ECOLI/{gene}/{gene}-uniprot.txt"
    for a in d["existing_annotations"]:
        tid = a["term"]["id"]
        rid = a["original_reference_id"]
        if tid == "GO:0005515":
            a["review"] = review(
                "REMOVE",
                "Bare protein binding does not describe the specific phosphocarrier or regulatory activity.",
                "Apply the repository policy for GO:0005515, without rejecting the reported interaction or its experimental provenance. Specific catalytic, regulatory and oligomeric roles are assessed separately; this is not evidence-based deduplication.",
                [sup(rid)],
            )
        elif tid == "GO:0005737":
            a["review"] = review(
                "MODIFY",
                "Refine cytoplasm to the experimentally annotated cytosol.",
                "The existing cytosol row supplies a supported descendant. Cytosol includes protein complexes; polar clustering or association with soluble partners does not by itself require a different cellular component. Retain assay limits rather than claiming membrane localization.",
                [sup("PMID:18304323" if gene == "ptsH" else "PMID:16858726"), sup(u)],
                [term("GO:0005829", "cytosol")],
            )
        elif tid == "GO:0005829":
            a["review"] = review(
                "ACCEPT",
                "The cytosolic localization agrees with the soluble phosphotransfer chemistry.",
                "Retain the curated experimental localization. The cached study describes cytosolic protein profiling/complex separation, while the curated UniProt record independently places the protein in the cytoplasm. No claim is made that the accessible abstract lists every identified target.",
                [sup(rid), sup(u)],
            )
        elif gene == "ptsI":
            if tid == "GO:0008965":
                a["review"] = review(
                    "ACCEPT",
                    "Enzyme I transfers phosphate from PEP to HPr through its catalytic histidine.",
                    "Target enzyme assays and the phosphorylated EI structure support this activity. Electronic and phylogenetic annotations agree with independently measured E. coli chemistry; donor count is not used as an evidential score.",
                    [sup("PMID:12705838"), sup("PMID:17053069"), sup(u)],
                )
            elif tid == "GO:0009401":
                a["review"] = review(
                    "ACCEPT",
                    "PtsI initiates the carbohydrate PTS phosphotransfer chain.",
                    "The target directly performs the phosphate-entry step used for coupled sugar uptake and phosphorylation. It is neither the membrane permease nor a sugar-specific EII protein, but its catalytic participation supports the process annotation.",
                    [sup("PMID:17053069"), sup(u)],
                )
            elif tid == "GO:0015764":
                a["review"] = review(
                    "KEEP_AS_NON_CORE",
                    "N-acetylglucosamine uptake is one substrate-specific use of the general PTS phosphate donor.",
                    "The inherited transport claim is compatible with native EI-HPr-EII phosphate flow. PtsI supplies a catalytic step shared by multiple sugar systems; this term does not make it the N-acetylglucosamine permease or establish substrate specificity. Retain the sugar-specific physiological context as non-core. No PAINT node loss or misplacement is asserted.",
                    [sup(u), sup("PMID:26784570")],
                )
            elif tid == "GO:0016772":
                a["review"] = review(
                    "MODIFY",
                    "Refine broad phosphorus transfer to the already present PEP-dependent protein phosphotransferase activity.",
                    "The existing GO:0008965 descendant captures the experimentally supported donor and acceptor class. This broad term is true and core, so it is refined rather than removed or marked peripheral.",
                    [sup("PMID:12705838"), sup(u)],
                    [
                        term(
                            "GO:0008965",
                            "phosphoenolpyruvate-protein phosphotransferase activity",
                        )
                    ],
                )
            elif tid == "GO:0042802":
                a["review"] = review(
                    "ACCEPT",
                    "PtsI forms a functional homodimer.",
                    "The solved phosphorylated target enzyme is dimeric, corroborating the curated homomeric interaction. Identical protein binding is distinct from bare GO:0005515 and here describes the enzyme assembly. No unsupported stable complex with all PTS partners is proposed.",
                    [sup("PMID:17053069"), sup(u)],
                )
            else:
                raise ValueError(tid)
        else:
            if tid == "GO:0004857":
                a["review"] = review(
                    "MODIFY",
                    "HPr inhibits the AI-2 kinase LsrK, supporting the more specific kinase inhibitor activity.",
                    "The target cocrystal and activity assays establish LsrK binding and inhibition. GO:0019210 is the appropriate narrower activity; sugar-dependent signaling outcomes are not substituted for the direct biochemical mechanism.",
                    [
                        sup(
                            "PMID:29868643",
                            "LsrK activity is inhibited\nwhen bound to HPr",
                        )
                    ],
                    [term("GO:0019210", "kinase inhibitor activity")],
                )
            elif tid == "GO:0008047":
                a["review"] = review(
                    "ACCEPT",
                    "HPr directly activates glycogen phosphorylase.",
                    "Binding and coupled enzyme assays support allosteric activation, with greater activity for unphosphorylated HPr. The native effect is species-specific and is not transferred to all HPr/NPr homologs. This term is retained at the specificity supported for the measured activator role.",
                    [
                        sup(
                            "PMID:9334229",
                            "HPr binding increases GP activity to 250% of the level in control\nassays.",
                        )
                    ],
                )
            elif tid == "GO:0009401":
                a["review"] = review(
                    "ACCEPT",
                    "HPr carries phosphate between enzyme I and sugar-specific EIIA components.",
                    "The carbohydrate-PTS carrier directly performs a required phosphotransfer step. Native structural/biochemical work and the curated functional record support both the experimental and inherited assertions. The old isolation-paper cache is bibliographic-only; no unseen assay detail is inferred from its title.",
                    [sup(u), sup("PMID:11060015"), sup("PMID:8246840")],
                )
            elif tid == "GO:0016775":
                a["review"] = review(
                    "ACCEPT",
                    "The acceptor histidine nitrogen defines the phosphate-transfer chemistry of HPr.",
                    "HPr transfers its histidyl phosphate to the histidine acceptor of EIIA. This molecular-function genus is chemically appropriate and avoids incorrectly specifying ATP as the phosphate donor. The curated native PTS function and partner-complex structures substantiate the review annotation.",
                    [sup(u), sup("PMID:11060015")],
                )
            elif tid == "GO:0018106":
                a["review"] = review(
                    "ACCEPT",
                    "HPr directly phosphorylates histidine residues on partner EIIA proteins.",
                    "This is catalytic participation in histidyl phosphate transfer, rather than an annotation based only on HPr being phosphorylated. Native phosphotransfer-complex evidence independently supports the older experimental assignment even though its cached isolation-paper record has no accessible abstract.",
                    [sup("PMID:11060015"), sup("PMID:22673508"), sup(u)],
                )
            elif tid == "GO:0030234":
                a["review"] = review(
                    "MODIFY",
                    "The target study resolves activation of several metabolic enzymes and inhibition of adenylate kinase.",
                    "HPr activates PykF, PfkB and NagB, whereas phosphorylated HPr inhibits Adk. Refine the general enzyme-regulator term to both supported activity classes; choosing only one would erase the opposite phosphostate-dependent effect. These directions are not automatically assigned to NPr paralogs.",
                    [sup("PMID:28634232")],
                    [
                        term("GO:0008047", "enzyme activator activity"),
                        term("GO:0019210", "kinase inhibitor activity"),
                    ],
                )
            elif tid == "GO:0043609":
                a["review"] = review(
                    "ACCEPT",
                    "HPr couples available PTS phosphate flux to carbon utilization.",
                    "Retain the curated experimental assignment. The accessible single-cell study supports competition between sugar-uptake systems but does not expose every target-specific perturbation; independent HPr biochemical evidence establishes its native phosphate-distribution and metabolic-regulator roles. No detailed unseen HPr assay is claimed.",
                    [sup("PMID:26784570"), sup("PMID:28634232"), sup(u)],
                )
            elif tid == "GO:0045152":
                a["review"] = review(
                    "ACCEPT",
                    "Dephosphorylated HPr binds the antisigma factor Rsd.",
                    "Native binding and transcription experiments show that HPr interferes with Rsd-sigma70 complex formation. This specific binding term captures an established regulatory partner class, unlike uninformative generic protein binding.",
                    [
                        sup(
                            "PMID:24324139",
                            "Only the dephosphorylated form of HPr formed a tight complex with\nRsd",
                        )
                    ],
                )
            elif tid == "GO:0045819":
                a["review"] = review(
                    "ACCEPT",
                    "Allosteric activation of glycogen phosphorylase promotes glycogen breakdown.",
                    "HPr itself performs the regulatory step through direct binding and activation of the native catabolic enzyme. This is an experimentally grounded regulatory process, not a NEW pathway annotation inferred from a growth phenotype.",
                    [sup("PMID:9334229")],
                )
            else:
                raise ValueError(tid)
    d["references"].append(
        {
            "id": u,
            "title": f"UniProtKB {d['id']}: Escherichia coli {gene}",
            "findings": [
                {
                    "statement": "The curated native carbohydrate-PTS function and soluble location support the annotation synthesis; family membership alone does not establish a nitrogen-regulatory relay."
                }
            ],
        }
    )
    if gene == "ptsI":
        # This independent physiological source is already available from the control panel.
        for id in ["26784570"]:
            if not any(r["id"] == "PMID:" + id for r in d["references"]):
                meta = yaml.safe_load(
                    (w / f"publications/PMID_{id}.md").read_text().split("---", 2)[1]
                )
                d["references"].append(
                    {
                        "id": "PMID:" + id,
                        "title": meta["title"],
                        "findings": [
                            {
                                "statement": "Single-cell experiments examine competition between N-acetylglucosamine and sorbitol utilization; this supports physiological PTS context, not direct EI substrate specificity."
                            }
                        ],
                    }
                )
        d["description"] = (
            "PtsI is the general enzyme I of the Escherichia coli carbohydrate phosphotransferase system. The soluble homodimer uses phosphoenolpyruvate to phosphorylate HPr through a histidyl intermediate, supplying phosphate to sugar-specific transport systems. TmaR-dependent polar sequestration modulates the availability of active enzyme I."
        )
        d["core_functions"] = [
            {
                "description": "Initiates carbohydrate-PTS phosphate flow by transferring phosphate from PEP through His189 to HPr; the enzyme acts as a homodimer.",
                "molecular_function": term(
                    "GO:0008965",
                    "phosphoenolpyruvate-protein phosphotransferase activity",
                ),
                "directly_involved_in": [
                    term(
                        "GO:0009401",
                        "phosphoenolpyruvate-dependent sugar phosphotransferase system",
                    )
                ],
                "locations": [term("GO:0005829", "cytosol")],
                "supported_by": [sup("PMID:12705838"), sup("PMID:17053069")],
            }
        ]
        focus = "P08839 belongs to PTHR46244:SF6 alongside alpha-lineage PtsP candidates. Its proven native role is carbohydrate EI, so SF6 alone cannot grant the nitrogen-relay entry role. Curated UniProt also records less-efficient phosphorylation of NPr in vitro (PMID:7876255); this is biochemical cross-talk and does not prove a native canonical PtsP relay. Polar localization is regulation of a soluble enzyme, not evidence for a membrane transporter."
    else:
        d["description"] = (
            "HPr is a soluble phosphocarrier in the Escherichia coli carbohydrate phosphotransferase system, relaying phosphate from enzyme I to sugar-specific EIIA proteins. Its phosphorylation state also controls interactions with metabolic enzymes, the AI-2 kinase LsrK and the antisigma factor Rsd, linking carbohydrate supply to enzyme activity and transcription."
        )
        d["core_functions"] = [
            {
                "description": "Transfers histidyl phosphate from enzyme I to EIIA proteins of carbohydrate transport systems.",
                "molecular_function": term(
                    "GO:0016775",
                    "phosphotransferase activity, nitrogenous group as acceptor",
                ),
                "directly_involved_in": [
                    term(
                        "GO:0009401",
                        "phosphoenolpyruvate-dependent sugar phosphotransferase system",
                    ),
                    term("GO:0018106", "peptidyl-histidine phosphorylation"),
                ],
                "locations": [term("GO:0005829", "cytosol")],
                "supported_by": [sup("PMID:11060015"), sup(u)],
            },
            {
                "description": "Allosterically activates native carbohydrate-metabolizing enzymes, including glycogen phosphorylase; partner and phosphorylation state determine the effect.",
                "molecular_function": term("GO:0008047", "enzyme activator activity"),
                "directly_involved_in": [
                    term(
                        "GO:0045819",
                        "positive regulation of glycogen catabolic process",
                    )
                ],
                "locations": [term("GO:0005829", "cytosol")],
                "supported_by": [sup("PMID:9334229"), sup("PMID:28634232")],
            },
            {
                "description": "Inhibits LsrK through direct association; phosphorylated HPr also inhibits Adk. These kinase targets respond differently to HPr phosphorylation and are not assigned a universal phosphostate rule.",
                "molecular_function": term("GO:0019210", "kinase inhibitor activity"),
                "locations": [term("GO:0005829", "cytosol")],
                "supported_by": [sup("PMID:29868643"), sup("PMID:28634232")],
            },
            {
                "description": "Dephosphorylated HPr binds Rsd and antagonizes its antisigma activity, thereby modulating sigma70-dependent transcription.",
                "molecular_function": term("GO:0045152", "antisigma factor binding"),
                "locations": [term("GO:0005829", "cytosol")],
                "supported_by": [sup("PMID:24324139")],
            },
        ]
        focus = "P0AA04 is the canonical carbohydrate HPr comparator in PTHR33705:SF1. It is not the same-SF2 counterexample; Bacillus HPr provides that test. A complete functional review preserves its phosphostate-dependent enzyme-regulatory and Rsd-binding activities rather than reducing the protein to a negative nitrogen-relay example. No universal output or phosphorylation-direction claim is transferred to NPr paralogs."
    d["status"] = "DRAFT"
    assert original == [
        {k: v for k, v in a.items() if k != "review"} for a in d["existing_annotations"]
    ]
    p.write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100))
    (p.parent / f"{gene}-notes.md").write_text(
        f"# Escherichia coli {gene} review notes\n\n## 2026-11-07\n\n{focus}\n\nAll {len(original)} original machine annotation payloads, qualifiers and supporting entities remain in order. Only their review sections are changed, with no NEW rows. Generic protein-binding removals follow the repository exception and do not deny experimentally observed interactions. Broad terms are refined to the specific supported descendants; precise but substrate-specific context is treated separately from the general catalytic activity.\n\nPrimary evidence was inspected in the canonical publication caches. Accessible abstracts constrain detailed assay claims: bibliographic-only PMID:5545082 is not treated as a newly inspected experiment, and complexomic abstracts do not identify every protein in their supplementary results. Existing experimental curators are not overruled on that basis. Native biochemical and structural results independently ground the major functions.\n\nCurrent official GO definitions were checked for authored activities. The shared Falcon module-research request failed HTTP403 authentication; direct evidence assessment was used and no provider report was fabricated. Full corpus and module-level validation remain separate integration gates.\n"
    )
    (c / f"ECOLI-{gene}-preservation.json").write_text(
        json.dumps(
            {
                "original_rows": len(original),
                "current_rows": len(d["existing_annotations"]),
                "new_rows": 0,
                "ordered_payloads_unchanged": True,
                "raw_files": {
                    str(f.relative_to(w)): hashlib.sha256(f.read_bytes()).hexdigest()
                    for f in p.parent.glob("*")
                    if f.name.endswith(("-uniprot.txt", "-goa.tsv"))
                },
            },
            indent=2,
        )
        + "\n"
    )
    print(gene, len(original), "rows reviewed", flush=True)
