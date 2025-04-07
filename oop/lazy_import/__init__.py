from typing import TYPE_CHECKING

# 类型检查时使用
if TYPE_CHECKING:
    from .libs.compute import Compute
    from .student import Student

__all__ = [
    "Compute",
    "Student",
]

_LAZY_IMPORTS = {
    # lib 子模块
    "Compute": (".lib.compute", "Compute"),
    # 主模块
    "Student": (".student", "Student"),
}

# 缓存已加载的类
_LAZY_CACHE = {}


def __getattr__(name):
    if name in _LAZY_IMPORTS:
        if name in _LAZY_CACHE:
            return _LAZY_CACHE[name]
        module_path, attr_name = _LAZY_IMPORTS[name]
        from importlib import import_module
        # 修正package参数为当前模块的包名
        module = import_module(module_path, package=__package__)
        attr = getattr(module, attr_name)
        _LAZY_CACHE[name] = attr
        print(f"lazy import {name}")
        return attr
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(all + list(_LAZY_IMPORTS.keys()))
