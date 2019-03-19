from statistics import (stdev, mean)
from ml_lib.learning import (err_ratio, train_and_test)

def cross_validation(learner, dataset, k=10):
    """
    Perform k-fold cross_validation
    Run k trials where each trial has a different (k-1)/k percentage
    of the data as training data and 1/k as test data.
    Returns tuple (mean_err, std_err, fold_errors, models)
    """
    if k is None: #if k is not initialized
        k = len(dataset.examples)

    fold_errV = []  # fold error on validation data # validation is testing
    n = len(dataset.examples)
    examples = dataset.examples

    for fold in range(k):  # for each fold
        train_data, val_data = train_and_test(dataset, fold * (n / k), (fold + 1) * (n / k))
        dataset.examples = train_data
        h = learner(dataset)  # # look into later, doesn't do testing

        # predict and accumulate the error rate on tthe validation data
        error_rate = err_ratio(h, dataset, val_data)
        fold_errV.append(round(error_rate, 3))
        # Reverting back to original once test is completed
        dataset.examples = examples

    mean_err = round(mean(fold_errV), 3)
    std_error = round(stdev(fold_errV), 3)
    return (mean_err, std_error, fold_errV, learner.__name__)