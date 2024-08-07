import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from data_processing import load_and_process_data

# Load and preprocess data
data_directory = 'plugins'  # Directory where plugins are stored
processed_data = load_and_process_data(data_directory)

# Function to prepare data for training
def prepare_data(processed_data):
    x_train = []
    y_train = []
    for item in processed_data:
        commands_and_events = item['commands'] + item['events']
        x_train.append(commands_and_events)
        y_train.append(item['name'])
    return np.array(x_train), np.array(y_train)

x_train, y_train = prepare_data(processed_data)

# Define the model
model = Sequential([
    Embedding(input_dim=10000, output_dim=64, input_length=len(x_train[0])),
    LSTM(128, return_sequences=True),
    Dropout(0.5),
    LSTM(128),
    Dense(256, activation='relu'),
    BatchNormalization(),
    Dropout(0.5),
    Dense(128, activation='relu'),
    BatchNormalization(),
    Dropout(0.5),
    Dense(10000, activation='softmax')  # Adjust output_dim as needed
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Callbacks
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
model_checkpoint = ModelCheckpoint('best_model.h5', monitor='val_loss', save_best_only=True)

# Train the model
model.fit(x_train, y_train, epochs=50, validation_split=0.2, callbacks=[early_stopping, model_checkpoint])
