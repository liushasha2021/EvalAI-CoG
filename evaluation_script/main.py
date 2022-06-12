import random


def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    
    output = {}        
    output["result"] = [
        {
            "train_split": {
            "Metric1": random.randint(0, 99),
            "Metric2": random.randint(0, 99),
            "Metric3": random.randint(0, 99),
            "Total": random.randint(0, 99),
            }
        },
        {
            "test_split": {
                "Metric1": random.randint(0, 99),
                "Metric2": random.randint(0, 99),
                "Metric3": random.randint(0, 99),
                "Total": random.randint(0, 99),
                }
            },
        ]
    output["submission_result"] = output["result"][0]
#         print("Completed evaluation for Test Phase")
    return output
