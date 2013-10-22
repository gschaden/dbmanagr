BUILD = build
SOURCES = src/pkg src/images src/info.plist
ARCHIVE = $(BUILD)/dbexplorer_alfred_0.1.tgz
ALFRED_WORKFLOW = /Volumes/Storage/Dropbox/Alfred/Alfred.alfredpreferences/workflows/user.workflow.FE656C03-5F95-4C20-AB50-92A1C286D7CD
TESTS = $(shell echo test/resources/*.sh)
ACTUALS = $(TESTS:test/resources/%.sh=build/test/%.actual)

init:
	mkdir -p $(BUILD)/ $(BUILD)/test $(BUILD)/files

clean:
	rm -rf $(BUILD)

assemble: init _assemble

_assemble: $(SOURCES)
	rm -rf $(BUILD)/files
	mkdir -p $(BUILD)/files
	cp -r $^ $(BUILD)/files

archive: assemble
	rm -f $(ARCHIVE)
	tar -C $(BUILD)/files -czf $(ARCHIVE) --exclude=.DS_Store --exclude="*.sketch" .

build: archive test

install: build
	tar -C $(ALFRED_WORKFLOW) -xzf $(ARCHIVE)

test: assemble $(ACTUALS)

$(BUILD)/test/%.actual: test/resources/%.sh
	test/test.sh $^
