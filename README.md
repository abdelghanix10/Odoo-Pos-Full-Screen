# POS Full Screen Button

## Overview

The **POS Full Screen Button** module is a simple yet highly effective add-on for Odoo 19 Point of Sale. It enhances the user interface by introducing a convenient button directly into the POS navigation bar. This button allows users (cashiers or managers) to effortlessly toggle their browser's full-screen mode on and off with a single click, providing a more immersive and distraction-free point-of-sale experience.

## Features

- **One-Click Full Screen:** Adds a clearly visible full-screen toggle button to the POS header (next to the search bar).
- **Improved UX:** Maximizes screen real estate for the POS application, hiding browser toolbars and tabs, which is particularly beneficial for touch screens and dedicated POS terminals.
- **Native Integration:** Seamlessly integrates with the standard Odoo 19 POS UI using OWL component patching.

## Technical Details

- **Odoo Version:** 19.0
- **Dependencies:** `point_of_sale`
- **Implementation:**
  - Patches the `@point_of_sale/app/components/navbar/navbar` component to add the `toggleFullScreen` behavior.
  - Extends the `point_of_sale.Navbar` XML template to inject the toggle button alongside the search input field.
  - Utilizes standard browser Fullscreen API.

## Installation

1. Copy the `pos_full_screen` directory into your Odoo 19 `addons` path.
2. Update your Odoo app list (Developer mode -> Apps -> Update Apps List).
3. Search for "POS Full Screen Button" in the Apps module.
4. Click **Activate**.

## Usage

Once installed, simply open a Point of Sale session. You will notice a new button with an expand arrows icon (`fa-arrows-alt`) in the top navigation bar, right next to the "Search products..." input field. Click it to enter full-screen mode, and click it again to exit.

## License

This module is licensed under the LGPL-3.
