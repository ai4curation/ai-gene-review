"""Apply manually adjudicated reviews while retaining every seeded annotation payload."""

from pathlib import Path
import copy
import json
import yaml

A = Path(__file__).resolve().parent
ROOT = A.parents[3]
BASE = json.loads((A / "baseline.json").read_text())
REL = str(A.relative_to(ROOT))
PRE = str(A.parent.relative_to(ROOT) / "preflight")
terms = {
    x["id"]: x["name"] for x in json.loads((A / "go-terms.json").read_text())["results"]
}


def term(id):
    return {"id": id, "label": terms[id]}


def support(ref, quote=None):
    item = {"reference_id": ref}
    if quote:
        item["supporting_text"] = quote
    return item


def pub(n, finding, quote=None, notes=None):
    text = (ROOT / f"publications/PMID_{n}.md").read_text()
    metadata = yaml.safe_load(text.split("---", 2)[1])
    f = {"statement": finding}
    if quote:
        assert quote in text, (n, quote)
        f["supporting_text"] = quote
    return {
        "id": f"PMID:{n}",
        "title": metadata["title"],
        "findings": [f],
        "reference_review": {
            "relevance": "HIGH",
            "correctness": "VERIFIED",
            "review_notes": notes or finding,
        },
    }


def core(desc, mf=None, contribution=False, location=None, refs=(), binding=False):
    c = {"description": desc, "supported_by": list(refs)}
    if mf:
        c["molecular_function"] = term(mf)
    if contribution:
        c["contributes_to_molecular_function"] = term("GO:0120014")
    c["directly_involved_in"] = [term("GO:0120010")]
    if location:
        c["locations"] = [term(location)]
    return c


bridge = (
    "PMID36518166 identifies BP3757–BP3761 as the MlaF/E/D/A/C locus in the Tohama I reference. "
    "The native experiments used B213, a streptomycin-resistant Tohama I derivative identified in Supplementary TableS1; "
    "complete experimental B213 protein sequences were not independently compared. "
    "Only MlaF was directly perturbed in this operon, and the clearest surface-PE defect involves combined mlaF/pldA loss. "
    "The source therefore supports a lineage-qualified Mla pathway, not five separate target assays or a measured native transport direction."
)
quote365 = "All mla genes found are adjacent to each other and probably form an operon"
quote348 = "We reveal that MlaC spontaneously transfers PLs to the IM transporter in an MlaD-dependent manner that can be further enhanced by coupled ATP hydrolysis."
quote283 = "MlaD, PqiB, and YebT each bound phospholipid species"
quote338 = "one cardiolipin"

for seed in BASE["seeds"]:
    org, g = seed["organism"], seed["gene"]
    path = ROOT / seed["review"]
    d = yaml.safe_load(path.read_text())
    d["status"] = "COMPLETE"
    rows = copy.deepcopy(seed.get("rows", []))
    up = f"file:{org}/{g}/{g}-uniprot.txt"
    ev = f"file:{REL}/evidence.md"
    refs = copy.deepcopy(
        [r for r in d.get("references", []) if r["id"].startswith("GO_REF:")]
    )
    for ref in refs:
        ref["reference_review"] = {
            "relevance": "HIGH",
            "correctness": "VERIFIED",
            "review_notes": "Annotation provenance identifies the mapping method, not an independent target assay. The biological assertion is evaluated using the protein classification, source-qualified primary evidence and target context below.",
        }
    refs.append(
        {
            "id": up,
            "title": f"UniProt record for {org} {g} ({d['id']})",
            "findings": [
                {
                    "statement": "Official accession, reference strain, sequence and independently identified protein-family signatures provide the target identity and classification. Unreviewed automatic functional prose is not treated as direct experimental evidence."
                }
            ],
            "reference_review": {
                "relevance": "HIGH",
                "correctness": "VERIFIED",
                "review_notes": "Used for accession/sequence and curated classification or signature evidence; ARBA and ProtNLM labels alone are not functional proof.",
            },
        }
    )
    refs.append(
        {
            "id": ev,
            "title": "Mla new-member source scope and identity assessment",
            "findings": [
                {
                    "statement": "Separates assay organisms, exact deposited mature-sequence matches, conserved-function inference and experimental limitations."
                }
            ],
            "reference_review": {
                "relevance": "HIGH",
                "correctness": "VERIFIED",
                "review_notes": "Manual analysis links the frozen official identity bridge and primary sources, with reproducible deposited-sequence checks.",
            },
        }
    )
    if org == "BORPE":
        refs.append(pub(36518166, bridge, quote365))
        common = [support("PMID:36518166", quote365), support(up), support(ev)]
        refs.append(
            pub(
                34873038,
                "Purified E. coli MlaC/MlaFEDB shows spontaneous exchange with ATP-enhanced retrograde movement. This is ortholog mechanism evidence, not a Bordetella directional reconstitution.",
                quote348,
            )
        )
        if g == "BP3757":
            d["description"] = (
                "BP3757 is the MlaF-family ATPase of the Bordetella pertussis Mla phospholipid-transport system. Its conserved nucleotide-binding domain supplies ATP-dependent energy to the inner-membrane MlaFED complex, supporting outer-membrane lipid asymmetry. Bordetella lacks an identifiable MlaB homolog; MlaF-associated envelope and growth phenotypes depend on physiological conditions."
            )
            d["core_functions"] = [
                core(
                    "ATP hydrolysis energizes the MlaFED phospholipid-transfer machinery. Catalytic activity is inferred from the ABC ATPase domain, conserved MlaF classification and related-system biochemistry; B213 genetics supports pathway participation, not a purified BP3757 turnover measurement.",
                    "GO:0016887",
                    True,
                    refs=common + [support("PMID:34873038", quote348)],
                )
            ]
            decisions = {
                "GO:0000166": (
                    "MODIFY",
                    "Nucleotide binding is correct but can be refined to ATP binding, already present as a separate source row. The PROSITE ABC transporter domain and ATP-binding site45–52 support the specific nucleotide; no new annotation row is required.",
                    "GO:0005524",
                ),
                "GO:0005524": (
                    "ACCEPT",
                    "ATP binding is integral to the conserved MlaF catalytic role. The target has an ABC transporter domain and PROSITE-supported ATP-binding site45–52; native B213 MlaF genetics identifies the pathway context. This is conserved-function inference, not a target nucleotide-affinity assay.",
                    None,
                ),
                "GO:0016887": (
                    "ACCEPT",
                    "ABC ATPase signatures and specific MlaF classification support ATP hydrolysis. The B213 MlaF phenotype and ATP-dependent transfer measured for E. coli establish compatible pathway and mechanistic context, while target-specific ATPase kinetics remain unmeasured.",
                    None,
                ),
            }
        elif g == "BP3758":
            d["description"] = (
                "BP3758 is the MlaE-family integral inner-membrane component of the Bordetella pertussis Mla system. It provides the membrane interface for phospholipid handling by the MlaFED ABC complex, coupled to the MlaF ATPase and periplasm-facing MlaD. Its role is inferred from conserved MlaE architecture and the native Mla locus; an identifiable MlaB subunit is absent in this lineage."
            )
            d["core_functions"] = [
                core(
                    "Contributes the membrane component of MlaFED-mediated phospholipid transfer. MlaE signatures, multiple membrane-spanning segments and the native operon support this conserved role; isolated BP3758 transport and an exact Bordetella complex stoichiometry have not been measured.",
                    contribution=True,
                    location="GO:0005886",
                    refs=common + [support("PMID:34873038", quote348)],
                )
            ]
            d["core_functions"][0]["in_complex"] = term("GO:0043190")
            decisions = {
                "GO:0005886": (
                    "ACCEPT",
                    "The conserved MlaE permease classification, RuleBase-supported multipass topology and placement in the inner-membrane MlaFED machinery support plasma-membrane localization. Native BP3758 localization was not independently fractionated; the assertion is a compatible topology/function inference.",
                    None,
                ),
                "GO:0015914": (
                    "MODIFY",
                    "The transport assertion is supported but the conserved Mla pathway is specifically intermembrane phospholipid transfer. MlaE supplies the membrane component of the active complex, rather than independently carrying lipid through the periplasm. This refinement is inferred from target classification/locus and characterized ortholog mechanism, without asserting a target flux assay.",
                    "GO:0120010",
                ),
                "GO:0043190": (
                    "ACCEPT",
                    "Specific MlaE signatures and the adjacent MlaF/MlaD locus support membership in an ABC transporter complex. Lack of an identifiable Bordetella MlaB does not negate ABC membership: the membrane and ATPase domains remain. The automatic UniProt MlaFEDB stoichiometry is not transferred to this lineage.",
                    None,
                ),
            }
        elif g == "BP3759":
            refs.append(
                pub(
                    28388411,
                    "Purified E. coli MlaD directly binds phospholipids and forms a membrane-associated MCE assembly. The MlaC interaction experiments measure binding; discussion transfer models are not treated as direct transfer assays.",
                    quote283,
                )
            )
            d["description"] = (
                "BP3759 is the MlaD-family MCE component of the Bordetella pertussis Mla system. Its periplasm-facing domain is predicted to bind phospholipids and participate in the handoff between the soluble MlaC carrier and the inner-membrane MlaEF machinery. The protein has an N-terminal hydrophobic anchor and a conserved MlaD domain; its assembly and transport role are inferred from the native locus and characterized homologs."
            )
            d["core_functions"] = [
                core(
                    "Phospholipid binding by the MlaD domain contributes to lipid transfer at the MlaFED periplasmic interface. Target MlaD-specific signatures and operon context support the inference; purified target binding, oligomeric stoichiometry and transfer kinetics remain unmeasured.",
                    "GO:0005543",
                    True,
                    "GO:0005886",
                    common
                    + [
                        support("PMID:28388411", quote283),
                        support("PMID:34873038", quote348),
                    ],
                )
            ]
            d["core_functions"][0]["in_complex"] = term("GO:0043190")
            decisions = {
                "GO:0005543": (
                    "ACCEPT",
                    "Specific MlaD classification (TIGR04430, PF02470 and PTHR33371:SF4), MCE-domain architecture and the native Mla locus support conserved phospholipid binding. This agrees with direct lipid binding by characterized E. coli MlaD; it is not a direct BP3759 binding measurement and does not assume all MCE proteins have identical substrates.",
                    None,
                ),
                "GO:0015914": (
                    "MODIFY",
                    "The target is the MlaD component of an intermembrane phospholipid pathway, allowing refinement to intermembrane phospholipid transfer. It contributes lipid-binding/interface work to the transport machinery; conserved-function inference is grounded in the specific MlaD domain and cognate locus, not generic MCE membership alone.",
                    "GO:0120010",
                ),
            }
        elif g == "BP3760":
            refs.append(
                pub(
                    40168124,
                    "An E. coli porin–MlaA complex directly promotes MlaC lipid loading. This supports the conserved outer-membrane interface mechanism, without identifying the Bordetella porin partner or proving native target flux.",
                    "significant enrichment of PG over PE",
                )
            )
            d["description"] = (
                "BP3760 is an MlaA-family lipoprotein of Bordetella pertussis. It is predicted to act at the outer membrane, helping transfer misplaced phospholipids to the periplasmic MlaC carrier for return through the Mla system. Its MlaA domain and lipoprotein signal support this role, while the cognate porin partner and target-specific transfer kinetics remain unresolved."
            )
            d["core_functions"] = [
                core(
                    "Contributes the outer-membrane lipid extraction/loading interface of the Mla pathway. Specific MlaA architecture, a lipidated signal-peptide cleavage product and the cognate Mla locus support this role; the exact Bordetella porin partner and native direction were not measured.",
                    contribution=True,
                    location="GO:0009279",
                    refs=common
                    + [
                        support("PMID:40168124", "significant enrichment of PG over PE")
                    ],
                )
            ]
            decisions = {
                "GO:0016020": (
                    "MODIFY",
                    "The membrane assertion can be refined to cell outer membrane by the combination of the MlaA-specific family/domain, lipoprotein signal and native Mla pathway context. A signal peptide alone would not identify which membrane; the conserved MlaA role supplies the additional localization evidence. Target fractionation was not performed.",
                    "GO:0009279",
                ),
                "GO:0120010": (
                    "ACCEPT",
                    "The MlaA-specific classification and cognate operon support participation in intermembrane phospholipid transfer as the outer-membrane loading interface. Ortholog assays show actual MlaA-assisted carrier loading. This target-level inference does not claim independent whole-pathway activity, a proven Bordetella porin partner or a B213 directional transport measurement.",
                    None,
                ),
            }
        else:
            refs.append(
                {
                    "id": f"file:{REL}/bp3761-structure-proof.json",
                    "title": "Official PDB11HY/11IF target sequence and phospholipid-ligand verification",
                    "findings": [
                        {
                            "statement": "Both deposited constructs contain an exact 181-residue match to Q7VSZ6 residues27–207, preceded by MAHHHHHH, and a PEF phosphatidylethanolamine ligand."
                        }
                    ],
                    "reference_review": {
                        "relevance": "HIGH",
                        "correctness": "VERIFIED",
                        "review_notes": "Official RCSB entry, entity and ligand JSONs are archived alongside the reproducible sequence proof. Deposited crystallography is direct binding evidence, not native flux or a peer-reviewed kinetic assay.",
                    },
                }
            )
            direct = support(f"file:{REL}/bp3761-structure-proof.json")
            d["description"] = (
                "BP3761 is the soluble MlaC-family phospholipid carrier of Bordetella pertussis. Its signal peptide directs export to the periplasm, where the carrier is inferred to shuttle lipid between the outer-membrane MlaA interface and inner-membrane MlaFED machinery. Deposited structures of its mature sequence contain bound phosphatidylethanolamine, directly supporting lipid binding; native transfer direction and loading stoichiometry remain unresolved."
            )
            d["core_functions"] = [
                core(
                    "Binds phospholipid in the mature MlaC carrier. Deposited recombinant structures11HY and11IF contain phosphatidylethanolamine and an exact match to Q7VSZ6 residues27–207; native lipid specificity and occupancy are not determined by those structures.",
                    "GO:0005543",
                    location="GO:0030288",
                    refs=common + [direct],
                ),
                core(
                    "Carries phospholipid through the aqueous periplasm between cognate Mla interfaces. The specific MlaC family, cleaved export signal, native locus and lipid-bound mature target structure support this conserved carrier function; no purified BP3761 transfer or native net-flux assay was read.",
                    "GO:0120014",
                    location="GO:0030288",
                    refs=common + [direct, support("PMID:34873038", quote348)],
                ),
            ]
            decisions = {}
    else:
        refs.append(
            pub(
                33837253,
                "The exact PAO1 Ttg2D sequence is characterized structurally and by native/denaturing mass spectrometry. The homologously expressed His-tagged protein was purified from the PAO1 periplasm, and its cargo includes two diacyl phospholipids or one cardiolipin. Heterologous crystallography is distinguished from that native-host preparation; the complete pathway direction and drug transport are not measured.",
                quote338,
            )
        )
        refs.append(
            pub(
                34873038,
                "E. coli carrier-to-complex transfer provides the related Mla mechanism; it does not itself demonstrate PAO1 whole-pathway direction.",
                quote348,
            )
        )
        d["description"] = (
            "Ttg2D is a soluble periplasmic phospholipid carrier in the Pseudomonas aeruginosa PAO1 Ttg2/Mla envelope-lipid system. Its large hydrophobic cavity accommodates two diacyl glycerophospholipids or one cardiolipin. The carrier is inferred to shuttle lipid between membrane-associated partners and supports envelope barrier function; effects on antibiotic susceptibility do not imply direct antibiotic export."
        )
        direct = [support("PMID:33837253", quote338), support(up), support(ev)]
        d["core_functions"] = [
            core(
                "Binds glycerophospholipid cargo in a cavity accommodating four acyl chains. Target crystallography and mass spectrometry directly establish lipid binding, including native-host periplasmic cargo; purified binding/reloading does not determine whole-pathway direction.",
                "GO:0005543",
                location="GO:0030288",
                refs=direct,
            ),
            core(
                "Shuttles phospholipid through the periplasm as the Ttg2/Mla soluble carrier. Direct target cargo binding/reloading, periplasmic recovery and specific carrier architecture support the mechanistic assignment, although donor-to-acceptor membrane transfer and net native PAO1 flux were not directly resolved.",
                "GO:0120014",
                location="GO:0030288",
                refs=direct + [support("PMID:34873038", quote348)],
            ),
        ]
        decisions = {}
    for row in rows:
        go = row["term"]["id"]
        action, reason, replacement = decisions[go]
        supporting = [support(up), support(ev)]
        if org == "BORPE":
            supporting.append(support("PMID:36518166", quote365))
        if g == "BP3757":
            supporting.append(support("PMID:34873038", quote348))
        elif g == "BP3759":
            supporting.append(support("PMID:28388411", quote283))
        elif g == "BP3760":
            supporting.append(
                support("PMID:40168124", "significant enrichment of PG over PE")
            )
        row["review"] = {
            "summary": f"{row['term']['label']} evaluated against target classification and source-qualified Mla biology.",
            "action": action,
            "reason": reason,
            "supported_by": supporting,
        }
        if replacement:
            row["review"]["proposed_replacement_terms"] = [term(replacement)]
    if rows:
        d["existing_annotations"] = rows
    d["references"] = refs
    d["suggested_questions"] = [
        {
            "question": "What are the native compatible membrane-interface partners and net phospholipid flux under the relevant growth conditions?"
        }
    ]
    path.write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100))
    notes = f"""# {org} {g} annotation review\n\n2026-11-07. Complete manual review of {len(rows)} seeded rows; source payload/order/qualifiers preserved. No NEW rows were added, including for zero-row proteins. Core functions independently synthesize the supported biology.\n\n{d["description"]}\n\n"""
    if org == "BORPE":
        notes += (
            bridge
            + "\n\nThe standard E. coli MlaFEDB composition is not imported into Bordetella: PMID36518166 found no identifiable MlaB homolog. In particular, the automatic MlaFEDB stoichiometry in BP3758 UniProt is not target-specific support.\n\n"
        )
    for c in d["core_functions"]:
        notes += c["description"] + "\n\n"
    notes += f"""Sources and identity proof: `{REL}/evidence.md`, frozen `preflight/identity-proof.json`, current immutable UniProt record and the cited primary full texts. Official GO definitions were checked in `go-terms.json`.\n\nA genuine `just deep-research {org} {g} --provider falcon` attempt failed with403 authentication/access error. The exact failed attempt is archived in this consultation; no provider report was invented. Manual review proceeded from primary evidence.\n\nPAINT-losses was run. Bordetella targets are absent from the cached reference trees, so the report cannot establish absence of ancestral loss; no imaginary target placement or loss node is asserted. PAO1 Ttg2D reports no applicable loss. Two first attempts raced the shared IBD download and were rerun sequentially after completion, with both attempts retained. TreeGrafter row nodes identify source ancestry, not donor-count or self-citation defects.\n\nNo universal essentiality, exact native stoichiometry, antibiotic transport or assay-derived native directional flux is inferred from growth/permeability phenotypes. See core descriptions for measured binding versus inferred transfer.\n"""
    (path.parent / f"{g}-notes.md").write_text(notes)
print("Curated six reviews; all original rows preserved, no NEW.")
