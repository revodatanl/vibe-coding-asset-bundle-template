# RevoData Vib Coding Asset Bundle Template for DLT

In today's fast-paced data engineering landscape, AI coding assistants are dramatically accelerating development cycles. Collaborating with AI is no longer just a luxury—it's becoming essential for teams that need to deliver robust Databricks solutions at scale.

Tools like Cursor or Continue.dev often struggle to keep pace with Databricks' rapid release schedule, as the underlying models are trained months ago, and thus are not aware of the latest feature sets. This template bridges that gap by combining custom AI coding rules derived from latest Databricks documentation with the power of Databricks Asset Bundles (DAB).

Whether you're building new DLT data pipelines, implementing advanced transformations, or orchestrating comprehensive workflows, this template provides the foundation to accomplish it all with increased speed and effectiveness, we support both [Cursor Rules](https://docs.cursor.com/context/rules) and [Conintue.dev](https://docs.continue.dev/customize/deep-dives/rules) rules.

## Getting Started

### Prerequisites

- [Databricks CLI](https://docs.databricks.com/dev-tools/cli/index.html) installed
- Access to a Databricks workspace
- Some experience with Databricks Asset Bundles
- Cursor IDE or Continue.dev extension

### Creating a New Project

1. Initialize the asset bundle template: 
 
    ```BASH
    databricks bundle init https://github.com/revodatanl/cursor-asset-bundle-template.git --profile <profile>
    ```

*Alternatively, you can clone this repository to expand the template to fit your needs.*

2. Deploy the example DLT pipeline to your workspace: 

    ```BASH 
    databricks bundle deploy --target dev
    ```

### Project Structure

After initialization (for Cursor), your project will have the following structure:

```TEXT
your-project-name/
├── .cursor/
│   └── rules/
│       ├── databricks_asset_bundles.mdc
│       └── delta_live_tables.mdc
├── databricks.yml     # Main bundle configuration file
├── resources/         # Directory for resource definitions 
└── src/               # Source code directory
```

## Additional IDE Configuration

We recommend indexing the following Databricks documentation:

- [Databricks DLT Documentation](https://docs.databricks.com/aws/en/dlt)
- [Asset Bundle Template Documentation](https://docs.databricks.com/aws/en/dev-tools/bundles/)

### For Cursor

Add these resources using the [`@docs`](https://docs.cursor.com/context/@-symbols/@-docs) command alongside the standard Cursor rules.

Additionally, consider integrating the Databricks [Model Context Protocol (MCP)](https://github.com/databrickslabs/mcp?tab=readme-ov-file#unity-catalog-server) developed by Databricks Labs. Learn how to [add MCP to Cursor here](https://docs.cursor.com/context/model-context-protocol).

### For Continue.dev

Similarly, we recommend indexing additional documentation in Continue.dev:

- Follow [this guide](https://docs.continue.dev/customize/deep-dives/docs) to index the additional documentation.
- MCP is also supported in Continue.dev - implementation details can be found [here](https://docs.continue.dev/customize/deep-dives/mcp)

## Contributing

Contributions to improve this template are welcome. Please feel free to submit issues or pull requests.