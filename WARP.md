# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is the **Self-Affirmed Refactoring (SAR) Project** research website repository, which serves as the academic presentation site for refactoring research conducted by the SMILEVO research group. The repository hosts a Jekyll-based website deployed via GitHub Pages at https://smilevo.github.io/self-affirmed-refactoring/.

**SAR** refers to developers' documentation of their refactoring activities - key to understanding refactoring motivation, procedures, and consequences as documented by code authors themselves.

## Architecture & Structure

### Website Organization
- **Main Entry Point**: `index.html` - Primary research showcase with carousel and study listings
- **Study-Specific Pages**: Individual HTML pages for each research paper (e.g., `ASE20_index.html`, `ESEM19_index.html`, `JSS19_index.html`)
- **Experiment Pages**: Corresponding experiment/dataset pages (e.g., `ASE20_Experiment.html`)
- **Case Studies**: `CaseStudy1.html` through `CaseStudy5.html` for detailed examples
- **Subsections**: 
  - `GPT-refactoring/` - ChatGPT refactoring research materials
  - `refactoring-review/` - Code review refactoring studies
  - `Data/` - Research datasets, Excel files, CSVs, and analysis scripts

### Data Architecture
The repository contains extensive research artifacts organized in the `Data/` folder:
- **Datasets**: CSV files with commit data, refactoring classifications, and metrics
- **Web Services**: Python scripts for Azure ML services (`CHI_webservice.py`)
- **Validation Data**: External validation datasets and quality assessment files
- **Supporting Materials**: Case study images, PDFs, and video materials

### Jekyll Configuration
- Uses `jekyll-theme-minimal` theme (configured in `_config.yml`)
- Bootstrap 3.4.1 for responsive design
- Google Analytics integration across all pages
- W3.CSS for additional styling components

## Common Development Tasks

### Website Development
```powershell
# Serve the website locally using Jekyll (if Jekyll is installed)
bundle exec jekyll serve

# Alternative: Use Python's built-in server for local development
python -m http.server 8000

# View the site at http://localhost:8000
```

### Content Management
```powershell
# Add new research paper page - copy existing template
Copy-Item "ASE20_index.html" "NEW_STUDY_index.html"
# Edit the new file with study-specific content

# Add datasets to Data folder
Copy-Item "new-dataset.csv" "Data/"

# Update main index.html to include new research
# Add entry in the research listing section
```

### File Operations
```powershell
# Find all HTML files for a specific study pattern
Get-ChildItem -Path . -Filter "*ASE20*" -Recurse

# Search for specific research topics across HTML files
Select-String -Path "*.html" -Pattern "refactoring" -CaseSensitive:$false

# Check for broken links or missing images
Select-String -Path "*.html" -Pattern 'src="[^"]*"' | ForEach-Object { $_.Matches.Value }
```

### Data Management
```powershell
# List all CSV datasets
Get-ChildItem -Path "Data/" -Filter "*.csv"

# Check Python web service scripts
Get-ChildItem -Path "Data/" -Filter "*.py"

# Validate Excel files existence
Get-ChildItem -Path "Data/" -Filter "*.xlsx"
```

## Research Content Guidelines

### Adding New Research Studies
1. **Create main study page**: `[VENUE][YEAR]_index.html`
2. **Create experiment page**: `[VENUE][YEAR]_Experiment.html` 
3. **Add datasets**: Place in `Data/` folder with descriptive names
4. **Update main index**: Add study entry to `index.html` research listing
5. **Include standard elements**:
   - Research questions (RQ1, RQ2, etc.)
   - Preprint PDF link
   - Official publication link
   - Dataset download links
   - Video links (if available)

### HTML Page Structure
- All pages use consistent Bootstrap 3 navigation
- Google Analytics tracking on every page
- Standard sidebar with collected data links
- Footer with appropriate attribution
- Responsive design for mobile compatibility

### Dataset Management
- **Naming Convention**: Descriptive names indicating study and data type
- **File Types**: CSV for data, XLSX for analysis, PDF for documentation
- **Organization**: Group related files in subdirectories when appropriate
- **Links**: Ensure all dataset links in HTML pages are functional

## Important Notes

- This is a **static website** hosted on GitHub Pages
- **Jekyll processing** is handled automatically by GitHub Pages
- **No build process** required - changes to HTML/CSS are deployed directly
- **Large files** should be hosted externally and linked (GitHub has size limits)
- **Academic citations** and preprint links should be maintained for all studies
- The website serves as the **official research artifact repository** for the SMILEVO group's refactoring research

## Research Data Context

The repository contains over 15 published studies spanning multiple venues:
- **Core venues**: ICSE, FSE, ASE, MSR, ESEM, JSS, IST
- **Research themes**: Self-affirmed refactoring, developer perception, code review practices, ML classification
- **Datasets**: Thousands of commits, refactoring operations, and developer surveys
- **Time span**: Research from 2019-2025 representing a comprehensive body of work

When working with this repository, maintain the academic integrity and ensure all research artifacts remain accessible and properly attributed.