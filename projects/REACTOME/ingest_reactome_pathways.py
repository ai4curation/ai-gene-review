from __future__ import annotations

import argparse
from collections import defaultdict, deque
from pathlib import Path
from typing import Any, Iterable

import requests
import yaml


REACTOME_BASE = "https://reactome.org/ContentService"
REACTION_LIKE = {
    "BlackBoxEvent",
    "Depolymerisation",
    "Polymerisation",
    "Reaction",
    "ReactionLikeEvent",
}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data: Any) -> bool:
        return True


def clean(value: Any) -> str:
    return " ".join(str(value or "").split())


def error_summary(error: BaseException) -> str:
    return clean(f"{type(error).__name__}: {error}")


def stable_sort(values: Iterable[str]) -> list[str]:
    return sorted({value for value in values if value})


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def drop_empty(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: cleaned
            for key, child in value.items()
            if (cleaned := drop_empty(child)) not in (None, "", [], {})
        }
    if isinstance(value, list):
        return [
            cleaned
            for child in value
            if (cleaned := drop_empty(child)) not in (None, "", [], {})
        ]
    return value


def write_yaml(path: Path, value: dict[str, Any], prune_empty: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    emitted = drop_empty(value) if prune_empty else value
    path.write_text(
        yaml.dump(
            emitted,
            Dumper=NoAliasDumper,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
            width=1000,
        ),
        encoding="utf-8",
    )


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.CSafeLoader) or {}


def markdown_table(headers: list[str], rows: Iterable[Iterable[str | int]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append(
            "| " + " | ".join(str(value).replace("|", "\\|") for value in row) + " |"
        )
    return "\n".join(lines)


def source_reactome_id(value: Any) -> str | None:
    if isinstance(value, str) and value.startswith("Reactome:R-"):
        return value.split(":", 1)[1]
    return None


def term_id(value: Any) -> str:
    if isinstance(value, dict) and isinstance(value.get("term"), dict):
        return str(value["term"].get("id") or "")
    return ""


def term_label(value: Any) -> str:
    if isinstance(value, dict) and isinstance(value.get("term"), dict):
        return clean(value["term"].get("label"))
    return ""


def uniprot_terms(value: Any) -> Iterable[tuple[str, str]]:
    if isinstance(value, dict):
        term = value.get("term")
        if isinstance(term, dict):
            term_id_value = str(term.get("id") or "")
            if term_id_value.startswith("UniProtKB:"):
                yield term_id_value, clean(term.get("label"))
        for child in value.values():
            yield from uniprot_terms(child)
    elif isinstance(value, list):
        for child in value:
            yield from uniprot_terms(child)


def module_source_scope(context: dict[str, str]) -> str:
    if context.get("annoton_id"):
        return "activity_evidence"
    if context.get("node_id"):
        return "node_evidence"
    return "module_evidence"


def iter_module_reactome_sources(
    value: Any, context: dict[str, str]
) -> Iterable[dict[str, str]]:
    if isinstance(value, list):
        for child in value:
            yield from iter_module_reactome_sources(child, context)
        return

    if not isinstance(value, dict):
        return

    reactome_id = source_reactome_id(value.get("source_id"))
    if reactome_id:
        yield {
            **context,
            "reactome_id": reactome_id,
            "scope": module_source_scope(context),
            "statement": clean(value.get("statement")),
        }

    annoton_context = context
    if "function" in value and ("participant" in value or "role_description" in value):
        participant_terms = sorted(set(uniprot_terms(value.get("participant") or {})))
        annoton_context = {
            **context,
            "annoton_id": str(value.get("id") or ""),
            "annoton_label": clean(value.get("label")),
            "function_id": term_id(value.get("function")),
            "function_label": term_label(value.get("function")),
            "participant_ids": sorted(term_id for term_id, _ in participant_terms),
        }

    for key, child in value.items():
        child_context = annoton_context
        if key == "node" and isinstance(child, dict):
            child_context = {
                **annoton_context,
                "node_id": str(child.get("id") or ""),
                "node_label": clean(child.get("label")),
                "node_type": str(child.get("module_type") or ""),
            }
        yield from iter_module_reactome_sources(child, child_context)


def load_module_sources(root: Path, module_id: str) -> list[dict[str, str]]:
    path = root / "modules" / f"{module_id}.yaml"
    doc = load_yaml(path)
    module = doc.get("module") or {}
    context = {
        "module": str(module.get("id") or module_id),
        "module_path": path.relative_to(root).as_posix(),
        "node_id": "",
        "node_label": "",
        "node_type": "",
        "annoton_id": "",
        "annoton_label": "",
        "function_id": "",
        "function_label": "",
        "participant_ids": [],
    }
    return sorted(
        iter_module_reactome_sources(doc, context),
        key=lambda row: (
            row["scope"],
            row["reactome_id"],
            row["node_id"],
            row["annoton_id"],
        ),
    )


def ref_to_external_id(ref: dict[str, Any]) -> str | None:
    st_id = str(ref.get("stId") or "")
    if st_id.startswith("uniprot:"):
        return f"UniProtKB:{st_id.split(':', 1)[1]}"
    if st_id.startswith("chebi:"):
        return f"CHEBI:{st_id.split(':', 1)[1]}"

    database = str(ref.get("databaseName") or "").upper()
    identifier = str(ref.get("identifier") or "")
    if database == "RHEA" and identifier:
        return f"RHEA:{identifier}"
    if database in {"GO", "GENE ONTOLOGY"} and identifier:
        return f"GO:{identifier}"
    return None


class ReactomeClient:
    def __init__(self, base_url: str = REACTOME_BASE, timeout: float = 30.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self._json_cache: dict[str, Any] = {}

    def get_text(self, path: str) -> str:
        url = f"{self.base_url}/{path.lstrip('/')}"
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.text

    def get_json(self, path: str) -> Any:
        if path not in self._json_cache:
            url = f"{self.base_url}/{path.lstrip('/')}"
            response = self.session.get(
                url, headers={"Accept": "application/json"}, timeout=self.timeout
            )
            response.raise_for_status()
            self._json_cache[path] = response.json()
        return self._json_cache[path]

    def database_version(self) -> str:
        return clean(self.get_text("data/database/version"))

    def query(self, identifier: str | int) -> dict[str, Any]:
        return self.get_json(f"data/query/{identifier}")

    def participants(self, stable_id: str) -> list[dict[str, Any]]:
        return self.get_json(f"data/participants/{stable_id}")


def go_term(value: dict[str, Any]) -> dict[str, str]:
    accession = str(value.get("accession") or "")
    return {
        "id": f"GO:{accession}"
        if accession and not accession.startswith("GO:")
        else accession,
        "label": clean(value.get("displayName") or value.get("name")),
    }


def simple_event_ref(value: Any) -> str:
    if isinstance(value, dict):
        return str(value.get("stId") or value.get("dbId") or "")
    return str(value)


def participant_ref_index(
    participants: list[dict[str, Any]],
) -> dict[int, list[dict[str, Any]]]:
    return {
        int(participant["peDbId"]): as_list(participant.get("refEntities"))
        for participant in participants
        if participant.get("peDbId") is not None
    }


def normalize_physical_entity(
    value: dict[str, Any],
    client: ReactomeClient,
    reference_entities: dict[int, list[dict[str, Any]]],
) -> dict[str, Any]:
    if not isinstance(value, dict):
        value = client.query(value)

    db_id = int(value["dbId"])
    xrefs = sorted(
        {
            xref
            for ref in reference_entities.get(db_id, [])
            if (xref := ref_to_external_id(ref))
        }
    )
    return {
        "reactome_db_id": db_id,
        "stable_id": str(value.get("stId") or ""),
        "display_name": clean(value.get("displayName")),
        "schema_class": str(value.get("schemaClass") or ""),
        "xrefs": xrefs,
    }


def normalize_database_identifier(value: dict[str, Any]) -> str:
    database = str(value.get("databaseName") or "").upper()
    identifier = str(value.get("identifier") or "")
    if database and identifier:
        return f"{database}:{identifier}"
    return clean(value.get("displayName"))


def normalize_literature_reference(value: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(value, dict):
        return {}
    return {
        "pmid": value.get("pubMedIdentifier"),
        "title": clean(value.get("title") or value.get("displayName")),
        "year": value.get("year"),
    }


def normalize_catalyst(
    value: dict[str, Any] | int,
    client: ReactomeClient,
    reference_entities: dict[int, list[dict[str, Any]]],
) -> dict[str, Any]:
    catalyst_id = value["dbId"] if isinstance(value, dict) else value
    catalyst = client.query(int(catalyst_id))
    activity = catalyst.get("activity") or {}
    physical_entity = catalyst.get("physicalEntity") or {}
    members = []
    if physical_entity.get("dbId") is not None:
        members = sorted(
            {
                xref
                for ref in reference_entities.get(int(physical_entity["dbId"]), [])
                if (xref := ref_to_external_id(ref)) and xref.startswith("UniProtKB:")
            }
        )

    return {
        "reactome_db_id": catalyst.get("dbId"),
        "display_name": clean(catalyst.get("displayName")),
        "activity": go_term(activity) if activity else {},
        "physical_entity": {
            "reactome_db_id": physical_entity.get("dbId"),
            "stable_id": physical_entity.get("stId"),
            "schema_class": physical_entity.get("schemaClass"),
            "display_name": clean(physical_entity.get("displayName")),
            "members": members,
        },
    }


def normalize_event(
    event: dict[str, Any],
    client: ReactomeClient,
    include_participants: bool,
) -> dict[str, Any]:
    reference_entities = {}
    if include_participants and event.get("stId"):
        reference_entities = participant_ref_index(client.participants(event["stId"]))

    go_bp = event.get("goBiologicalProcess") or {}
    normalized = {
        "stable_id": event.get("stId"),
        "stable_id_version": event.get("stIdVersion"),
        "reactome_db_id": event.get("dbId"),
        "schema_class": event.get("schemaClass"),
        "display_name": clean(event.get("displayName")),
        "names": [clean(name) for name in event.get("name", [])],
        "species": event.get("speciesName"),
        "category": event.get("category"),
        "is_disease": event.get("isInDisease"),
        "is_inferred": event.get("isInferred"),
        "go_biological_process": go_term(go_bp) if go_bp else {},
        "compartments": [
            go_term(compartment) for compartment in as_list(event.get("compartment"))
        ],
        "cross_references": sorted(
            {
                xref
                for xref in (
                    normalize_database_identifier(ref)
                    for ref in as_list(event.get("crossReference"))
                )
                if xref
            }
        ),
        "literature": sorted(
            [
                normalize_literature_reference(ref)
                for ref in as_list(event.get("literatureReference"))
            ],
            key=lambda ref: (
                ref.get("pmid") or 0,
                ref.get("year") or 0,
                ref.get("title") or "",
            ),
        ),
    }

    if event.get("schemaClass") in REACTION_LIKE:
        normalized.update(
            {
                "inputs": [
                    normalize_physical_entity(entity, client, reference_entities)
                    for entity in as_list(event.get("input"))
                ],
                "outputs": [
                    normalize_physical_entity(entity, client, reference_entities)
                    for entity in as_list(event.get("output"))
                ],
                "catalysts": [
                    normalize_catalyst(catalyst, client, reference_entities)
                    for catalyst in as_list(event.get("catalystActivity"))
                ],
            }
        )

    return normalized


def event_uniprots(event: dict[str, Any]) -> list[str]:
    uniprots = []
    for catalyst in event.get("catalysts", []):
        physical_entity = catalyst.get("physical_entity") or {}
        uniprots.extend(physical_entity.get("members", []))
    return stable_sort(uniprots)


def activity_label(row: dict[str, Any]) -> str:
    return f"{row['node_id']}/{row['annoton_id']}"


def activity_key(row: dict[str, Any]) -> tuple[str, str, str]:
    return (row["node_id"], row["annoton_id"], row["reactome_id"])


def activity_participants(row: dict[str, Any]) -> set[str]:
    return set(row.get("participant_ids") or [])


def reaction_like_events(
    events: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    return {
        event_id: event
        for event_id, event in events.items()
        if event.get("schema_class") in REACTION_LIKE
    }


def collect_root_events(
    root_id: str,
    scope: str,
    include_events: list[str],
    client: ReactomeClient,
) -> tuple[dict[str, dict[str, Any]], dict[str, list[str]]]:
    queue: deque[str | int] = deque([root_id])
    if scope == "curated_slice":
        queue.extend(include_events)

    events: dict[str, dict[str, Any]] = {}
    hierarchy: dict[str, list[str]] = defaultdict(list)

    while queue:
        identifier = queue.popleft()
        event = client.query(identifier)
        stable_id = event.get("stId")
        if not stable_id or stable_id in events:
            continue

        events[stable_id] = event
        if event.get("schemaClass") != "Pathway":
            continue

        children = [simple_event_ref(child) for child in event.get("hasEvent", [])]
        if scope == "curated_slice" and stable_id == root_id:
            children = include_events
        elif scope == "curated_slice":
            children = []

        for child in children:
            if child:
                child_event = client.query(child)
                child_id = child_event["stId"]
                hierarchy[stable_id].append(child_id)
                queue.append(child_id)

    return events, {
        key: list(dict.fromkeys(values)) for key, values in hierarchy.items()
    }


def build_import(config: dict[str, Any], client: ReactomeClient) -> dict[str, Any]:
    events, hierarchy = collect_root_events(
        str(config["reactome_root"]),
        str(config["scope"]),
        [str(event_id) for event_id in config.get("include_events", [])],
        client,
    )
    normalized_events = {
        stable_id: normalize_event(
            events[stable_id],
            client,
            include_participants=events[stable_id].get("schemaClass") in REACTION_LIKE,
        )
        for stable_id in sorted(events)
    }

    return {
        "reactome": {
            "release": client.database_version(),
            "root": config["reactome_root"],
            "scope": config["scope"],
            "module": config["module"],
            "organism": config.get("organism"),
        },
        "hierarchy": {
            parent: sorted(set(children))
            for parent, children in sorted(hierarchy.items())
        },
        "events": normalized_events,
    }


def match_basis_for_source(row: dict[str, str], event: dict[str, Any]) -> list[str]:
    basis = ["cited_reactome_id"]
    module_participants = activity_participants(row)
    event_participants = set(event_uniprots(event))
    if module_participants and module_participants & event_participants:
        basis.append("executor_match")
    if row["function_id"] and any(
        row["function_id"] == (catalyst.get("activity") or {}).get("id")
        for catalyst in event.get("catalysts", [])
    ):
        basis.append("mf_match")
    return basis


def exact_match_verdict(row: dict[str, Any], event: dict[str, Any]) -> str:
    basis = set(match_basis_for_source(row, event))
    if "executor_match" not in basis:
        return "same_reaction_missing_executor"
    if row["function_id"] and "mf_match" not in basis:
        return "same_reaction_mf_unconfirmed"
    return "reaction_id_exact"


def reactome_only_verdict(
    event: dict[str, Any], candidate_module_activities: list[str]
) -> str:
    if event.get("schema_class") == "BlackBoxEvent":
        return "black_box_event"
    if candidate_module_activities:
        return "same_executor_different_reaction"
    if len(event_uniprots(event)) > 1:
        return "unmatched_family_event"
    return "reactome_only_event"


def same_executor_module_activities(
    event: dict[str, Any], activity_rows: list[dict[str, Any]]
) -> list[str]:
    event_participants = set(event_uniprots(event))
    return sorted(
        activity_label(row)
        for row in activity_rows
        if event_participants & activity_participants(row)
    )


def same_executor_reactome_events(
    row: dict[str, Any], reaction_events: dict[str, dict[str, Any]]
) -> list[str]:
    module_participants = activity_participants(row)
    return sorted(
        event_id
        for event_id, event in reaction_events.items()
        if module_participants & set(event_uniprots(event))
    )


def align_module(
    config: dict[str, Any],
    imported: dict[str, Any],
    module_sources: list[dict[str, str]],
) -> dict[str, Any]:
    events = imported.get("events", {})
    reaction_events = reaction_like_events(events)
    reaction_ids = set(reaction_events)
    activity_rows = [
        row for row in module_sources if row["scope"] == "activity_evidence"
    ]
    module_activity_ids = {row["reactome_id"] for row in activity_rows}
    rows_by_reactome: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in activity_rows:
        rows_by_reactome[row["reactome_id"]].append(row)

    matches = []
    for reactome_id in sorted(reaction_ids & module_activity_ids):
        event = events[reactome_id]
        for row in rows_by_reactome[reactome_id]:
            matches.append(
                {
                    "module_node": row["node_id"],
                    "module_annoton": row["annoton_id"],
                    "reactome_event": reactome_id,
                    "verdict": exact_match_verdict(row, event),
                    "match_basis": match_basis_for_source(row, event),
                }
            )

    reactome_only_events = []
    for reactome_id in sorted(reaction_ids - module_activity_ids):
        event = reaction_events[reactome_id]
        candidate_module_activities = same_executor_module_activities(
            event, activity_rows
        )
        reactome_only_events.append(
            {
                "reactome_event": reactome_id,
                "verdict": reactome_only_verdict(event, candidate_module_activities),
                "candidate_module_activities": candidate_module_activities,
            }
        )

    module_only_events = []
    for row in sorted(
        (row for row in activity_rows if row["reactome_id"] not in reaction_ids),
        key=activity_key,
    ):
        candidate_reactome_events = same_executor_reactome_events(row, reaction_events)
        module_only_events.append(
            {
                "module_node": row["node_id"],
                "module_annoton": row["annoton_id"],
                "reactome_event": row["reactome_id"],
                "verdict": (
                    "same_executor_different_reaction"
                    if candidate_reactome_events
                    else "module_only_event"
                ),
                "candidate_reactome_events": candidate_reactome_events,
            }
        )

    return {
        "module": config["module"],
        "reactome_root": config["reactome_root"],
        "scope": config["scope"],
        "matches": matches,
        "container_evidence": sorted(
            {
                row["reactome_id"]
                for row in module_sources
                if row["scope"] == "module_evidence"
            }
        ),
        "reactome_only_events": reactome_only_events,
        "module_only_events": module_only_events,
    }


def write_alignment_report(
    path: Path,
    config: dict[str, Any],
    imported: dict[str, Any],
    alignment: dict[str, Any],
    module_sources: list[dict[str, str]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    events = imported["events"]
    activity_rows = [
        row for row in module_sources if row["scope"] == "activity_evidence"
    ]
    rows_by_activity = {activity_key(row): row for row in activity_rows}

    exact_rows = []
    for match in alignment["matches"]:
        row = rows_by_activity[
            (
                match["module_node"],
                match["module_annoton"],
                match["reactome_event"],
            )
        ]
        event = events[match["reactome_event"]]
        exact_rows.append(
            [
                match["reactome_event"],
                match["verdict"],
                ", ".join(match["match_basis"]),
                row["node_id"],
                row["annoton_id"],
                row["function_id"] or row["function_label"],
                event.get("display_name", ""),
            ]
        )

    reactome_only_rows = [
        [
            gap["reactome_event"],
            gap["verdict"],
            ", ".join(gap.get("candidate_module_activities", [])),
            events[gap["reactome_event"]].get("schema_class", ""),
            ", ".join(event_uniprots(events[gap["reactome_event"]]))
            or "no catalyst members",
            events[gap["reactome_event"]].get("display_name", ""),
        ]
        for gap in alignment["reactome_only_events"]
    ]

    module_only_rows = []
    for gap in alignment["module_only_events"]:
        row = rows_by_activity[
            (
                gap["module_node"],
                gap["module_annoton"],
                gap["reactome_event"],
            )
        ]
        module_only_rows.append(
            [
                gap["reactome_event"],
                gap["verdict"],
                ", ".join(gap.get("candidate_reactome_events", [])),
                row["node_id"],
                row["annoton_id"],
                row["function_id"] or row["function_label"],
            ]
        )

    same_executor_fuzzy_links = sum(
        len(gap.get("candidate_module_activities", []))
        for gap in alignment["reactome_only_events"]
    ) + sum(
        len(gap.get("candidate_reactome_events", []))
        for gap in alignment["module_only_events"]
    )

    black_box_events = sum(
        gap["verdict"] == "black_box_event" for gap in alignment["reactome_only_events"]
    )

    exact_reaction_rows = sum(
        match["verdict"] == "reaction_id_exact" for match in alignment["matches"]
    )

    same_reaction_review_rows = [
        [
            match["reactome_event"],
            match["verdict"],
            ", ".join(match["match_basis"]),
            match["module_node"],
            match["module_annoton"],
            events[match["reactome_event"]].get("display_name", ""),
        ]
        for match in alignment["matches"]
        if match["verdict"] != "reaction_id_exact"
    ]

    title = str(config["id"]).replace("_", " ")
    path.write_text(
        "\n\n".join(
            [
                (
                    "---\n"
                    f'title: "Reactome pathway alignment: {title}"\n'
                    "species:\n"
                    "  - human\n"
                    "---"
                ),
                f"# Reactome pathway alignment: `{config['module']}`",
                "[Back to Reactome-GO Alignment](../REACTOME.md)",
                "Generated by `ingest_reactome_pathways.py` from "
                f"`{config['reactome_root']}` using `{config['scope']}` scope.",
                "## Counts\n\n"
                + markdown_table(
                    ["Measure", "Count"],
                    [
                        ["Imported events", len(events)],
                        [
                            "Imported reaction-like events",
                            sum(
                                event.get("schema_class") in REACTION_LIKE
                                for event in events.values()
                            ),
                        ],
                        [
                            "Activity-level cited event matches",
                            len(alignment["matches"]),
                        ],
                        ["Full executor/MF matches", exact_reaction_rows],
                        [
                            "Same-reaction rows needing review",
                            len(same_reaction_review_rows),
                        ],
                        [
                            "Reactome-only reaction-like events",
                            len(alignment["reactome_only_events"]),
                        ],
                        [
                            "Module-only activity Reactome IDs",
                            len(alignment["module_only_events"]),
                        ],
                        ["Same-executor fuzzy links", same_executor_fuzzy_links],
                        ["Reactome-only black-box events", black_box_events],
                    ],
                ),
                "## Activity-Level Cited Event Matches\n\n"
                + markdown_table(
                    [
                        "Reactome ID",
                        "Verdict",
                        "Basis",
                        "Node",
                        "Annoton",
                        "Function",
                        "Event",
                    ],
                    exact_rows,
                ),
                "## Same-Reaction Rows Needing Review\n\n"
                + markdown_table(
                    ["Reactome ID", "Verdict", "Basis", "Node", "Annoton", "Event"],
                    same_reaction_review_rows,
                ),
                "## Reactome-Only Reaction-Like Events\n\n"
                + markdown_table(
                    [
                        "Reactome ID",
                        "Verdict",
                        "Candidate local activities",
                        "Class",
                        "Catalyst members",
                        "Event",
                    ],
                    reactome_only_rows,
                ),
                "## Module-Only Activity Evidence\n\n"
                + markdown_table(
                    [
                        "Reactome ID",
                        "Verdict",
                        "Candidate imported events",
                        "Node",
                        "Annoton",
                        "Function",
                    ],
                    module_only_rows,
                ),
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def select_pathways(
    config: dict[str, Any], requested_ids: set[str]
) -> list[dict[str, Any]]:
    pathways = list(config.get("pathways", []))
    known_ids = {str(pathway["id"]) for pathway in pathways}
    unknown_ids = requested_ids - known_ids
    if unknown_ids:
        raise ValueError("Unknown pathway id(s): " + ", ".join(sorted(unknown_ids)))
    if not requested_ids:
        return pathways
    return [pathway for pathway in pathways if str(pathway["id"]) in requested_ids]


def parse_args() -> argparse.Namespace:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Ingest selected Reactome pathway subtrees as deterministic YAML."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=here.parents[1],
        help="Repository root. Defaults to this script's repository.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=here / "reactome_pathways.yaml",
        help="YAML file listing Reactome roots to ingest.",
    )
    parser.add_argument(
        "--imports-dir",
        type=Path,
        default=here / "imports",
        help="Directory for normalized Reactome import YAML.",
    )
    parser.add_argument(
        "--alignments-dir",
        type=Path,
        default=here / "alignments",
        help="Directory for module/Reactome alignment YAML.",
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=here / "pathway-alignments",
        help="Directory for Markdown alignment reports.",
    )
    parser.add_argument(
        "--use-existing-imports",
        action="store_true",
        help=(
            "Regenerate alignments/reports from existing import YAML files "
            "instead of fetching Reactome."
        ),
    )
    parser.add_argument(
        "--pathway",
        action="append",
        default=[],
        dest="pathways",
        help=("Only process this pathway id from the config. May be repeated."),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = args.root.resolve()
    client = ReactomeClient()
    config = load_yaml(args.config.resolve())

    try:
        pathways = select_pathways(config, set(args.pathways))
    except ValueError as e:
        raise SystemExit(str(e)) from e

    for pathway in pathways:
        slug = str(pathway["id"])
        import_path = args.imports_dir / f"{slug}.reactome.yaml"
        if args.use_existing_imports:
            if not import_path.exists():
                print(f"{slug}\tskipped=missing_import")
                continue
            imported = load_yaml(import_path)
        else:
            try:
                imported = build_import(pathway, client)
            except requests.RequestException as e:
                print(f"{slug}\tskipped=fetch_failed\terror={error_summary(e)}")
                continue

        module_sources = load_module_sources(root, str(pathway["module"]))
        alignment = align_module(pathway, imported, module_sources)

        write_yaml(import_path, imported)
        write_yaml(args.alignments_dir / f"{slug}.yaml", alignment, prune_empty=False)
        write_alignment_report(
            args.reports_dir / f"{slug}.md",
            pathway,
            imported,
            alignment,
            module_sources,
        )
        print(
            f"{slug}\tevents={len(imported['events'])}"
            f"\tmatches={len(alignment['matches'])}"
        )


if __name__ == "__main__":
    main()
