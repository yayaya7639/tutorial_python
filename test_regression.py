from assignments.MyRidgeRegression import MyRidgeRegression
from sklearn.utils.estimator_checks import check_estimator


def test_scikit():
	check_estimator(MyRidgeRegression)


def test_score():
	
