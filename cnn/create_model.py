from keras.layers import Dense, Input
from keras.layers import Flatten
from keras.layers import Conv1D
from keras.layers import MaxPooling1D, Dropout
from keras.layers import Activation
from keras.models import Model
from keras.optimizers import SGD
from keras.regularizers import l2
# custom R2-score metrics for keras backend
from keras import backend as K


# coefficient of determination (R^2) for regression  (only for Keras tensors)
def r_square(y_true, y_pred):
	SS_res =  K.sum(K.square(y_true - y_pred))
	SS_tot = K.sum(K.square(y_true - K.mean(y_true)))
	return ( 1 - SS_res/(SS_tot + K.epsilon()) )


def load_model(input_shape, trained=False, weight_path=''):
	inputs = Input(shape=input_shape)
	x = Conv1D(64, kernel_size=749, activation='relu', name='conv1', kernel_regularizer=l2(0.0000001))(inputs)
	x = MaxPooling1D(name='pool')(x)
	x = Dropout(0.2)(x)
	x = Flatten(name='flatten')(x)
	x = Dense(128, activation='relu', name='fc1')(x)
	x = Dense(1, name='fc2')(x)
	predictions = Activation('linear')(x)
	#predictions = Activation('sigmoid')(x)
	model = Model(outputs=predictions, inputs=inputs)

	#opt = SGD(lr=0.1, momentum=0.9)
	#model.compile(loss='mean_squared_error', optimizer=opt, metrics=[r_square, 'mse'])

	if trained:
		model.load_weights(weight_path)

	model.compile(optimizer='adam', loss='mse', metrics=[r_square, 'mse'])
	return model
