"""GIS Compression Utilities."""


# Standard
import pathlib
import tarfile
import zipfile

# Third-Party
import py7zr
import rarfile


def decompress(file: pathlib.Path) -> pathlib.Path:
    """Decompresses a file and flattens it if required.

    Args:
        file (pathlib.Path): File to be decompressed.

    Returns:
        pathlib.Path: Path to the decompressed directory.
    """
    # Check file
    if zipfile.is_zipfile(file):
        # `.zip`
        algorithm = zipfile.ZipFile

    elif tarfile.is_tarfile(file):
        # `.tar`
        algorithm = tarfile.TarFile  # type: ignore

    elif rarfile.is_rarfile(file):
        # `.rar`
        algorithm = rarfile.RarFile

    elif py7zr.is_7zfile(file):
        # `.7z`
        algorithm = py7zr.SevenZipFile  # type: ignore

    else:
        # None!
        algorithm = None

    # Check
    if not algorithm:
        # Return the file unchanged
        return file

    # Construct Path for Extraction
    extracted_path = file.with_name(f"extracted_{file.stem}")

    # Decompress
    with algorithm(file) as archive:
        # Extract
        archive.extractall(path=extracted_path)

    # Return
    return extracted_path


def flatten(path: pathlib.Path) -> pathlib.Path:
    """Flattens a directory.

    Args:
        path (pathlib.Path): Directory to be flattened.

    Returns:
        pathlib.Path: Flattened directory.
    """
    # Enumerate subpaths
    subpaths = list(path.glob("*"))

    # Check if there is a single directory inside
    if len(subpaths) == 1 and subpaths[0].is_dir():
        # Recurse, flatten that directory also if applicable and return
        return flatten(subpaths[0])

    # Return
    return path
