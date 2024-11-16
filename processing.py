from sklearn.base import BaseEstimator, TransformerMixin

class FeatureConstructor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        # Extract title from name
        X['Title'] = X['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
        rare_titles = ['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona']
        X['Title'] = X['Title'].replace(rare_titles, 'Rare')
        # Family size
        X['FamilySize'] = X['SibSp'] + X['Parch'] + 1
        # Is alone
        X['IsAlone'] = (X['FamilySize'] == 1).astype(int)
        # Fare per person
        X['FarePerPerson'] = X['Fare'] / X['FamilySize']
        # Age * Class
        X['Age*Class'] = X['Age'] * X['Pclass']
        return X