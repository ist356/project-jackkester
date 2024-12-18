from helpers import  run_python_script

from code.scraping_code import main

def test_should_pass():
    print("This will always pass!")
    assert True

def test_scraping_code():
    expected_start = "Scraping UFC Rankin Scrolling through the page...Waiting for rankings content to load...Found Weight Class: Men's Pound-for-PoundTop Rank- Fighter: Islam Makhachev- Fighter: Jon Jones-"
    expected_end = "Chelsea Chandler Scraping Rankings Done."
    print("Running scraping code test")
    result = main()
    if result.startswith(expected_start) and result.endswith(expected_end):
        print("Scraping code test passed")
        assert True
    else:
        print("Scraping code test failed")
        assert False
    