from tensorflow.keras.models import model_from_json


def get_model():
    # load json and create model
    json_file = open('data/model_acc6076_loss_11008.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("data/model_acc6076_loss_11008.h5")
    model.compile(loss = 'categorical_crossentropy', 
              optimizer = 'adam',
              metrics = ['accuracy'])
    return model