# Makefile to automate the build of different parts of the project

JUP_DIR=src/jupyter

all: docker slides

slides:
    # To exclude all input cells \
	  To remove specific input cells, add tag 'hide' to the cell \
	  --TagRemovePreprocessor.remove_input_tags={\"hide\"}
	jupyter nbconvert $(JUP_DIR)/presentation.ipynb \
    --SlidesExporter.reveal_scroll=True \
	--to slides

slides_sans_input:
	jupyter nbconvert $(JUP_DIR)/presentation.ipynb \
	--TemplateExporter.exclude_input=True \
	--SlidesExporter.reveal_scroll=True \
	--to slides

docker:
	docker build -t tfg_tools util/tfg_tools
	docker build -t data_script util/data_script
