import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import numpy as np

# Příklady emailových adres
emails = [
    "example@example.com",
    "invalid.email",
    "another@example.com",
    "notvalid@",
    "test123@test.com"
]

# Příznaky pro trénování modelu
features = np.array([len(email) for email in emails])
# 1 označuje platnou emailovou adresu, 0 označuje neplatnou emailovou adresu
labels = np.array([1, 0, 1, 0, 1])

# Normalizace příznaků
features = (features - features.min()) / (features.max() - features.min())

# Vytvoření modelu
model = Sequential()
model.add(Dense(1, activation='sigmoid', input_shape=(1,)))

# Kompilace modelu
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Trénování modelu
model.fit(features, labels, epochs=50)

# Ověření nových emailových adres
new_emails = [
    "hello@example.com",
    "invalid",
    "test@test.com",
    "notvalidemail",
    "example123@example.com"
]

# Normalizace příznaků nových emailů
new_features = np.array([len(email) for email in new_emails])
new_features = (new_features - features.min()) / (features.max() - features.min())

# Klasifikace nových emailů
predictions = model.predict(new_features)

# Výpis výsledků
for email, prediction in zip(new_emails, predictions):
    is_valid = 'platná' if prediction >= 0.5 else 'neplatná'
    print(f"Email: {email} je {is_valid}")
