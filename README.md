# Code detect
# introduction：
Code Copy detection is a code plagiarism detection tool I made based on the method proposed in "Winnowing: Local Algorithms for Document Fingerprinting" for the popular MOSS platform. Repeated parts of the code can be extracted, and a GUI report output can be generated. However, detection tools can only detect repeated parts of the code and cannot detect whether there is plagiarism in the code.
Code Defect detection is a tool I made to detect code functional defects. It extracts keywords in the code for comparison, finds the defects in them for comparison, and outputs the defective part through the GUI report.
These two parts together form a complete code plagiarism detection tool. The main language tested is Python, and other languages may be added later.
# Features:
## Code Copy detection：
1. At present, simple identification can be carried out. Basic detection such as modified variable names and extraction functions in the two codes can be identified, and rapid detection can be achieved.
2. Currently, it only supports the python language. It will be continuously updated in the future to add java, C++ and other search languages.
3. Simple operation page and download. During the investigation, many code detection tools of the same type had problems such as difficulty in downloading, system unsupported, and inability to recognize codes. So here I have simplified the download steps and designed a simple operation interface. Even if you are a novice, you can get started quickly and complete the task efficiently.
4. For similar code segments, analysis reports will be provided to help you find duplicate content in the code and provide you with a basis for further improvement and editing of the code.
## Code Defect detection：
1. There are many types of detection, which can comprehensively check various defects in the code and find out various problems in your own code.
2. Real-time detection: high efficiency and speed, can quickly identify existing defects and errors
3. Currently, only python language is supported, and more languages may be added later to achieve full language support.
4. Intelligent repair suggestions: It can effectively point out the problem and the detailed error cause, which can help developers solve the problem quickly.
5. Can generate detailed GUI reports to help developers improve code quality
6． It can be used together with the code duplication detection in the first part to find duplication problems in the code and at the same time detect defects and errors in the code, thereby identifying the plagiarized parts of the code. This is more conducive to the implementation of academic integrity.
# Usage:
Open the config.py file in the file, in # test_file = r'D:\bishe\Others-Code-Code Defect Detection+Style Judgment+GUI\Code-defect-detection-Style-determination\test.py', please Place the file that needs to be tested where the file is located, and then run the program to start testing.
# Installation: (as easy as possible)
## To download the file to local, the following conditions are required to run:
1.Python3.9
2.pycharm
# Information currently being viewed:
https://github.com/blingenf/copydetect
https://github.com/dodona-edu/dolos
https://github.com/fyrestone/pycode_similar
# Check related papers：
References:
[1] Schleimer S, Wilkerson D S, Aiken A. Winnowing: local algorithms for document fingerprinting[C]//Proceedings of the 2003 ACM SIGMOD international conference on Management of data. 2003: 76-85.
[2] Chang, Hung-Fu, and Audris Mockus. "Evaluation of source code copy detection methods on freebsd." Proceedings of the 2008 international working            
conference on Mining software repositories. 2008.
[3] Roy, Chanchal K., James R. Cordy, and Rainer Koschke. "Comparison and evaluation of code clone detection techniques and tools: A qualitative   
approach." Science of computer programming 74.7 (2009): 470-495.
