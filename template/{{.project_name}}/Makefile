list-catalogs:
	@read -p "Enter profile name (default: $(PROFILE)): " input_profile; \
	read -p "Enter output file name (default: catalogs.json): " input_file; \
	profile=$${input_profile:-$(PROFILE)}; \
	file=$${input_file:-catalogs.json}; \
	mkdir -p run; \
	databricks catalogs list --profile $$profile -o json > run/$$file; \
	echo "Catalogs list saved to run/$$file"

list-schemas:
	@read -p "Enter catalog name: " input_catalog; \
	read -p "Enter profile name (default: $(PROFILE)): " input_profile; \
	read -p "Enter output file name (default: schemas.json): " input_file; \
	catalog=$${input_catalog}; \
	profile=$${input_profile:-$(PROFILE)}; \
	file=$${input_file:-schemas.json}; \
	mkdir -p run; \
	databricks schemas list $$catalog --profile $$profile -o json > run/$$file; \
	echo "Schemas list saved to run/$$file"

list-tables:
	@read -p "Enter catalog name: " input_catalog; \
	read -p "Enter schema name: " input_schema; \
	read -p "Enter profile name (default: $(PROFILE)): " input_profile; \
	read -p "Enter output file name (default: tables.json): " input_file; \
	catalog=$${input_catalog}; \
	schema=$${input_schema}; \
	profile=$${input_profile:-$(PROFILE)}; \
	file=$${input_file:-tables.json}; \
	mkdir -p run; \
	databricks tables list $$catalog $$schema --profile $$profile -o json > run/$$file; \
	echo "Tables list saved to run/$$file"

# Creates a JSON file with all tables from all catalogs and schemas
export-tables:
	@read -p "Enter profile name (default: $(PROFILE)): " input_profile; \
	profile=$${input_profile:-$(PROFILE)}; \
	mkdir -p run; \
	echo "Exporting all tables from all catalogs and schemas..."; \
	echo "[]" > run/all_tables.json; \
	echo "Getting catalog list..."; \
	databricks catalogs list --profile $$profile -o json > run/temp_catalogs.json; \
	echo "Processing catalogs..."; \
	for catalog in $$(jq -r ".[].name" run/temp_catalogs.json); do \
		echo "Processing catalog: $$catalog"; \
		databricks schemas list "$$catalog" --profile $$profile -o json > run/temp_schemas.json; \
		for schema in $$(jq -r ".[].name" run/temp_schemas.json); do \
			echo "Processing schema: $$catalog.$$schema"; \
			databricks tables list "$$catalog" "$$schema" --profile $$profile -o json > run/temp_tables.json; \
			if [ -s run/temp_tables.json ]; then \
				jq -c '.[] | { \
					namespace: (.catalog_name + "." + .schema_name + "." + .name), \
					columns: [.columns[].name] \
				}' run/temp_tables.json | while read -r table; do \
					table_name=$$(echo "$$table" | jq -r '.namespace' | cut -d'.' -f3); \
					echo "Processing table: $$catalog.$$schema.$$table_name"; \
					echo "$$table" > run/temp_table.json; \
					jq -s '.[0] + [.[1]]' run/all_tables.json run/temp_table.json > run/all_tables_new.json; \
					mv run/all_tables_new.json run/all_tables.json; \
				done; \
				rm -f run/temp_table.json; \
			fi; \
		done; \
	done; \
	rm -f run/temp_catalogs.json run/temp_schemas.json run/temp_tables.json; \
	echo "All tables exported to run/all_tables.json"