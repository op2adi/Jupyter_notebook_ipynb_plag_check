# 🚀 **Automated MOSS Submission for Jupyter Notebooks**: Streamline Your Code Plagiarism Checks!

## Overview

MOSS (Measure of Software Similarity) is a powerful tool for detecting code plagiarism. However, **MOSS currently doesn't support Jupyter Notebooks (`.ipynb`)**. This script is designed to fill that gap by automating the conversion of `.ipynb` files to `.py` files, and then submitting them to MOSS for plagiarism checks. Now, you can effortlessly check your Jupyter Notebook submissions for plagiarism, just like Python files!

### **Features** ✨

- **Automated Conversion**: Converts `.ipynb` Jupyter Notebooks to `.py` Python files for easy MOSS submission.
- **Boilerplate Exclusion**: Excludes base Python files from plagiarism checks (perfect for checking student code without checking common boilerplate code).
- **MOSS Submission**: Submits converted `.py` files to MOSS for plagiarism detection.
- **Directory Mode**: Automatically processes all files in the provided directories, allowing bulk submission of notebooks.
- **Quick and Easy Setup**: Minimal setup is required—just provide your MOSS User ID and let the script handle the rest!

---

## How It Works 🔧

### Step-by-Step Process

1. **Find `.ipynb` Files**: The script will search through the specified directories to find all Jupyter Notebook (`.ipynb`) files.
2. **Convert to Python**: It uses `nbconvert` to convert Jupyter Notebooks (`.ipynb`) into Python scripts (`.py`), which can be processed by MOSS.
3. **Submit to MOSS**: The converted Python files are submitted to MOSS for plagiarism detection, with the option to exclude certain base files (such as common starter code) from the comparison.

### Important Notes
- **MOSS does not directly support `.ipynb` files**. This tool helps you work around this by converting your notebooks to Python scripts for submission.
- The script handles both **Jupyter Notebook** (`.ipynb`) files and regular **Python** (`.py`) files, making it versatile for various use cases.

---

## 🏁 **Quick Start**

### 1. Clone the Repository

To begin, clone this repository to your local machine:

```bash
git clone https://github.com/op2adi/Deployment_Project.git
cd Deployment_Project
```

To run add your files in source 

For boilerplates you provided to students please add in base folder and thar code will be excluded 

Some requirements 

Please have python 3.xx
Please install Perl link is 
```bash
http://strawberryperl.com/
```

Add it in you Environment Variables 

Also Lastly don't Forgot to use your own Moss UserId 

Here is There Link
```bash
https://theory.stanford.edu/~aiken/moss/
```

You will get the steps to how to get your own user id 

When you will get your usedid then enjoy


# Here add your Userid 
Ctrl+F in moss.pl there you will find your important stuff $userid=123456789; 

Bang Proffs and Students Enjoy don't Plagarize 

also included some test files to check plagrism you will see Good 

Also spl thanks and credit to MIT for Moss

And the person whose this ipynb is 
Created by: Tarun Reddi (also known as Teen Different)
LinkedIn: Tarun Reddi
Portfolio: Tarun's Portfolio
Medium Blogs: Teen Different on Medium
Explore: Enhancing Omni for the Visually Impaired: Read the article

His Details 

## License 📜

No License but MAde by me in sitting Inside my Institute IIITD

- **Institution**: Indraprastha Institute of Information Technology, Delhi (IIITD)
- **Usage**: This software is intended for educational and research purposes only. Commercial use is strictly prohibited without prior written consent from IIITD.
- **Redistribution**: Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
    - Redistributions must retain the above copyright notice, this list of conditions, and the following disclaimer.
    - Neither the name of IIITD nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

For more information, please visit the [IIITD website](https://www.iiitd.ac.in/).

---
Binadss distribut Karo 🫡🫡🫡🫡🫡
```
