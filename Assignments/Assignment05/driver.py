'''
Created on Apr 15, 2018
@author: mroch
'''
#from ml_lib.example_reader import CSVDataSet
from ml_lib.learning import (DataSet, DecisionTreeLearner, NeuralNetLearner)
from std_cv import cross_validation, mean, stdev
from random import shuffle
from copy import deepcopy

    
def learn(dataset):
    """
    :param dataset - passed in the cross_validation function to calculate mean_err, std_err, fold_errors, on all models
    :param k - is the number of folds
    :param learner switches to be different classes so that the learning model can do a cross validation
    """
    shuffle(dataset.examples)  #  Shuffle the sequence x in place, in place operations.
    learners = [DecisionTreeLearner, NeuralNetLearner]
    for learner in learners:
        if learner is NeuralNetLearner:
            dataset.attributes_to_numbers()
        statistics = cross_validation(learner, dataset, k=10)

    print("Learner            Mean   StdDev  Errors for folds")
    for curr_idx in range(len(statistics)):
            statistic = statistics
            mean = statistic[0]
            std = statistic[1]
            fold_errors = str(statistic[2])
            model_name = str(statistic[3])
            print("{}   {}   {}   {}".format(model_name, mean,  std, fold_errors))

def main():
    """
    Initialize data set,
    then call learn on dataset to """
    names = ['iris', 'orings', 'restaurant', 'zoo']
    for name in names:
        dataset = DataSet(name=name)
        # error print(dataset) just prints string repr ... | use debugging skills
        learn(dataset)

if __name__ == '__main__':
    main()

'''
Output:
Learner            Mean   StdDev  Errors for folds
NeuralNetLearner   0.307   0.244   [0.133, 0.067, 0.533, 0.267, 0.2, 0.867, 0.267, 0.267, 0.067, 0.4]
NeuralNetLearner   0.307   0.244   [0.133, 0.067, 0.533, 0.267, 0.2, 0.867, 0.267, 0.267, 0.067, 0.4]
NeuralNetLearner   0.307   0.244   [0.133, 0.067, 0.533, 0.267, 0.2, 0.867, 0.267, 0.267, 0.067, 0.4]
NeuralNetLearner   0.307   0.244   [0.133, 0.067, 0.533, 0.267, 0.2, 0.867, 0.267, 0.267, 0.067, 0.4]
Learner            Mean   StdDev  Errors for folds
NeuralNetLearner   0.233   0.263   [0.0, 0.0, 0.5, 0.333, 0.5, 0.0, 0.333, 0.0, 0.0, 0.667]
NeuralNetLearner   0.233   0.263   [0.0, 0.0, 0.5, 0.333, 0.5, 0.0, 0.333, 0.0, 0.0, 0.667]
NeuralNetLearner   0.233   0.263   [0.0, 0.0, 0.5, 0.333, 0.5, 0.0, 0.333, 0.0, 0.0, 0.667]
NeuralNetLearner   0.233   0.263   [0.0, 0.0, 0.5, 0.333, 0.5, 0.0, 0.333, 0.0, 0.0, 0.667]
Learner            Mean   StdDev  Errors for folds
NeuralNetLearner   0.6   0.516   [0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0]
NeuralNetLearner   0.6   0.516   [0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0]
NeuralNetLearner   0.6   0.516   [0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0]
NeuralNetLearner   0.6   0.516   [0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0]
Learner            Mean   StdDev  Errors for folds
NeuralNetLearner   0.586   0.15   [0.5, 0.7, 0.8, 0.6, 0.4, 0.6, 0.8, 0.5, 0.6, 0.364]
NeuralNetLearner   0.586   0.15   [0.5, 0.7, 0.8, 0.6, 0.4, 0.6, 0.8, 0.5, 0.6, 0.364]
NeuralNetLearner   0.586   0.15   [0.5, 0.7, 0.8, 0.6, 0.4, 0.6, 0.8, 0.5, 0.6, 0.364]
NeuralNetLearner   0.586   0.15   [0.5, 0.7, 0.8, 0.6, 0.4, 0.6, 0.8, 0.5, 0.6, 0.364]

Process finished with exit code 0

'''