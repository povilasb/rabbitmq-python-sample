src_dir = src


all:
	@echo "Usage:"
	@echo -e "\tmake produce - sends message to message broker."
	@echo -e "\tmake consule - receives message from message broker."
.PHONY: all


produce:
	python $(src_dir)/producer.py
.PHONY: produce


consume:
	python $(src_dir)/consumer.py
.PHONY: produce
