all: 
	python3 -m pip install --upgrade build
	python3 -m build
	python3 -m pip install ./dist/ft_package-0.0.1-py3-none-any.whl --force-reinstall

clean:
	pip uninstall -y ft_package
	rm -rf ./dist

fclean: clean

re: fclean all

.PHONY: all clean fclean re
