from pyplater.utils.tree import DisplayablePath
from pathlib import Path
from pyfakefs.fake_filesystem_unittest import TestCase


class TestDisplayablePath(TestCase):
    def setUp(self):
        self.setUpPyfakefs()

    def test_make_tree(self):
        # Set up a fake filesystem
        self.fs.create_dir("/root/dir1")
        self.fs.create_file("/root/dir1/file1.txt")
        self.fs.create_file("/root/dir1/file2.txt")
        self.fs.create_dir("/root/dir2")
        self.fs.create_file("/root/file3.txt")

        # Test the make_tree class method
        tree = list(DisplayablePath.make_tree(Path("/root")))
        assert len(tree) == 6
        assert tree[0].displayname == "root/"
        assert tree[1].displayname == "dir1/"
        assert tree[2].displayname == "file1.txt"
        assert tree[3].displayname == "file2.txt"
        assert tree[4].displayname == "dir2/"
        assert tree[5].displayname == "file3.txt"
        assert tree[2].displayable() == "│   ├── file1.txt"
        assert tree[3].displayable() == "│   └── file2.txt"
        assert tree[4].displayable() == "├── dir2/"
        assert tree[5].displayable() == "└── file3.txt"
