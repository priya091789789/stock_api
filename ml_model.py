from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def train_predictor(df):
    df = df.dropna().copy()
    df['MACD'] = df['Close'].ewm(span=12).mean() - df['Close'].ewm(span=26).mean()
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)

    features = ['RSI', 'MA20', 'MA50', 'MACD', 'Volume']
    X = df[features].iloc[:-1]
    y = df['Target'].iloc[:-1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = DecisionTreeClassifier().fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    return model, accuracy
