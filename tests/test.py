import unittest

from screenshot import screenshot

class TestResult(unittest.TestCase):
    def test_output_is_string(self):
        """
        (about:blank) Test that output is of type string
        """
        url="about:blank"
        result=screenshot.main(url)
        self.assertTrue(isinstance(result, str))
        print("Everything passed")

    def test_output_is_base64(self):
        pass
    
if __name__ == "__main__":
    unittest.main()

