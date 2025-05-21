# RevoData Vibe Coding Asset Bundle Template for DLT

In today's fast-paced data engineering landscape, AI coding assistants are dramatically accelerating development cycles. Collaborating with AI is no longer just a luxury—it's becoming essential for teams that need to deliver robust solutions at scale. However, the vibes for Databricks are not yet there. This Databricks Asset Bundles (DAB) template is designed to help developers use the latest Databricks features with AI coding assistants.

Tools like Cursor or Continue.dev often struggle to keep pace with Databricks' rapid release schedule, as the underlying models were trained months ago and thus are not aware of the latest feature sets. This template bridges that gap by combining custom AI coding rules derived from the latest Databricks documentation with the power of DAB. With the end goal of assisting you in building and deploying DLT pipelines with ease. We support both [Cursor Rules](https://docs.cursor.com/context/rules) and [Conintue.dev Rules](https://docs.continue.dev/customize/deep-dives/rules).

## Getting Started

### Prerequisites

- [Databricks CLI](https://docs.databricks.com/dev-tools/cli/index.html)
- Access to a Databricks workspace
- Some experience with Databricks Asset Bundles
- Cursor IDE or Continue.dev extension

### Creating a New Project

Initialize the asset bundle template and deploy it to your workspace:

```bash
databricks bundle init https://github.com/revodatanl/cursor-asset-bundle-template.git --profile <profile>
databricks bundle deploy --target dev
```

### Project Structure

After initialization (for Cursor), your project will have the following structure:

```bash
your-project-name/
├── .cursor/
│   └── rules/
│       ├── databricks_asset_bundles.mdc
│       └── delta_live_tables.mdc
├── databricks.yml     # Main bundle configuration file
├── resources/         # Directory for resource definitions 
└── src/               # Source code directory
```

## Adding latest Databricks Documentation to model context

We recommend indexing the following Databricks documentation, this will provide additional context to the IDE:

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
