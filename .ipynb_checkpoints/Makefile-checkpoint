
# creates and configures the environment
.PHONY: env
env:
	conda env create -f environment.yml
	bash -ic 'conda activate ligo;python -m ipykernel install --user --name ligo --display-name "IPython - ligo"'


# build the JupyterBook normally (calling jupyterbook build .)
.PHONY: html
html:
	jupyter-book build .
	
	
# build the JupyterBook so that you can view it on the hub with the URL proxy trick as indicated above
.PHONY: html-hub
html-hub:
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	
	
# clean up the figures, audio and _build folders
.PHONY: clean
clean:
	rm -f audio/*.wav
	rm -f figurs/*.png
	rm -r _build