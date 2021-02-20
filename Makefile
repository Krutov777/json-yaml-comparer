lint:
	poetry run flake8 gendiff
run_test:
	poetry run pytest
package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall
publish:
	poetry publish --dry-run
