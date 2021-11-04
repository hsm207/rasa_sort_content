import click
import yaml
from rasa.shared.nlu.training_data.loading import load_data
from rasa.shared.utils.io import write_text_file


def read_nlu_file(file_path):
    """
    Reads an nlu file given its path
    """
    nlu_data = load_data(file_path)
    return nlu_data


def write_nlu_file(nlu, output_path):
    """
    Writes the dict_file into a yaml at output_path
    """
    write_text_file(nlu.nlu_as_yaml(), output_path)


def sort_intent_examples(training_examples):
    """
    Sorts the examples in an intent dictionary
    """

    def f(x): return (x.get("intent", None), x.get("text", None))

    return sorted(training_examples, key=f)


@click.command()
@click.option(
    "--nlu_file",
    default="nlu.yml",
    help="Full path to the nlu file that needs to be sorted",
)
@click.option(
    "--output_file",
    default="nlu_sorted.yml",
    help="Full path to save the sorted nlu file",
)
def main(nlu_file, output_file):
    nlu = read_nlu_file(nlu_file)

    training_examples = nlu.training_examples
    sorted_training_examples = sort_intent_examples(training_examples)

    nlu.training_examples = sorted_training_examples

    write_nlu_file(nlu, output_file)


if __name__ == "__main__":
    main()
