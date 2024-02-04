import tensorflow_text as text
import tensorflow as tf 




def make_predictions(example_line_number_of_total_lines_one_hot,example_total_lines_one_hot,example_sentences,example_chars):
    loaded_model = tf.keras.models.load_model("/content/Skimlit-Abstract-Simpilifier/Skimlit/skimlit-Model")

    
    example_pred_probs = loaded_model.predict(x = (example_line_number_of_total_lines_one_hot,
                                               example_total_lines_one_hot,
                                                tf.constant(example_sentences), 
                                                tf.constant(example_chars)))
    example_preds = tf.argmax(example_pred_probs, axis=1)
    
    classes = ["BACKGROUND","CONCLUSIONS", "METHODS", "OBJECTIVE", "RESULTS"]
    class_dict = {i: class_name for i, class_name in enumerate(classes)}
    
    example_preds_list = example_preds.numpy().tolist()
    example_abstract_pred_classes = [class_dict[i] for i in example_preds_list]
    
    
    return example_abstract_pred_classes
