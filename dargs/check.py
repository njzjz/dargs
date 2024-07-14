from __future__ import annotations

from dargs.dargs import Argument


def check(
    arginfo: Argument | list[Argument] | tuple[Argument, ...],
    data: dict,
    strict: bool = True,
) -> None:
    """Check and normalize input data.

    Parameters
    ----------
    arginfo : Union[Argument, List[Argument], Tuple[Argument, ...]]
        Argument object
    data : dict
        data to check
    strict : bool, optional
        If True, raise an error if the key is not pre-defined, by default True

    Returns
    -------
    dict
        normalized data
    """
    if isinstance(arginfo, (list, tuple)):
        arginfo = Argument("base", dtype=dict, sub_fields=arginfo)

    data = arginfo.normalize_value(data, trim_pattern="_*")
    arginfo.check_value(data, strict=strict)
    return data
