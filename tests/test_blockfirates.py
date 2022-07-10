from blockfirates.client import BlockFiRates


def test_rates_returned():
    assert len(BlockFiRates().get_all_rates()) > 0


def test_get_amount():
    assert BlockFiRates().get_amount("BTC (Tier 1)")


def test_get_apy():
    assert BlockFiRates().get_apy("BTC (Tier 1)") > 0
