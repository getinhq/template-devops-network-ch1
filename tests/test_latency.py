import latency


def test_measure_returns_float():
    assert isinstance(latency.measure_once("127.0.0.1"), float)
