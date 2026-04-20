from contributor_readiness_kit import format_readiness_summary


def test_format_readiness_summary() -> None:
    assert format_readiness_summary("ready") == "Contributor readiness: ready"
