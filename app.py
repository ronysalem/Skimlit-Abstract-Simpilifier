import streamlit  as st 

from predection import make_predictions
from preprocessing import create_input_dataframe,create_embeddings
import altair as alt

# Function to process the abstract and make predictions
def process_abstract(abstract):
    # Create input dataframe from the abstract
    data = [{'abstract': abstract}]
    example_df = create_input_dataframe(data)

    # Create embeddings from the dataframe
    example_sentences, example_chars, example_line_number_of_total_lines_one_hot, example_total_lines_one_hot = create_embeddings(example_df)

    # Make predictions using the preprocessed data
    example_abstract_pred_classes = make_predictions(example_line_number_of_total_lines_one_hot, example_total_lines_one_hot, example_sentences, example_chars)
    return example_sentences, example_abstract_pred_classes



# Main Streamlit app
def main():
    st.title("SkimLit Abstract Simplifier")

    # Text area for user to enter the abstract
    abstract = st.text_area("Enter the abstract here:", height=300)

    # Button to make predictions
    if st.button("Simplify Abstract"):
        # Check if abstract is not empty
        if abstract.strip():
            # Process abstract and get predictions
            sentences, pred_classes = process_abstract(abstract)

            # Initialize a dictionary to group sentences by their predicted class
            class_sentence_dict = {}

            # Group sentences by their predicted class
            for sentence, pred_class in zip(sentences, pred_classes):
                if pred_class not in class_sentence_dict:
                    class_sentence_dict[pred_class] = [sentence]
                else:
                    class_sentence_dict[pred_class].append(sentence)

            # Display sentences grouped by their predicted class
            for pred_class, sentences in class_sentence_dict.items():
                st.subheader(pred_class)
                for sentence in sentences:
                    st.write(sentence)
 







if __name__ == "__main__":
    main()