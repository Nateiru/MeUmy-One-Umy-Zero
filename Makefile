compile : template.tex check
	xelatex -shell-escape template.tex
	xelatex -shell-escape template.tex
update : template.tex
	xelatex -shell-escape template.tex
check : template.tex
	python check.py
clean : template.tex
	del template.aux
	del template.log
	del template.out
	del template.toc
	rmdir /s /q _minted-template
