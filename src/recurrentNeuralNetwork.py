import numpy as np 
import os
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from area import Area
from typing import List

def trainRNN(sequences: List[List[str]], filename: str, rnnUnits: int = 128, embeddingDim: int = 50,):

    areas = [location for seq in sequences for location in seq] #List of unique areas

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(areas) #Converts each location to an integer
    locationIndex = tokenizer.word_index #Index for dictionary 
    numLocations = len(locationIndex)

    paths = tokenizer.texts_to_sequences(sequences)
    x = [seq[:-1] for seq in paths] #Input sequences(all but the last area on the path)
    y = [seq[-1] for seq in paths] #Next location to predict

    sequenceLength = max(len(seq) for seq in x)
    x_padded = pad_sequences(x, maxlen=sequenceLength, padding='pre') #Pads each sequence to be the same length

    x_padded = np.array(x_padded)
    y = np.array(x)

    model = Sequential([
    Embedding(input_dim=numLocations + 1, output_dim=embeddingDim, input_length=sequenceLength),
    LSTM(rnnUnits, return_sequences=False),
    Dense(numLocations + 1, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(x_padded, y, epochs=10, batch_size=32, validation_split=0.2)

    currentDirectory = os.getcwd()
    modelPath = os.path.join(currentDirectory, filename + '.h5')
    model.save(modelPath)

def summariseModel(model):
    model.summary()

def evaluateModel(model, x, y):
    loss, accuracy = model.evaluate(x, y)
    print(f'Test Loss: {loss}')
    print(f'Test Accuracy: {accuracy}')


def predictNextArea(path: List[str], model) -> str:
    pathEncoded = tokenizer.texts_to_sequences([path])
    pathPadded = pad_sequences(pathEncoded, maxlen=path, padding='pre')
    predictedArea = model.predict(pathPadded)
    predictedAreaID = np.argmax(predictedArea, axis=1)[0]
    predictedAreaName = tokenizer.index_word[predictedAreaID]

    return predictedAreaName