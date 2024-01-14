try:
    from polars.polars import (
        CategoricalRemappingWarning,
        ColumnNotFoundError,
        ComputeError,
        DuplicateError,
        InvalidOperationError,
        NoDataError,
        OutOfBoundsError,
        PolarsError,
        PolarsPanicError,
        PolarsWarning,
        SchemaError,
        SchemaFieldNotFoundError,
        ShapeError,
        StringCacheMismatchError,
        StructFieldNotFoundError,
    )
except ImportError:
    # redefined for documentation purposes when there is no binary

    class PolarsError(Exception):  # type: ignore[no-redef]
        """Base class for all Polars errors."""

    class ColumnNotFoundError(PolarsError):  # type: ignore[no-redef, misc]
        """
        Exception raised when a specified column is not found.

        Example
        -------
        >>> df = pl.DataFrame({"a": [1, 2, 3]})
        >>> df.select("b")
        Traceback (most recent call last):
        polars.exceptions.ColumnNotFoundError: b
        """

    class ComputeError(PolarsError):  # type: ignore[no-redef, misc]
        """
        Exception raised when polars could not finish the computation.

        Example
        -------
        >>> df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
        >>> df.filter(pl.col("a") == "x")
        Traceback (most recent call last):
        polars.exceptions.ComputeError: cannot compare string with numeric data
        """

    class DuplicateError(PolarsError):  # type: ignore[no-redef, misc]
        """
        Exception raised when a column name is duplicated.

        Example
        -------
        >>> df = pl.DataFrame({"a": [1, 1, 1]})
        >>> pl.concat([df, df], how="horizontal")
        Traceback (most recent call last):
        polars.exceptions.DuplicateError: unable to hstack, column with name "a" already exists
        """  # noqa: W505

    class InvalidOperationError(PolarsError):  # type: ignore[no-redef, misc]
        """
        Exception raised when an operation is not allowed on a certain data type.

        Example
        -------
        >>> s = pl.Series("a", [1, 2, 3])
        >>> s.is_in(["x", "y"])
        Traceback (most recent call last):
        polars.exceptions.InvalidOperationError: `is_in` cannot check for String values in Int64 data
        """  # noqa: W505

    class NoDataError(PolarsError):  # type: ignore[no-redef, misc]
        """
        Exception raised when an operation can not be performed on an empty data structure.

        Example
        -------
        >>> pl.from_dicts([])
        Traceback (most recent call last):
        polars.exceptions.NoDataError: no data, cannot infer schema
        """  # noqa: W505

    class OutOfBoundsError(PolarsError):  # type: ignore[no-redef, misc]
        """Exception raised when the given index is out of bounds."""

    class PolarsPanicError(PolarsError):  # type: ignore[no-redef, misc]
        """Exception raised when an unexpected state causes a panic in the underlying Rust library."""  # noqa: W505

    class SchemaError(PolarsError):  # type: ignore[no-redef, misc]
        """
        Exception raised when trying to combine data structures with mismatched schemas.

        Example
        -------
        >>> pl.Series([0, 1, 0]).any()
        Traceback (most recent call last):
        polars.exceptions.SchemaError: invalid series dtype: expected `Boolean`, got `i64`
        """  # noqa: W505

    class SchemaFieldNotFoundError(PolarsError):  # type: ignore[no-redef, misc]
        """Exception raised when a specified schema field is not found."""

    class ShapeError(PolarsError):  # type: ignore[no-redef, misc]
        """
        Exception raised when trying to combine data structures with incompatible shapes.

        Example
        -------
        >>> pl.DataFrame({"a": [1, 2, 3], "b": [4, 5]})
        Traceback (most recent call last):
        polars.exceptions.ShapeError: could not create a new DataFrame: series "a" has length 3 while series "b" has length 2
        """  # noqa: W505

    class StringCacheMismatchError(PolarsError):  # type: ignore[no-redef, misc]
        """Exception raised when string caches come from different sources."""

    class StructFieldNotFoundError(PolarsError):  # type: ignore[no-redef, misc]
        """Exception raised when a specified schema field is not found."""

    class PolarsWarning(Exception):  # type: ignore[no-redef]
        """Base class for all Polars warnings."""

    class CategoricalRemappingWarning(PolarsWarning):  # type: ignore[no-redef, misc]
        """Warning raised when a categorical needs to be remapped to be compatible with another categorical."""  # noqa: W505


class InvalidAssert(PolarsError):  # type: ignore[misc]
    """Exception raised when an unsupported testing assert is made."""


class RowsError(PolarsError):  # type: ignore[misc]
    """Exception raised when the number of returned rows does not match expectation."""


class NoRowsReturnedError(RowsError):
    """Exception raised when no rows are returned, but at least one row is expected."""


class TooManyRowsReturnedError(RowsError):
    """Exception raised when more rows than expected are returned."""


class ModuleUpgradeRequired(ModuleNotFoundError):
    """Exception raised when the module is installed but needs to be upgraded."""


class ParameterCollisionError(PolarsError):  # type: ignore[misc]
    """Exception raised when the same parameter occurs multiple times."""


class UnsuitableSQLError(PolarsError):  # type: ignore[misc]
    """Exception raised when unsuitable SQL is given to a database method."""


class ChronoFormatWarning(PolarsWarning):  # type: ignore[misc]
    """
    Warning raised when a chrono format string contains dubious patterns.

    Polars uses Rust's chrono crate to convert between string data and temporal data.
    The patterns used by chrono differ slightly from Python's built-in datetime module.
    Refer to the `chrono strftime documentation
    <https://docs.rs/chrono/latest/chrono/format/strftime/index.html>`_ for the full
    specification.
    """


class PolarsInefficientMapWarning(PolarsWarning):  # type: ignore[misc]
    """Warning raised when a potentially slow `apply` operation is performed."""


class TimeZoneAwareConstructorWarning(PolarsWarning):  # type: ignore[misc]
    """Warning raised when constructing Series from non-UTC time-zone-aware inputs."""


class ArrowError(Exception):
    """deprecated will be removed."""


__all__ = [
    "ArrowError",
    "ColumnNotFoundError",
    "ComputeError",
    "ChronoFormatWarning",
    "DuplicateError",
    "InvalidOperationError",
    "ModuleUpgradeRequired",
    "NoDataError",
    "NoRowsReturnedError",
    "OutOfBoundsError",
    "PolarsInefficientMapWarning",
    "CategoricalRemappingWarning",
    "PolarsError",
    "PolarsPanicError",
    "PolarsWarning",
    "RowsError",
    "SchemaError",
    "SchemaFieldNotFoundError",
    "ShapeError",
    "StringCacheMismatchError",
    "StructFieldNotFoundError",
    "TooManyRowsReturnedError",
]
