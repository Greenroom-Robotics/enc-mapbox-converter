# ENC Mapbox converter

This tool is used to convert ENC files (S57) to mbtiles.

Internally this uses:

- `enc` to `geojson` using gdal's `ogr2ogr`
- `geojson` to `mbtiles` using mapbox's `tippecanoe`

## Requirements

- Git
- Docker

## Usage

This tool uses a bunch of tools internally so it has been dockerised with a simple cli exposed.

1. Clone this repo:

```bash
git clone git@github.com:Greenroom-Robotics/enc-mapbox-converter.git
```

2. Build the docker container

```bash
docker build . -t enc-converter
```

3. Run the cli. Be sure to replace `<absolute_path_to_this_repo>`

```bash
docker run -it -v /$PWD:/app enc-converter python3 cli.py
```

4. You will be prompted for an input file and output name. For example.

```
Input file path: /app/data/AU5193P0/5/0/AU5193P0.000
Output file name: output_mb_tiles_file

```

5. Look in `./output_mbtiles` and you will find your `.mbtiles` file!
