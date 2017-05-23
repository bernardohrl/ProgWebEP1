Utilizado:

	Python: 3.5.2
	Pytest: 3.0.7
	Pytest-cov: 2.5.1
	FactoryBoy: 1.3.1
	Flake8: 3.3.0 (mccabe: 0.6.1, pycodestyle: 2.3.1, pyflakes: 1.5.0) CPython 3.5.2


Não sei se o pre-hook está atualizando, já que é feito dentro do .git, mas está funcionado localmente.

em: ProgWebEP1/.git/hooks/ , adicionar um arquivo 'pre-commit'

#Dentro do 'pre-commit'

echo "\n\nTesting.....\n\n"

# Se pytest falha, segue para o else a aborta o commit
if pytest; then
	echo "\n\n\n\n\n\t\t\t\tAll Tests Passed, commiting now!\n\n\n\n\n\n"

else
	echo "\n\n\n\n\n\t\t\t\tTests didn't Pass, aborting commit...\n\n\n\n\n"
	exit 1
fi	


Ou, pegue a pasta hook, entre em ProgWebEP1/.git/, delete a pasta atual e cole-a.
