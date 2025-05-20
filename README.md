# Revo Cursor Asset Bundle Template

A template repository for creating Databricks Asset Bundles (DAB) projects with Cursor IDE support. This template provides a basic foundation for developing, deploying, and managing Databricks assets using the Asset Bundle framework.

## Overview

This repository serves as a template for creating new Databricks Asset Bundle projects. It includes:

- A templated project structure that follows Databricks Asset Bundle best practices
- Configuration for seamless development in Cursor IDE
- Basic deployment configuration for development environments

## Getting Started

### Prerequisites

- [Databricks CLI](https://docs.databricks.com/dev-tools/cli/index.html) installed
- Access to a Databricks workspace
- Cursor IDE

### Creating a New Project

1. Initialize the asset bundle template: `databricks bundle init https://github.com/revodatanl/deepseek-r1-asset-bundle-template --profile <profile>`
2. Deploy and run the asset bundle to your workspace: `databricks bundle deploy --target dev`

Alternatively you can also clone this repository to expand the template to fit your use-case.

### Project Structure

After initialization, your project will have the following structure:

```
.cursor
├── rules
└──── delta_live_tables.mdc
your-project-name/
├── databricks.yml     # Main bundle configuration file
├── resources/         # Directory for resource definitions (jobs, pipelines, etc.)
└── src/               # Source code directory
```

## Development Workflow

1. Define your resources in the `resources/` directory using YAML files
2. Write your code in the `src/` directory
3. Test your deployment locally:

```bash
databricks bundle deploy --target dev
```

4. Verify your resources in the Databricks workspace

## Advanced Configuration

The `databricks.yml` file supports various configuration options:

- Different deployment targets (dev, staging, prod)
- Workspace-specific settings
- Resource inclusion patterns
- And more

Refer to the [Databricks Asset Bundle documentation](https://docs.databricks.com/dev-tools/bundles/index.html) for detailed configuration options.

## Contributing

Contributions to improve this template are welcome. Please feel free to submit issues or pull requests.