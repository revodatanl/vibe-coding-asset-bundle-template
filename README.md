# RevoData AI Assistant Asset Bundle Template for DLT

In today's fast-paced data engineering landscape, AI coding assistants are dramatically accelerating development cycles. Collaborating with AI is no longer just a luxury—it's becoming essential for teams that need to deliver robust Databricks solutions at scale.

However, tools like Cursor or Continue.dev often struggle to keep pace with Databricks' rapid release schedule, as the underlying models aren't trained and thus aware of the latest feature sets. This template bridges that gap by combining custom AI coding rules derived from current Databricks documentation with the power of Databricks Asset Bundles (DAB).

Whether you're building new data pipelines, implementing advanced transformations, or orchestrating comprehensive workflows, this template provides the foundation to accomplish it all with increased speed and effectiveness. We support both [Cursor Rules](https://docs.cursor.com/context/rules) and [Conintue.dev rules](https://docs.continue.dev/customize/deep-dives/rules).

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