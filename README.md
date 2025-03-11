# Nebula-nights
A VS code dark theme using blues, purples and pinks

## Colors

This theme uses the following color palette:
- Dark Blue: #404E5C (main background)
- Steel Blue: #4F6272 (inactive elements)
- Lavender: #B7C3F3 (main text)
- Pink: #DD7596 (keywords/ highlights)
- Magenta: #ECDA90 (constants)
- Light Blue: #83AFDF (strings)
- Bright Cyan: #63C5EA (functions)
- Pale Blue: #AED6F1 (parameters)
- Deep Lavender: #9F7EBE (punctuation)
- Pale Yellow: #D05786 (JSON properties)

## Screenshots

![Screenshot](https://github.com/Tom-Fynes/nebula-nights/blob/main/resources/Images/Screenshot.png)

## Installation

### VS Code Marketplace

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Nebula Nights
4. Click Install

### Manual Installation from GitHub Releases

1. Download the latest `.vsix` file from the [GitHub Releases](https://github.com/tom-fynes/nebula-nights/releases)
2. Open VS Code
3. Go to Extensions (Ctrl+Shift+X)
4. Click the "..." menu in the top-right of the Extensions panel
5. Select "Install from VSIX..."
6. Navigate to the downloaded `.vsix` file and select it

## Building and Contributing

### Prerequisites

- Node.js and npm
- [Visual Studio Code Extension Manager (vsce)](https://github.com/microsoft/vscode-vsce)

### Setup

```bash
# Clone the repository
git clone https://github.com/tom-fynes/nebula-nights.git

# Navigate to the project
cd nebula-nights

# Install dependencies
npm install
```

### Building

```bash
# Package the extension
npm run package
```

This will generate a `.vsix` file in the root directory.

## License

[MIT](LICENSE)
