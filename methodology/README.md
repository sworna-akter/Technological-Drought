
# Methodology

This folder documents the methodological framework and analytical procedures used in the research project **"Underlying Dimensions and Determinants of Technological Drought in Relatively Uplifted Regions of Bangladesh."**

The study employed a mixed-methods approach combining quantitative survey analysis with qualitative information from field interviews, focus group discussions, and consultations with relevant local stakeholders.

## 1. Study Area

The research was conducted in the Madhupur Tract region of central Bangladesh, covering Tangail, Mymensingh, Jamalpur, and Gazipur districts. The region represents a distinct geomorphological unit characterized by elevated terrace-like topography and red-brown soils.

## 2. Data Collection and Sampling

Primary data were collected through structured questionnaire surveys using the Qualtrics online survey platform. A stratified random sampling procedure was followed to obtain responses from different socioeconomic and agricultural groups across the study area.

The sampling process involved:

1. Selecting upazilas based on their geographical location within the Madhupur Tract.
2. Selecting unions within the identified upazilas.
3. Randomly selecting respondents based on their geographical distribution and relevant agricultural and socioeconomic characteristics.

A total of 471 respondents were interviewed. After data cleaning and the removal of incomplete or erroneous records, 459 valid responses were retained for analysis.

The questionnaire included 55 variables/statements covering socioeconomic, agronomic, technological, environmental, and perception-based dimensions of technological drought.

## 3. Data Preparation

The collected survey responses were screened and prepared for statistical analysis.

The data-preparation procedure included:

- Reviewing survey responses for missing and erroneous entries.
- Removing incomplete or invalid records as required.
- Organizing the 55 variables for multivariate analysis.
- Standardizing the variables using z-scores before conducting Principal Component Analysis (PCA).

## 4. Principal Component Analysis (PCA)

Principal Component Analysis was employed to identify the underlying dimensions and interconnected determinants of technological drought.

The analysis used Pearson correlation coefficients calculated from the 55 standardized variables. Although the survey statements were ordinal and measured using Likert scales, they were treated as approximately continuous for the PCA.

### 4.1. Assessment of Data Suitability

The suitability of the dataset for PCA was evaluated using:

- Kaiser–Meyer–Olkin (KMO) measure of sampling adequacy.
- Bartlett's test of sphericity.

The reported KMO value was 0.94, indicating strong sampling adequacy for PCA.

### 4.2. Component Extraction

The correlation matrix (55 × 55) was used as the input for PCA. Eigenvalues and eigenvectors were obtained through eigenvalue decomposition.

### 4.3. Determination of the Number of Components

Three criteria were considered to determine the number of components to retain:

- **Kaiser Criterion:** Components with eigenvalues greater than 1.0 were retained.
- **Scree Plot Analysis:** The pattern and inflection point of the eigenvalue curve were examined.
- **Parallel Analysis:** Observed eigenvalues were compared with eigenvalues generated from random data.

Based on these criteria, ten principal components were retained.

### 4.4. Rotation and Interpretation

Varimax orthogonal rotation with Kaiser normalization was applied to improve the interpretability of the extracted components.

Variables with rotated factor loadings of ≥ |0.30| were considered meaningful contributions to component interpretation.

Communalities were also calculated to examine the proportion of each variable's variance explained by the retained components.

### 4.5. Component Scores

Component scores were calculated using the regression method, following the expression:

`T = ZV`

Where:

- `T` represents the component score matrix.
- `Z` represents the standardized data matrix.
- `V` represents the rotated loading matrix.

These scores were used to examine the underlying structure of technological drought-related dimensions.

## 5. Software and Analytical Tools

The primary PCA extraction and Varimax rotation were conducted using IBM SPSS.

Python was additionally tested to examine the stability and reproducibility of the extracted components.


