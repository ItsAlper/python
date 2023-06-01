import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import numpy as np

# Typy emailů
emails = [
    "example@example.com",
    "invalid.email",
    "another@example.com",
    "notvalid@",
    "test123@test.com"
]

features = np.array([len(email) for email in emails])
# 0 označuji neplatnou emailovou adresu, 1 označuji platnou emailovou adresu
labels = np.array([1, 0, 1, 0, 1])

features = (features - features.min()) / (features.max() - features.min())

# V této části vytvářím model
model = Sequential()
model.add(Dense(1, activation='sigmoid', input_shape=(1,)))

# Kompilace modelu
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Trénování modelu
model.fit(features, labels, epochs=50)

# Ověřuji nové emailové adres
new_emails = [
    "hello@example.com",
    "invalid",
    "test@test.com",
    "notvalidemail",
    "example123@example.com"
]

new_features = np.array([len(email) for email in new_emails])
new_features = (new_features - features.min()) / (features.max() - features.min())

# Klasifikuji nových emailů
predictions = model.predict(new_features)

# Výsledek
for email, prediction in zip(new_emails, predictions):
    is_valid = 'platná' if prediction >= 0.5 else 'neplatná'
    print(f"Email: {email} je {is_valid}")
