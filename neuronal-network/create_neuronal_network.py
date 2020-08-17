import numpy as np
from keras.utils.vis_utils import plot_model
from keras.models import Model, Sequential
from keras.layers import Input, Dense, Dropout, Concatenate  # Merge
from keras.layers.merge import concatenate
from keras.optimizers import Adam
import sys
import random
import os

from load import load_data, load_data_e


def create_nn(n_input_layers, n_output_layers):
    # Creates the NN model, then return it.

    # Input layer
    input = Input(shape=(n_input_layers,))

    # Hidden layer
    hidden_layer = Dense(units=16*10, activation='relu')(input)
    hidden_layer = Dense(units=16*5, activation='relu')(hidden_layer)
    hidden_layer = Dense(units=16, activation='relu')(hidden_layer)
    #hidden_layer = Dense(units=16, activation='relu')(hidden_layer)

    # Output layer
    output_layer = Dense(units=n_output_layers,
                         activation='softmax')(hidden_layer)

    model = Model(inputs=input, outputs=output_layer)

    # Compile
    optimizer = Adam()
    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizer, metrics=['accuracy'])

    return model


def nn_read_samples(batch_size):
    global training_data
    x_sample, y_sample = load_data(batch_size, training_data)
    return [x_sample, y_sample]


def nn_read_evaluation_samples(batch_size):
    global validation_data
    x_sample, y_sample = load_data_e(batch_size, validation_data)
    return [x_sample, y_sample]


def generator(batch_size):
    while 1:
        yield nn_read_samples(batch_size)


def validation_generator(batch_size):
    while 1:
        yield nn_read_evaluation_samples(batch_size)


def see_weights(model):
    for capa in model.layers:
        print("weights: ", capa.get_weights())


def load_files(data, initial, final):
    for i in range(initial, final):
        fo = open('../data/ida-solutions/sol_ida_problem_'+str(i)+'_.txt')
        for l in fo.readlines():
            data.append(l)
        fo.close()
    random.shuffle(data)


# training
os.environ["THEANO_FLAGS"] = "device=cpu,floatX=float32,mode=FAST_RUN,allow_gc=False"
PLOT_IMAGE_FILE_NAME = "model_diagram"
#TOTAL_FILES = 30367
TRIANING_FILES = 27367
VALIDATION_FILES = 3000

training_data = []
validation_data = []

# cargar en trainging_data una lista con todos los datos para trining
load_files(training_data, 0, TRIANING_FILES)
# cargar en validation_data una lista con todos los datos para validation
load_files(validation_data, TRIANING_FILES, TRIANING_FILES + VALIDATION_FILES)

TRAINING_STATES_AMOUNT = len(training_data)
VALIDATION_STATES_AMOUNT = len(validation_data)


BATCH_SIZE = 300
EPOCHS = 5

# cuantos batches tomo por epoch -> ideal : total/batchsize
STEPS_PER_EPOCH = int(TRAINING_STATES_AMOUNT/BATCH_SIZE)
VALIDATION_STEPS = int(VALIDATION_STATES_AMOUNT/BATCH_SIZE)


if __name__ == "__main__":
    test_mode = False
    debugger = False

    model = create_nn(16*16, 4)
    if debugger:
        plot_model(model, to_file=(
            PLOT_IMAGE_FILE_NAME + '.png'), show_shapes=True)
        see_weights(model)
        # model.summary()

    model.fit_generator(
        epochs=EPOCHS,
        generator=generator(BATCH_SIZE),
        steps_per_epoch=STEPS_PER_EPOCH,
        # validation_data=validation_generator(BATCH_SIZE),
        # validation_steps=VALIDATION_STEPS,
        verbose=1
    )
    import time
    time.sleep(5)
    print("\n\t*** EVALUATION: ***")
    evaluation = model.evaluate_generator(
        generator=validation_generator(BATCH_SIZE),
        steps=VALIDATION_STEPS,
        verbose=1
    )
    print(evaluation)
    model.save('15puzzle_solver_model_v22.h5')

    if test_mode:
        test(model)
