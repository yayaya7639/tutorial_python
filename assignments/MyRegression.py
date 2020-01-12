

class MyLinearRegression(BaseEstimator, RegressorMixin):
    def __init__(self, lam = 1.0):
        self.lam = lam
        self.w_ = None
        
    def fit(self, X, y):
        
        X, y = check_X_y(X, y, y_numeric=True)
        if self.lam != 0:
            pass
        else:
            pass
        
        XX = np.c_[np.ones(X.shape[0]),X]
        I = np.eye(XX.shape[1])
        A = XX.T@XX + self.lam * I
        b = XX.T@y
        self.w_ = np.dot(np.linalg.inv(A),b)
        
        return self
    
    def predict(self, X):
        X = np.array(X)
        XX = np.c_[np.ones(X.shape[0]),X]
        y = np.dot(XX,self.w_)
        
        check_is_fitted(self, "w_") 
        XX = check_array(XX)
        return y
    

if __name__=="__main__":
	clf = MyRegression()
