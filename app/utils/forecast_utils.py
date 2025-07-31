def predict(model, hour, day_of_week):
    return model.predict([[hour, day_of_week]])[0]
