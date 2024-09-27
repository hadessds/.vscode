from _typeshed import Incomplete

class VCPythonEngine:
    verifier: Incomplete
    ffi: Incomplete
    def __init__(self, verifier) -> None: ...
    def patch_extension_kwds(self, kwds) -> None: ...
    def find_module(self, module_name, path, so_suffixes): ...
    def collect_types(self) -> None: ...
    def write_source_to_f(self) -> None: ...
    def load_library(self, flags: Incomplete | None = None): ...

cffimod_header: str
