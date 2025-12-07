# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a ZMK firmware configuration repository for a Corne (3x6 with 3 thumb keys) split keyboard with nice!nano v2 controllers. ZMK is a modern, wireless-first keyboard firmware built on the Zephyr RTOS.

## Build System

The firmware is built automatically via GitHub Actions on push, pull request, or manual workflow dispatch. The workflow uses ZMK's official `build-user-config.yml` action.

Local building is not typically needed - push changes to GitHub and download the compiled firmware from the Actions artifacts.

Build configuration:
- `build.yaml`: Defines the build matrix (nice_nano_v2 board with corne_left and corne_right shields)
- `.github/workflows/build.yml`: Triggers the build workflow
- `config/west.yml`: West manifest pointing to zmkfirmware/zmk main branch

## Repository Structure

```
config/
  ├── corne.keymap       # Main keymap configuration (devicetree format)
  └── corne.conf         # Keyboard configuration (Kconfig format)
boards/                  # Custom board definitions (if any)
zephyr/                  # Zephyr RTOS integration
  └── module.yml
```

## Keymap Architecture

The keymap is defined in `config/corne.keymap` using devicetree syntax. Key concepts:

### Layer System

15 layers are defined as numeric constants (lines 12-24):
- `DEFAULT (0)`: Base QWERTY layer for macOS, ESC on hold of Ctrl key
- `WINDOWS (1)`: Windows-specific modifier adjustments (Cmd↔Ctrl swap)
- `SYMBOLS (2)`: Symbol layer with brackets, minus, equal in right hand
- `NUMBERS (3)`: Number row (1-0) and arrow keys
- `BLUETOOTH (4)`: Bluetooth pairing and output selection
- `KEYPAD (7)`: Numeric keypad layout
- `F_BUTTONS (8)`: Function keys F1-F12
- `GAME0 (12)` / `GAME1 (13)`: Gaming layouts with different modifier positions
- `MEDIA (14)`: Media controls (play/pause, volume, navigation)
- `MODES (15)`: Mode switcher to toggle between DEFAULT, WINDOWS, and GAME0

Layers 5, 6, 10, 11 are placeholder layers (all `&trans`).

### Layer Access Patterns

- **Momentary layers**: `&mo LAYER` - active while held
- **Layer-tap**: `&lt LAYER KEY` - tap for key, hold for layer
- **Sticky layer**: `&sl LAYER` - remains active for one keypress (configured for 5s timeout)
- **Toggle to layer**: `&to LAYER` - switches base layer
- **Mod-tap**: `&mt MOD KEY` - tap for key, hold for modifier

### Conditional Layer

Lines 181-187 define a conditional layer: when both WINDOWS and F_BUTTONS are active, ADJUST_LAYER_FOR_WINDOWS (layer 9) activates automatically to provide additional Windows-specific adjustments.

### Behavioral Configuration

Line 27-29: Sticky layer timeout configured to 5000ms (default is shorter).

## Configuration Settings

`config/corne.conf` contains Kconfig options:
- Battery reporting enabled with 5-minute intervals
- Split keyboard central battery fetching and proxy enabled
- RGB underglow and OLED display are commented out (disabled)

## Making Changes

1. Edit `config/corne.keymap` to modify key bindings
2. Edit `config/corne.conf` to enable/disable features
3. Commit and push changes
4. GitHub Actions will build the firmware automatically
5. Download `.uf2` files from Actions artifacts
6. Flash to keyboard by mounting controller as USB drive and copying the appropriate left/right `.uf2` file

## Key Syntax Reference

- `&kp KEY`: Key press behavior
- `&trans`: Transparent (pass through to lower layer)
- `&mt MOD KEY`: Mod-tap (tap=key, hold=modifier)
- `&lt LAYER KEY`: Layer-tap (tap=key, hold=layer)
- `&mo LAYER`: Momentary layer activation
- `&sl LAYER`: Sticky layer (one-shot)
- `&to LAYER`: Toggle to layer
- `&bt BT_SEL N`: Select Bluetooth profile N
- `&bt BT_CLR`: Clear current Bluetooth profile
- `&bt BT_PRV/BT_NXT`: Previous/next Bluetooth profile
- `&out OUT_TOG`: Toggle output (USB/BLE)

Keycodes follow ZMK conventions (e.g., `LGUI`, `LCTL`, `LALT`, `LSHFT` for modifiers; `KP_N0`-`KP_N9` for keypad numbers).
