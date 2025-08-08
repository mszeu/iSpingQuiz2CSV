# iSpringQuiz2CSV
<img src=images/supporting-member-badge.png width=100 alt="logo of Python Foundation Supporting Member">
Extracts questions for a .QUIZ iSpring Suite file to a CSV file
 
The script can be useful if you need to extract the content from the .QUIZ file generated using the iSpring Suite to a text file format to ease the import into another E-learning suite.

It requires **Python 3**. It was tested on **Python 3.12** using a basic .QUIZ file created with the iSpring Suite.

## Version

**0.1.0**

## Usage

    quiz2CSV.py [-h] quizfile [csvfile]

### Mandatory parameter(s)

**quizfile** name of the iSpring QUIZ file.

### Optional parameter

**csvfile** name of the output CSV file.

If not specified, the file name will be the same as the quiz file but with the **.csv** extension.
 
## Example

    C:\Test>python quiz2CSV.py myNiceQuiz.quiz extract.csv

## NOTES

The program is experimental! Use it at your own risk.

## COPYRIGHT & LICENSE
  Please refer to the **LICENSE** file that is part of this project.
  The license is **[AGPL 3.0](https://www.gnu.org/licenses/agpl-3.0.en.html)**
  
  Copyright&copy; 2025  **Marco S. Zuppone** - **msz@msz.eu** - [https://msz.eu](https://msz.eu)

  **iSpring&reg;** is a registered trademark of **iSpring Solutions, Inc.**

This program is free software: you can redistribute it and/or modify  
it under the terms of the GNU Affero General Public License as  
published by the Free Software Foundation, either version 3 of the  
License, or any later version.

This program is distributed in the hope that it will be useful,  
but **WITHOUT ANY WARRANTY; without even the implied warranty of  
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.** See the  
**GNU Affero General Public License** for more details.

## Questions, bugs & suggestions
For any questions, feedback, suggestions, send money ***(yes...it's a dream, I know)*** you can contact the author at [msz@msz.eu](mailto:msz@msz.eu)
