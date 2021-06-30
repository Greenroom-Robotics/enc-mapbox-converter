from osgeo import ogr
import subprocess
import click

OGR_S57_OPTIONS = "SPLIT_MULTIPOINT=ON,ADD_SOUNDG_DEPTH=ON"

DEFAULT_INPUT = "/app/example/US5OH10M/US5OH10M.000"
DEFAULT_OUTPUT = "output_mb_tiles_file"


@click.command()
@click.option("--input", prompt="Input file path", default=DEFAULT_INPUT)
@click.option("--output", prompt="Output file name", default=DEFAULT_OUTPUT)
def convert(input=DEFAULT_INPUT, output=DEFAULT_OUTPUT):
    input_file = ogr.Open(input, 0)

    # Get the layers in the file
    enc_layers = []
    for featsClass_idx in range(input_file.GetLayerCount()):
        featsClass = input_file.GetLayerByIndex(featsClass_idx)
        enc_layer = featsClass.GetName()
        enc_layers.append(enc_layer)

    # Convert them into geojson
    geojson_layers = []
    for enc_layer in enc_layers:
        print(f"Converting {enc_layer} to geojson...")
        geojson_layer = f"./output_geojson/{enc_layer}.geojson"
        geojson_layers.append(geojson_layer)

        # Use ogr2ogr to extract geojson from the enc file
        subprocess.call(
            f"OGR_S57_OPTIONS={OGR_S57_OPTIONS} ogr2ogr -f GeoJSON -t_srs EPSG:4326 {geojson_layer} {input} {enc_layer}",
            shell=True,
        )

    geojson_layers_str = " ".join(geojson_layers)
    subprocess.call(
        f"tippecanoe --output=./output_mbtiles/{output}.mbtiles {geojson_layers_str}",
        shell=True,
    )


if __name__ == "__main__":
    convert()
