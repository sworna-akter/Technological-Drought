# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 21:49:18 2026

@author: Admin
"""

#####------Heatmap-----#####
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------------------
# 1. Load the Rotated Component Matrix Excel file
# ------------------------------
df = pd.read_excel("D:/MY RE/Dissertation writing/Paper_4/Rotated Component Matrix.xlsx")

# If your file contains a column named 'Variable', set it as index
if 'Variable' in df.columns:
    df = df.set_index('Variable')

# ------------------------------
# 2. Create the heatmap
# ------------------------------
plt.figure(figsize=(18, 22))        # Large figure for readability
sns.set(font_scale=1.8)             # Increase overall font size

ax = sns.heatmap(
    df,
    cmap="coolwarm",                # Color scheme
    linewidths=0.8,
    linecolor="gray",
    fmt=".2f",
    cbar_kws={"shrink": 0.6, "label": "Factor Loading"},
)

# ------------------------------
# 3. Axis labels and title
# ------------------------------
ax.set_xlabel("Principal Components", fontsize=24, labelpad=24)
ax.set_ylabel("Variables", fontsize=24, labelpad=24)

plt.xticks(rotation=45, fontsize=20)
plt.yticks(rotation=0, fontsize=20)



# ------------------------------
# 4. Save high-resolution figure
# ------------------------------
plt.tight_layout()
plt.savefig("heatmap_rotated_matrix.png", dpi=400, bbox_inches="tight")

# ------------------------------
# 5. Show figure
# ------------------------------
plt.show()
