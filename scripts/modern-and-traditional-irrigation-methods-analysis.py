# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 21:50:45 2026

@author: Admin
"""

#####------Modern-Traditinal Irrigation Methods-----#####
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
# 1. LOAD DATA
# ---------------------------------
modern_file = "D:/MY RE/Dissertation writing/Paper_4/ModernIrrigationMethods.xlsx"
traditional_file = "D:/MY RE/Dissertation writing/Paper_4/TraditionalIrrigationMethods.xlsx"

df_mod = pd.read_excel(modern_file)
df_trad = pd.read_excel(traditional_file)

# ---------------------------------
# 2. CLEAN COLUMN NAMES
# ---------------------------------
df_mod.columns = df_mod.columns.str.strip()
df_trad.columns = df_trad.columns.str.strip()

# ---------------------------------
# 3. DEFINE CATEGORIES & COLORS
# ---------------------------------
categories = [
    "Currently Using",
    "Currently Not Using",
    "Used Before",
    "Not Used Before",
    "Never Used"
]

colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#B8860B']  # last one = dark gold
width = 0.15  # bar width

# ---------------------------------
# 4. CLEAN & PREPARE MODERN DATA
# ---------------------------------
for col in categories:
    df_mod[col] = pd.to_numeric(df_mod[col], errors='coerce')
df_mod[categories] = df_mod[categories].fillna(0)
if df_mod[categories].max().max() <= 1:
    df_mod[categories] = df_mod[categories] * 100

# ---------------------------------
# 5. CLEAN & PREPARE TRADITIONAL DATA
# ---------------------------------
for col in categories:
    df_trad[col] = pd.to_numeric(
        df_trad[col].astype(str).str.replace('%','', regex=False).str.strip(),
        errors='coerce'
    )
df_trad[categories] = df_trad[categories].fillna(0)
if df_trad[categories].max().max() <= 1:
    df_trad[categories] = df_trad[categories] * 100

# ---------------------------------
# 6. CREATE SUBPLOTS
# ---------------------------------
fig, axes = plt.subplots(1, 2, figsize=(16, 8), sharey=True)

fontsize_labels = 16
fontsize_ticks = 16
fontsize_title = 18
fontsize_legend = 16

# ---------------------------------
# 6a. MODERN IRRIGATION (LEFT)
# ---------------------------------
methods_mod = df_mod["Modern Irrigation Method"].astype(str)
x_mod = np.arange(len(methods_mod))

for i, cat in enumerate(categories):
    axes[0].bar(x_mod + i*width, df_mod[cat].values, width, color=colors[i], label=cat)

axes[0].set_xticks(x_mod + width*2)
axes[0].set_xticklabels(methods_mod, rotation=30, ha='right', fontsize=fontsize_ticks)
axes[0].tick_params(axis='y', labelsize=16)  # left subplot
axes[0].set_ylabel("Percentage (%)", fontsize=fontsize_labels)
axes[0].set_xlabel("Modern Irrigation Methods", fontsize=fontsize_labels)
axes[0].grid(axis='y', linestyle='--', alpha=0.6)
axes[0].set_title("(a)", fontsize=fontsize_title, loc='center')

# ---------------------------------
# 6b. TRADITIONAL IRRIGATION (RIGHT)
# ---------------------------------
methods_trad = df_trad["Traditional Irrigation Method"].astype(str)
x_trad = np.arange(len(methods_trad))

for i, cat in enumerate(categories):
    axes[1].bar(x_trad + i*width, df_trad[cat].values, width, color=colors[i])

axes[1].set_xticks(x_trad + width*2)
axes[1].set_xticklabels(methods_trad, rotation=30, ha='right', fontsize=fontsize_ticks)
axes[1].set_xlabel("Traditional Irrigation Methods", fontsize=fontsize_labels)
axes[1].grid(axis='y', linestyle='--', alpha=0.6)
axes[1].tick_params(axis='y', left=False, labelleft=False)
axes[1].set_title("(b)", fontsize=fontsize_title, loc='center')

# ---------------------------------
# 7. LEGEND
# ---------------------------------
fig.legend(categories,
           loc='lower center',
           ncol=5,
           frameon=False,
           fontsize=fontsize_legend,
           bbox_to_anchor=(0.5, -0.05))

# ---------------------------------
# 8. FINAL LAYOUT
# ---------------------------------
plt.tight_layout(rect=[0, 0.05, 1, 1])

# ---------------------------------
# 9. SAVE HIGH-RES IMAGE
# ---------------------------------
plt.savefig("D:/Dissertation writing/Paper_4/Modern_Traditional_Irrigation.png", dpi=400, bbox_inches='tight')

plt.show()