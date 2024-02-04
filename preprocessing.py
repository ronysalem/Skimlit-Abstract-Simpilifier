import pandas as pd
import tensorflow as tf 

def create_input_dataframe(data):
    example_samples = []

    for entry in data:
        abstract_lines = entry["abstract"].splitlines()

        for abstract_line in abstract_lines:
            abstract_lines_split = abstract_line.split('. ')

            for abstract_line_number, line_text in enumerate(abstract_lines_split):
                if line_text != "":
                    line_data = {
                        "text": line_text.lower(),
                        "line_number": abstract_line_number,
                        "total_lines": len(abstract_lines_split) - 1,
                        "line_number_of_total_lines": str(abstract_line_number) + '_of_' + str(len(abstract_lines_split) - 1)
                    }

                    example_samples.append(line_data)

    example_df = pd.DataFrame(example_samples)

    return example_df


def split_chars(text):
  return " ".join(list(text))

def create_embeddings(example_df):
    # Extract the numeric part and convert to integers for 'line_number_of_total_lines'
    example_df['line_number_of_total_lines'] = example_df['line_number_of_total_lines'].apply(lambda x: int(x.split('_of_')[0]) if isinstance(x, str) else x)

    # Get the text and characters
    example_sentences = example_df["text"].tolist()
    example_chars = [split_chars(sentence) for sentence in example_sentences]

    # One-hot encoding
    example_line_number_of_total_lines_one_hot = tf.one_hot(example_df["line_number_of_total_lines"].to_numpy(), depth=460)
    example_total_lines_one_hot = tf.one_hot(example_df["total_lines"].to_numpy(), depth=20)

    return example_sentences, example_chars, example_line_number_of_total_lines_one_hot, example_total_lines_one_hot