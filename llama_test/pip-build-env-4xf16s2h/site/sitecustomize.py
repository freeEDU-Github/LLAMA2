
import os, site, sys

# First, drop system-sites related paths.
original_sys_path = sys.path[:]
known_paths = set()
for path in {'/mnt/storage1/local_LLM/LLAMA/LLAMA2/lib/python3.8/site-packages'}:
    site.addsitedir(path, known_paths=known_paths)
system_paths = set(
    os.path.normcase(path)
    for path in sys.path[len(original_sys_path):]
)
original_sys_path = [
    path for path in original_sys_path
    if os.path.normcase(path) not in system_paths
]
sys.path = original_sys_path

# Second, add lib directories.
# ensuring .pth file are processed.
for path in ['/mnt/storage1/local_LLM/LLAMA/llama_test/pip-build-env-4xf16s2h/overlay/lib/python3.8/site-packages', '/mnt/storage1/local_LLM/LLAMA/llama_test/pip-build-env-4xf16s2h/normal/lib/python3.8/site-packages']:
    assert not path in sys.path
    site.addsitedir(path)
