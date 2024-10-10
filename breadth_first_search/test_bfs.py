import unittest
from unittest.mock import patch
from bfs import main, bfs, validate_input


class TestBfsFunctionClass(unittest.TestCase):

    # Positive tests
    def test_bfs_output_1(self):
        result = bfs(6, [1, 3, 4])
        expected_result = [3, 3]
        self.assertEqual(result, expected_result)

    def test_bfs_output_2(self):
        result = bfs(23, [1, 5, 10, 20])
        expected_result = [1, 1, 1, 20]
        self.assertEqual(result, expected_result)

    def test_bfs_output_3(self):
        result = bfs(1017, [50, 100, 200, 1, 2, 5, 10, 20])
        expected_result = [200, 200, 200, 200, 200, 2, 5, 10]
        self.assertEqual(result, expected_result)

    # Negative tests
    @patch('builtins.print')
    def test_bfs_input_invalid_1(self, mock_print):
        bfs("invalid", [1, 4, 5])
        mock_print.assert_called_once_with("An error occurred")

    @patch('builtins.print')
    def test_bfs_input_invalid_2(self, mock_print):
        bfs(6, "invalid")
        mock_print.assert_called_with("An error occurred")


class TestValidateInput(unittest.TestCase):

    # Positive tests
    def test_validate_input_1(self):
        result = validate_input(6, [1, 3, 4])
        self.assertTrue(result)

    def test_validate_input_2(self):
        result = validate_input(23, [1, 5, 10, 20])
        self.assertTrue(result)

    def test_validate_input_3(self):
        result = validate_input(1017, [50, 100, 200, 1, 2, 5, 10, 20])
        self.assertTrue(result)

    # Negative tests
    def test_validate_input_invalid_1(self):
        result = validate_input("invalid", [1, 2, 3])
        self.assertFalse(result)

    def test_validate_input_invalid_2(self):
        result = validate_input(1017, (50, 100, 200, 1, 2, 5, 10, 20))
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
