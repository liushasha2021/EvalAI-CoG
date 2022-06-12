import random


def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    
    output = {}
    output['result'] = [
                {
                    'train_split': {
                        'Metric1': 123,
                        'Metric2': 123,
                        'Metric3': 123,
                        'Total': 123,
                    }
                },
                {
                    'test_split': {
                        'Metric1': 123,
                        'Metric2': 123,
                        'Metric3': 123,
                        'Total': 123,
                    }
                }
            ]

    return output
