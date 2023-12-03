## What to do for revise vocabulary 

### 1. create a Microsoft xls file.                ✔
### 2. add data to the xls file.                   ✔
### 3. find some tools for parsing xls file data.  ✔
### 4. write code to parsing data from xls.        ✔
### 5. rewrite the code of LearningVocabulary.py   ✔
### 6. Figure out a way for the program to read the XLS file and render the same result even when the second column contains TWO OR MORE translations. For example, if 'hello' can be translated both as 你好 and 您好, and 'ni hao', we need the program to work for all options.    ✔
### 7. Figure out a way to count correct and wrong answers (keep the 'statistics') ✔
### 8. Come back to the wrong answers later to revise the words again.
### 9. Expand the XLS file so that we have more words to practice on    ✔
### 10. Right now, the revision part will iterate through all items in our list. Every time in the same order. starting from 1st row and finishing with the last row. We need to 1] randomize the words, 2] only select e.g. 5 words to revise (because if the list gets too long, we dont want to go through ALL the words each time we revise) ✔
### 11. After 'What is XY in Chinese?', we should reverse the format to 'What is XY in English'. Do 5 revisions into each language, randomly selected from the dictionary keys/values respectively.
### 12. Do some testing: add to the XLS one line with only EN word, and one line with only ZH word. Run to see what happens.
