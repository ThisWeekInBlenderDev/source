
SPHINXOPTS    =
PAPER         =
SPHINXBUILD   = sphinx-build
BUILDDIR      = build

all: FORCE
	$(SPHINXBUILD) -b html $(SPHINXOPTS) ./content "$(BUILDDIR)/html"
	@echo " xdg-open \"$(BUILDDIR)/html/index.html\""

clean: FORCE
	rm -rf "$(BUILDDIR)/html"

upload: all FORCE
	if [ -d "docs/.git" ]; then \
		rsync \
			-av \
			--exclude=".doctrees" \
			--filter='protect .git' \
			--delete \
			--delete-excluded \
			--prune-empty-dirs \
			./build/html/ ./docs/ ; \
		cd docs ; \
		git add -A ; \
		git commit -m "$$(date '+%Y-%m-%d %H:%M:%S')" ; \
		git push --force; \
	fi \

FORCE:
