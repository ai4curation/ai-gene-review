import gzip
import math
from pathlib import Path

from ai_gene_review.evaluation.cafa import (
    evaluate_cafa_predictions,
    format_cafa_rows_tsv,
)


GENE1 = "HUMAN|HGNC=1|UniProtKB=P1"
GENE2 = "HUMAN|HGNC=2|UniProtKB=P2"
GENE3 = "HUMAN|HGNC=3|UniProtKB=P3"


def write(path: Path, text: str) -> Path:
    path.write_text(text)
    return path


def test_cafa_metric_uses_parent_exclusion_and_protein_centric_averages(
    tmp_path: Path,
) -> None:
    genes = write(
        tmp_path / "genes.tsv",
        f"{GENE1}\n{GENE2}\n{GENE3}\n",
    )
    training = write(
        tmp_path / "training.tsv",
        "P1\tGO:0000001\tmf\tIDA\ts\n",
    )
    parents = write(
        tmp_path / "parents.tsv",
        "\n".join(
            [
                "child term(GO:0000001)\tparent term(GO:0000002)\tis_a\tmolecular_function",
                "positively regulates(positively_regulates)\tregulates(regulates)\tis_a\texternal",
                "",
            ]
        ),
    )
    new = write(
        tmp_path / "new.tsv",
        "\n".join(
            [
                "P1\tGO:0000002\tmf\tIDA\tp",  # excluded via training parent closure
                "P1\tGO:0000003\tmf\tIDA\ts",
                "P2\tGO:0000006\tmf\tIDA\ts",
                "P3\tGO:0000007\tmf\tIDA\ts",  # dropped: no predictions for this gene
                "",
            ]
        ),
    )
    predictions = write(
        tmp_path / "predictions.tsv",
        "\n".join(
            [
                f"{GENE1}\tGO:0000003\tterm\tmf\t0.9\t1",
                f"{GENE1}\tGO:9999999\tterm\tmf\t0.8\t1",
                f"{GENE2}\tGO:0000006\tterm\tmf\t0.7\t2",
                f"{GENE2}\tGO:8888888\tterm\tmf\t0.6\t2",
                "",
            ]
        ),
    )

    rows = evaluate_cafa_predictions(
        predictions,
        training,
        new,
        genes,
        parents,
        thresholds=(1, 2),
        aspects=("mf",),
    )

    threshold_1, threshold_2 = rows
    assert threshold_1.precision_count == 1
    assert threshold_1.recall_count == 2
    assert threshold_1.precision == 0.5
    assert threshold_1.recall == 0.5
    assert threshold_1.f_score == 0.5

    assert threshold_2.precision_count == 2
    assert threshold_2.recall_count == 2
    assert threshold_2.precision == 0.5
    assert threshold_2.recall == 1.0
    assert math.isclose(threshold_2.f_score or 0.0, 2 / 3)


def test_cafa_metric_reads_gzip_predictions_and_formats_tsv(tmp_path: Path) -> None:
    genes = write(tmp_path / "genes.tsv", f"{GENE1}\n")
    training = write(tmp_path / "training.tsv", "")
    new = write(tmp_path / "new.tsv", "P1\tGO:0000003\tmf\tIDA\ts\n")
    predictions = tmp_path / "predictions.tsv.gz"
    with gzip.open(predictions, "wt") as handle:
        handle.write(f"{GENE1}\tGO:0000003\tterm\tmf\t0.9\t1\n")

    rows = evaluate_cafa_predictions(
        predictions,
        training,
        new,
        genes,
        thresholds=(1,),
        aspects=("mf",),
    )
    tsv = format_cafa_rows_tsv(rows)

    assert rows[0].precision == 1.0
    assert rows[0].recall == 1.0
    assert tsv.splitlines() == [
        "\t".join(
            [
                "threshold_rank",
                "threshold_fraction",
                "aspect",
                "precision_total",
                "precision_count",
                "precision",
                "recall_total",
                "recall_count",
                "recall",
                "f_score",
            ]
        ),
        "1\t1\tmf\t1\t1\t1\t1\t1\t1\t1",
    ]


def test_cafa_metric_populates_default_all_aspect(tmp_path: Path) -> None:
    genes = write(tmp_path / "genes.tsv", f"{GENE1}\n{GENE2}\n{GENE3}\n")
    training = write(tmp_path / "training.tsv", "")
    new = write(
        tmp_path / "new.tsv",
        "\n".join(
            [
                "P1\tGO:0000003\tmf\tIDA\ts",
                "P2\tGO:0000004\tbp\tIDA\tp",
                "P3\tGO:0000005\tcc\tIDA\tc",
                "",
            ]
        ),
    )
    predictions = write(
        tmp_path / "predictions.tsv",
        "\n".join(
            [
                f"{GENE1}\tGO:0000003\tterm\tmf\t0.9\t1",
                f"{GENE2}\tGO:0000004\tterm\tbp\t0.8\t2",
                f"{GENE3}\tGO:0000005\tterm\tcc\t0.7\t2",
                "",
            ]
        ),
    )

    rows = evaluate_cafa_predictions(
        predictions,
        training,
        new,
        genes,
        thresholds=(1, 2),
    )

    by_threshold_aspect = {
        (row.threshold_rank, row.aspect): row for row in rows
    }

    assert len(rows) == 8
    assert by_threshold_aspect[(1, "all")].precision == 1.0
    assert by_threshold_aspect[(1, "all")].recall == 1 / 3
    assert by_threshold_aspect[(2, "all")].precision == 1.0
    assert by_threshold_aspect[(2, "all")].recall == 1.0


def test_cafa_metric_keeps_excluded_only_predictions_in_recall_denominator(
    tmp_path: Path,
) -> None:
    genes = write(tmp_path / "genes.tsv", f"{GENE1}\n")
    training = write(tmp_path / "training.tsv", "")
    new = write(tmp_path / "new.tsv", "P1\tGO:0000003\tmf\tIDA\ts\n")
    predictions = write(
        tmp_path / "predictions.tsv",
        f"{GENE1}\tGO:0005515\tprotein binding\tmf\t0.9\t1\n",
    )

    rows = evaluate_cafa_predictions(
        predictions,
        training,
        new,
        genes,
        thresholds=(1,),
        aspects=("mf",),
    )

    assert rows[0].precision_count == 0
    assert rows[0].precision is None
    assert rows[0].recall_count == 1
    assert rows[0].recall == 0.0
    assert rows[0].f_score is None


def test_cafa_metric_skips_ranks_above_configured_thresholds(tmp_path: Path) -> None:
    genes = write(tmp_path / "genes.tsv", f"{GENE1}\n")
    training = write(tmp_path / "training.tsv", "")
    new = write(tmp_path / "new.tsv", "P1\tGO:0000003\tmf\tIDA\ts\n")
    predictions = write(
        tmp_path / "predictions.tsv",
        "\n".join(
            [
                f"{GENE1}\tGO:0000003\tterm\tmf\t0.9\t1",
                f"{GENE1}\tGO:9999999\tterm\tmf\t0.1\t10",
                "",
            ]
        ),
    )

    rows = evaluate_cafa_predictions(
        predictions,
        training,
        new,
        genes,
        thresholds=tuple(range(1, 6)),
        aspects=("mf",),
    )

    assert rows[-1].precision == 1.0
    assert rows[-1].recall == 1.0
