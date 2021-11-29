import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
import json

if __name__ == '__main__':

    def handle_json(json):
        with open('/autograder/results/results_test.json', 'w') as f1:
            json.dump(json, f1)

    suite = unittest.defaultTestLoader.discover('/autograder/source/instructor/tests')
    with open('/autograder/results/results.json', 'w') as f:
        JSONTestRunner(visibility='visible', stream=f, post_processor=handle_json).run(suite)
