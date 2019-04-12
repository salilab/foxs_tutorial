import contextlib
import tempfile
import shutil

def get_shell_commands(md_file):
    with open(md_file) as fh:
        in_shell = False
        for line in fh:
            if line.startswith('\code{.sh}'):
                in_shell = True
            elif line.startswith('\endcode'):
                in_shell = False
            elif in_shell:
                yield line.rstrip('\r\n')

@contextlib.contextmanager
def temporary_directory(dir=None):
    """Simple context manager to make a temporary directory."""
    tmpdir = tempfile.mkdtemp(dir=dir)
    yield tmpdir
    shutil.rmtree(tmpdir, ignore_errors=True)
