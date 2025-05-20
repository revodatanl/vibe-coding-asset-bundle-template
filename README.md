# Revo Vibe Code Asset Bundle Template

A template repository for creating Databricks Asset Bundles (DAB) projects with Vibe Coding support. This template provides a basic foundation for developing, deploying, and managing Databricks assets using the Asset Bundle framework, enriched with either [Cursor Rules](https://docs.cursor.com/context/rules) or [Conintue.dev rules](https://docs.continue.dev/customize/deep-dives/rules).

## Getting Started

### Prerequisites

- [Databricks CLI](https://docs.databricks.com/dev-tools/cli/index.html) installed
- Access to a Databricks workspace
- Cursor IDE or Continue.dev extension

### Creating a New Project

1. Initialize the asset bundle template: 
 
    ```BASH
    databricks bundle init https://github.com/revodatanl/cursor-asset-bundle-template.git --profile <profile>
    ```

2. Deploy and run the asset bundle to your workspace: 

    ```BASH 
    databricks bundle deploy --target dev
    ```

Alternatively, you can clone this repository to expand the template to fit your needs.

### Project Structure

After initialization (for Cursor), your project will have the following structure:

```
your-project-name/
├── .cursor/
│   └── rules/
│       ├── databricks_asset_bundles_cursor_rules.mdc
│       └── delta_live_tables.mdc
├── databricks.yml     # Main bundle configuration file
├── resources/         # Directory for resource definitions 
└── src/               # Source code directory
```

### Additional Cursor Configuration

We recommend indexing the Databricks [DLT documentation](https://docs.databricks.com/aws/en/dlt) and the [Asset Bundle Template documentation]() in addition to the Cursor rules. You can do this by using the [`@docs`](https://docs.cursor.com/context/@-symbols/@-docs) command.

Furthermore, you can also add the Databricks [MCP](https://github.com/databrickslabs/mcp?tab=readme-ov-file#unity-catalog-server), which is being developed by Databricks Labs. See how to [add MCP to Cursor](https://docs.cursor.com/context/model-context-protocol).

## Contributing

Contributions to improve this template are welcome. Please feel free to submit issues or pull requests.