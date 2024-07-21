import unittest

# Assume the extract_parts function is defined in a file named extract.py
from sports import extract_parts

class TestExtractParts(unittest.TestCase):
    def setUp(self):
        # Sample README content for testing
        self.readme_content = """
# Introduction
This is the introduction section.

# Installation
This is the installation section.

# Usage
This is the usage section.
"""
        
    def test_extract_introduction(self):
        start_marker = "# Introduction"
        end_marker = "# Installation"
        expected_output = """
# Introduction
This is the introduction section.
"""
        result = extract_parts(self.readme_content, start_marker, end_marker)
        self.assertEqual(result.strip(), expected_output.strip())

    def test_extract_installation(self):
        start_marker = "# Installation"
        end_marker = "# Usage"
        expected_output = """
# Installation
This is the installation section.
"""
        result = extract_parts(self.readme_content, start_marker, end_marker)
        self.assertEqual(result.strip(), expected_output.strip())

    def test_extract_not_found(self):
        start_marker = "# Nonexistent"
        end_marker = "# Installation"
        expected_output = """
# Introduction
This is the introduction section.

"""
        result = extract_parts(self.readme_content, start_marker, end_marker)
        self.assertEqual(result, expected_output)

#     def test_extract_partial_content(self):
#         start_marker = "# Introduction"
#         end_marker = "# Nonexistent"
#         expected_output = """
# # Introduction
# This is the introduction section.

# # Installation
# This is the installation section.

# # Usage
# This is the usage section.
# """
#         result = extract_parts(self.readme_content, start_marker, end_marker)
#         self.assertEqual(result.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
