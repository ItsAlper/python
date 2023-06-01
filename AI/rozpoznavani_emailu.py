import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import numpy as np

# Typy emailů
emails = [
    "notvalid@",
    "karel@test.com"
    "tomas@something.com",
    "invalid.email",
    "vitek@word.com",
]

# 0 označuji neplatnou emailovou adresu, 1 označuji platnou emailovou adresu
features = np.array([len(email) for email in emails])
labels = np.array([1, 0, 1, 0, 1])
features = (features - features.min()) / (features.max() - features.min())
# V této části vytvářím model
model = Sequential()
model.add(Dense(1, activation='sigmoid', input_shape=(1,)))
# Kompilace a trénoví modelu
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(features, labels, epochs=50)

# Nové emaily, následné ověřování
new_emails = [
    "hello@example.com",
    "invalid",
    "test@test.com",
    "notvalidemail",
    "example123@example.com"
]
new_features = np.array([len(email) for email in new_emails])
new_features = (new_features - features.min()) / (features.max() - features.min())
predictions = model.predict(new_features)

# Výsledek
for email, prediction in zip(new_emails, predictions):
    is_valid = 'platná' if prediction >= 0.5 else 'neplatná'
    print(f"Email: {email} je {is_valid}")
