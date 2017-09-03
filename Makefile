
SPHINXOPTS    =
PAPER         =
SPHINXBUILD   = sphinx-build
BUILDDIR      = build

all: FORCE
	$(SPHINXBUILD) -b html $(SPHINXOPTS) ./content "$(BUILDDIR)/html"
	@echo " xdg-open \"$(BUILDDIR)/html/index.html\""

clean: FORCE
	rm -rf "$(BUILDDIR)/html" "$(BUILDDIR)/latex"

# TODO, different target!
upload: all FORCE
	rsync --progress -ave "ssh -p 22" $(BUILDDIR)/html/* ideasman42@download.blender.org:/data/ftp/ideasman42/donelist

FORCE:
