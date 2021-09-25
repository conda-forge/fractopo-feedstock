"""
Simple test case for fractopo conda build.
"""

import geopandas as gpd
from fractopo import Network

KB11_TRACES = gpd.read_file(
    "https://raw.githubusercontent.com/nialov/"
    "fractopo/master/tests/sample_data/KB11/KB11_traces.geojson"
)
KB11_AREA = gpd.read_file(
    "https://raw.githubusercontent.com/nialov/"
    "fractopo/master/tests/sample_data/KB11/KB11_area.geojson"
)
NAME = "KB11"

# from fractopo import Validation
# print("Validating KB11_traces")
# validation = Validation(traces=KB11_TRACES, area=KB11_AREA, name=NAME, allow_fix=True)

# validated_traces = validation.run_validation()

# Create fractopo Network
print("Creating fractopo Network out of validated KB11_traces.")
kb11_network = Network(
    name=NAME,
    trace_gdf=KB11_TRACES,
    area_gdf=KB11_AREA,
    truncate_traces=True,
    circular_target_area=False,
    determine_branches_nodes=True,
    snap_threshold=0.001,
)

print(kb11_network.parameters)

kb11_network.plot_trace_lengths()
