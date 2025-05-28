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
│       ├── databricks_general.mdc
│       └── delta_live_tables.mdc
├── mcp/               # optional; only if you choose to use the MCP
│   └── server.py
├── databricks.yml     # Main bundle configuration file
├── resources/         # Directory for resource definitions 
└── src/               # Source code directory
```

## Adding Latest Databricks Documentation 

We recommend indexing the following Databricks documentation, which will provide additional context to the IDE:

- [Databricks DLT Documentation](https://docs.databricks.com/aws/en/dlt)
- [Asset Bundle Template Documentation](https://docs.databricks.com/aws/en/dev-tools/bundles/)

This works slightly differently for each tool:

- Cursor: Add these resources using the [`@docs`](https://docs.cursor.com/context/@-symbols/@-docs) command.
- Continue.dev: Follow [this guide](https://docs.continue.dev/customize/deep-dives/docs) to index the additional documentation.

## Add the Model Context Protocol for Unity Catalog

Ideally the 'agents' in Cursor or Continue.dev can access Unity Catalog to look up table names and definitions. This can be achieved by adding a simple MCP Server. When you initialize this bundle, you will be asked if you want to add it. In order to activate it, you need to take a the following of steps.

### 1: Install UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2:  Move to the `mcp` folder and install all requirements

```bash
cd mcp
uv venv
uv sync
```

### 3: Configure your environment variables

For Cursor you need to adjust the `mcp.json`:

```json
{
    "mcpServers": {
        "revodata_databricks_mcp": {
            "command": "/Users/<username>/.local/bin/uv",
            "args": [
                "run",
                "--directory",
                "/Users/<other_paths>/mcp",
                "python",
                "server.py"
            ],
            "env": {
                "DATABRICKS_HOST": "{{workspace_host}}",
                "DATABRICKS_TOKEN": "<personal_access_token>"
            }
        }
    }
}
```

For Continue.dev you need to adjust the `revodata_databricks_mcp.yml`:

```yml
name: revodata_databricks_mcp
version: 0.0.1
schema: v1
mcpServers:
  - name: revodata_databricks_mcp
    command: /Users/<username>/.local/bin/uv # change <username> to your username
    args:
      - run
      - --directory
      - /Users/<other_paths>/mcp # in Cursor or VSCode simply copy the absolute path of the `mcp` folder
      - python
      - server.py
    env:
      DATABRICKS_HOST: {{workspace_host}}
      DATABRICKS_TOKEN: <personal_access_token> # insert your personal access token
```

## Contributing

Contributions to improve this template are welcome. Please feel free to submit issues or pull requests.
