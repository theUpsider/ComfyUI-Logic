# ComfyUI Logic Nodes Extension

This repository contains an extension to [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that introduces logic nodes and conditional rendering capabilities:
- If
- Compare
- Int, String, Float, Bool

![image](https://github.com/theUpsider/ComfyUI-Logic/assets/25013640/7807b2a4-989d-4021-9572-1d2d13725304)
> **_NOTE:_** This extension is still in development and may contain bugs. Please report any issues you encounter. New features are in development!


## Installation
- Clone this repository into the `custom_nodes` folder of ComfyUI. Restart ComfyUI and the extension should be loaded.

## Features

- **Comparison Nodes**: Compare two values using various comparison operators.
- **Data Type Nodes**: Convert and handle `Int`, `String`, `Float` and `Bool` data types.
- **Conditional Execution**: Execute different nodes based on a boolean condition.
- **Debugging**: Print any input to the console for debugging purposes.

## Nodes

### Compare

Compares two inputs (`a` and `b`) based on the provided comparison operator. Supported operators include:

- `a == b`
- `a != b`
- `a < b`
- `a > b`
- `a <= b`
- `a >= b`

### Int

Accepts an integer value and returns it.

### String

Accepts a string value and returns it.

### Float

Accepts a float value and returns it.

### Bool

Accepts a boolean value and returns it.

### If

Executes the `IF_TRUE` node if the `ANY` input is `True`, otherwise it executes the `IF_FALSE` node.

### DebugPrint

Prints the provided input to the console. Useful for debugging.


## Author
- David Fischer
- GitHub: [theUpsider](https://github.com/theUpsider)
- Support me on [BuyMeACoffee](https://www.buymeacoffee.com/theupsider)
