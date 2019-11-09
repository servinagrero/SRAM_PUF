# Makefile to automate the build of different parts of the project

JUP_DIR=src/jupyter
DOCKER_IMG=tfg_tools

all: docker slides

slides:
    # To exclude all input cells \
	  jupyter nbconvert --TemplateExporter.exclude_input=True --to slides my_notebook.ipynb \
	  To remove specific input cells, add tag 'hide' \
	  --TagRemovePreprocessor.remove_input_tags={\"hide\"}
	jupyter nbconvert $(JUP_DIR)/viewer.ipynb --to slides

docker:
	@cp -r $(JUP_DIR) util/Docker
	docker build -t $(DOCKER_IMG) util/Docker
