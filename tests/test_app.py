import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def app():
    return import_app("app")


def test_header_present(dash_duo, app):
    # Start the Dash application
    dash_duo.start_server(app)

    # Wait until the header appears
    dash_duo.wait_for_element("h1")

    # Find the header
    header = dash_duo.find_element("h1")

    # Check the header text
    assert header.text == "Pink Morsel Sales Visualiser"


def test_visualisation_present(dash_duo, app):
    # Start the Dash application
    dash_duo.start_server(app)

    # Wait until the graph appears
    dash_duo.wait_for_element("#sales-chart")

    # Find the graph
    graph = dash_duo.find_element("#sales-chart")

    # Check that the graph exists
    assert graph is not None


def test_region_picker_present(dash_duo, app):
    # Start the Dash application
    dash_duo.start_server(app)

    # Wait until the radio buttons appear
    dash_duo.wait_for_element("#region-filter")

    # Find the region picker
    picker = dash_duo.find_element("#region-filter")

    # Check that the region picker exists
    assert picker is not None