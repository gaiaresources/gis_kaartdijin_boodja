"""GIS Conversion Functionality."""


# Standard
import logging
import pathlib
import subprocess  # noqa: S404
import tempfile

# Local
from govapp.gis import compression


# Logging
log = logging.getLogger(__name__)


def to_geopackage(filepath: pathlib.Path, layer: str) -> pathlib.Path:
    """Converts a GIS file to the GeoPackage format.

    Args:
        filepath (pathlib.Path): Path to the file to be converted.
        layer (str): Layer to be converted.

    Returns:
        pathlib.Path: Path to the converted GeoPackage file.
    """
    # Log
    log.info(f"Converting file '{filepath}' layer: '{layer}' to GeoPackage")

    # Decompress and Flatten if Required
    filepath = compression.decompress(filepath)
    filepath = compression.flatten(filepath)

    # Construct Output Filepath
    output_dir = tempfile.mkdtemp()
    output_filepath = pathlib.Path(output_dir) / f"{layer}.gpkg"

    # Run Command
    subprocess.check_call(  # noqa: S603,S607
        [
            "ogr2ogr",
            "-overwrite",
            str(output_filepath),
            str(filepath),
            str(layer),
        ]
    )

    # Return
    return output_filepath


def to_geojson(filepath: pathlib.Path, layer: str) -> pathlib.Path:
    """Converts a GIS file to the GeoJSON format.

    Args:
        filepath (pathlib.Path): Path to the file to be converted.
        layer (str): Layer to be converted.

    Returns:
        pathlib.Path: Path to the converted GeoJSON file.
    """
    # Log
    log.info(f"Converting file '{filepath}' layer: '{layer}' to GeoJSON")

    # Decompress and Flatten if Required
    filepath = compression.decompress(filepath)
    filepath = compression.flatten(filepath)

    # Construct Output Filepath
    output_dir = tempfile.mkdtemp()
    output_filepath = pathlib.Path(output_dir) / f"{layer}.geojson"

    # Run Command
    subprocess.check_call(  # noqa: S603,S607
        [
            "ogr2ogr",
            "-overwrite",
            str(output_filepath),
            str(filepath),
            str(layer),
        ]
    )

    # Return
    return output_filepath


def to_shapefile(filepath: pathlib.Path, layer: str) -> pathlib.Path:
    """Converts a GIS file to the ShapeFile format.

    Args:
        filepath (pathlib.Path): Path to the file to be converted.
        layer (str): Layer to be converted.

    Returns:
        pathlib.Path: Path to the converted ShapeFile file.
    """
    # Log
    log.info(f"Converting file '{filepath}' layer: '{layer}' to ShapeFile")

    # Decompress and Flatten if Required
    filepath = compression.decompress(filepath)
    filepath = compression.flatten(filepath)

    # Construct Output Filepath
    # Here we double up on the `layer.shp` to ensure its in a directory
    output_dir = tempfile.mkdtemp()
    output_filepath = pathlib.Path(output_dir) / f"{layer}.shp"
    output_filepath.mkdir(parents=True, exist_ok=True)
    output_filepath = output_filepath / f"{layer}.shp"

    # Run Command
    subprocess.check_call(  # noqa: S603,S607
        [
            "ogr2ogr",
            "-overwrite",
            str(output_filepath),
            str(filepath),
            str(layer),
        ]
    )

    # Compress!
    compressed_filepath = compression.compress(output_filepath.parent)

    # Return
    return compressed_filepath


def to_geodatabase(filepath: pathlib.Path, layer: str) -> pathlib.Path:
    """Converts a GIS file to the GeoDatabase format.

    Args:
        filepath (pathlib.Path): Path to the file to be converted.
        layer (str): Layer to be converted.

    Returns:
        pathlib.Path: Path to the converted GeoDatabase file.
    """
    # Log
    log.info(f"Converting file '{filepath}' layer: '{layer}' to GeoDatabase")

    # Decompress and Flatten if Required
    filepath = compression.decompress(filepath)
    filepath = compression.flatten(filepath)

    # Construct Output Filepath
    # Here we double up on the `layer.gdb` to ensure its in a directory
    output_dir = tempfile.mkdtemp()
    output_filepath = pathlib.Path(output_dir) / f"{layer}.gdb"
    output_filepath.mkdir(parents=True, exist_ok=True)
    output_filepath = output_filepath / f"{layer}.gdb"

    # Run Command
    subprocess.check_call(  # noqa: S603,S607
        [
            "ogr2ogr",
            "-overwrite",
            str(output_filepath),
            str(filepath),
            str(layer),
        ]
    )

    # Compress!
    compressed_filepath = compression.compress(output_filepath.parent)

    # Return
    return compressed_filepath
