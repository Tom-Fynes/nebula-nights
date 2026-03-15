# Nebula-nights
A VS Code theme collection using blues, purples, and pinks — available in dark, light, and additional variants.

## Themes

### Nebula Nights (Dark)
The original dark theme featuring deep blues, purples, and pinks.

### Nebula Nights Light
A light counterpart to Nebula Nights using the same colour palette, adapted for bright backgrounds. Dark blues become text colours, while the pastel accents are deepened for readability.

### Sakura (Dark)
A warm dark theme inspired by cherry blossoms — deep purples and pinks with soft spring greens and sky blues as accents.

### Tokyo Nights (Dark)
A neon-accented dark theme inspired by the glow of city lights at night — deep blue-purple backgrounds with bright cyan, green, and amber highlights.

### By the Sea (Light)
A calm light theme inspired by the ocean — soft blues and whites with teal, coral, and sandy gold accents.

## Colors

### Nebula Nights (Dark) Palette
- Dark Blue: `#404E5C` (main background)
- Steel Blue: `#4F6272` (inactive elements)
- Lavender: `#B7C3F3` (main text)
- Pink: `#DD7596` (keywords/highlights)
- Gold: `#ECDA90` (JSON properties)
- Light Blue: `#83AFDF` (strings)
- Bright Cyan: `#63C5EA` (functions)
- Pale Blue: `#AED6F1` (parameters)
- Deep Lavender: `#9F7EBE` (punctuation)
- Deep Pink: `#D05786` (constants)

### Nebula Nights Light Palette
Same colour palette as the dark theme, adapted for light backgrounds:
- Background: `#F4F5FF` (light lavender-white)
- Text: `#2E3A48` (dark blue)
- Keywords: `#B83060` (deepened pink)
- Functions: `#0D7BA8` (deepened cyan)
- Strings: `#2A6898` (deepened blue)
- Operators/Punctuation: `#6B4F9E` (deepened purple)

### Sakura Palette
- Background: `#1E1520` (deep warm purple)
- Text: `#F2CEE0` (soft pink-white)
- Keywords: `#F070A0` (hot pink)
- Functions: `#FFB8D0` (light pink)
- Classes: `#FF7BAC` (medium pink)
- Operators: `#C890C8` (lavender)

### Tokyo Nights Palette
- Background: `#1A1B2E` (deep blue-purple)
- Text: `#C0CAF5` (light blue-lavender)
- Keywords: `#BB9AF7` (bright purple)
- Functions: `#7AA2F7` (neon blue)
- Strings: `#9ECE6A` (green)
- Operators: `#89DDFF` (bright cyan)
- Classes: `#FF9E64` (neon orange)

### By the Sea Palette
- Background: `#F0F8FF` (alice blue)
- Text: `#0A3050` (deep navy)
- Keywords: `#0060A0` (ocean blue)
- Functions: `#0080C0` (clear ocean blue)
- Strings: `#006E6E` (deep teal)
- Classes: `#C06820` (sandy coral)
- Operators: `#5070A0` (steel blue)

## Screenshots

![Screenshot](https://github.com/Tom-Fynes/nebula-nights/blob/main/resources/Images/Screenshot.png)

## Installation

### VS Code Marketplace

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Nebula Nights"
4. Click Install
5. Open the Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
6. Type **Preferences: Color Theme** and select your preferred theme

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

## Platform Support

All themes work on **Windows**, **Linux**, and **macOS** — VS Code theme files are platform-independent JSON files.

## License

[MIT](LICENSE)
