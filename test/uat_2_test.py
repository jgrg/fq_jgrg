import fq_stats


def test_long():
    assert fq_stats.main(["--length", "test/data/wiki_example.fq"]) == 72 * 2


def test_short():
    assert fq_stats.main(["-l", "test/data/wiki_example.fq"]) == 72 * 2
