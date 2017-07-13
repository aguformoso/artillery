docker run --rm -ti \
	-v $(pwd)/data:/data \
	-v $(pwd)/bin:/bin \
	lacniclabs/artillery $@
