install:
	poetry install

make sort:
	poetry run python rasa_sort_content/main.py  --nlu_file $(NLU_FILE) \
		--output_file $(OUTPUT_FILE)

make help:
	poetry run python rasa_sort_content/main.py  --help