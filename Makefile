task_%:
	python lib/tasks/day_$*.py lib/tasks/data/day_$*.txt

test_%:
	pytest lib/tests/test_day_$*.py

init_%:
	touch lib/tasks/day_$*.py lib/tests/test_day_$*.py lib/tasks/data/day_$*.txt lib/tests/data/test_day_$*.txt
